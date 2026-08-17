"""Conditional finite joint-state construction for CREST common lifts.

The least-common-fixed-point construction used here is classical closure-operator
substrate. This module makes the conditional CREST synthesis executable; it is not
an independent novelty claim for partition refinement or fixed-point theory.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Iterable

World = Hashable
Label = Hashable
Partition = tuple[int, ...]
Successor = int | None


def _canonical(values: Iterable[Hashable]) -> Partition:
    labels: dict[Hashable, int] = {}
    result: list[int] = []
    for value in values:
        try:
            hash(value)
        except TypeError as error:
            raise ValueError("partition signatures must be hashable") from error
        if value not in labels:
            labels[value] = len(labels)
        result.append(labels[value])
    return tuple(result)


def _validate_hashable(
    name: str, values: Iterable[Hashable]
) -> tuple[Hashable, ...]:
    result = tuple(values)
    for value in result:
        try:
            hash(value)
        except TypeError as error:
            raise ValueError(f"{name} values must be hashable") from error
    return result


def partition_refines(
    fine: Iterable[Hashable], coarse: Iterable[Hashable]
) -> bool:
    """Return whether every ``fine`` block lies inside one ``coarse`` block."""

    fine_labels = _canonical(fine)
    coarse_labels = _canonical(coarse)
    if len(fine_labels) != len(coarse_labels):
        raise ValueError("partitions must have the same finite carrier")
    return all(
        fine_labels[left] != fine_labels[right]
        or coarse_labels[left] == coarse_labels[right]
        for left in range(len(fine_labels))
        for right in range(left + 1, len(fine_labels))
    )


def evidence_licenses(
    values: Iterable[Hashable], evidence: Iterable[Hashable]
) -> bool:
    """Whether a value is a deterministic function of the evidence class."""

    value_tuple = _validate_hashable("values", values)
    evidence_tuple = _validate_hashable("evidence", evidence)
    if len(value_tuple) != len(evidence_tuple):
        raise ValueError("values and evidence must align on one finite carrier")
    return all(
        evidence_tuple[left] != evidence_tuple[right]
        or value_tuple[left] == value_tuple[right]
        for left in range(len(value_tuple))
        for right in range(left + 1, len(value_tuple))
    )


def compatible_values_by_evidence(
    values: Iterable[Hashable], evidence: Iterable[Hashable]
) -> tuple[tuple[Hashable, ...], ...]:
    """Return the sharp set-valued report for every canonical evidence class."""

    value_tuple = _validate_hashable("values", values)
    evidence_tuple = _validate_hashable("evidence", evidence)
    if len(value_tuple) != len(evidence_tuple):
        raise ValueError("values and evidence must align on one finite carrier")
    evidence_labels = _canonical(evidence_tuple)
    reports: list[list[Hashable]] = [
        [] for _ in range(max(evidence_labels, default=-1) + 1)
    ]
    for evidence_label, value in zip(evidence_labels, value_tuple):
        if value not in reports[evidence_label]:
            reports[evidence_label].append(value)
    return tuple(tuple(report) for report in reports)


@dataclass(frozen=True)
class AuditRefinement:
    """One finite audit closure on a shared ordered latent-world carrier.

    ``static_labels`` are distinctions that this audit must preserve. Each action
    column in ``successors`` is a partial deterministic transition; ``None`` means
    the action is illegal at that world. ``close`` returns the unique coarsest
    refinement of an input partition that preserves the static labels and has a
    deterministic legal-action row and successor block under every action.
    """

    name: str
    static_labels: tuple[Label, ...]
    actions: tuple[Hashable, ...]
    successors: tuple[tuple[Successor, ...], ...]

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("audit name must be a nonempty string")
        labels = _validate_hashable("static_labels", self.static_labels)
        actions = _validate_hashable("actions", self.actions)
        if not labels:
            raise ValueError("an audit requires a nonempty finite carrier")
        if len(set(actions)) != len(actions):
            raise ValueError("audit actions must be unique")
        successors = tuple(tuple(row) for row in self.successors)
        if len(successors) != len(labels) or any(
            len(row) != len(actions) for row in successors
        ):
            raise ValueError(
                "successors must provide one entry per world and audit action"
            )
        world_count = len(labels)
        if any(
            successor is not None
            and (
                not isinstance(successor, int)
                or isinstance(successor, bool)
                or not 0 <= successor < world_count
            )
            for row in successors
            for successor in row
        ):
            raise ValueError("successor entries must be world indices or None")
        object.__setattr__(self, "static_labels", labels)
        object.__setattr__(self, "actions", actions)
        object.__setattr__(self, "successors", successors)

    @property
    def world_count(self) -> int:
        return len(self.static_labels)

    def close(self, partition: Iterable[Hashable]) -> Partition:
        """Return this audit's coarsest stable refinement of ``partition``."""

        partition_tuple = tuple(partition)
        if len(partition_tuple) != self.world_count:
            raise ValueError("partition must align with the audit carrier")
        labels = _canonical(
            (partition_tuple[index], self.static_labels[index])
            for index in range(self.world_count)
        )
        initial_count = max(labels) + 1
        strict_steps = 0
        while True:
            signatures: list[Hashable] = []
            for index, row in enumerate(self.successors):
                successor_signature = tuple(
                    None if successor is None else labels[successor]
                    for successor in row
                )
                signatures.append(
                    (labels[index], self.static_labels[index], successor_signature)
                )
            refined = _canonical(signatures)
            if refined == labels:
                return labels
            labels = refined
            strict_steps += 1
            if strict_steps > self.world_count - initial_count:
                raise RuntimeError("finite audit refinement failed to stabilize")

    def is_fixed(self, partition: Iterable[Hashable]) -> bool:
        labels = _canonical(partition)
        return self.close(labels) == labels


@dataclass(frozen=True)
class JointCRESTContract:
    """A declared finite common lift for the CREST audit obligations."""

    worlds: tuple[World, ...]
    base_labels: tuple[Label, ...]
    evidence_labels: tuple[Label, ...]
    target_labels: tuple[Label, ...]
    audits: tuple[AuditRefinement, ...]

    def __post_init__(self) -> None:
        worlds = _validate_hashable("worlds", self.worlds)
        if not worlds or len(set(worlds)) != len(worlds):
            raise ValueError("worlds must be nonempty and unique")
        base = _validate_hashable("base_labels", self.base_labels)
        evidence = _validate_hashable("evidence_labels", self.evidence_labels)
        targets = _validate_hashable("target_labels", self.target_labels)
        if any(len(values) != len(worlds) for values in (base, evidence, targets)):
            raise ValueError("all contract labels must align with worlds")
        audits = tuple(self.audits)
        if not audits or any(audit.world_count != len(worlds) for audit in audits):
            raise ValueError("all audits must use the same nonempty finite carrier")
        names = tuple(audit.name for audit in audits)
        if len(set(names)) != len(names):
            raise ValueError("audit names must be unique")
        object.__setattr__(self, "worlds", worlds)
        object.__setattr__(self, "base_labels", base)
        object.__setattr__(self, "evidence_labels", evidence)
        object.__setattr__(self, "target_labels", targets)
        object.__setattr__(self, "audits", audits)


@dataclass(frozen=True)
class JointCRESTState:
    """The unique coarsest common fixed point for one finite CREST contract."""

    contract: JointCRESTContract
    class_labels: Partition
    strict_passes: int
    audit_order: tuple[str, ...]

    def __post_init__(self) -> None:
        labels = _canonical(self.class_labels)
        if len(labels) != len(self.contract.worlds) or labels != self.class_labels:
            raise ValueError("class_labels must be canonical and align with worlds")
        if not isinstance(self.strict_passes, int) or self.strict_passes < 0:
            raise ValueError("strict_passes must be a nonnegative integer")
        if any(not audit.is_fixed(labels) for audit in self.contract.audits):
            raise ValueError("joint state must be fixed by every audit closure")
        if not partition_refines(labels, self.contract.base_labels):
            raise ValueError("joint state must refine the base contract")

    @property
    def state_count(self) -> int:
        return max(self.class_labels) + 1

    @property
    def blocks(self) -> tuple[tuple[World, ...], ...]:
        return tuple(
            tuple(
                world
                for world, label in zip(self.contract.worlds, self.class_labels)
                if label == block
            )
            for block in range(self.state_count)
        )

    @property
    def full_state_licensed(self) -> bool:
        """Whether reliability-qualified evidence identifies the joint state."""

        return evidence_licenses(self.class_labels, self.contract.evidence_labels)

    @property
    def target_report_licensed(self) -> bool:
        """Whether evidence licenses the target, possibly without the full state."""

        return evidence_licenses(
            self.contract.target_labels, self.contract.evidence_labels
        )

    @property
    def sharp_state_report(self) -> tuple[tuple[Hashable, ...], ...]:
        return compatible_values_by_evidence(
            self.class_labels, self.contract.evidence_labels
        )

    @property
    def sharp_target_report(self) -> tuple[tuple[Hashable, ...], ...]:
        return compatible_values_by_evidence(
            self.contract.target_labels, self.contract.evidence_labels
        )

    def class_of(self, world: World) -> int:
        try:
            return self.class_labels[self.contract.worlds.index(world)]
        except ValueError as error:
            raise ValueError("unknown latent world") from error


def _ordered_audits(
    contract: JointCRESTContract, audit_order: Iterable[str] | None
) -> tuple[AuditRefinement, ...]:
    if audit_order is None:
        return contract.audits
    names = tuple(audit_order)
    expected = tuple(audit.name for audit in contract.audits)
    if len(names) != len(expected) or set(names) != set(expected):
        raise ValueError("audit_order must be a permutation of all audit names")
    by_name = {audit.name: audit for audit in contract.audits}
    return tuple(by_name[name] for name in names)


def apply_audits_once(
    contract: JointCRESTContract,
    partition: Iterable[Hashable] | None = None,
    *,
    audit_order: Iterable[str] | None = None,
) -> Partition:
    """Apply every audit once in the requested order.

    This helper intentionally exposes order dependence before the common fixed point
    is reached. Use :func:`solve_joint_crest_state` for the order-independent result.
    """

    labels = _canonical(
        contract.base_labels if partition is None else tuple(partition)
    )
    if len(labels) != len(contract.worlds):
        raise ValueError("partition must align with the common carrier")
    for audit in _ordered_audits(contract, audit_order):
        labels = audit.close(labels)
    return labels


def solve_joint_crest_state(
    contract: JointCRESTContract,
    *,
    audit_order: Iterable[str] | None = None,
) -> JointCRESTState:
    """Compute the least common fixed point of all finite audit closures.

    A fair cyclic schedule is used. The order can change the number of passes and
    intermediate partitions, but not the final partition. Every strict pass adds at
    least one block, so at most ``|worlds| - |base blocks|`` strict passes occur.
    """

    audits = _ordered_audits(contract, audit_order)
    order_names = tuple(audit.name for audit in audits)
    labels = _canonical(contract.base_labels)
    base_count = max(labels) + 1
    strict_passes = 0
    while True:
        before = labels
        for audit in audits:
            labels = audit.close(labels)
        if labels == before:
            return JointCRESTState(
                contract=contract,
                class_labels=labels,
                strict_passes=strict_passes,
                audit_order=order_names,
            )
        strict_passes += 1
        if strict_passes > len(contract.worlds) - base_count:
            raise RuntimeError("fair finite audit iteration failed to stabilize")
