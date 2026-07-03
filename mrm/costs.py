"""Exact finite active discrimination under declared positive intervention costs."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from itertools import combinations
from math import isclose, isfinite
from numbers import Real
from typing import Iterable

from .laws import Action, CandidateLawFamily, State


_COST_TOLERANCE = 1e-12


def _validated_response_types(
    family: CandidateLawFamily, response_types: Iterable[int] | None
) -> tuple[int, ...]:
    values = (
        tuple(range(family.response_type_count))
        if response_types is None
        else tuple(response_types)
    )
    if (
        not values
        or len(set(values)) != len(values)
        or any(
            not isinstance(value, int)
            or isinstance(value, bool)
            or not 0 <= value < family.response_type_count
            for value in values
        )
    ):
        raise ValueError(
            "response_types must be a nonempty subset of response-type labels"
        )
    return tuple(sorted(values))


def _validated_action_costs(
    family: CandidateLawFamily, action_costs: Mapping[Action, Real]
) -> dict[Action, float]:
    if not isinstance(action_costs, Mapping) or set(action_costs) != set(
        family.actions
    ):
        raise ValueError(
            "action_costs must assign exactly one cost to every declared action"
        )
    normalized: dict[Action, float] = {}
    for action in family.actions:
        value = action_costs[action]
        if (
            not isinstance(value, Real)
            or isinstance(value, bool)
            or not isfinite(float(value))
            or value <= 0
        ):
            raise ValueError("every declared action cost must be a finite positive number")
        normalized[action] = float(value)
    return normalized


@dataclass(frozen=True)
class CostAwareDiscriminationPlan:
    """An adaptive exact identification tree with positive intervention costs.

    The plan is conditional on a declared finite candidate family and exact observed
    macrostates. ``worst_case_cost`` is the largest total cost over its observable
    outcome branches.
    """

    state: State
    response_types: tuple[int, ...]
    action: Action | None = None
    action_cost: float = 0.0
    outcomes: tuple[tuple[State, "CostAwareDiscriminationPlan"], ...] = ()

    def __post_init__(self) -> None:
        if len(self.response_types) == 1:
            if self.action is not None or self.outcomes or self.action_cost != 0.0:
                raise ValueError(
                    "terminal cost-aware plans must have no action, outcomes, or cost"
                )
        elif (
            self.action is None
            or not self.outcomes
            or not isfinite(self.action_cost)
            or self.action_cost <= 0
        ):
            raise ValueError(
                "nonterminal cost-aware plans require a positive-cost action and outcomes"
            )

    @property
    def worst_case_cost(self) -> float:
        return (
            0.0
            if self.action is None
            else self.action_cost
            + max(child.worst_case_cost for _, child in self.outcomes)
        )

    @property
    def worst_case_steps(self) -> int:
        return (
            0
            if self.action is None
            else 1 + max(child.worst_case_steps for _, child in self.outcomes)
        )


def _strictly_better(
    candidate: CostAwareDiscriminationPlan,
    incumbent: CostAwareDiscriminationPlan | None,
) -> bool:
    """Prefer lower cost; break numerical ties by fewer worst-case steps."""
    if incumbent is None:
        return True
    candidate_cost = candidate.worst_case_cost
    incumbent_cost = incumbent.worst_case_cost
    same_cost = isclose(
        candidate_cost,
        incumbent_cost,
        rel_tol=0.0,
        abs_tol=_COST_TOLERANCE,
    )
    if candidate_cost < incumbent_cost and not same_cost:
        return True
    return same_cost and candidate.worst_case_steps < incumbent.worst_case_steps


def minimum_cost_active_discrimination_plan(
    family: CandidateLawFamily,
    state: State,
    action_costs: Mapping[Action, Real],
    response_types: Iterable[int] | None = None,
) -> CostAwareDiscriminationPlan | None:
    """Return an exact plan minimizing worst-case total action cost.

    Costs must be finite and strictly positive. The dynamic program ranges over the
    finite configurations ``Q × {S: nonempty S subseteq R}``. Strict positivity lets
    an optimal plan be chosen without revisiting a configuration on any branch; the
    search therefore reaches a fixed point after finitely many relaxations. ``None``
    means that the declared action grammar cannot identify the requested types from
    the supplied observed macrostate.
    """

    if state not in family.states:
        raise ValueError("unknown observable state")
    target = _validated_response_types(family, response_types)
    costs = _validated_action_costs(family, action_costs)
    subsets = [
        tuple(combo)
        for size in range(1, family.response_type_count + 1)
        for combo in combinations(range(family.response_type_count), size)
    ]
    configurations = [
        (macrostate, subset) for macrostate in family.states for subset in subsets
    ]
    plans: dict[tuple[State, tuple[int, ...]], CostAwareDiscriminationPlan] = {
        (macrostate, (response_type,)): CostAwareDiscriminationPlan(
            macrostate, (response_type,)
        )
        for macrostate in family.states
        for response_type in range(family.response_type_count)
    }
    for _ in range(len(configurations)):
        current = plans
        updated = dict(current)
        changed = False
        for macrostate, subset in configurations:
            if len(subset) == 1:
                continue
            best = current.get((macrostate, subset))
            for action in family.actions:
                grouped: dict[State, list[int]] = {}
                for response_type in subset:
                    successor_state, _ = family.typed_transition(
                        response_type, action, macrostate
                    )
                    grouped.setdefault(successor_state, []).append(response_type)
                children: list[tuple[State, CostAwareDiscriminationPlan]] = []
                for observed_state in family.states:
                    group = grouped.get(observed_state)
                    if not group:
                        continue
                    child = current.get((observed_state, tuple(group)))
                    if child is None:
                        break
                    children.append((observed_state, child))
                else:
                    candidate = CostAwareDiscriminationPlan(
                        macrostate,
                        subset,
                        action,
                        costs[action],
                        tuple(children),
                    )
                    if _strictly_better(candidate, best):
                        best = candidate
            key = (macrostate, subset)
            if best is not None and best != current.get(key):
                updated[key] = best
                changed = True
        plans = updated
        if not changed:
            break
    return plans.get((state, target))
