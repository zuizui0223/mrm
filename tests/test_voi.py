import math

import pytest

from mrm.laws import CandidateLawFamily
from mrm.probabilistic import ProbabilisticObservationModel
from mrm.voi import rank_actions_by_value_of_information, score_action_information_value


def binary_probe_family() -> CandidateLawFamily:
    return CandidateLawFamily(
        states=(0, 1, 2, 3),
        actions=("perfect", "half_split", "uninformative"),
        transitions=tuple(
            (
                (response_type,) * 4,
                ((response_type >> 1) & 1,) * 4,
                (0,) * 4,
            )
            for response_type in range(4)
        ),
    )


def exact_model(family: CandidateLawFamily) -> ProbabilisticObservationModel:
    return ProbabilisticObservationModel.exact(family.states)


def test_expected_information_gain_ranks_exact_probe_above_half_split_and_none():
    family = binary_probe_family()
    design = rank_actions_by_value_of_information(
        family,
        exact_model(family),
        0,
        {"perfect": 0.0, "half_split": 0.0, "uninformative": 0.0},
        resolution_threshold=0.99,
    )
    values = {value.action: value for value in design.action_values}
    assert math.isclose(values["perfect"].prior_entropy_bits, 2.0)
    assert math.isclose(values["perfect"].expected_information_gain_bits, 2.0)
    assert math.isclose(values["half_split"].expected_information_gain_bits, 1.0)
    assert math.isclose(values["uninformative"].expected_information_gain_bits, 0.0)
    assert math.isclose(values["perfect"].resolution_probability, 1.0)
    assert math.isclose(values["half_split"].resolution_probability, 0.0)
    assert design.best_by_expected_information_gain.action == "perfect"


def test_net_information_gain_can_prefer_cheaper_partial_probe():
    family = binary_probe_family()
    design = rank_actions_by_value_of_information(
        family,
        exact_model(family),
        0,
        {"perfect": 3.0, "half_split": 0.25, "uninformative": 0.0},
        cost_per_bit=1.0,
        resolution_threshold=0.99,
    )
    values = {value.action: value for value in design.action_values}
    assert math.isclose(values["perfect"].net_information_gain_bits, -1.0)
    assert math.isclose(values["half_split"].net_information_gain_bits, 0.75)
    assert math.isclose(values["uninformative"].net_information_gain_bits, 0.0)
    assert design.best_by_expected_information_gain.action == "perfect"
    assert design.best_by_net_information_gain.action == "half_split"


def test_noisy_observation_reduces_expected_information_gain():
    family = binary_probe_family()
    noisy_model = ProbabilisticObservationModel(
        family.states,
        {
            0: {0: 0.8, 1: 0.1, 2: 0.1, 3: 0.0},
            1: {0: 0.1, 1: 0.8, 2: 0.1, 3: 0.0},
            2: {0: 0.1, 1: 0.1, 2: 0.8, 3: 0.0},
            3: {0: 0.1, 1: 0.1, 2: 0.0, 3: 0.8},
        },
    )
    perfect = score_action_information_value(
        family,
        noisy_model,
        0,
        "perfect",
        action_cost=0.0,
        resolution_threshold=0.75,
    )
    assert 0.0 < perfect.expected_information_gain_bits < 2.0
    assert 0.0 < perfect.resolution_probability < 1.0
    assert len(perfect.outcome_probabilities) == 4
    assert math.isclose(sum(probability for _, probability in perfect.outcome_probabilities), 1.0)


@pytest.mark.parametrize(
    "costs",
    [
        {"perfect": 0.0, "half_split": 0.0},
        {"perfect": 0.0, "half_split": 0.0, "uninformative": 0.0, "extra": 0.0},
        {"perfect": -1.0, "half_split": 0.0, "uninformative": 0.0},
        {"perfect": True, "half_split": 0.0, "uninformative": 0.0},
    ],
)
def test_value_of_information_rejects_invalid_action_costs(costs):
    family = binary_probe_family()
    with pytest.raises(ValueError):
        rank_actions_by_value_of_information(family, exact_model(family), 0, costs)


@pytest.mark.parametrize("threshold", [0.0, 1.1, True, float("inf")])
def test_value_of_information_rejects_invalid_resolution_threshold(threshold):
    family = binary_probe_family()
    with pytest.raises(ValueError):
        score_action_information_value(
            family,
            exact_model(family),
            0,
            "perfect",
            resolution_threshold=threshold,
        )
