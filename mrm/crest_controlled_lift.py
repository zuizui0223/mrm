"""Controlled common-lift viability for finite CREST synchronizations.

Greatest controlled-invariant kernels and memoryless safety policies are standard
viability/game-theoretic substrate.  This module separates unavoidable exterior
transitions from selectable ecological-management actions at the CREST common-lift
gate and returns finite AND/OR elimination certificates when viability fails.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Iterable, Literal

from .crest_common_lift import ComponentCoverage

World = Hashable
Action = Hashable
Successor = int | None
ReasonKind = Literal["static", "uncontrollable_escape", "no_safe_control"]


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


def _validated_successors(
    name: str,
    rows: Iterable[Iterable[Successor]],
    *,
    world_count: int,
    action_count: int,
) -> tuple[tuple[Successor, ...], ...]:
    result = tuple(tuple(row) for row in rows)
    if len(result) != world_count or any(
        len(row) != action_count for row in result
    ):
        raise ValueError(f"{name} must align with worlds and actions")
    if any(
        successor is not None
        and (
            not isinstance(successor, int)
            or isinstance(successor, bool)
            or not 0 <= successor < world_count
        )
        for row in result
        for successor in row
    ):
        raise ValueError(f"{name} entries must be world indices or None")
    return result


@dataclass(frozen=True)
class ControlledSynchronizedLiftProblem:
    """A finite common-lift problem with environment and controller moves.

    Every retained world must survive all legal uncontrollable actions and admit at
    least one legal controllable action whose successor is retained.  A terminal or
    no-op choice must therefore be represented explicitly as a controllable
    self-loop when the scientific contract intends it to be available.
    """

    worlds: tuple[World, ...]
    compatible: tuple[bool, ...]
    uncontrollable_actions: tuple[Action, ...]
    controllable_actions: tuple[Action, ...]
    uncontrollable_successors: tuple[tuple[Successor, ...], ...]
    controllable_successors: tuple[tuple[Successor, ...], ...]
    components: tuple[ComponentCoverage, ...]

    def __post_init__(self) -> None:
        worlds = _validated_hashable("worlds", self.worlds)
        if not worlds or len(set(worlds)) != len(worlds):
            raise ValueError("worlds must be nonempty and unique")
        compatible = tuple(self.compatible)
        if len(compatible) != len(worlds) or any(
            not isinstance(value, bool) for value in compatible
        ):
            raise ValueError("compatible must contain one boolean per world")

        uncontrollable = _validated_hashable(
            "uncontrollable_actions", self.uncontrollable_actions
        )
        controllable = _validated_hashable(
            "controllable_actions", self.controllable_actions
        )
        if len(set(uncontrollable)) != len(uncontrollable):
            raise ValueError("uncontrollable actions must be unique")
        if not controllable or len(set(controllable)) != len(controllable):
            raise ValueError("controllable actions must be nonempty and unique")
        if set(uncontrollable) & set(controllable):
            raise ValueError("controllable and uncontrollable actions must be disjoint")

        uncontrollable_successors = _validated_successors(
            "uncontrollable_successors",
            self.uncontrollable_successors,
            world_count=len(worlds),
            action_count=len(uncontrollable),
        )
        controllable_successors = _validated_successors(
            "controllable_successors",
            self.controllable_successors,
            world_count=len(worlds),
            action_count=len(controllable),
        )

        components = tuple(self.components)
        if not components:
            raise ValueError("at least one component coverage contract is required")
        if len({component.name for component in components}) != len(components):
            raise ValueError("component names must be unique")
        if any(len(component.labels) != len(worlds) for component in components):
            raise ValueError("component labels must align with worlds")

        object.__setattr__(self, "worlds", worlds)
        object.__setattr__(self, "compatible", compatible)
        object.__setattr__(self, "uncontrollable_actions", uncontrollable)
        object.__setattr__(self, "controllable_actions", controllable)
        object.__setattr__(
            self, "uncontrollable_successors", uncontrollable_successors
        )
        object.__setattr__(self, "controllable_successors", controllable_successors)
        object.__setattr__(self, "components", components)

    def _validated_indices(self, indices: Iterable[int]) -> tuple[int, ...]:
        chosen = tuple(sorted(set(indices)))
        if any(
            not isinstance(index, int)
            or isinstance(index, bool)
            or not 0 <= index < len(self.worlds)
            for index in chosen
        ):
            raise ValueError("subset contains an invalid world index")
        return chosen

    def safe_control_indices(
        self, world_index: int, retained_indices: Iterable[int]
    ) -> tuple[int, ...]:
        retained = set(self._validated_indices(retained_indices))
        if not 0 <= world_index < len(self.worlds):
            raise ValueError("world_index outside the ambient carrier")
        return tuple(
            action_index
            for action_index, successor in enumerate(
                self.controllable_successors[world_index]
            )
            if successor is not None and successor in retained
        )

    def is_controlled_invariant_subset(self, indices: Iterable[int]) -> bool:
        """Whether a subset is compatible and robustly control invariant."""

        chosen = set(self._validated_indices(indices))
        if any(not self.compatible[index] for index in chosen):
            return False
        for index in chosen:
            if any(
                successor is not None and successor not in chosen
                for successor in self.uncontrollable_successors[index]
            ):
                return False
            if not any(
                successor is not None and successor in chosen
                for successor in self.controllable_successors[index]
            ):
                return False
        return True


@dataclass(frozen=True)
class ControlledEliminationReason:
    """One finite reason for removing a world from the controlled kernel."""

    round: int
    kind: ReasonKind
    action: Action | None = None
    successor: World | None = None
    control_frontier: tuple[tuple[Action, World], ...] = ()

    def __post_init__(self) -> None:
        if (
            not isinstance(self.round, int)
            or isinstance(self.round, bool)
            or self.round < 0
        ):
            raise ValueError("elimination round must be a nonnegative integer")
        if self.kind not in (
            "static",
            "uncontrollable_escape",
            "no_safe_control",
        ):
            raise ValueError("unknown controlled elimination kind")
        frontier = tuple(self.control_frontier)
        object.__setattr__(self, "control_frontier", frontier)

        if self.kind == "static":
            if self.round != 0 or self.action is not None or self.successor is not None or frontier:
                raise ValueError("static elimination must be a round-zero leaf")
        elif self.kind == "uncontrollable_escape":
            if self.round == 0 or self.action is None or self.successor is None or frontier:
                raise ValueError(
                    "uncontrollable escape requires one action and successor"
                )
        else:
            if self.round == 0 or self.action is not None or self.successor is not None:
                raise ValueError(
                    "no-safe-control elimination uses only its control frontier"
                )
            if len({action for action, _ in frontier}) != len(frontier):
                raise ValueError("control frontier actions must be unique")


@dataclass(frozen=True)
class ControlledNoGoCertificate:
    """A finite AND/OR tree witnessing controlled nonviability."""

    world: World
    round: int
    kind: ReasonKind
    action: Action | None = None
    children: tuple[tuple[Action, "ControlledNoGoCertificate"], ...] = ()

    @property
    def depth(self) -> int:
        return 0 if not self.children else 1 + max(
            child.depth for _, child in self.children
        )


@dataclass(frozen=True)
class MaximalControlledCommonLift:
    """The greatest compatible robust controlled-invariant common lift."""

    problem: ControlledSynchronizedLiftProblem
    viable_indices: tuple[int, ...]
    elimination_reasons: tuple[ControlledEliminationReason | None, ...]

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
        if any(
            (index in viable_set) != (reason is None)
            for index, reason in enumerate(reasons)
        ):
            raise ValueError("viability and elimination reasons are inconsistent")
        if not self.problem.is_controlled_invariant_subset(viable):
            raise ValueError("viable_indices must be robustly control invariant")
        object.__setattr__(self, "viable_indices", viable)
        object.__setattr__(self, "elimination_reasons", reasons)

    @property
    def worlds(self) -> tuple[World, ...]:
        return tuple(self.problem.worlds[index] for index in self.viable_indices)

    @property
    def exists(self) -> bool:
        return bool(self.viable_indices)

    @property
    def policy(self) -> tuple[tuple[World, Action, World], ...]:
        """One canonical memoryless viable control selector on the kernel."""

        retained = set(self.viable_indices)
        result = []
        for world_index in self.viable_indices:
            for action_index, successor in enumerate(
                self.problem.controllable_successors[world_index]
            ):
                if successor is not None and successor in retained:
                    result.append(
                        (
                            self.problem.worlds[world_index],
                            self.problem.controllable_actions[action_index],
                            self.problem.worlds[successor],
                        )
                    )
                    break
            else:
                raise RuntimeError("controlled kernel world lacks a safe control")
        return tuple(result)

    @property
    def missing_coverage(self) -> tuple[tuple[str, tuple[Hashable, ...]], ...]:
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

    def elimination_certificate(self, world: World) -> ControlledNoGoCertificate:
        """Return a finite rank-decreasing AND/OR certificate for one removed world."""

        try:
            index = self.problem.worlds.index(world)
        except ValueError as error:
            raise ValueError("unknown ambient world") from error
        if index in self.viable_indices:
            raise ValueError("viable worlds have no elimination certificate")

        def build(current_index: int) -> ControlledNoGoCertificate:
            reason = self.elimination_reasons[current_index]
            if reason is None:
                raise RuntimeError("viable world appeared inside a no-go certificate")
            if reason.kind == "static":
                return ControlledNoGoCertificate(
                    world=self.problem.worlds[current_index],
                    round=reason.round,
                    kind=reason.kind,
                )
            if reason.kind == "uncontrollable_escape":
                assert reason.action is not None and reason.successor is not None
                successor_index = self.problem.worlds.index(reason.successor)
                child_reason = self.elimination_reasons[successor_index]
                if child_reason is None or child_reason.round >= reason.round:
                    raise RuntimeError(
                        "uncontrollable certificate ranks must strictly decrease"
                    )
                child = build(successor_index)
                return ControlledNoGoCertificate(
                    world=self.problem.worlds[current_index],
                    round=reason.round,
                    kind=reason.kind,
                    action=reason.action,
                    children=((reason.action, child),),
                )

            children = []
            for action, successor in reason.control_frontier:
                successor_index = self.problem.worlds.index(successor)
                child_reason = self.elimination_reasons[successor_index]
                if child_reason is None or child_reason.round >= reason.round:
                    raise RuntimeError(
                        "control certificate ranks must strictly decrease"
                    )
                children.append((action, build(successor_index)))
            return ControlledNoGoCertificate(
                world=self.problem.worlds[current_index],
                round=reason.round,
                kind=reason.kind,
                children=tuple(children),
            )

        return build(index)

    def coverage_elimination_certificates(
        self, component_name: str, required_label: Hashable
    ) -> tuple[ControlledNoGoCertificate, ...]:
        """Return no-go certificates for all worlds carrying one missing label."""

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
            self.elimination_certificate(self.problem.worlds[index])
            for index in candidates
        )


def maximal_controlled_common_lift(
    problem: ControlledSynchronizedLiftProblem,
) -> MaximalControlledCommonLift:
    """Compute the greatest compatible robust controlled-invariant subset.

    Each simultaneous round removes a world if one uncontrollable transition exits
    the current set or if no controllable transition remains inside it.  Finiteness
    guarantees stabilization, and the retained set admits a memoryless safe control
    selector.
    """

    current = {index for index, value in enumerate(problem.compatible) if value}
    reasons: list[ControlledEliminationReason | None] = [None] * len(problem.worlds)
    for index, value in enumerate(problem.compatible):
        if not value:
            reasons[index] = ControlledEliminationReason(round=0, kind="static")

    round_number = 1
    while True:
        removals: dict[int, ControlledEliminationReason] = {}
        for index in sorted(current):
            for action_index, successor in enumerate(
                problem.uncontrollable_successors[index]
            ):
                if successor is not None and successor not in current:
                    removals[index] = ControlledEliminationReason(
                        round=round_number,
                        kind="uncontrollable_escape",
                        action=problem.uncontrollable_actions[action_index],
                        successor=problem.worlds[successor],
                    )
                    break
            if index in removals:
                continue

            safe_control_exists = any(
                successor is not None and successor in current
                for successor in problem.controllable_successors[index]
            )
            if not safe_control_exists:
                frontier = tuple(
                    (
                        problem.controllable_actions[action_index],
                        problem.worlds[successor],
                    )
                    for action_index, successor in enumerate(
                        problem.controllable_successors[index]
                    )
                    if successor is not None
                )
                removals[index] = ControlledEliminationReason(
                    round=round_number,
                    kind="no_safe_control",
                    control_frontier=frontier,
                )

        if not removals:
            return MaximalControlledCommonLift(
                problem=problem,
                viable_indices=tuple(sorted(current)),
                elimination_reasons=tuple(reasons),
            )
        for index, reason in removals.items():
            current.remove(index)
            reasons[index] = reason
        round_number += 1
        if round_number > len(problem.worlds) + 1:
            raise RuntimeError("finite controlled-lift pruning failed to stabilize")
