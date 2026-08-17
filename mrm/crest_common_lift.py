"""Maximal transition-closed common lifts for finite CREST synchronizations.

The greatest-fixed-point construction is standard finite invariant-kernel
substrate.  This module makes explicit when a declared compatibility relation among
component states supports any common CREST lift, and returns finite elimination
certificates when it does not.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Iterable

World = Hashable
Action = Hashable
Label = Hashable
Successor = int | None


def _validated_hashable(
    name: str, values: Iterable[Hashable]
) -> tuple[Hashable, ...]:
    result = tuple(values)
    for value in result:
        try:
            hash(value)
        except TypeError as error:
            raise ValueError(f"{name} values must be hashable") from error
    return result


@dataclass(frozen=True)
class ComponentCoverage:
    """One component projection and the labels a complete lift must represent."""

    name: str
    labels: tuple[Label, ...]
    required_labels: tuple[Label, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("component name must be a nonempty string")
        labels = _validated_hashable("component labels", self.labels)
        required = _validated_hashable("required component labels", self.required_labels)
        if len(set(required)) != len(required):
            raise ValueError("required component labels must be unique")
        object.__setattr__(self, "labels", labels)
        object.__setattr__(self, "required_labels", required)


@dataclass(frozen=True)
class SynchronizedLiftProblem:
    """A finite ambient synchronization from which a common lift may be pruned.

    ``compatible`` marks tuples satisfying the static cross-component alignment.
    Every legal transition of a retained tuple must remain retained; ``None`` means
    the action is illegal at that tuple.  Component coverage obligations express
    which local states the final common lift must still represent.
    """

    worlds: tuple[World, ...]
    compatible: tuple[bool, ...]
    actions: tuple[Action, ...]
    successors: tuple[tuple[Successor, ...], ...]
    components: tuple[ComponentCoverage, ...]

    def __post_init__(self) -> None:
        worlds = _validated_hashable("worlds", self.worlds)
        if not worlds or len(set(worlds)) != len(worlds):
            raise ValueError("worlds must be nonempty and unique")
        compatible = tuple(self.compatible)
        if len(compatible) != len(worlds) or any(
            not isinstance(value, bool) for value in compatible
        ):
            raise ValueError("compatible must be one boolean per ambient world")
        actions = _validated_hashable("actions", self.actions)
        if len(set(actions)) != len(actions):
            raise ValueError("actions must be unique")
        successors = tuple(tuple(row) for row in self.successors)
        if len(successors) != len(worlds) or any(
            len(row) != len(actions) for row in successors
        ):
            raise ValueError("successors must align with worlds and actions")
        if any(
            successor is not None
            and (
                not isinstance(successor, int)
                or isinstance(successor, bool)
                or not 0 <= successor < len(worlds)
            )
            for row in successors
            for successor in row
        ):
            raise ValueError("successors must be ambient-world indices or None")
        components = tuple(self.components)
        if not components:
            raise ValueError("at least one component coverage contract is required")
        if len({component.name for component in components}) != len(components):
            raise ValueError("component names must be unique")
        if any(len(component.labels) != len(worlds) for component in components):
            raise ValueError("component labels must align with ambient worlds")

        object.__setattr__(self, "worlds", worlds)
        object.__setattr__(self, "compatible", compatible)
        object.__setattr__(self, "actions", actions)
        object.__setattr__(self, "successors", successors)
        object.__setattr__(self, "components", components)

    def is_closed_subset(self, indices: Iterable[int]) -> bool:
        """Whether indices form a statically compatible transition-closed subset."""

        chosen = set(indices)
        if any(
            not isinstance(index, int)
            or isinstance(index, bool)
            or not 0 <= index < len(self.worlds)
            for index in chosen
        ):
            raise ValueError("subset contains an invalid world index")
        if any(not self.compatible[index] for index in chosen):
            return False
        return all(
            successor is None or successor in chosen
            for index in chosen
            for successor in self.successors[index]
        )


@dataclass(frozen=True)
class EliminationReason:
    """Why one candidate tuple was removed from the common-lift kernel."""

    round: int
    action: Action | None
    successor: World | None

    def __post_init__(self) -> None:
        if not isinstance(self.round, int) or isinstance(self.round, bool) or self.round < 0:
            raise ValueError("elimination round must be a nonnegative integer")
        if self.round == 0 and (self.action is not None or self.successor is not None):
            raise ValueError("round-zero elimination denotes static incompatibility")
        if self.round > 0 and (self.action is None or self.successor is None):
            raise ValueError("dynamic elimination requires an action and successor")


@dataclass(frozen=True)
class MaximalCommonLift:
    """The greatest compatible subset closed under every declared legal action."""

    problem: SynchronizedLiftProblem
    viable_indices: tuple[int, ...]
    elimination_reasons: tuple[EliminationReason | None, ...]

    def __post_init__(self) -> None:
        viable = tuple(self.viable_indices)
        if viable != tuple(sorted(set(viable))) or any(
            not 0 <= index < len(self.problem.worlds) for index in viable
        ):
            raise ValueError("viable_indices must be sorted unique world indices")
        reasons = tuple(self.elimination_reasons)
        if len(reasons) != len(self.problem.worlds):
            raise ValueError("elimination_reasons must align with ambient worlds")
        viable_set = set(viable)
        if any((index in viable_set) != (reason is None) for index, reason in enumerate(reasons)):
            raise ValueError("viability and elimination reasons are inconsistent")
        if not self.problem.is_closed_subset(viable):
            raise ValueError("viable_indices must be compatible and transition closed")
        object.__setattr__(self, "viable_indices", viable)
        object.__setattr__(self, "elimination_reasons", reasons)

    @property
    def worlds(self) -> tuple[World, ...]:
        return tuple(self.problem.worlds[index] for index in self.viable_indices)

    @property
    def exists(self) -> bool:
        return bool(self.viable_indices)

    @property
    def missing_coverage(self) -> tuple[tuple[str, tuple[Label, ...]], ...]:
        result = []
        for component in self.problem.components:
            represented = {
                component.labels[index] for index in self.viable_indices
            }
            missing = tuple(
                label for label in component.required_labels if label not in represented
            )
            if missing:
                result.append((component.name, missing))
        return tuple(result)

    @property
    def coverage_complete(self) -> bool:
        return not self.missing_coverage

    @property
    def admissible(self) -> bool:
        return self.exists and self.coverage_complete

    @property
    def restricted_successors(self) -> tuple[tuple[World | None, ...], ...]:
        """Successors on the retained kernel, returned as ambient world values."""

        return tuple(
            tuple(
                None if successor is None else self.problem.worlds[successor]
                for successor in self.problem.successors[index]
            )
            for index in self.viable_indices
        )

    def elimination_chain(self, world: World) -> tuple[World, ...]:
        """Return a finite witness chain ending at a statically incompatible world."""

        try:
            index = self.problem.worlds.index(world)
        except ValueError as error:
            raise ValueError("unknown ambient world") from error
        if index in self.viable_indices:
            return (world,)

        chain = [index]
        seen = {index}
        while True:
            reason = self.elimination_reasons[index]
            if reason is None:
                raise RuntimeError("viable world appeared inside an elimination chain")
            if reason.round == 0:
                break
            successor_value = reason.successor
            assert successor_value is not None
            successor = self.problem.worlds.index(successor_value)
            if successor in seen:
                raise RuntimeError("elimination certificate contains a cycle")
            next_reason = self.elimination_reasons[successor]
            if next_reason is None or next_reason.round >= reason.round:
                raise RuntimeError("elimination ranks must strictly decrease along a chain")
            chain.append(successor)
            seen.add(successor)
            index = successor
        return tuple(self.problem.worlds[item] for item in chain)

    def coverage_elimination_chains(
        self, component_name: str, required_label: Label
    ) -> tuple[tuple[World, ...], ...]:
        """Certificates for every candidate tuple carrying one missing component label."""

        by_name = {component.name: component for component in self.problem.components}
        if component_name not in by_name:
            raise ValueError("unknown component name")
        component = by_name[component_name]
        if required_label not in component.required_labels:
            raise ValueError("label is not a declared coverage obligation")
        candidates = [
            index
            for index, label in enumerate(component.labels)
            if label == required_label and self.problem.compatible[index]
        ]
        if any(index in self.viable_indices for index in candidates):
            return ()
        return tuple(
            self.elimination_chain(self.problem.worlds[index]) for index in candidates
        )


def maximal_common_lift(problem: SynchronizedLiftProblem) -> MaximalCommonLift:
    """Compute the greatest compatible transition-closed subset.

    Starting from every statically compatible tuple, one simultaneous pruning round
    removes each tuple having a legal successor outside the current set.  Finiteness
    guarantees stabilization.  Every other compatible transition-closed subset is
    contained in the returned kernel.
    """

    current = {index for index, value in enumerate(problem.compatible) if value}
    reasons: list[EliminationReason | None] = [None] * len(problem.worlds)
    for index, value in enumerate(problem.compatible):
        if not value:
            reasons[index] = EliminationReason(round=0, action=None, successor=None)

    round_number = 1
    while True:
        removals: list[tuple[int, int, int]] = []
        for index in sorted(current):
            for action_index, successor in enumerate(problem.successors[index]):
                if successor is not None and successor not in current:
                    removals.append((index, action_index, successor))
                    break
        if not removals:
            return MaximalCommonLift(
                problem=problem,
                viable_indices=tuple(sorted(current)),
                elimination_reasons=tuple(reasons),
            )
        for index, action_index, successor in removals:
            current.remove(index)
            reasons[index] = EliminationReason(
                round=round_number,
                action=problem.actions[action_index],
                successor=problem.worlds[successor],
            )
        round_number += 1
        if round_number > len(problem.worlds) + 1:
            raise RuntimeError("finite common-lift pruning failed to stabilize")
