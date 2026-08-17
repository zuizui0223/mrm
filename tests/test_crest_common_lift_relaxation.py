from __future__ import annotations

import pytest

from mrm.crest_common_lift import (
    ComponentCoverage,
    SynchronizedLiftProblem,
    maximal_common_lift,
)
from mrm.crest_common_lift_relaxation import (
    CommonLiftRelaxationCosts,
    minimum_common_lift_relaxation,
    relaxation_plan_for_subset,
)


def _cascade_problem(
    *,
    required: tuple[str, ...] = ("f0", "stable"),
    stable_to_bad: bool = False,
) -> SynchronizedLiftProblem:
    worlds = ("w0", "w1", "w2", "stable", "bad")
    successors = (
        (1,),
        (2,),
        (4,),
        ((4,) if stable_to_bad else (3,)),
        (4,),
    )
    return SynchronizedLiftProblem(
        worlds=worlds,
        compatible=(True, True, True, True, False),
        actions=("step",),
        successors=successors,
        components=(
            ComponentCoverage(
                "future",
                ("f0", "f1", "f2", "stable", "bad"),
                required,
            ),
        ),
    )


def _costs(
    problem: SynchronizedLiftProblem,
    *,
    enable_bad: int = 2,
    edge_costs: tuple[int, ...] = (10, 10, 1, 10, 10),
    drop_costs: tuple[int, ...] | None = None,
) -> CommonLiftRelaxationCosts:
    if drop_costs is None:
        drop_costs = tuple(
            5 for _ in problem.components[0].required_labels
        )
    return CommonLiftRelaxationCosts(
        problem=problem,
        enable_world_costs=(0, 0, 0, 0, enable_bad),
        disable_transition_costs=tuple((value,) for value in edge_costs),
        drop_coverage_costs=(drop_costs,),
    )


def test_unique_minimum_repairs_coverage_by_cutting_one_transition() -> None:
    problem = _cascade_problem()
    original = maximal_common_lift(problem)
    assert original.worlds == ("stable",)
    assert not original.coverage_complete

    result = minimum_common_lift_relaxation(_costs(problem))

    assert result.minimum_cost == 1
    assert result.unique
    plan = result.canonical_plan
    assert plan.retained_worlds == ("w0", "w1", "w2", "stable")
    assert plan.enabled_worlds == ()
    assert plan.disabled_transitions == ((2, 0),)
    assert plan.dropped_coverage == ()
    assert plan.operation_count == 1

    repaired = plan.verified_kernel()
    assert repaired.admissible
    assert set(plan.retained_worlds).issubset(repaired.worlds)


def test_fixed_subset_operation_set_is_forced_and_sufficient() -> None:
    problem = _cascade_problem()
    costs = _costs(problem)

    for mask in range(1, 1 << len(problem.worlds)):
        retained = tuple(
            index
            for index in range(len(problem.worlds))
            if mask & (1 << index)
        )
        plan = relaxation_plan_for_subset(costs, retained)
        repaired = plan.repaired_problem()

        assert repaired.is_closed_subset(retained)
        assert plan.verified_kernel().admissible
        assert set(retained).issubset(plan.verified_kernel().viable_indices)


def test_positive_cost_zero_if_and_only_if_original_problem_is_admissible() -> None:
    no_go_problem = _cascade_problem()
    no_go_costs = _costs(no_go_problem)
    assert no_go_costs.strictly_positive_operations
    assert not maximal_common_lift(no_go_problem).admissible
    assert minimum_common_lift_relaxation(no_go_costs).minimum_cost > 0

    admissible_problem = _cascade_problem(required=("stable",))
    admissible_costs = _costs(admissible_problem, drop_costs=(5,))
    assert admissible_costs.strictly_positive_operations
    assert maximal_common_lift(admissible_problem).admissible
    assert minimum_common_lift_relaxation(admissible_costs).minimum_cost == 0


def test_distinct_contract_repairs_can_tie_at_the_same_minimum_cost() -> None:
    problem = _cascade_problem()
    result = minimum_common_lift_relaxation(
        _costs(problem, enable_bad=1)
    )

    assert result.minimum_cost == 1
    assert not result.unique
    witnesses = {
        (
            plan.retained_worlds,
            plan.enabled_worlds,
            plan.disabled_transitions,
            plan.dropped_coverage,
        )
        for plan in result.optimal_plans
    }
    assert witnesses == {
        (
            ("w0", "w1", "w2", "stable"),
            (),
            ((2, 0),),
            (),
        ),
        (
            ("w0", "w1", "w2", "stable", "bad"),
            (4,),
            (),
            (),
        ),
    }


def test_empty_kernel_can_be_recovered_by_the_cheapest_declared_operation() -> None:
    problem = _cascade_problem(required=("stable",), stable_to_bad=True)
    assert not maximal_common_lift(problem).exists

    result = minimum_common_lift_relaxation(
        _costs(
            problem,
            enable_bad=3,
            edge_costs=(10, 10, 10, 1, 10),
            drop_costs=(8,),
        )
    )

    assert result.minimum_cost == 1
    plan = result.canonical_plan
    assert plan.retained_worlds == ("stable",)
    assert plan.disabled_transitions == ((3, 0),)
    assert plan.verified_kernel().admissible


def test_cost_contract_rejects_misaligned_or_illegal_operation_costs() -> None:
    problem = _cascade_problem()

    with pytest.raises(ValueError, match="enable_world_costs"):
        CommonLiftRelaxationCosts(
            problem,
            (0,),
            tuple((1,) for _ in problem.worlds),
            ((1, 1),),
        )

    illegal_problem = SynchronizedLiftProblem(
        worlds=("x",),
        compatible=(True,),
        actions=("a",),
        successors=((None,),),
        components=(ComponentCoverage("c", ("x",), ("x",)),),
    )
    with pytest.raises(ValueError, match="illegal transitions"):
        CommonLiftRelaxationCosts(
            illegal_problem,
            (0,),
            ((1,),),
            ((1,),),
        )
