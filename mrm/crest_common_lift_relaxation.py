"""Exact finite minimum relaxations for CREST common-lift no-go cases.

This module continues CREST-J3.  When a declared synchronized common-lift problem
has an empty or coverage-incomplete maximal kernel, it computes the minimum-cost
contract weakening within one explicit repair language:

* admit a statically incompatible ambient tuple;
* disable one declared legal transition; or
* waive one component-coverage obligation.

The weighted subset optimization is finite and exact.  It is a contract-repair
calculus, not MLTR inherited-semantic repair and not a claim of generic novelty for
minimum-cost model repair.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .crest_common_lift import (
    ComponentCoverage,
    Label,
    MaximalCommonLift,
    SynchronizedLiftProblem,
    maximal_common_lift,
)

TransitionIndex = tuple[int, int]
CoverageObligation = tuple[str, Label]


def _cost(name: str, value: int) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return value


@dataclass(frozen=True)
class CommonLiftRelaxationCosts:
    """Integer costs for the three declared common-lift relaxation operations."""

    problem: SynchronizedLiftProblem
    enable_world_costs: tuple[int, ...]
    disable_transition_costs: tuple[tuple[int | None, ...], ...]
    drop_coverage_costs: tuple[tuple[int, ...], ...]

    def __post_init__(self) -> None:
        enable = tuple(
            _cost("enable-world cost", value) for value in self.enable_world_costs
        )
        if len(enable) != len(self.problem.worlds):
            raise ValueError("enable_world_costs must align with ambient worlds")

        disable = tuple(tuple(row) for row in self.disable_transition_costs)
        if len(disable) != len(self.problem.worlds) or any(
            len(row) != len(self.problem.actions) for row in disable
        ):
            raise ValueError(
                "disable_transition_costs must align with worlds and actions"
            )
        validated_disable: list[tuple[int | None, ...]] = []
        for world_index, row in enumerate(disable):
            values: list[int | None] = []
            for action_index, value in enumerate(row):
                successor = self.problem.successors[world_index][action_index]
                if successor is None:
                    if value is not None:
                        raise ValueError(
                            "illegal transitions must have relaxation cost None"
                        )
                    values.append(None)
                else:
                    if value is None:
                        raise ValueError(
                            "every legal transition needs a disable cost"
                        )
                    values.append(_cost("disable-transition cost", value))
            validated_disable.append(tuple(values))

        drop = tuple(tuple(row) for row in self.drop_coverage_costs)
        if len(drop) != len(self.problem.components) or any(
            len(row) != len(component.required_labels)
            for row, component in zip(drop, self.problem.components)
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
            self, "disable_transition_costs", tuple(validated_disable)
        )
        object.__setattr__(self, "drop_coverage_costs", validated_drop)

    @property
    def strictly_positive_operations(self) -> bool:
        """Whether every operation that changes the original contract costs > 0."""

        enable_positive = all(
            self.problem.compatible[index] or self.enable_world_costs[index] > 0
            for index in range(len(self.problem.worlds))
        )
        disable_positive = all(
            successor is None
            or self.disable_transition_costs[world_index][action_index] > 0
            for world_index, row in enumerate(self.problem.successors)
            for action_index, successor in enumerate(row)
        )
        drop_positive = all(
            value > 0 for row in self.drop_coverage_costs for value in row
        )
        return enable_positive and disable_positive and drop_positive


@dataclass(frozen=True)
class CommonLiftRelaxationPlan:
    """The forced least-cost operation set for one retained nonempty subset."""

    costs: CommonLiftRelaxationCosts
    retained_indices: tuple[int, ...]
    enabled_worlds: tuple[int, ...]
    disabled_transitions: tuple[TransitionIndex, ...]
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
            for action_index, successor in enumerate(problem.successors[world_index])
            if successor is not None and successor not in retained_set
        )
        if tuple(self.disabled_transitions) != expected_disabled:
            raise ValueError(
                "disabled_transitions must be exactly the outgoing retained edges"
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
            self.costs.disable_transition_costs[world_index][action_index]
            for world_index, action_index in expected_disabled
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
        object.__setattr__(self, "disabled_transitions", expected_disabled)
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
            + len(self.disabled_transitions)
            + len(self.dropped_coverage)
        )

    def repaired_problem(self) -> SynchronizedLiftProblem:
        """Apply this plan to the declared finite relaxation language."""

        problem = self.costs.problem
        compatible = list(problem.compatible)
        for index in self.enabled_worlds:
            compatible[index] = True

        successors = [list(row) for row in problem.successors]
        for world_index, action_index in self.disabled_transitions:
            successors[world_index][action_index] = None

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
        return SynchronizedLiftProblem(
            worlds=problem.worlds,
            compatible=tuple(compatible),
            actions=problem.actions,
            successors=tuple(tuple(row) for row in successors),
            components=components,
        )

    def verified_kernel(self) -> MaximalCommonLift:
        """Return the repaired maximal kernel, checking that the witness is retained."""

        repaired = self.repaired_problem()
        if not repaired.is_closed_subset(self.retained_indices):
            raise RuntimeError("relaxation plan did not make its witness closed")
        retained_set = set(self.retained_indices)
        for component in repaired.components:
            represented = {component.labels[index] for index in retained_set}
            if any(label not in represented for label in component.required_labels):
                raise RuntimeError("relaxation plan did not satisfy retained coverage")
        kernel = maximal_common_lift(repaired)
        if not kernel.admissible or not retained_set.issubset(kernel.viable_indices):
            raise RuntimeError("repaired maximal kernel failed the admissibility gate")
        return kernel


@dataclass(frozen=True)
class MinimumCommonLiftRelaxation:
    """All optimal retained-subset witnesses under one integer cost contract."""

    costs: CommonLiftRelaxationCosts
    optimal_plans: tuple[CommonLiftRelaxationPlan, ...]

    def __post_init__(self) -> None:
        plans = tuple(self.optimal_plans)
        if not plans or any(plan.costs != self.costs for plan in plans):
            raise ValueError("optimal_plans must be nonempty and share one cost contract")
        minimum = plans[0].total_cost
        if any(plan.total_cost != minimum for plan in plans):
            raise ValueError("all optimal plans must have the same total cost")
        retained = tuple(plan.retained_indices for plan in plans)
        if retained != tuple(sorted(set(retained))):
            raise ValueError("optimal plans must be unique and canonically ordered")
        object.__setattr__(self, "optimal_plans", plans)

    @property
    def minimum_cost(self) -> int:
        return self.optimal_plans[0].total_cost

    @property
    def unique(self) -> bool:
        return len(self.optimal_plans) == 1

    @property
    def canonical_plan(self) -> CommonLiftRelaxationPlan:
        """Deterministic representative; uniqueness is reported separately."""

        return self.optimal_plans[0]


def relaxation_plan_for_subset(
    costs: CommonLiftRelaxationCosts,
    retained_indices: Iterable[int],
) -> CommonLiftRelaxationPlan:
    """Return the exact forced relaxation operations for one retained subset."""

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
        for action_index, successor in enumerate(problem.successors[world_index])
        if successor is not None and successor not in retained_set
    )

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
        costs.disable_transition_costs[world_index][action_index]
        for world_index, action_index in disabled
    )
    drop_lookup = {
        (component.name, label): costs.drop_coverage_costs[component_index][
            label_index
        ]
        for component_index, component in enumerate(problem.components)
        for label_index, label in enumerate(component.required_labels)
    }
    total += sum(drop_lookup[item] for item in dropped)

    return CommonLiftRelaxationPlan(
        costs=costs,
        retained_indices=retained,
        enabled_worlds=enabled,
        disabled_transitions=disabled,
        dropped_coverage=tuple(dropped),
        total_cost=total,
    )


def minimum_common_lift_relaxation(
    costs: CommonLiftRelaxationCosts,
) -> MinimumCommonLiftRelaxation:
    """Enumerate the exact minimum over all nonempty retained ambient subsets.

    The solver is exponential in the ambient carrier size and is intended as a
    theorem oracle and finite benchmark.  For a fixed retained subset, the operation
    set is forced; the global optimum is therefore the minimum of those exact subset
    costs.
    """

    world_count = len(costs.problem.worlds)
    best_cost: int | None = None
    best: list[CommonLiftRelaxationPlan] = []
    for mask in range(1, 1 << world_count):
        retained = tuple(
            index for index in range(world_count) if mask & (1 << index)
        )
        plan = relaxation_plan_for_subset(costs, retained)
        if best_cost is None or plan.total_cost < best_cost:
            best_cost = plan.total_cost
            best = [plan]
        elif plan.total_cost == best_cost:
            best.append(plan)
    return MinimumCommonLiftRelaxation(costs=costs, optimal_plans=tuple(best))
