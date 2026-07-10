import pytest

from mrm.laws import CandidateLawFamily
from mrm.robust import (
    RobustObservationModel,
    robust_observation_update,
    robust_set_valued_successor,
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


def test_exact_observation_update_recovers_single_response_type():
    family = direct_four_type_family()
    model = RobustObservationModel.exact(family.states)
    update = robust_observation_update(family, model, 0, "direct", 2)
    assert update.prior_response_types == (0, 1, 2, 3)
    assert update.remaining_response_types == (2,)
    assert update.eliminated_response_types == (0, 1, 3)
    assert update.identified
    assert not update.contradicted


def test_bounded_error_keeps_all_compatible_response_types():
    family = direct_four_type_family()
    model = RobustObservationModel(
        family.states,
        {
            0: (0, 1),
            1: (0, 1, 2),
            2: (1, 2, 3),
            3: (2, 3),
        },
    )
    update = robust_observation_update(family, model, 0, "direct", 1)
    assert update.compatible_true_states == (0, 1, 2)
    assert update.remaining_response_types == (0, 1, 2)
    assert update.eliminated_response_types == (3,)
    assert not update.identified
    assert robust_set_valued_successor(
        family, update.remaining_response_types, 0, "flip"
    ) == frozenset({1, 2, 3})


def test_robust_update_can_certify_contradiction_against_declared_error_support():
    family = direct_four_type_family()
    model = RobustObservationModel(family.states, {0: (0,), 1: (1,), 2: (2,), 3: (3,)})
    update = robust_observation_update(
        family, model, 0, "direct", 3, response_types=(0, 1)
    )
    assert update.remaining_response_types == ()
    assert update.eliminated_response_types == (0, 1)
    assert update.contradicted
    assert not update.identified


def test_robust_update_respects_prior_response_subset():
    family = direct_four_type_family()
    model = RobustObservationModel(
        family.states,
        {0: (0, 1), 1: (1, 2), 2: (2, 3), 3: (0, 3)},
    )
    update = robust_observation_update(
        family, model, 0, "direct", 2, response_types=(1, 2, 3)
    )
    assert update.prior_response_types == (1, 2, 3)
    assert update.remaining_response_types == (2, 3)
    assert update.eliminated_response_types == (1,)


@pytest.mark.parametrize(
    "neighborhoods",
    [
        {0: (0,), 1: (1,), 2: (2,)},
        {0: (), 1: (1,), 2: (2,), 3: (3,)},
        {0: (0, 0), 1: (1,), 2: (2,), 3: (3,)},
        {0: (0,), 1: (1,), 2: (2,), 3: (4,)},
    ],
)
def test_observation_model_rejects_invalid_neighborhoods(neighborhoods):
    with pytest.raises(ValueError):
        RobustObservationModel((0, 1, 2, 3), neighborhoods)


def test_robust_update_rejects_mismatched_state_spaces():
    family = direct_four_type_family()
    model = RobustObservationModel.exact((0, 1))
    with pytest.raises(ValueError):
        robust_observation_update(family, model, 0, "direct", 1)
