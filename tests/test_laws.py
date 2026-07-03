import math

import pytest

from mrm.laws import CandidateLawFamily, candidate_safe_memory_bits


def test_duplicate_candidates_collapse_to_one_universal_response_type():
    family = CandidateLawFamily(
        states=(0, 1),
        actions=("act",),
        transitions=(((0, 1),), ((0, 1),)),
    )
    assert family.universal
    assert family.response_type_labels == (0, 0)
    assert family.response_type_count == 1
    assert family.universal_transition("act", 1) == 1
    assert family.set_valued_transition("act", 0) == frozenset({0})


def test_disagreeing_candidates_require_typed_or_set_valued_report():
    family = CandidateLawFamily(
        states=(0, 1),
        actions=("passive", "intervene"),
        transitions=(
            ((0, 1), (0, 1)),
            ((0, 1), (1, 0)),
        ),
    )
    assert not family.universal
    assert family.response_type_count == 2
    assert family.report_kind() == "typed-or-set-valued"
    assert family.set_valued_transition("intervene", 0) == frozenset({0, 1})
    assert family.typed_transition(1, "intervene", 0) == (1, 1)
    assert family.response_separated()
    assert math.isclose(candidate_safe_memory_bits(family), 2.0)
    with pytest.raises(ValueError):
        family.universal_transition("intervene", 0)


def test_product_bound_requires_uniform_response_separation():
    family = CandidateLawFamily(
        states=(0, 1),
        actions=("act",),
        transitions=(((0, 1),), ((1, 1),)),
    )
    assert family.response_type_count == 2
    assert not family.response_separated()
    with pytest.raises(ValueError):
        candidate_safe_memory_bits(family)
