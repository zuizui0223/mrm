"""One-step value-of-information scores for posterior response-type ambiguity."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from math import isclose, isfinite, log2
from numbers import Real
from typing import Iterable

from .laws import Action, CandidateLawFamily, State
from .probabilistic import (
    PosteriorObservationUpdate,
    ProbabilisticObservationModel,
    posterior_observation_update,
)


_VOI_TOLERANCE = 1e-12


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


def _as_nonnegative_real(value: Real, label: str) -> float:
    if (
        not isinstance(value, Real)
        or isinstance(value, bool)
        or not isfinite(float(value))
        or value < 0
    ):
        raise ValueError(f"{label} must be a finite nonnegative number")
    return float(value)


def _normalize_distribution(values: Mapping[int, Real], support: tuple[int, ...]) -> dict[int, float]:
    if set(values) != set(support):
        raise ValueError("prior must assign exactly one value to every response type")
    normalized = {
        response_type: _as_nonnegative_real(values[response_type], "prior mass")
        for response_type in support
    }
    total = sum(normalized.values())
    if total <= 0:
        raise ValueError("prior must have positive total mass")
    return {response_type: value / total for response_type, value in normalized.items()}


def _entropy_bits(distribution: Mapping[int, float]) -> float:
    return -sum(
        probability * log2(probability)
        for probability in distribution.values()
        if probability > 0
    )


def _validated_action_costs(
    family: CandidateLawFamily, action_costs: Mapping[Action, Real]
) -> dict[Action, float]:
    if set(action_costs) != set(family.actions):
        raise ValueError("action_costs must assign exactly one value to every action")
    return {
        action: _as_nonnegative_real(action_costs[action], "action cost")
        for action in family.actions
    }


def _posterior_distribution(update: PosteriorObservationUpdate) -> dict[int, float]:
    return {response_type: probability for response_type, probability in update.posterior}


@dataclass(frozen=True)
class ActionInformationValue:
    """One-step expected ambiguity reduction for one declared action."""

    action: Action
    action_cost: float
    prior_entropy_bits: float
    expected_posterior_entropy_bits: float
    expected_information_gain_bits: float
    net_information_gain_bits: float
    resolution_probability: float | None
    outcome_probabilities: tuple[tuple[State, float], ...]
    outcome_posteriors: tuple[tuple[State, tuple[tuple[int, float], ...]], ...]

    def __post_init__(self) -> None:
        for label, value in (
            ("action_cost", self.action_cost),
            ("prior_entropy_bits", self.prior_entropy_bits),
            (
                "expected_posterior_entropy_bits",
                self.expected_posterior_entropy_bits,
            ),
            ("expected_information_gain_bits", self.expected_information_gain_bits),
        ):
            if value < -_VOI_TOLERANCE or not isfinite(value):
                raise ValueError(f"{label} must be finite and nonnegative")
        if self.resolution_probability is not None and (
            self.resolution_probability < -_VOI_TOLERANCE
            or self.resolution_probability > 1 + _VOI_TOLERANCE
            or not isfinite(self.resolution_probability)
        ):
            raise ValueError("resolution_probability must be in [0, 1]")


@dataclass(frozen=True)
class ValueOfInformationDesign:
    """Finite one-step action ranking for a declared posterior design problem."""

    state: State
    prior: tuple[tuple[int, float], ...]
    action_values: tuple[ActionInformationValue, ...]

    @property
    def best_by_expected_information_gain(self) -> ActionInformationValue:
        return max(
            self.action_values,
            key=lambda value: (
                value.expected_information_gain_bits,
                -value.action_cost,
                str(value.action),
            ),
        )

    @property
    def best_by_net_information_gain(self) -> ActionInformationValue:
        return max(
            self.action_values,
            key=lambda value: (
                value.net_information_gain_bits,
                value.expected_information_gain_bits,
                -value.action_cost,
                str(value.action),
            ),
        )


def score_action_information_value(
    family: CandidateLawFamily,
    observation_model: ProbabilisticObservationModel,
    current_state: State,
    action: Action,
    prior: Mapping[int, Real] | None = None,
    response_types: Iterable[int] | None = None,
    action_cost: Real = 0.0,
    cost_per_bit: Real = 0.0,
    resolution_threshold: Real | None = None,
) -> ActionInformationValue:
    """Score one action by expected posterior entropy reduction.

    ``net_information_gain_bits`` subtracts ``action_cost / cost_per_bit`` when
    ``cost_per_bit`` is positive. If ``cost_per_bit`` is zero, it subtracts the raw
    action cost, allowing dimensionless toy witnesses while keeping the convention
    explicit.
    """

    if tuple(family.states) != tuple(observation_model.states):
        raise ValueError("family and observation model must use the same state tuple")
    if current_state not in family.states:
        raise ValueError("unknown current state")
    if action not in family.actions:
        raise ValueError("unknown action")
    support = _validated_response_types(family, response_types)
    prior_distribution = (
        {response_type: 1.0 / len(support) for response_type in support}
        if prior is None
        else _normalize_distribution(prior, support)
    )
    normalized_action_cost = _as_nonnegative_real(action_cost, "action cost")
    normalized_cost_per_bit = _as_nonnegative_real(cost_per_bit, "cost_per_bit")
    threshold: float | None
    if resolution_threshold is None:
        threshold = None
    elif (
        not isinstance(resolution_threshold, Real)
        or isinstance(resolution_threshold, bool)
        or not isfinite(float(resolution_threshold))
        or not 0 < float(resolution_threshold) <= 1
    ):
        raise ValueError("resolution_threshold must be in (0, 1]")
    else:
        threshold = float(resolution_threshold)

    prior_entropy = _entropy_bits(prior_distribution)
    outcome_probabilities: list[tuple[State, float]] = []
    outcome_posteriors: list[tuple[State, tuple[tuple[int, float], ...]]] = []
    expected_posterior_entropy = 0.0
    resolution_probability = 0.0 if threshold is not None else None
    for observed_state in family.states:
        update = posterior_observation_update(
            family,
            observation_model,
            current_state,
            action,
            observed_state,
            prior=prior_distribution,
            response_types=support,
        )
        if update is None:
            continue
        outcome_probability = update.evidence_probability
        outcome_probabilities.append((observed_state, outcome_probability))
        outcome_posteriors.append((observed_state, update.posterior))
        expected_posterior_entropy += outcome_probability * update.entropy_bits
        if threshold is not None and update.resolved_at(threshold):
            resolution_probability += outcome_probability
    information_gain = prior_entropy - expected_posterior_entropy
    if isclose(information_gain, 0.0, rel_tol=0.0, abs_tol=_VOI_TOLERANCE):
        information_gain = 0.0
    if normalized_cost_per_bit > 0:
        net_information_gain = information_gain - normalized_action_cost / normalized_cost_per_bit
    else:
        net_information_gain = information_gain - normalized_action_cost
    return ActionInformationValue(
        action=action,
        action_cost=normalized_action_cost,
        prior_entropy_bits=prior_entropy,
        expected_posterior_entropy_bits=expected_posterior_entropy,
        expected_information_gain_bits=information_gain,
        net_information_gain_bits=net_information_gain,
        resolution_probability=resolution_probability,
        outcome_probabilities=tuple(outcome_probabilities),
        outcome_posteriors=tuple(outcome_posteriors),
    )


def rank_actions_by_value_of_information(
    family: CandidateLawFamily,
    observation_model: ProbabilisticObservationModel,
    current_state: State,
    action_costs: Mapping[Action, Real],
    prior: Mapping[int, Real] | None = None,
    response_types: Iterable[int] | None = None,
    cost_per_bit: Real = 0.0,
    resolution_threshold: Real | None = None,
) -> ValueOfInformationDesign:
    """Return one-step VOI scores for every declared action."""

    costs = _validated_action_costs(family, action_costs)
    support = _validated_response_types(family, response_types)
    prior_distribution = (
        {response_type: 1.0 / len(support) for response_type in support}
        if prior is None
        else _normalize_distribution(prior, support)
    )
    action_values = tuple(
        score_action_information_value(
            family,
            observation_model,
            current_state,
            action,
            prior=prior_distribution,
            response_types=support,
            action_cost=costs[action],
            cost_per_bit=cost_per_bit,
            resolution_threshold=resolution_threshold,
        )
        for action in family.actions
    )
    return ValueOfInformationDesign(
        state=current_state,
        prior=tuple((response_type, prior_distribution[response_type]) for response_type in support),
        action_values=action_values,
    )
