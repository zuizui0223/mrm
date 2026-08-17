from __future__ import annotations

from itertools import combinations

from mrm.crest_common_lift import ComponentCoverage, SynchronizedLiftProblem
from mrm.crest_common_lift_relaxation import (
    CommonLiftRelaxationCosts,
    minimum_common_lift_relaxation,
)
from mrm.crest_controlled_lift import ControlledSynchronizedLiftProblem
from mrm.crest_controlled_lift_relaxation import (
    ControlledLiftRelaxationCosts,
    minimum_controlled_lift_relaxation,
)


WORLDS = ("ab", "bc", "a")
SET_MEMBERS = (
    frozenset({"a", "b"}),
    frozenset({"b", "c"}),
    frozenset({"a"}),
)
SET_COSTS = (2, 2, 1)
UNIVERSE = frozenset({"a", "b", "c"})
BUDGET = 3
WAIVER_PENALTY = BUDGET + 1


def _components() -> tuple[ComponentCoverage, ...]:
    return tuple(
        ComponentCoverage(
            name=f"element-{element}",
            labels=tuple(1 if element in members else 0 for members in SET_MEMBERS),
            required_labels=(1,),
        )
        for element in sorted(UNIVERSE)
    )


def _set_cover_optimum() -> tuple[int, tuple[int, ...]]:
    best_cost: int | None = None
    best_indices: tuple[int, ...] | None = None
    for width in range(1, len(SET_MEMBERS) + 1):
        for chosen in combinations(range(len(SET_MEMBERS)), width):
            covered = frozenset().union(*(SET_MEMBERS[index] for index in chosen))
            if covered != UNIVERSE:
                continue
            cost = sum(SET_COSTS[index] for index in chosen)
            if best_cost is None or cost < best_cost:
                best_cost = cost
                best_indices = chosen
    assert best_cost is not None and best_indices is not None
    return best_cost, best_indices


def _j4_costs() -> CommonLiftRelaxationCosts:
    problem = SynchronizedLiftProblem(
        worlds=WORLDS,
        compatible=(False,) * len(WORLDS),
        actions=(),
        successors=tuple(() for _ in WORLDS),
        components=_components(),
    )
    return CommonLiftRelaxationCosts(
        problem=problem,
        enable_world_costs=SET_COSTS,
        disable_transition_costs=tuple(() for _ in WORLDS),
        drop_coverage_costs=tuple((WAIVER_PENALTY,) for _ in UNIVERSE),
    )


def _j7_costs() -> ControlledLiftRelaxationCosts:
    problem = ControlledSynchronizedLiftProblem(
        worlds=WORLDS,
        compatible=(False,) * len(WORLDS),
        uncontrollable_actions=(),
        controllable_actions=("stay",),
        uncontrollable_successors=tuple(() for _ in WORLDS),
        controllable_successors=tuple((index,) for index in range(len(WORLDS))),
        components=_components(),
    )
    return ControlledLiftRelaxationCosts(
        problem=problem,
        enable_world_costs=SET_COSTS,
        disable_uncontrollable_costs=tuple(() for _ in WORLDS),
        fallback_action="fallback",
        fallback_successors=(None,) * len(WORLDS),
        install_fallback_costs=(None,) * len(WORLDS),
        drop_coverage_costs=tuple((WAIVER_PENALTY,) for _ in UNIVERSE),
    )


def test_j4_exact_oracle_contains_weighted_set_cover() -> None:
    cover_cost, cover_indices = _set_cover_optimum()
    result = minimum_common_lift_relaxation(_j4_costs())

    assert cover_cost == BUDGET
    assert cover_indices == (1, 2)
    assert result.minimum_cost == cover_cost
    assert result.unique
    assert result.canonical_plan.retained_indices == cover_indices
    assert result.canonical_plan.retained_worlds == ("bc", "a")
    assert result.canonical_plan.dropped_coverage == ()
    assert result.canonical_plan.disabled_transitions == ()


def test_j7_exact_oracle_contains_weighted_set_cover() -> None:
    cover_cost, cover_indices = _set_cover_optimum()
    result = minimum_controlled_lift_relaxation(_j7_costs())

    assert result.feasible
    assert result.minimum_cost == cover_cost
    assert result.unique
    assert result.canonical_plan.retained_indices == cover_indices
    assert result.canonical_plan.retained_worlds == ("bc", "a")
    assert result.canonical_plan.dropped_coverage == ()
    assert result.canonical_plan.disabled_uncontrollable == ()
    assert result.canonical_plan.installed_fallbacks == ()
