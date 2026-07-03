import math

import pytest

from mrm.joint import JointUncertaintyFamily, joint_safe_memory_bits


def test_joint_family_adds_only_under_declared_joint_separation_contract():
    family = JointUncertaintyFamily(
        inside_cardinality=4,
        exterior_cardinalities=(2, 4),
        response_type_count=4,
    )
    assert family.joint_state_count == 128
    assert math.isclose(family.fixed_candidate_memory_bits, 5.0)
    assert math.isclose(family.joint_safe_memory_bits, 7.0)
    assert family.verify()
    assert math.isclose(joint_safe_memory_bits(4, (2, 4), 4), 7.0)


def test_canonical_joint_witness_requires_large_enough_inside_register():
    with pytest.raises(ValueError):
        JointUncertaintyFamily(inside_cardinality=2, exterior_cardinalities=(2,), response_type_count=3)
