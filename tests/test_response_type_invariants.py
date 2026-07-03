import math

from mrm.joint import JointUncertaintyFamily
from mrm.laws import CandidateLawFamily


def test_response_type_count_is_invariant_to_duplicate_candidate_order():
    first = CandidateLawFamily(
        states=(0, 1),
        actions=("a",),
        transitions=(((0, 1),), ((1, 0),), ((0, 1),)),
    )
    second = CandidateLawFamily(
        states=(0, 1),
        actions=("a",),
        transitions=(((1, 0),), ((0, 1),), ((0, 1),)),
    )
    assert first.response_type_count == second.response_type_count == 2
    assert first.set_valued_transition("a", 0) == second.set_valued_transition("a", 0) == frozenset({0, 1})


def test_joint_bit_formula_is_stable_for_nonbinary_cardinalities():
    family = JointUncertaintyFamily(
        inside_cardinality=3,
        exterior_cardinalities=(3, 5),
        response_type_count=2,
    )
    assert family.joint_state_count == 90
    assert math.isclose(family.joint_safe_memory_bits, math.log2(90))
    assert family.verify()
