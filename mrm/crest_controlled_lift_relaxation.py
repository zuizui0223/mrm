"""Exact finite repairs for failed CREST controlled common-lift contracts.

This module continues CREST-J6.  Within one explicit weighted repair language it
computes the exact minimum weakening needed to obtain a nonempty coverage-complete
robustly controlled-invariant carrier:

* admit a statically incompatible ambient world;
* disable one uncontrollable transition;
* install one declared local fallback control transition; or
* waive one component-coverage obligation.

The exhaustive subset optimization is a theorem oracle, not a scalability claim and
not a claim of generic novelty for safety-game or model repair.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Iterable

from .crest_common_lift import ComponentCoverage, Label
from .crest_controlled_lift import (
    ControlledSynchronizedLiftProblem,
    MaximalControlledCommonLift,
    maximal_controlled_common_lift,
)

UncontrollableTransitionIndex = tuple[int, int]
CoverageObligation = tuple[str, Label]


def _cost(name: str, value: int) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return value


def _successor(
    name: str, value: int | None, *, world_count: int
) -> int | None:
    if value is None:
        return None
    if (
        not isinstance(value, int)
        or isinstance(value, bool)
        or not 0 <= value < world_count
    ):
        raise ValueError(f"{name} must be a world index or None")
    return value


@dataclass(frozen=True)
class ControlledLiftRelaxationCosts:
    """Costs and fallback options for the declared J6 repair language."""

    problem: ControlledSynchronizedLiftProblem
    enable_world_costs: tuple[int, ...]
    disable_uncontrollable_costs: tuple[tuple[int | None, ...], ...]
    fallback_action: Hashable
    fallback_successors: tuple[int | None, ...]
    install_fallback_costs: tuple[int | None, ...]
    drop_coverage_costs: tuple[tuple[int, ...], ...]

    def __post_init__(self) -> None:
        problem = self.problem
        try:
            hash(self.fallback_action)
        except TypeError as error:
            raise ValueError("fallback_action must be hashable") from error
        if self.fallback_action in (
            set(problem.uncontrollable_actions) | set(problem.controllable_actions)
        ):
            raise ValueError("fallback_action must be new to the controlled contract")

        enable = tuple(
            _cost("enable-world cost", value) for value in self.enable_world_costs
        )
        if len(enable) != len(problem.worlds):
            raise ValueError("enable_world_costs must align with ambient worlds")

        disable = tuple(tuple(row) for row in self.disable_uncontrollable_costs)
        if len(disable) != len(problem.worlds) or any(
            len(row) != len(problem.uncontrollable_actions) for row in disable
        ):
            raise ValueError(
                "disable_uncontrollable_costs must align with worlds and "
                "uncontrollable actions"
            )
        validated_disable: list[tuple[int | None, ...]] = []
        for world_index, row in enumerate(disable):
            values: list[int | None] = []
            for action_index, value in enumerate(row):
                successor = problem.uncontrollable_successors[world_index][
                    action_index
                ]
                if successor is None:
                    if value is not None:
                        raise ValueError(
                            "illegal uncontrollable transitions need cost None"
                        )
                    values.append(None)
                else:
                    if value is None:
                        raise ValueError(
                            "every legal uncontrollable transition needs a disable cost"
                        )
                    values.append(_cost("disable-uncontrollable cost", value))
            validated_disable.append(tuple(values))

        fallback_successors = tuple(
            _successor(
                "fallback successor",
                value,
                world_count=len(problem.worlds),
            )
            for value in self.fallback_successors
        )
        fallback_costs = tuple(self.install_fallback_costs)
        if len(fallback_successors) != len(problem.worlds) or len(
            fallback_costs
        ) != len(problem.worlds):
            raise ValueError(
                "fallback successors and costs must align with ambient worlds"
            )
        validated_fallback_costs: list[int | None] = []
        for successor, value in zip(fallback_successors, fallback_costs):
            if successor is None:
                if value is not None:
                    raise ValueError("unavailable fallback controls need cost None")
                validated_fallback_costs.append(None)
            else:
                if value is None:
                    raise ValueError("every available fallback control needs a cost")
                validated_fallback_costs.append(
                    _cost("install-fallback cost", value)
                )

        drop = tuple(tuple(row) for row in self.drop_coverage_costs)
        if len(drop) != len(problem.components) or any(
            len(row) != len(component.required_labels)
            for row, component in zip(drop, problem.components)
        ):
            raise ValueError(
                "drop_coverage_costs must align with component obligations"
            )
        validated_drop = tuple(
            tuple(_cost("drop-coverage cost", value) for value in row)
            for row in drop
        )

        object.__setattr__(self, "enable_world_costs", enable)
        object.__setattr__(
            self,
            "disable_uncontrollable_costs",
            tuple(validated_disable),
        )
        object.__setattr__(self, "fallback_successors", fallback_successors)
        object.__setattr__(
            self,
            "install_fallback_costs",
            tuple(validated_fallback_costs),
        )
        object.__setattr__(self, "drop_coverage_costs", validated_drop)

    @property
    def strictly_positive_operations(self) -> bool:
        """Whether every operation that changes the original contract costs > 0."""

        problem = self.problem
        enable_positive = all(
            problem.compatible[index] or self.enable_world_costs[index] > 0
            for index in range(len(problem.worlds))
        )
        disable_positive = all(
            successor is None
            or self.disable_uncontrollable_costs[world_index][action_index] > 0
            for world_index, row in enumerate(problem.uncontrollable_successors)
            for action_index, successor in enumerate(row)
        )
        fallback_positive = all(
            successor is None or self.install_fallback_costs[index] > 0
            for index, successor in enumerate(self.fallback_successors)
        )
        drop_positive = all(
            value > 0 for row in self.drop_coverage_costs for value in row
        )
        return (
            enable_positive
            and disable_positive
            and fallback_positive
            and drop_positive
        )


@dataclass(frozen=True)
class ControlledLiftRelaxationPlan:
    """Forced operation set for one feasible retained-world witness."""

    costs: ControlledLiftRelaxationCosts
    retained_indices: tuple[int, ...]
    enabled_worlds: tuple[int, ...]
    disabled_uncontrollable: tuple[UncontrollableTransitionIndex, ...]
    installed_fallbacks: tuple[int, ...]
    dropped_coverage: tuple[CoverageObligation, ...]
    total_cost: int

    def __post_init__(self) -> None:
        problem = self.costs.problem
        retained = tuple(self.retained_indices)
        if (
            not retained
            or retained != tuple(sorted(set(retained)))
            or any(not 0 <= index < len(problem.worlds) for index in retained)
        ):
            raise ValueError(
                "retained_indices must be a nonempty sorted set of world indices"
            )
        retained_set = set(retained)

        expected_enabled = tuple(
            index for index in retained if not problem.compatible[index]
        )
        if tuple(self.enabled_worlds) != expected_enabled:
            raise ValueError(
                "enabled_worlds must be exactly the incompatible retained worlds"
            )

        expected_disabled = tuple(
            (world_index, action_index)
            for world_index in retained
            for action_index, successor in enumerate(
                problem.uncontrollable_successors[world_index]
            )
            if successor is not None and successor not in retained_set
        )
        if tuple(self.disabled_uncontrollable) != expected_disabled:
            raise ValueError(
                "disabled_uncontrollable must be exactly the escaping "
                "uncontrollable transitions"
            )

        expected_fallbacks: list[int] = []
        for world_index in retained:
            original_safe = any(
                successor is not None and successor in retained_set
                for successor in problem.controllable_successors[world_index]
            )
            if original_safe:
                continue
            fallback_successor = self.costs.fallback_successors[world_index]
            if fallback_successor is None or fallback_successor not in retained_set:
                raise ValueError(
                    "retained witness lacks both an original safe control and an "
                    "installable fallback into the witness"
                )
            expected_fallbacks.append(world_index)
        if tuple(self.installed_fallbacks) != tuple(expected_fallbacks):
            raise ValueError(
                "installed_fallbacks must be exactly the control-deficient retained worlds"
            )

        expected_dropped: list[CoverageObligation] = []
        for component in problem.components:
            represented = {component.labels[index] for index in retained}
            expected_dropped.extend(
                (component.name, label)
                for label in component.required_labels
                if label not in represented
            )
        if tuple(self.dropped_coverage) != tuple(expected_dropped):
            raise ValueError(
                "dropped_coverage must be exactly the unrepresented obligations"
            )

        expected_cost = sum(
            self.costs.enable_world_costs[index] for index in expected_enabled
        )
        expected_cost += sum(
            self.costs.disable_uncontrollable_costs[world_index][action_index]
            for world_index, action_index in expected_disabled
        )
        expected_cost += sum(
            self.costs.install_fallback_costs[index]
            for index in expected_fallbacks
        )
        drop_lookup = {
            (component.name, label): self.costs.drop_coverage_costs[
                component_index
            ][label_index]
            for component_index, component in enumerate(problem.components)
            for label_index, label in enumerate(component.required_labels)
        }
        expected_cost += sum(drop_lookup[item] for item in expected_dropped)
        if self.total_cost != expected_cost:
            raise ValueError("total_cost does not equal the forced operation cost")

        object.__setattr__(self, "retained_indices", retained)
        object.__setattr__(self, "enabled_worlds", expected_enabled)
        object.__setattr__(
            self, "disabled_uncontrollable", expected_disabled
        )
        object.__setattr__(
            self, "installed_fallbacks", tuple(expected_fallbacks)
        )
        object.__setattr__(self, "dropped_coverage", tuple(expected_dropped))

    @property
    def retained_worlds(self) -> tuple[object, ...]:
        return tuple(
            self.costs.problem.worlds[index] for index in self.retained_indices
        )

    @property
    def operation_count(self) -> int:
        return (
            len(self.enabled_worlds)
            + len(self.disabled_uncontrollable)
            + len(self.installed_fallbacks)
            + len(self.dropped_coverage)
        )

    def repaired_problem(self) -> ControlledSynchronizedLiftProblem:
        """Apply this plan to the declared finite repair language."""

        problem = self.costs.problem
        compatible = list(problem.compatible)
        for index in self.enabled_worlds:
            compatible[index] = True

        uncontrollable_successors = [
            list(row) for row in problem.uncontrollable_successors
        ]
        for world_index, action_index in self.disabled_uncontrollable:
            uncontrollable_successors[world_index][action_index] = None

        installed = set(self.installed_fallbacks)
        controllable_actions = (
            tuple(problem.controllable_actions) + (self.costs.fallback_action,)
        )
        controllable_successors = tuple(
            tuple(row)
            + (
                self.costs.fallback_successors[world_index]
                if world_index in installed
                else None,
            )
            for world_index, row in enumerate(problem.controllable_successors)
        )

        dropped = set(self.dropped_coverage)
        components = tuple(
            ComponentCoverage(
                component.name,
                component.labels,
                tuple(
                    label
                    for label in component.required_labels
                    if (component.name, label) not in dropped
                ),
            )
            for component in problem.components
        )

        return ControlledSynchronizedLiftProblem(
            worlds=problem.worlds,
            compatible=tuple(compatible),
            uncontrollable_actions=problem.uncontrollable_actions,
            controllable_actions=controllable_actions,
            uncontrollable_successors=tuple(
                tuple(row) for row in uncontrollable_successors
            ),
            controllable_successors=controllable_successors,
            components=components,
        )

    def verified_kernel(self) -> MaximalControlledCommonLift:
        """Rerun J6 and verify that the retained witness survives and covers."""

        repaired = self.repaired_problem()
        if not repaired.is_controlled_invariant_subset(self.retained_indices):
            raise RuntimeError(
                "controlled relaxation plan did not make its witness viable"
            )
        retained_set = set(self.retained_indices)
        for component in repaired.components:
            represented = {component.labels[index] for index in retained_set}
            if any(label not in represented for label in component.required_labels):
                raise RuntimeError(
                    "controlled relaxation plan did not satisfy retained coverage"
                )
        kernel = maximal_controlled_common_lift(repaired)
        if not kernel.admissible or not retained_set.issubset(
            kernel.viable_indices
        ):
            raise RuntimeError(
                "repaired controlled kernel failed the admissibility gate"
            )
        return kernel


@dataclass(frozen=True)
class MinimumControlledLiftRelaxation:
    """All optimal feasible witnesses under one controlled repair contract."""

    costs: ControlledLiftRelaxationCosts
    optimal_plans: tuple[ControlledLiftRelaxationPlan, ...]

    def __post_init__(self) -> None:
        raw = tuple(self.optimal_plans)
        if any(plan.costs != self.costs for plan in raw):
            raise ValueError("all optimal plans must share one cost contract")
        plans = tuple(sorted(raw, key=lambda plan: plan.retained_indices))
        if plans:
            minimum = plans[0].total_cost
            if any(plan.total_cost != minimum for plan in plans):
                raise ValueError("all optimal plans must have the same total cost")
            retained = tuple(plan.retained_indices for plan in plans)
            if len(set(retained)) != len(retained):
                raise ValueError("optimal retained witnesses must be unique")
        object.__setattr__(self, "optimal_plans", plans)

    @property
    def feasible(self) -> bool:
        return bool(self.optimal_plans)

    @property
    def minimum_cost(self) -> int | None:
        return None if not self.optimal_plans else self.optimal_plans[0].total_cost

    @property
    def unique(self) -> bool:
        return len(self.optimal_plans) == 1

    @property
    def canonical_plan(self) -> ControlledLiftRelaxationPlan:
        if not self.optimal_plans:
            raise ValueError("no feasible repair exists in the declared language")
        return self.optimal_plans[0]


def controlled_relaxation_plan_for_subset(
    costs: ControlledLiftRelaxationCosts,
    retained_indices: Iterable[int],
) -> ControlledLiftRelaxationPlan | None:
    """Return the exact forced plan for a subset, or ``None`` if controls cannot be repaired."""

    problem = costs.problem
    retained = tuple(sorted(set(retained_indices)))
    if not retained or any(
        not isinstance(index, int)
        or isinstance(index, bool)
        or not 0 <= index < len(problem.worlds)
        for index in retained
    ):
        raise ValueError("retained_indices must be a nonempty valid subset")
    retained_set = set(retained)

    enabled = tuple(index for index in retained if not problem.compatible[index])
    disabled = tuple(
        (world_index, action_index)
        for world_index in retained
        for action_index, successor in enumerate(
            problem.uncontrollable_successors[world_index]
        )
        if successor is not None and successor not in retained_set
    )

    fallbacks: list[int] = []
    for world_index in retained:
        original_safe = any(
            successor is not None and successor in retained_set
            for successor in problem.controllable_successors[world_index]
        )
        if original_safe:
            continue
        fallback_successor = costs.fallback_successors[world_index]
        if fallback_successor is None or fallback_successor not in retained_set:
            return None
        fallbacks.append(world_index)

    dropped: list[CoverageObligation] = []
    for component in problem.components:
        represented = {component.labels[index] for index in retained}
        dropped.extend(
            (component.name, label)
            for label in component.required_labels
            if label not in represented
        )

    total = sum(costs.enable_world_costs[index] for index in enabled)
    total += sum(
        costs.disable_uncontrollable_costs[world_index][action_index]
        for world_index, action_index in disabled
    )
    total += sum(costs.install_fallback_costs[index] for index in fallbacks)
    drop_lookup = {
        (component.name, label): costs.drop_coverage_costs[component_index][
            label_index
        ]
        for component_index, component in enumerate(problem.components)
        for label_index, label in enumerate(component.required_labels)
    }
    total += sum(drop_lookup[item] for item in dropped)

    return ControlledLiftRelaxationPlan(
        costs=costs,
        retained_indices=retained,
        enabled_worlds=enabled,
        disabled_uncontrollable=disabled,
        installed_fallbacks=tuple(fallbacks),
        dropped_coverage=tuple(dropped),
        total_cost=total,
    )


def minimum_controlled_lift_relaxation(
    costs: ControlledLiftRelaxationCosts,
) -> MinimumControlledLiftRelaxation:
    """Enumerate the exact optimum over all feasible nonempty retained subsets."""

    world_count = len(costs.problem.worlds)
    best_cost: int | None = None
    best: list[ControlledLiftRelaxationPlan] = []
    for mask in range(1, 1 << world_count):
        retained = tuple(
            index for index in range(world_count) if mask & (1 << index)
        )
        plan = controlled_relaxation_plan_for_subset(costs, retained)
        if plan is None:
            continue
        if best_cost is None or plan.total_cost < best_cost:
            best_cost = plan.total_cost
            best = [plan]
        elif plan.total_cost == best_cost:
            best.append(plan)
    return MinimumControlledLiftRelaxation(
        costs=costs,
        optimal_plans=tuple(best),
    )
