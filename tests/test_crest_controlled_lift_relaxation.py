from __future__ import annotations

import pytest

from mrm.crest_common_lift import ComponentCoverage
from mrm.crest_controlled_lift import (
    ControlledSynchronizedLiftProblem,
    maximal_controlled_common_lift,
)
from mrm.crest_controlled_lift_relaxation import (
    ControlledLiftRelaxationCosts,
    controlled_relaxation_plan_for_subset,
    minimum_controlled_lift_relaxation,
)


def _problem(*, require_trap: bool = True) -> ControlledSynchronizedLiftProblem:
    required = ("safe", "choice", "trap") if require_trap else ("safe", "choice")
    return ControlledSynchronizedLiftProblem(
        worlds=("safe", "choice", "hazard", "trapped", "bad"),
        compatible=(True, True, True, True, False),
        uncontrollable_actions=("weather",),
        controllable_actions=("protect", "exploit"),
        uncontrollable_successors=((0,), (1,), (4,), (3,), (4,)),
        controllable_successors=(
            (0, 0),
            (0, 4),
            (2, 2),
            (2, 4),
            (4, 4),
        ),
        components=(
            ComponentCoverage(
                "role",
                ("safe", "choice", "hazard", "trap", "bad"),
                required,
            ),
        ),
    )


def _costs(
    *,
    require_trap: bool = True,
    fallback_cost: int = 1,
    hazard_cut_cost: int = 2,
    bad_enable_cost: int = 3,
    trap_drop_cost: int = 5,
) -> ControlledLiftRelaxationCosts:
    problem = _problem(require_trap=require_trap)
    drop = (
        (100, 100, trap_drop_cost)
        if require_trap
        else (100, 100)
    )
    return ControlledLiftRelaxationCosts(
        problem=problem,
        enable_world_costs=(0, 0, 0, 0, bad_enable_cost),
        disable_uncontrollable_costs=(
            (10,),
            (10,),
            (hazard_cut_cost,),
            (10,),
            (10,),
        ),
        fallback_action="fallback",
        fallback_successors=(None, None, None, 0, None),
        install_fallback_costs=(None, None, None, fallback_cost, None),
        drop_coverage_costs=(drop,),
    )


def test_unique_optimum_installs_local_fallback_control() -> None:
    result = minimum_controlled_lift_relaxation(_costs())

    assert result.feasible
    assert result.minimum_cost == 1
    assert result.unique
    plan = result.canonical_plan
    assert plan.retained_worlds == ("safe", "choice", "trapped")
    assert plan.enabled_worlds == ()
    assert plan.disabled_uncontrollable == ()
    assert plan.installed_fallbacks == (3,)
    assert plan.dropped_coverage == ()
    assert plan.operation_count == 1

    kernel = plan.verified_kernel()
    assert kernel.admissible
    assert set(plan.retained_indices).issubset(kernel.viable_indices)
    assert kernel.worlds == ("safe", "choice", "trapped")
    assert ("trapped", "fallback", "safe") in kernel.policy


def test_equal_cost_cut_and_fallback_produce_two_optimal_repairs() -> None:
    result = minimum_controlled_lift_relaxation(
        _costs(fallback_cost=2, hazard_cut_cost=2)
    )

    assert result.feasible
    assert result.minimum_cost == 2
    assert not result.unique
    assert tuple(plan.retained_worlds for plan in result.optimal_plans) == (
        ("safe", "choice", "trapped"),
        ("safe", "choice", "hazard", "trapped"),
    )

    fallback_plan, cut_plan = result.optimal_plans
    assert fallback_plan.installed_fallbacks == (3,)
    assert fallback_plan.disabled_uncontrollable == ()
    assert cut_plan.installed_fallbacks == ()
    assert cut_plan.disabled_uncontrollable == ((2, 0),)
    assert all(plan.verified_kernel().admissible for plan in result.optimal_plans)


def test_zero_cost_is_equivalent_to_original_admissibility_under_positive_changes() -> None:
    costs = _costs(require_trap=False)
    original = maximal_controlled_common_lift(costs.problem)
    result = minimum_controlled_lift_relaxation(costs)

    assert costs.strictly_positive_operations
    assert original.admissible
    assert result.minimum_cost == 0
    assert result.canonical_plan.retained_worlds == ("safe", "choice")
    assert result.canonical_plan.operation_count == 0


def test_increasing_one_declared_cost_cannot_lower_the_optimum() -> None:
    low = minimum_controlled_lift_relaxation(_costs(fallback_cost=1))
    high = minimum_controlled_lift_relaxation(_costs(fallback_cost=4))

    assert low.minimum_cost == 1
    assert high.minimum_cost == 2
    assert high.minimum_cost >= low.minimum_cost
    assert high.canonical_plan.disabled_uncontrollable == ((2, 0),)


def test_fixed_subset_plan_is_forced_and_infeasible_subsets_return_none() -> None:
    costs = _costs()

    fallback_plan = controlled_relaxation_plan_for_subset(costs, (0, 1, 3))
    assert fallback_plan is not None
    assert fallback_plan.installed_fallbacks == (3,)
    assert fallback_plan.total_cost == 1

    cut_plan = controlled_relaxation_plan_for_subset(costs, (0, 1, 2, 3))
    assert cut_plan is not None
    assert cut_plan.disabled_uncontrollable == ((2, 0),)
    assert cut_plan.total_cost == 2

    assert controlled_relaxation_plan_for_subset(costs, (3,)) is None


def test_declared_language_can_be_infeasible() -> None:
    problem = ControlledSynchronizedLiftProblem(
        worlds=("blocked",),
        compatible=(True,),
        uncontrollable_actions=(),
        controllable_actions=("act",),
        uncontrollable_successors=((),),
        controllable_successors=((None,),),
        components=(ComponentCoverage("role", ("blocked",), ()),),
    )
    costs = ControlledLiftRelaxationCosts(
        problem=problem,
        enable_world_costs=(0,),
        disable_uncontrollable_costs=((),),
        fallback_action="fallback",
        fallback_successors=(None,),
        install_fallback_costs=(None,),
        drop_coverage_costs=((),),
    )
    result = minimum_controlled_lift_relaxation(costs)

    assert not result.feasible
    assert result.minimum_cost is None
    assert not result.unique
    with pytest.raises(ValueError, match="no feasible repair"):
        _ = result.canonical_plan


def test_admitting_bad_world_is_a_valid_but_nonoptimal_repair() -> None:
    costs = _costs()
    plan = controlled_relaxation_plan_for_subset(costs, (0, 1, 2, 3, 4))

    assert plan is not None
    assert plan.enabled_worlds == (4,)
    assert plan.disabled_uncontrollable == ()
    assert plan.installed_fallbacks == ()
    assert plan.total_cost == 3
    assert plan.verified_kernel().worlds == costs.problem.worlds


def test_cost_contract_validation() -> None:
    problem = _problem()

    with pytest.raises(ValueError, match="fallback_action must be new"):
        ControlledLiftRelaxationCosts(
            problem=problem,
            enable_world_costs=(0, 0, 0, 0, 1),
            disable_uncontrollable_costs=((1,),) * 5,
            fallback_action="protect",
            fallback_successors=(None,) * 5,
            install_fallback_costs=(None,) * 5,
            drop_coverage_costs=((1, 1, 1),),
        )

    with pytest.raises(ValueError, match="every available fallback control needs a cost"):
        ControlledLiftRelaxationCosts(
            problem=problem,
            enable_world_costs=(0, 0, 0, 0, 1),
            disable_uncontrollable_costs=((1,),) * 5,
            fallback_action="fallback",
            fallback_successors=(None, None, None, 0, None),
            install_fallback_costs=(None,) * 5,
            drop_coverage_costs=((1, 1, 1),),
        )
