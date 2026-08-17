from mrm.crest_common_lift import ComponentCoverage, SynchronizedLiftProblem
from mrm.crest_common_lift_relaxation import (
    CommonLiftRelaxationCosts,
    minimum_common_lift_relaxation,
)


def test_all_equal_cost_witnesses_are_returned_in_canonical_order() -> None:
    problem = SynchronizedLiftProblem(
        worlds=("x", "y"),
        compatible=(True, True),
        actions=(),
        successors=((), ()),
        components=(
            ComponentCoverage("component", ("same", "same"), ("same",)),
        ),
    )
    costs = CommonLiftRelaxationCosts(
        problem=problem,
        enable_world_costs=(0, 0),
        disable_transition_costs=((), ()),
        drop_coverage_costs=((1,),),
    )

    result = minimum_common_lift_relaxation(costs)

    assert result.minimum_cost == 0
    assert not result.unique
    assert tuple(plan.retained_indices for plan in result.optimal_plans) == (
        (0,),
        (0, 1),
        (1,),
    )
