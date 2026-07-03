import math

import pytest

from mrm.costs import minimum_cost_active_discrimination_plan
from mrm.laws import CandidateLawFamily
from mrm.quotient import shortest_active_discrimination_plan


def cost_tradeoff_family() -> CandidateLawFamily:
    return CandidateLawFamily(
        states=(0, 1, 2, 3),
        actions=("direct", "cheap_high_bit", "cheap_low_bit"),
        transitions=tuple(
            (
                (response_type,) * 4,
                ((response_type >> 1) & 1,) * 4,
                (2 + (response_type & 1),) * 4,
            )
            for response_type in range(4)
        ),
    )


def test_cost_aware_plan_prefers_two_cheap_probes_to_one_expensive_direct_probe():
    family = cost_tradeoff_family()
    shortest = shortest_active_discrimination_plan(family, 0)
    cheapest = minimum_cost_active_discrimination_plan(
        family,
        0,
        {"direct": 5.0, "cheap_high_bit": 1.0, "cheap_low_bit": 1.0},
    )
    assert shortest is not None
    assert shortest.action == "direct"
    assert shortest.worst_case_steps == 1
    assert cheapest is not None
    assert cheapest.action == "cheap_high_bit"
    assert cheapest.worst_case_steps == 2
    assert math.isclose(cheapest.worst_case_cost, 2.0)
    children = dict(cheapest.outcomes)
    assert children[0].response_types == (0, 1)
    assert children[1].response_types == (2, 3)
    assert all(child.action == "cheap_low_bit" for child in children.values())


def test_unit_costs_recover_the_shortest_worst_case_depth():
    family = CandidateLawFamily(
        states=(0, 1),
        actions=("probe", "split"),
        transitions=(
            ((0, 0), (0, 0)),
            ((0, 0), (1, 0)),
            ((1, 1), (0, 0)),
        ),
    )
    shortest = shortest_active_discrimination_plan(family, 0)
    cheapest = minimum_cost_active_discrimination_plan(
        family, 0, {"probe": 1.0, "split": 1.0}
    )
    assert shortest is not None
    assert cheapest is not None
    assert cheapest.worst_case_steps == shortest.worst_case_steps == 2
    assert math.isclose(cheapest.worst_case_cost, 2.0)


def test_cost_aware_plan_returns_none_when_types_remain_inseparable():
    family = CandidateLawFamily(
        states=(0, 1),
        actions=("act",),
        transitions=(((0, 1),), ((1, 1),)),
    )
    assert minimum_cost_active_discrimination_plan(
        family, 1, {"act": 1.0}
    ) is None


@pytest.mark.parametrize(
    "costs",
    [
        {"direct": 1.0},
        {"direct": 1.0, "cheap_high_bit": 1.0, "extra": 1.0},
        {"direct": 0.0, "cheap_high_bit": 1.0, "cheap_low_bit": 1.0},
        {"direct": -1.0, "cheap_high_bit": 1.0, "cheap_low_bit": 1.0},
        {"direct": float("inf"), "cheap_high_bit": 1.0, "cheap_low_bit": 1.0},
        {"direct": True, "cheap_high_bit": 1.0, "cheap_low_bit": 1.0},
    ],
)
def test_cost_aware_planner_rejects_invalid_action_costs(costs):
    with pytest.raises(ValueError):
        minimum_cost_active_discrimination_plan(cost_tradeoff_family(), 0, costs)
