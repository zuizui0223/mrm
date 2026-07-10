"""Conservative response-type updates under bounded observation error."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Iterable

from .laws import Action, CandidateLawFamily, State


def _validated_response_types(
    family: CandidateLawFamily, response_types: Iterable[int] | None
) -> tuple[int, ...]:
    values = (
        tuple(range(family.response_type_count))
        if response_types is None
        else tuple(response_types)
    )
    if (
        not values
        or len(set(values)) != len(values)
        or any(
            not isinstance(value, int)
            or isinstance(value, bool)
            or not 0 <= value < family.response_type_count
            for value in values
        )
    ):
        raise ValueError(
            "response_types must be a nonempty subset of response-type labels"
        )
    return tuple(sorted(values))


@dataclass(frozen=True)
class RobustObservationModel:
    """Observation neighborhoods for conservative finite MRM updates.

    ``neighborhoods[observed]`` is the nonempty set of true successor macrostates
    compatible with the observed macrostate. The model is deliberately set-valued:
    it records bounded error support, not a probability model.
    """

    states: tuple[State, ...]
    neighborhoods: Mapping[State, Iterable[State]]

    def __post_init__(self) -> None:
        if not self.states or len(set(self.states)) != len(self.states):
            raise ValueError("states must be a nonempty tuple of unique values")
        state_set = set(self.states)
        if set(self.neighborhoods) != state_set:
            raise ValueError("neighborhoods must contain exactly one entry per observed state")
        normalized: dict[State, tuple[State, ...]] = {}
        for observed in self.states:
            values = tuple(self.neighborhoods[observed])
            if not values or len(set(values)) != len(values):
                raise ValueError("each observation neighborhood must be nonempty and unique")
            if any(value not in state_set for value in values):
                raise ValueError("observation neighborhoods must stay inside the state set")
            normalized[observed] = tuple(sorted(values, key=self.states.index))
        object.__setattr__(self, "neighborhoods", normalized)

    @classmethod
    def exact(cls, states: tuple[State, ...]) -> "RobustObservationModel":
        """Return the identity observation model."""
        return cls(states, {state: (state,) for state in states})

    def compatible_true_states(self, observed_state: State) -> tuple[State, ...]:
        try:
            return tuple(self.neighborhoods[observed_state])
        except KeyError as error:
            raise ValueError("unknown observed state") from error


@dataclass(frozen=True)
class RobustObservationUpdate:
    """One-step conservative update after a possibly noisy observation."""

    prior_response_types: tuple[int, ...]
    remaining_response_types: tuple[int, ...]
    observed_state: State
    compatible_true_states: tuple[State, ...]

    def __post_init__(self) -> None:
        if not set(self.remaining_response_types).issubset(self.prior_response_types):
            raise ValueError("remaining response types must be a subset of the prior")
        if not self.compatible_true_states:
            raise ValueError("compatible_true_states must be nonempty")

    @property
    def eliminated_response_types(self) -> tuple[int, ...]:
        remaining = set(self.remaining_response_types)
        return tuple(value for value in self.prior_response_types if value not in remaining)

    @property
    def identified(self) -> bool:
        return len(self.remaining_response_types) == 1

    @property
    def contradicted(self) -> bool:
        return len(self.remaining_response_types) == 0


def robust_observation_update(
    family: CandidateLawFamily,
    observation_model: RobustObservationModel,
    current_state: State,
    action: Action,
    observed_successor: State,
    response_types: Iterable[int] | None = None,
) -> RobustObservationUpdate:
    """Retain exactly the response types compatible with a noisy observation.

    A response type is retained when its deterministic successor from the known
    current state lies inside the observation neighborhood of ``observed_successor``.
    This is a support-level update: retained types remain possible and eliminated
    types are impossible under the declared error model.
    """

    if tuple(family.states) != tuple(observation_model.states):
        raise ValueError("family and observation model must use the same state tuple")
    if current_state not in family.states:
        raise ValueError("unknown current state")
    if action not in family.actions:
        raise ValueError("unknown action")
    prior = _validated_response_types(family, response_types)
    compatible_states = observation_model.compatible_true_states(observed_successor)
    compatible_set = set(compatible_states)
    remaining = tuple(
        response_type
        for response_type in prior
        if family.typed_transition(response_type, action, current_state)[0]
        in compatible_set
    )
    return RobustObservationUpdate(
        prior_response_types=prior,
        remaining_response_types=remaining,
        observed_state=observed_successor,
        compatible_true_states=compatible_states,
    )


def robust_set_valued_successor(
    family: CandidateLawFamily,
    response_types: Iterable[int],
    current_state: State,
    action: Action,
) -> frozenset[State]:
    """Set-valued successor after retaining a robustly possible type subset."""

    retained = _validated_response_types(family, response_types)
    return frozenset(
        family.typed_transition(response_type, action, current_state)[0]
        for response_type in retained
    )
