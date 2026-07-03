import math
from itertools import product

from mrm.laws import CandidateLawFamily
from mrm.quotient import (
    minimal_candidate_safe_quotient,
    shortest_active_discrimination_plan,
)


def test_minimal_candidate_safe_quotient_merges_locally_irrelevant_types_only():
    family = CandidateLawFamily(
        states=(0, 1),
        actions=("act",),
        transitions=(((0, 1),), ((1, 1),)),
    )
    quotient = minimal_candidate_safe_quotient(family)
    assert quotient.full_typed_product_state_count == 4
    assert quotient.state_count == 3
    assert math.isclose(quotient.memory_bits, math.log2(3))
    assert quotient.class_of(1, 0) == quotient.class_of(1, 1)
    assert quotient.class_of(0, 0) != quotient.class_of(0, 1)
    for state in family.states:
        for response_type in range(family.response_type_count):
            quotient_state = quotient.class_of(state, response_type)
            typed_successor, _ = family.typed_transition(
                response_type, "act", state
            )
            assert quotient.successor(quotient_state, "act") == quotient.class_of(
                typed_successor, response_type
            )


def test_exhaustive_two_state_one_action_quotient_matches_future_trajectories():
    maps = tuple(product((0, 1), repeat=2))
    for first, second in product(maps, repeat=2):
        family = CandidateLawFamily(
            states=(0, 1),
            actions=("act",),
            transitions=((first,), (second,)),
        )
        quotient = minimal_candidate_safe_quotient(family)
        product_size = len(family.states) * family.response_type_count
        for state in family.states:
            for left_type in range(family.response_type_count):
                for right_type in range(family.response_type_count):
                    left_state = state
                    right_state = state
                    equivalent = True
                    for _ in range(product_size):
                        if left_state != right_state:
                            equivalent = False
                            break
                        left_state, _ = family.typed_transition(
                            left_type, "act", left_state
                        )
                        right_state, _ = family.typed_transition(
                            right_type, "act", right_state
                        )
                    assert (
                        quotient.class_of(state, left_type)
                        == quotient.class_of(state, right_type)
                    ) is equivalent


def test_shortest_active_plan_uses_observed_outcomes_to_branch():
    family = CandidateLawFamily(
        states=(0, 1),
        actions=("probe", "split"),
        transitions=(
            ((0, 0), (0, 0)),
            ((0, 0), (1, 0)),
            ((1, 1), (0, 0)),
        ),
    )
    plan = shortest_active_discrimination_plan(family, 0)
    assert plan is not None
    assert plan.action == "probe"
    assert plan.worst_case_steps == 2
    children = dict(plan.outcomes)
    assert children[1].response_types == (2,)
    assert children[0].action == "split"


def test_active_plan_is_absent_when_current_state_never_exposes_the_type():
    family = CandidateLawFamily(
        states=(0, 1),
        actions=("act",),
        transitions=(((0, 1),), ((1, 1),)),
    )
    assert shortest_active_discrimination_plan(family, 1) is None
