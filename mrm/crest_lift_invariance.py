"""Faithful-lift invariance for finite CREST joint-state contracts.

The naturality result implemented here is classical quotient/closure substrate.  It
makes precise when adding latent-world detail is scientifically redundant for all
four declared CREST audits and therefore cannot change the joint minimal state.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Iterable

from .crest_joint_state import (
    JointCRESTContract,
    JointCRESTState,
    Partition,
    solve_joint_crest_state,
)


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


def pullback_partition(
    target_partition: Iterable[Hashable],
    source_to_target: Iterable[int],
) -> Partition:
    """Pull a target partition back along a finite world projection.

    The returned labels are canonical in source-world order.  The projection need
    not be injective; every source world inherits the block of its target image.
    """

    target_labels = tuple(target_partition)
    projection = tuple(source_to_target)
    if not target_labels:
        raise ValueError("target_partition must be nonempty")
    if not projection:
        raise ValueError("source_to_target must be nonempty")
    if any(
        not isinstance(index, int)
        or isinstance(index, bool)
        or not 0 <= index < len(target_labels)
        for index in projection
    ):
        raise ValueError("source_to_target contains an invalid target index")
    return _canonical(target_labels[index] for index in projection)


@dataclass(frozen=True)
class FaithfulContractProjection:
    """A surjective audit-faithful projection between two finite CREST lifts.

    The source may duplicate target worlds, but the duplicated detail must be
    invisible to the baseline, evidence, target, audit-static labels, action
    legality, and projected successors.  Under these conditions every audit
    closure commutes with partition pullback.
    """

    source: JointCRESTContract
    target: JointCRESTContract
    source_to_target: tuple[int, ...]

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
        object.__setattr__(self, "source_to_target", projection)

        self._require_partition_pullback(
            "baseline", self.source.base_labels, self.target.base_labels
        )
        self._require_partition_pullback(
            "evidence", self.source.evidence_labels, self.target.evidence_labels
        )
        self._require_partition_pullback(
            "target", self.source.target_labels, self.target.target_labels
        )

        source_by_name = {audit.name: audit for audit in self.source.audits}
        target_by_name = {audit.name: audit for audit in self.target.audits}
        if set(source_by_name) != set(target_by_name):
            raise ValueError("source and target must declare the same audit names")

        for name, source_audit in source_by_name.items():
            target_audit = target_by_name[name]
            if source_audit.actions != target_audit.actions:
                raise ValueError(
                    f"audit {name!r} must declare the same ordered actions"
                )
            self._require_partition_pullback(
                f"audit {name!r} static labels",
                source_audit.static_labels,
                target_audit.static_labels,
            )
            for source_index, source_row in enumerate(source_audit.successors):
                target_index = projection[source_index]
                target_row = target_audit.successors[target_index]
                for action_index, (source_successor, target_successor) in enumerate(
                    zip(source_row, target_row)
                ):
                    if (source_successor is None) != (target_successor is None):
                        raise ValueError(
                            f"audit {name!r} action legality does not factor "
                            f"at source world {source_index}, action {action_index}"
                        )
                    if source_successor is not None and (
                        projection[source_successor] != target_successor
                    ):
                        raise ValueError(
                            f"audit {name!r} successors do not commute with the "
                            f"world projection at source world {source_index}, "
                            f"action {action_index}"
                        )

    def _require_partition_pullback(
        self,
        name: str,
        source_values: Iterable[Hashable],
        target_values: Iterable[Hashable],
    ) -> None:
        expected = pullback_partition(target_values, self.source_to_target)
        if not _same_partition(source_values, expected):
            raise ValueError(f"{name} partition must be a pullback from the target")

    def pullback(self, target_partition: Iterable[Hashable]) -> Partition:
        return pullback_partition(target_partition, self.source_to_target)

    def audit_closure_commutes(
        self,
        audit_name: str,
        target_partition: Iterable[Hashable],
    ) -> bool:
        """Check the naturality equation for one audit and one target partition."""

        source_by_name = {audit.name: audit for audit in self.source.audits}
        target_by_name = {audit.name: audit for audit in self.target.audits}
        if audit_name not in source_by_name:
            raise ValueError("unknown audit name")
        target_labels = tuple(target_partition)
        if len(target_labels) != len(self.target.worlds):
            raise ValueError("target_partition must align with target worlds")
        left = source_by_name[audit_name].close(self.pullback(target_labels))
        right = self.pullback(target_by_name[audit_name].close(target_labels))
        return left == right


@dataclass(frozen=True)
class LiftInvariantJointState:
    """Joint states related by one faithful surjective lift projection."""

    projection: FaithfulContractProjection
    source_state: JointCRESTState
    target_state: JointCRESTState
    target_block_by_source_block: tuple[int, ...]

    def __post_init__(self) -> None:
        if self.source_state.contract != self.projection.source:
            raise ValueError("source_state does not match the projection source")
        if self.target_state.contract != self.projection.target:
            raise ValueError("target_state does not match the projection target")
        expected = self.projection.pullback(self.target_state.class_labels)
        if self.source_state.class_labels != expected:
            raise ValueError("source joint state is not the target-state pullback")
        mapping = tuple(self.target_block_by_source_block)
        if len(mapping) != self.source_state.state_count:
            raise ValueError("block map must cover every source quotient state")
        if set(mapping) != set(range(self.target_state.state_count)):
            raise ValueError("block map must be a quotient-state bijection")
        if len(set(mapping)) != len(mapping):
            raise ValueError("block map must be injective")
        if self.source_state.full_state_licensed != self.target_state.full_state_licensed:
            raise ValueError("full-state licensing must be projection invariant")
        if (
            self.source_state.target_report_licensed
            != self.target_state.target_report_licensed
        ):
            raise ValueError("target licensing must be projection invariant")

    @property
    def quotient_isomorphic(self) -> bool:
        return self.source_state.state_count == self.target_state.state_count

    @property
    def full_state_licensing_preserved(self) -> bool:
        return (
            self.source_state.full_state_licensed
            == self.target_state.full_state_licensed
        )

    @property
    def target_licensing_preserved(self) -> bool:
        return (
            self.source_state.target_report_licensed
            == self.target_state.target_report_licensed
        )


def solve_lift_invariant_joint_states(
    projection: FaithfulContractProjection,
    *,
    audit_order: Iterable[str] | None = None,
) -> LiftInvariantJointState:
    """Solve both lifts and certify their quotient-state isomorphism.

    Exact audit naturality implies that fair joint refinement on the source is the
    pullback of fair refinement on the target.  The source may contain more latent
    worlds, but it contains no additional CREST-visible state distinction.
    """

    order = None if audit_order is None else tuple(audit_order)
    target_state = solve_joint_crest_state(
        projection.target, audit_order=order
    )
    source_state = solve_joint_crest_state(
        projection.source, audit_order=order
    )
    expected = projection.pullback(target_state.class_labels)
    if source_state.class_labels != expected:
        raise RuntimeError(
            "faithful projection invariant failed: audit implementation is not natural"
        )

    block_map: list[int] = []
    for source_block in range(source_state.state_count):
        representative = source_state.class_labels.index(source_block)
        target_world = projection.source_to_target[representative]
        block_map.append(target_state.class_labels[target_world])

    return LiftInvariantJointState(
        projection=projection,
        source_state=source_state,
        target_state=target_state,
        target_block_by_source_block=tuple(block_map),
    )
