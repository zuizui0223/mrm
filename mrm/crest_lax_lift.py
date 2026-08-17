"""One-sided comparison bounds for finite CREST lift projections.

Exact faithful-lift invariance is the equality case.  This module handles two lax
situations: a source contract may retain every target obligation and add more, or
it may forget some target obligations.  The resulting refinement inequalities are
classical monotone/abstract-interpretation substrate; the CREST role is to keep the
scientific direction of the comparison explicit.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Iterable, Literal

from .crest_joint_state import (
    JointCRESTContract,
    JointCRESTState,
    Partition,
    partition_refines,
    solve_joint_crest_state,
)
from .crest_lift_invariance import pullback_partition

ComparisonDirection = Literal["source_stronger", "source_weaker"]


def _canonical(values: Iterable[Hashable]) -> Partition:
    labels: dict[Hashable, int] = {}
    result: list[int] = []
    for value in values:
        try:
            hash(value)
        except TypeError as error:
            raise ValueError("partition values must be hashable") from error
        if value not in labels:
            labels[value] = len(labels)
        result.append(labels[value])
    return tuple(result)


def _same_partition(left: Iterable[Hashable], right: Iterable[Hashable]) -> bool:
    return _canonical(left) == _canonical(right)


@dataclass(frozen=True)
class OneSidedContractProjection:
    """A surjective projection carrying a one-sided CREST contract comparison.

    ``source_stronger`` means that the source baseline and audit-static partitions
    refine the pulled target partitions, and every target action is preserved while
    the source may add action columns.  The source therefore carries at least the
    target's representational obligations.

    ``source_weaker`` reverses the partition relations and permits the target to add
    action columns.  The source therefore forgets some target obligations.

    Shared actions must preserve legality exactly and their successors must commute
    with the world projection.  Evidence and report-target partitions are required
    to be exact pullbacks so that changes in full-state licensing can be attributed
    to the representational audits rather than to a simultaneous evidence change.
    """

    source: JointCRESTContract
    target: JointCRESTContract
    source_to_target: tuple[int, ...]
    direction: ComparisonDirection

    def __post_init__(self) -> None:
        projection = tuple(self.source_to_target)
        if len(projection) != len(self.source.worlds):
            raise ValueError("source_to_target must align with source worlds")
        if any(
            not isinstance(index, int)
            or isinstance(index, bool)
            or not 0 <= index < len(self.target.worlds)
            for index in projection
        ):
            raise ValueError("source_to_target contains an invalid target index")
        if set(projection) != set(range(len(self.target.worlds))):
            raise ValueError("source_to_target must be surjective")
        if self.direction not in ("source_stronger", "source_weaker"):
            raise ValueError(
                "direction must be 'source_stronger' or 'source_weaker'"
            )
        object.__setattr__(self, "source_to_target", projection)

        self._require_one_sided_partition(
            "baseline", self.source.base_labels, self.target.base_labels
        )
        self._require_exact_pullback(
            "evidence", self.source.evidence_labels, self.target.evidence_labels
        )
        self._require_exact_pullback(
            "target", self.source.target_labels, self.target.target_labels
        )

        source_by_name = {audit.name: audit for audit in self.source.audits}
        target_by_name = {audit.name: audit for audit in self.target.audits}
        if set(source_by_name) != set(target_by_name):
            raise ValueError("source and target must declare the same audit names")

        for name, source_audit in source_by_name.items():
            target_audit = target_by_name[name]
            self._require_one_sided_partition(
                f"audit {name!r} static labels",
                source_audit.static_labels,
                target_audit.static_labels,
            )
            source_actions = set(source_audit.actions)
            target_actions = set(target_audit.actions)
            if self.direction == "source_stronger":
                if not target_actions.issubset(source_actions):
                    raise ValueError(
                        f"audit {name!r}: a stronger source must retain every "
                        "target action"
                    )
                shared_actions = target_audit.actions
            else:
                if not source_actions.issubset(target_actions):
                    raise ValueError(
                        f"audit {name!r}: a weaker source may not add target-absent "
                        "actions"
                    )
                shared_actions = source_audit.actions

            source_action_index = {
                action: index for index, action in enumerate(source_audit.actions)
            }
            target_action_index = {
                action: index for index, action in enumerate(target_audit.actions)
            }
            for source_index, target_index in enumerate(projection):
                for action in shared_actions:
                    source_successor = source_audit.successors[source_index][
                        source_action_index[action]
                    ]
                    target_successor = target_audit.successors[target_index][
                        target_action_index[action]
                    ]
                    if (source_successor is None) != (target_successor is None):
                        raise ValueError(
                            f"audit {name!r}: shared-action legality must factor "
                            f"at source world {source_index}, action {action!r}"
                        )
                    if source_successor is not None and (
                        projection[source_successor] != target_successor
                    ):
                        raise ValueError(
                            f"audit {name!r}: shared-action successors do not "
                            f"commute at source world {source_index}, action {action!r}"
                        )

    def _require_exact_pullback(
        self,
        name: str,
        source_values: Iterable[Hashable],
        target_values: Iterable[Hashable],
    ) -> None:
        expected = pullback_partition(target_values, self.source_to_target)
        if not _same_partition(source_values, expected):
            raise ValueError(f"{name} partition must be an exact target pullback")

    def _require_one_sided_partition(
        self,
        name: str,
        source_values: Iterable[Hashable],
        target_values: Iterable[Hashable],
    ) -> None:
        source_partition = _canonical(source_values)
        pulled_target = self.pullback(target_values)
        if self.direction == "source_stronger":
            valid = partition_refines(source_partition, pulled_target)
            relation = "refine"
        else:
            valid = partition_refines(pulled_target, source_partition)
            relation = "be coarser than"
        if not valid:
            raise ValueError(
                f"{name} source partition must {relation} the target pullback"
            )

    def pullback(self, target_partition: Iterable[Hashable]) -> Partition:
        return pullback_partition(target_partition, self.source_to_target)

    def audit_closure_bound(
        self,
        audit_name: str,
        target_partition: Iterable[Hashable],
    ) -> bool:
        """Check the one-sided closure inequality for one target partition."""

        source_by_name = {audit.name: audit for audit in self.source.audits}
        target_by_name = {audit.name: audit for audit in self.target.audits}
        if audit_name not in source_by_name:
            raise ValueError("unknown audit name")
        target_labels = tuple(target_partition)
        if len(target_labels) != len(self.target.worlds):
            raise ValueError("target_partition must align with target worlds")
        source_closed = source_by_name[audit_name].close(
            self.pullback(target_labels)
        )
        pulled_target_closed = self.pullback(
            target_by_name[audit_name].close(target_labels)
        )
        if self.direction == "source_stronger":
            return partition_refines(source_closed, pulled_target_closed)
        return partition_refines(pulled_target_closed, source_closed)


@dataclass(frozen=True)
class OneSidedLiftComparison:
    """Joint-state refinement bound induced by one one-sided projection."""

    projection: OneSidedContractProjection
    source_state: JointCRESTState
    target_state: JointCRESTState

    def __post_init__(self) -> None:
        if self.source_state.contract != self.projection.source:
            raise ValueError("source_state does not match the projection source")
        if self.target_state.contract != self.projection.target:
            raise ValueError("target_state does not match the projection target")
        pulled_target = self.projection.pullback(self.target_state.class_labels)
        if self.projection.direction == "source_stronger":
            if not partition_refines(self.source_state.class_labels, pulled_target):
                raise ValueError(
                    "a stronger source joint state must refine the target pullback"
                )
            if (
                self.source_state.full_state_licensed
                and not self.target_state.full_state_licensed
            ):
                raise ValueError(
                    "source full-state licensing must imply target licensing"
                )
        else:
            if not partition_refines(pulled_target, self.source_state.class_labels):
                raise ValueError(
                    "a weaker source joint state must be coarser than the target pullback"
                )
            if (
                self.target_state.full_state_licensed
                and not self.source_state.full_state_licensed
            ):
                raise ValueError(
                    "target full-state licensing must imply source licensing"
                )
        if (
            self.source_state.target_report_licensed
            != self.target_state.target_report_licensed
        ):
            raise ValueError(
                "target-only licensing must be invariant under exact evidence/target pullback"
            )

    @property
    def pulled_target_partition(self) -> Partition:
        return self.projection.pullback(self.target_state.class_labels)

    @property
    def equality(self) -> bool:
        return self.source_state.class_labels == self.pulled_target_partition

    @property
    def strict(self) -> bool:
        return not self.equality

    @property
    def state_count_bound_holds(self) -> bool:
        if self.projection.direction == "source_stronger":
            return self.source_state.state_count >= self.target_state.state_count
        return self.source_state.state_count <= self.target_state.state_count

    @property
    def target_licensing_preserved(self) -> bool:
        return (
            self.source_state.target_report_licensed
            == self.target_state.target_report_licensed
        )

    @property
    def full_state_licensing_implication(self) -> tuple[str, bool]:
        if self.projection.direction == "source_stronger":
            return (
                "source_implies_target",
                not self.source_state.full_state_licensed
                or self.target_state.full_state_licensed,
            )
        return (
            "target_implies_source",
            not self.target_state.full_state_licensed
            or self.source_state.full_state_licensed,
        )


def solve_one_sided_lift_comparison(
    projection: OneSidedContractProjection,
    *,
    audit_order: Iterable[str] | None = None,
) -> OneSidedLiftComparison:
    """Solve both contracts and certify the corresponding refinement inequality."""

    order = None if audit_order is None else tuple(audit_order)
    source_state = solve_joint_crest_state(
        projection.source, audit_order=order
    )
    target_state = solve_joint_crest_state(
        projection.target, audit_order=order
    )
    return OneSidedLiftComparison(
        projection=projection,
        source_state=source_state,
        target_state=target_state,
    )
