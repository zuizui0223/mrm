"""Posterior response-type updates under declared observation likelihoods."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from math import isclose, isfinite, log2
from numbers import Real
from typing import Iterable

from .laws import Action, CandidateLawFamily, State


_PROB_TOLERANCE = 1e-12


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


def _as_probability(value: Real) -> float:
    if (
        not isinstance(value, Real)
        or isinstance(value, bool)
        or not isfinite(float(value))
        or value < 0
    ):
        raise ValueError("probabilities must be finite nonnegative numbers")
    return float(value)


def _normalized_distribution(values: Mapping[int, Real], support: tuple[int, ...]) -> dict[int, float]:
    if set(values) != set(support):
        raise ValueError("distribution must assign exactly one value to every support item")
    normalized = {item: _as_probability(values[item]) for item in support}
    total = sum(normalized.values())
    if total <= 0:
        raise ValueError("distribution must have positive total mass")
    return {item: value / total for item, value in normalized.items()}


@dataclass(frozen=True)
class ProbabilisticObservationModel:
    """Observation likelihoods ``P(observed_state | true_state)``.

    The model is conditional on the finite observed macrostate alphabet. It does not
    declare priors over response types or losses for decisions.
    """

    states: tuple[State, ...]
    likelihoods: Mapping[State, Mapping[State, Real]]

    def __post_init__(self) -> None:
        if not self.states or len(set(self.states)) != len(self.states):
            raise ValueError("states must be a nonempty tuple of unique values")
        state_set = set(self.states)
        if set(self.likelihoods) != state_set:
            raise ValueError("likelihoods must contain exactly one row per true state")
        normalized: dict[State, dict[State, float]] = {}
        for true_state in self.states:
            row = self.likelihoods[true_state]
            if set(row) != state_set:
                raise ValueError("each likelihood row must cover every observed state")
            values = {observed: _as_probability(row[observed]) for observed in self.states}
            total = sum(values.values())
            if total <= 0:
                raise ValueError("each likelihood row must have positive probability mass")
            if not isclose(total, 1.0, rel_tol=0.0, abs_tol=_PROB_TOLERANCE):
                raise ValueError("each likelihood row must sum to one")
            normalized[true_state] = values
        object.__setattr__(self, "likelihoods", normalized)

    @classmethod
    def exact(cls, states: tuple[State, ...]) -> "ProbabilisticObservationModel":
        """Return the identity observation-likelihood model."""
        return cls(
            states,
            {
                true_state: {
                    observed_state: 1.0 if observed_state == true_state else 0.0
                    for observed_state in states
                }
                for true_state in states
            },
        )

    def probability(self, observed_state: State, true_state: State) -> float:
        if observed_state not in self.states or true_state not in self.states:
            raise ValueError("unknown true or observed state")
        return float(self.likelihoods[true_state][observed_state])


@dataclass(frozen=True)
class PosteriorObservationUpdate:
    """Bayesian response-type update from one declared observation likelihood."""

    prior: tuple[tuple[int, float], ...]
    posterior: tuple[tuple[int, float], ...]
    observed_state: State
    evidence_probability: float

    def __post_init__(self) -> None:
        if not self.prior or not self.posterior:
            raise ValueError("prior and posterior records must be nonempty")
        if tuple(response_type for response_type, _ in self.prior) != tuple(
            response_type for response_type, _ in self.posterior
        ):
            raise ValueError("prior and posterior must share response-type order")
        if self.evidence_probability <= 0 or not isfinite(self.evidence_probability):
            raise ValueError("evidence_probability must be finite and positive")
        for distribution in (self.prior, self.posterior):
            values = [value for _, value in distribution]
            if any(value < 0 or not isfinite(value) for value in values):
                raise ValueError("posterior update probabilities must be finite and nonnegative")
            if not isclose(sum(values), 1.0, rel_tol=0.0, abs_tol=_PROB_TOLERANCE):
                raise ValueError("prior and posterior probabilities must sum to one")

    @property
    def posterior_response_types(self) -> tuple[int, ...]:
        return tuple(response_type for response_type, _ in self.posterior)

    @property
    def positive_posterior_response_types(self) -> tuple[int, ...]:
        return tuple(
            response_type for response_type, probability in self.posterior if probability > 0
        )

    @property
    def map_probability(self) -> float:
        return max(probability for _, probability in self.posterior)

    @property
    def map_response_types(self) -> tuple[int, ...]:
        maximum = self.map_probability
        return tuple(
            response_type
            for response_type, probability in self.posterior
            if isclose(probability, maximum, rel_tol=0.0, abs_tol=_PROB_TOLERANCE)
        )

    @property
    def entropy_bits(self) -> float:
        return -sum(
            probability * log2(probability)
            for _, probability in self.posterior
            if probability > 0
        )

    def resolved_at(self, confidence_threshold: float) -> bool:
        if (
            not isinstance(confidence_threshold, Real)
            or isinstance(confidence_threshold, bool)
            or not isfinite(float(confidence_threshold))
            or not 0 < confidence_threshold <= 1
        ):
            raise ValueError("confidence_threshold must be in (0, 1]")
        return self.map_probability >= float(confidence_threshold)

    def credible_set(self, mass: float) -> tuple[int, ...]:
        if (
            not isinstance(mass, Real)
            or isinstance(mass, bool)
            or not isfinite(float(mass))
            or not 0 < mass <= 1
        ):
            raise ValueError("mass must be in (0, 1]")
        ordered = sorted(self.posterior, key=lambda item: (-item[1], item[0]))
        selected: list[int] = []
        cumulative = 0.0
        for response_type, probability in ordered:
            selected.append(response_type)
            cumulative += probability
            if cumulative + _PROB_TOLERANCE >= float(mass):
                break
        return tuple(selected)


def posterior_observation_update(
    family: CandidateLawFamily,
    observation_model: ProbabilisticObservationModel,
    current_state: State,
    action: Action,
    observed_successor: State,
    prior: Mapping[int, Real] | None = None,
    response_types: Iterable[int] | None = None,
) -> PosteriorObservationUpdate | None:
    """Update response-type probabilities after one observed successor.

    Returns ``None`` when the observed event has zero probability under every
    retained response type with positive prior mass. That is the probabilistic
    analogue of a contradiction against the declared likelihood model.
    """

    if tuple(family.states) != tuple(observation_model.states):
        raise ValueError("family and observation model must use the same state tuple")
    if current_state not in family.states:
        raise ValueError("unknown current state")
    if action not in family.actions:
        raise ValueError("unknown action")
    if observed_successor not in family.states:
        raise ValueError("unknown observed successor")
    support = _validated_response_types(family, response_types)
    if prior is None:
        prior_distribution = {response_type: 1.0 / len(support) for response_type in support}
    else:
        prior_distribution = _normalized_distribution(prior, support)
    weighted: dict[int, float] = {}
    for response_type in support:
        true_successor, _ = family.typed_transition(response_type, action, current_state)
        likelihood = observation_model.probability(observed_successor, true_successor)
        weighted[response_type] = prior_distribution[response_type] * likelihood
    evidence = sum(weighted.values())
    if evidence <= 0:
        return None
    posterior = {
        response_type: weighted[response_type] / evidence for response_type in support
    }
    return PosteriorObservationUpdate(
        prior=tuple((response_type, prior_distribution[response_type]) for response_type in support),
        posterior=tuple((response_type, posterior[response_type]) for response_type in support),
        observed_state=observed_successor,
        evidence_probability=evidence,
    )


def posterior_set_valued_successor(
    family: CandidateLawFamily,
    update: PosteriorObservationUpdate,
    current_state: State,
    action: Action,
) -> frozenset[State]:
    """Set-valued successor over response types with positive posterior mass."""

    if current_state not in family.states:
        raise ValueError("unknown current state")
    if action not in family.actions:
        raise ValueError("unknown action")
    return frozenset(
        family.typed_transition(response_type, action, current_state)[0]
        for response_type in update.positive_posterior_response_types
    )
