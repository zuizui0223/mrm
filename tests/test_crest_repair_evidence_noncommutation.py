from __future__ import annotations

from mrm.crest_common_lift import ComponentCoverage
from mrm.crest_controlled_lift import ControlledSynchronizedLiftProblem
from mrm.crest_controlled_lift_relaxation import (
    ControlledLiftRelaxationCosts,
    controlled_relaxation_plan_for_subset,
    minimum_controlled_lift_relaxation,
)
from mrm.crest_joint_state import (
    AuditRefinement,
    JointCRESTContract,
    solve_joint_crest_state,
)


def _costs() -> ControlledLiftRelaxationCosts:
    problem = ControlledSynchronizedLiftProblem(
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
                ("safe", "choice", "trap"),
            ),
        ),
    )
    return ControlledLiftRelaxationCosts(
        problem=problem,
        enable_world_costs=(0, 0, 0, 0, 3),
        disable_uncontrollable_costs=((10,), (10,), (2,), (10,), (10,)),
        fallback_action="fallback",
        fallback_successors=(None, None, None, 0, None),
        install_fallback_costs=(None, None, None, 1, None),
        drop_coverage_costs=((100, 100, 5),),
    )


def _joint_contract_for_plan(plan) -> JointCRESTContract:
    """Build the declared downstream J1 contract for one repaired J7 carrier.

    The downstream future audit asks only whether a locally installed fallback is
    available. Evidence deliberately records none of those fallback distinctions,
    while the report target is constant. This isolates full-state licensing from
    target-only licensing.
    """

    kernel = plan.verified_kernel()
    ambient_indices = kernel.viable_indices
    local_index = {
        ambient_index: position
        for position, ambient_index in enumerate(ambient_indices)
    }
    installed = set(plan.installed_fallbacks)

    fallback_rows = []
    for ambient_index in ambient_indices:
        if ambient_index not in installed:
            fallback_rows.append((None,))
            continue
        successor = plan.costs.fallback_successors[ambient_index]
        assert successor is not None and successor in local_index
        fallback_rows.append((local_index[successor],))

    size = len(ambient_indices)
    same = ("same",) * size
    empty_rows = tuple(() for _ in range(size))
    audits = (
        AuditRefinement(
            "future",
            same,
            (plan.costs.fallback_action,),
            tuple(fallback_rows),
        ),
        AuditRefinement("semantic", same, (), empty_rows),
        AuditRefinement("mechanism", same, (), empty_rows),
        AuditRefinement("target", same, (), empty_rows),
    )
    return JointCRESTContract(
        worlds=kernel.worlds,
        base_labels=("base",) * size,
        evidence_labels=("one-record",) * size,
        target_labels=("one-target",) * size,
        audits=audits,
    )


def _all_feasible_plans(costs: ControlledLiftRelaxationCosts):
    count = len(costs.problem.worlds)
    for mask in range(1, 1 << count):
        retained = tuple(index for index in range(count) if mask & (1 << index))
        plan = controlled_relaxation_plan_for_subset(costs, retained)
        if plan is not None:
            yield plan


def test_cheapest_carrier_repair_need_not_be_cheapest_licensed_repair() -> None:
    costs = _costs()
    structural = minimum_controlled_lift_relaxation(costs)
    assert structural.minimum_cost == 1
    assert structural.unique

    cheapest = structural.canonical_plan
    cheapest_state = solve_joint_crest_state(_joint_contract_for_plan(cheapest))
    assert cheapest.retained_worlds == ("safe", "choice", "trapped")
    assert cheapest.installed_fallbacks == (3,)
    assert cheapest_state.state_count == 2
    assert not cheapest_state.full_state_licensed
    assert cheapest_state.target_report_licensed

    evaluated = []
    for plan in _all_feasible_plans(costs):
        state = solve_joint_crest_state(_joint_contract_for_plan(plan))
        evaluated.append((plan, state))

    licensed = [
        (plan, state) for plan, state in evaluated if state.full_state_licensed
    ]
    assert licensed
    licensed_cost = min(plan.total_cost for plan, _ in licensed)
    assert licensed_cost == 2
    assert licensed_cost > structural.minimum_cost

    minimum_licensed = [
        (plan, state)
        for plan, state in licensed
        if plan.total_cost == licensed_cost
    ]
    assert len(minimum_licensed) == 1
    plan, state = minimum_licensed[0]
    assert plan.retained_worlds == ("safe", "choice", "hazard", "trapped")
    assert plan.disabled_uncontrollable == ((2, 0),)
    assert plan.installed_fallbacks == ()
    assert state.state_count == 1
    assert state.full_state_licensed
    assert state.target_report_licensed
