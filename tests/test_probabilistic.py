import math

import pytest

from mrm.laws import CandidateLawFamily
from mrm.probabilistic import (
    ProbabilisticObservationModel,
    posterior_observation_update,
    posterior_set_valued_successor,
)


def direct_four_type_family() -> CandidateLawFamily:
    return CandidateLawFamily(
        states=(0, 1, 2, 3),
        actions=("direct", "flip"),
        transitions=tuple(
            (
                (response_type,) * 4,
                ((response_type + 1) % 4,) * 4,
            )
            for response_type in range(4)
        ),
    )


def test_exact_likelihood_update_recovers_single_response_type():
    family = direct_four_type_family()
    update = posterior_observation_update(
        family,
        ProbabilisticObservationModel.exact(family.states),
        0,
        "direct",
        2,
    )
    assert update is not None
    assert update.posterior == ((0, 0.0), (1, 0.0), (2, 1.0), (3, 0.0))
    assert update.map_response_types == (2,)
    assert update.resolved_at(0.99)
    assert math.isclose(update.entropy_bits, 0.0)
    assert posterior_set_valued_successor(family, update, 0, "flip") == frozenset({3})


def test_noisy_likelihood_updates_posterior_without_forcing_resolution():
    family = direct_four_type_family()
    model = ProbabilisticObservationModel(
        family.states,
        {
            0: {0: 0.70, 1: 0.20, 2: 0.10, 3: 0.00},
            1: {0: 0.10, 1: 0.60, 2: 0.20, 3: 0.10},
            2: {0: 0.05, 1: 0.25, 2: 0.60, 3: 0.10},
            3: {0: 0.00, 1: 0.10, 2: 0.20, 3: 0.70},
        },
    )
    update = posterior_observation_update(family, model, 0, "direct", 1)
    assert update is not None
    posterior = dict(update.posterior)
    assert math.isclose(update.evidence_probability, 0.2875)
    assert update.map_response_types == (1,)
    assert math.isclose(posterior[1], 0.60 / 1.15)
    assert not update.resolved_at(0.90)
    assert update.resolved_at(0.50)
    assert update.credible_set(0.70) == (1, 2)
    assert update.credible_set(0.75) == (1, 2, 0)
    assert posterior_set_valued_successor(family, update, 0, "flip") == frozenset({1, 2, 3, 0})


def test_prior_distribution_changes_the_posterior():
    family = direct_four_type_family()
    model = ProbabilisticObservationModel(
        family.states,
        {
            0: {0: 0.60, 1: 0.40, 2: 0.00, 3: 0.00},
            1: {0: 0.10, 1: 0.80, 2: 0.10, 3: 0.00},
            2: {0: 0.00, 1: 0.30, 2: 0.60, 3: 0.10},
            3: {0: 0.00, 1: 0.10, 2: 0.30, 3: 0.60},
        },
    )
    update = posterior_observation_update(
        family,
        model,
        0,
        "direct",
        1,
        prior={0: 0.05, 1: 0.15, 2: 0.60, 3: 0.20},
    )
    assert update is not None
    posterior = dict(update.posterior)
    assert update.map_response_types == (2,)
    assert math.isclose(posterior[2], 0.18 / 0.34)
    assert update.credible_set(0.90) == (2, 1, 0)


def test_zero_evidence_observation_returns_none():
    family = direct_four_type_family()
    model = ProbabilisticObservationModel(
        family.states,
        {
            0: {0: 1.0, 1: 0.0, 2: 0.0, 3: 0.0},
            1: {0: 1.0, 1: 0.0, 2: 0.0, 3: 0.0},
            2: {0: 1.0, 1: 0.0, 2: 0.0, 3: 0.0},
            3: {0: 1.0, 1: 0.0, 2: 0.0, 3: 0.0},
        },
    )
    assert posterior_observation_update(family, model, 0, "direct", 3) is None


@pytest.mark.parametrize(
    "likelihoods",
    [
        {0: {0: 1.0}, 1: {1: 1.0}, 2: {2: 1.0}, 3: {3: 1.0}},
        {
            0: {0: 0.5, 1: 0.5, 2: 0.0, 3: 0.0},
            1: {0: 0.5, 1: 0.5, 2: 0.0, 3: 0.0},
            2: {0: 0.5, 1: 0.5, 2: 0.0, 3: 0.0},
        },
        {
            0: {0: 0.5, 1: 0.4, 2: 0.0, 3: 0.0},
            1: {0: 0.5, 1: 0.5, 2: 0.0, 3: 0.0},
            2: {0: 0.5, 1: 0.5, 2: 0.0, 3: 0.0},
            3: {0: 0.5, 1: 0.5, 2: 0.0, 3: 0.0},
        },
        {
            0: {0: -0.1, 1: 1.1, 2: 0.0, 3: 0.0},
            1: {0: 0.5, 1: 0.5, 2: 0.0, 3: 0.0},
            2: {0: 0.5, 1: 0.5, 2: 0.0, 3: 0.0},
            3: {0: 0.5, 1: 0.5, 2: 0.0, 3: 0.0},
        },
    ],
)
def test_probabilistic_model_rejects_invalid_likelihoods(likelihoods):
    with pytest.raises(ValueError):
        ProbabilisticObservationModel((0, 1, 2, 3), likelihoods)


@pytest.mark.parametrize("threshold", [0.0, 1.1, True, float("inf")])
def test_resolved_at_rejects_invalid_thresholds(threshold):
    family = direct_four_type_family()
    update = posterior_observation_update(
        family,
        ProbabilisticObservationModel.exact(family.states),
        0,
        "direct",
        2,
    )
    assert update is not None
    with pytest.raises(ValueError):
        update.resolved_at(threshold)
