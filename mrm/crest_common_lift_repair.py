"""Minimum local-transition relaxation for finite CREST common-lift no-go cases.

The reduction to directed minimum cut is classical network-flow substrate.  This
module turns a J3 elimination/no-go certificate into the least-cost set of local
legal transition instances that must be disabled to make one required compatible
world belong to a transition-closed common lift.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Hashable

from .crest_common_lift import (
    MaximalCommonLift,
    SynchronizedLiftProblem,
    maximal_common_lift,
)

World = Hashable
Action = Hashable
Cost = int


@dataclass(frozen=True)
class TransitionCostContract:
    """Nonnegative integer cost for disabling each legal transition instance."""

    problem: SynchronizedLiftProblem
    costs: tuple[tuple[Cost | None, ...], ...]

    def __post_init__(self) -> None:
        costs = tuple(tuple(row) for row in self.costs)
        if len(costs) != len(self.problem.worlds) or any(
            len(row) != len(self.problem.actions) for row in costs
        ):
            raise ValueError("costs must align with worlds and actions")
        for world_index, row in enumerate(costs):
            for action_index, cost in enumerate(row):
                successor = self.problem.successors[world_index][action_index]
                if successor is None:
                    if cost is not None:
                        raise ValueError("illegal actions must have cost None")
                elif (
                    not isinstance(cost, int)
                    or isinstance(cost, bool)
                    or cost < 0
                ):
                    raise ValueError(
                        "every legal transition needs a nonnegative integer cost"
                    )
        object.__setattr__(self, "costs", costs)


@dataclass(frozen=True)
class DisabledTransition:
    world: World
    action: Action
    successor: World
    cost: Cost


@dataclass(frozen=True)
class TransitionRelaxationPlan:
    """An exact minimum-cut repair for one required compatible root world."""

    contract: TransitionCostContract
    root: World
    disabled: tuple[DisabledTransition, ...]
    total_cost: Cost
    repaired_problem: SynchronizedLiftProblem
    repaired_lift: MaximalCommonLift

    def __post_init__(self) -> None:
        if self.root not in self.contract.problem.worlds:
            raise ValueError("unknown repair root")
        root_index = self.contract.problem.worlds.index(self.root)
        if not self.contract.problem.compatible[root_index]:
            raise ValueError("repair root must be statically compatible")
        if not isinstance(self.total_cost, int) or self.total_cost < 0:
            raise ValueError("total_cost must be a nonnegative integer")
        if sum(item.cost for item in self.disabled) != self.total_cost:
            raise ValueError("disabled transition costs do not match total_cost")
        if self.repaired_problem.worlds != self.contract.problem.worlds:
            raise ValueError("repair must preserve the ambient carrier")
        if root_index not in self.repaired_lift.viable_indices:
            raise ValueError("minimum-cut repair did not rescue the root")

    @property
    def root_rescued(self) -> bool:
        return self.contract.problem.worlds.index(self.root) in self.repaired_lift.viable_indices


def _residual_reachable(
    residual: list[list[int]], source: int
) -> set[int]:
    reached = {source}
    queue = deque([source])
    while queue:
        current = queue.popleft()
        for target, capacity in enumerate(residual[current]):
            if capacity > 0 and target not in reached:
                reached.add(target)
                queue.append(target)
    return reached


def _minimum_cut_reachable(
    capacity: list[list[int]], source: int, sink: int
) -> tuple[int, set[int]]:
    """Edmonds-Karp max flow and the source side of a minimum cut."""

    size = len(capacity)
    residual = [row[:] for row in capacity]
    flow = 0
    while True:
        parent = [-1] * size
        parent[source] = source
        queue = deque([source])
        while queue and parent[sink] == -1:
            current = queue.popleft()
            for target, remaining in enumerate(residual[current]):
                if remaining > 0 and parent[target] == -1:
                    parent[target] = current
                    queue.append(target)
                    if target == sink:
                        break
        if parent[sink] == -1:
            return flow, _residual_reachable(residual, source)

        bottleneck = None
        current = sink
        while current != source:
            previous = parent[current]
            remaining = residual[previous][current]
            bottleneck = remaining if bottleneck is None else min(bottleneck, remaining)
            current = previous
        assert bottleneck is not None

        current = sink
        while current != source:
            previous = parent[current]
            residual[previous][current] -= bottleneck
            residual[current][previous] += bottleneck
            current = previous
        flow += bottleneck


def minimum_transition_relaxation(
    contract: TransitionCostContract,
    root: World,
) -> TransitionRelaxationPlan:
    """Disable a minimum-cost set of local transitions that rescues ``root``.

    Feasible disabled sets are exactly directed cuts separating ``root`` from every
    statically incompatible ambient world.  The repaired common lift is recomputed
    by the J3 maximal-kernel solver.
    """

    problem = contract.problem
    try:
        root_index = problem.worlds.index(root)
    except ValueError as error:
        raise ValueError("unknown repair root") from error
    if not problem.compatible[root_index]:
        raise ValueError("repair root must be statically compatible")

    world_count = len(problem.worlds)
    sink = world_count
    capacity = [[0] * (world_count + 1) for _ in range(world_count + 1)]
    total_legal_cost = 0
    for world_index, row in enumerate(problem.successors):
        for action_index, successor in enumerate(row):
            if successor is None:
                continue
            cost = contract.costs[world_index][action_index]
            assert cost is not None
            capacity[world_index][successor] += cost
            total_legal_cost += cost

    prohibitive = total_legal_cost + 1
    for world_index, compatible in enumerate(problem.compatible):
        if not compatible:
            capacity[world_index][sink] = prohibitive

    minimum_cost, reachable = _minimum_cut_reachable(
        capacity, root_index, sink
    )

    disabled_items: list[DisabledTransition] = []
    disabled_keys: set[tuple[int, int]] = set()
    for world_index, row in enumerate(problem.successors):
        if world_index not in reachable:
            continue
        for action_index, successor in enumerate(row):
            if successor is None or successor in reachable:
                continue
            cost = contract.costs[world_index][action_index]
            assert cost is not None
            disabled_keys.add((world_index, action_index))
            disabled_items.append(
                DisabledTransition(
                    world=problem.worlds[world_index],
                    action=problem.actions[action_index],
                    successor=problem.worlds[successor],
                    cost=cost,
                )
            )

    if sum(item.cost for item in disabled_items) != minimum_cost:
        raise RuntimeError("recovered cut edges do not match max-flow value")

    repaired_successors = tuple(
        tuple(
            None if (world_index, action_index) in disabled_keys else successor
            for action_index, successor in enumerate(row)
        )
        for world_index, row in enumerate(problem.successors)
    )
    repaired_problem = SynchronizedLiftProblem(
        worlds=problem.worlds,
        compatible=problem.compatible,
        actions=problem.actions,
        successors=repaired_successors,
        components=problem.components,
    )
    repaired_lift = maximal_common_lift(repaired_problem)

    return TransitionRelaxationPlan(
        contract=contract,
        root=root,
        disabled=tuple(disabled_items),
        total_cost=minimum_cost,
        repaired_problem=repaired_problem,
        repaired_lift=repaired_lift,
    )


def minimum_label_transition_relaxation(
    contract: TransitionCostContract,
    component_name: str,
    required_label: Hashable,
) -> TransitionRelaxationPlan | None:
    """Cheapest local-transition repair rescuing at least one carrier of a label.

    Returns ``None`` when no statically compatible ambient tuple carries the
    requested label; such a failure requires changing static compatibility or the
    component mapping rather than only disabling transitions.
    """

    by_name = {
        component.name: component for component in contract.problem.components
    }
    if component_name not in by_name:
        raise ValueError("unknown component name")
    component = by_name[component_name]
    if required_label not in component.required_labels:
        raise ValueError("label is not a declared coverage obligation")

    candidates = [
        contract.problem.worlds[index]
        for index, label in enumerate(component.labels)
        if label == required_label and contract.problem.compatible[index]
    ]
    if not candidates:
        return None

    plans = [minimum_transition_relaxation(contract, root) for root in candidates]
    return min(
        plans,
        key=lambda plan: (
            plan.total_cost,
            contract.problem.worlds.index(plan.root),
        ),
    )
