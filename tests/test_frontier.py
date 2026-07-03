import math

import pytest

from mrm.frontier import BinarySignatureFrontier, binary_signature_frontier
from mrm.quotient import shortest_active_discrimination_plan


def test_binary_signature_frontier_has_exact_state_and_memory_scaling():
    for width in range(1, 6):
        frontier = BinarySignatureFrontier(width)
        family = frontier.family()
        assert family.response_type_count == 2**width
        assert family.response_separated()
        assert frontier.candidate_safe_state_count == 2 ** (width + 1)
        assert math.isclose(frontier.fixed_candidate_memory_bits, 1.0)
        assert math.isclose(frontier.candidate_safe_memory_bits, width + 1)
        assert math.isclose(frontier.ambiguity_memory_surcharge_bits, width)
        assert frontier.information_lower_bound_steps == width
        assert frontier.verify()


def test_canonical_probe_schedule_identifies_each_binary_response_signature():
    frontier = BinarySignatureFrontier(4)
    observations = {
        frontier.observations(response_type)
        for response_type in range(frontier.candidate_count)
    }
    assert observations == {
        frontier.signature(response_type)
        for response_type in range(frontier.candidate_count)
    }
    assert len(observations) == frontier.candidate_count
    assert [
        frontier.remaining_candidate_count_after_probes(probe_count)
        for probe_count in range(5)
    ] == [16, 8, 4, 2, 1]


def test_generic_active_planner_reaches_the_frontier_lower_bound_for_width_three():
    frontier = BinarySignatureFrontier(3)
    plan = shortest_active_discrimination_plan(frontier.family(), 0)
    assert plan is not None
    assert plan.worst_case_steps == frontier.information_lower_bound_steps


def test_frontier_records_are_deterministic_and_monotone():
    records = [point.replay_record() for point in binary_signature_frontier(4)]
    assert [record["response_type_count"] for record in records] == [2, 4, 8, 16]
    assert [record["candidate_safe_state_count"] for record in records] == [4, 8, 16, 32]
    assert [record["ambiguity_memory_surcharge_bits"] for record in records] == [1.0, 2.0, 3.0, 4.0]
    assert [record["optimal_identification_steps"] for record in records] == [1, 2, 3, 4]


@pytest.mark.parametrize("invalid", [0, -1, True, 1.5])
def test_frontier_rejects_invalid_width(invalid):
    with pytest.raises(ValueError):
        BinarySignatureFrontier(invalid)
