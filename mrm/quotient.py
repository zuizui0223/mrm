"""Exact finite candidate-safe quotients and active discrimination plans."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from math import log2
from typing import Hashable, Iterable

from .laws import Action, CandidateLawFamily, State

Pair = tuple[State, int]


def _canonical(values: Iterable[Hashable]) -> tuple[int, ...]:
    labels: dict[Hashable, int] = {}
    result: list[int] = []
    for value in values:
        if value not in labels:
            labels[value] = len(labels)
        result.append(labels[value])
    return tuple(result)


def _validated_types(
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
class CandidateSafeQuotient:
    """Coarsest exact quotient of ``Q × R`` that preserves the observed macrostate.

    A quotient class may merge response types only at observable states from which no
    declared action word can make their future observable trajectories diverge.
    """

    family: CandidateLawFamily
    pairs: tuple[Pair, ...]
    class_labels: tuple[int, ...]

    def __post_init__(self) -> None:
        expected = tuple(
            (state, response_type)
            for state in self.family.states
            for response_type in range(self.family.response_type_count)
        )
        if self.pairs != expected or len(self.class_labels) != len(expected):
            raise ValueError("quotient must cover the canonical full typed product")
        for left, pair in enumerate(self.pairs):
            for right in range(left + 1, len(self.pairs)):
                if (
                    self.class_labels[left] == self.class_labels[right]
                    and pair[0] != self.pairs[right][0]
                ):
                    raise ValueError(
                        "a candidate-safe quotient cannot merge distinct observable macrostates"
                    )
        for pair_index, (state, response_type) in enumerate(self.pairs):
            source_class = self.class_labels[pair_index]
            for action in self.family.actions:
                target = self.class_of(
                    self.family.typed_transition(response_type, action, state)[0],
                    response_type,
                )
                for other_index, other_pair in enumerate(self.pairs):
                    if self.class_labels[other_index] != source_class:
                        continue
                    other_target = self.class_of(
                        self.family.typed_transition(
                            other_pair[1], action, other_pair[0]
                        )[0],
                        other_pair[1],
                    )
                    if target != other_target:
                        raise ValueError(
                            "quotient classes must have deterministic action successors"
                        )

    @property
    def state_count(self) -> int:
        return max(self.class_labels) + 1

    @property
    def memory_bits(self) -> float:
        return log2(self.state_count)

    @property
    def full_typed_product_state_count(self) -> int:
        return len(self.pairs)

    def class_of(self, state: State, response_type: int) -> int:
        try:
            return self.class_labels[self.pairs.index((state, response_type))]
        except ValueError as error:
            raise ValueError("unknown observable state or response type") from error

    def observable_state(self, quotient_state: int) -> State:
        if (
            not isinstance(quotient_state, int)
            or isinstance(quotient_state, bool)
            or not 0 <= quotient_state < self.state_count
        ):
            raise ValueError("quotient state outside quotient")
        return self.pairs[self.class_labels.index(quotient_state)][0]

    def successor(self, quotient_state: int, action: Action) -> int:
        if action not in self.family.actions:
            raise ValueError("unknown action")
        state = self.observable_state(quotient_state)
        pair_index = self.class_labels.index(quotient_state)
        response_type = self.pairs[pair_index][1]
        successor_state, _ = self.family.typed_transition(
            response_type, action, state
        )
        return self.class_of(successor_state, response_type)


def minimal_candidate_safe_quotient(
    family: CandidateLawFamily,
) -> CandidateSafeQuotient:
    """Construct the coarsest observation-preserving deterministic quotient of ``Q × R``.

    Partition refinement begins with blocks sharing the currently observed macrostate
    and refines by successor blocks under every declared action. At the fixed point,
    the quotient is exact for all finite action words and has the fewest states among
    deterministic candidate-safe interfaces that retain the current macrostate.
    """

    pairs = tuple(
        (state, response_type)
        for state in family.states
        for response_type in range(family.response_type_count)
    )
    pair_indices = {pair: index for index, pair in enumerate(pairs)}
    state_index = {state: index for index, state in enumerate(family.states)}
    labels = tuple(state_index[state] for state, _ in pairs)
    while True:
        signatures: list[Hashable] = []
        for state, response_type in pairs:
            successor_labels = []
            for action in family.actions:
                successor_state, _ = family.typed_transition(
                    response_type, action, state
                )
                successor_labels.append(
                    labels[pair_indices[(successor_state, response_type)]]
                )
            signatures.append((state_index[state], tuple(successor_labels)))
        refined = _canonical(signatures)
        if refined == labels:
            return CandidateSafeQuotient(
                family=family, pairs=pairs, class_labels=labels
            )
        labels = refined


@dataclass(frozen=True)
class ActiveDiscriminationPlan:
    """A finite adaptive intervention tree that identifies the retained response type."""

    state: State
    response_types: tuple[int, ...]
    action: Action | None = None
    outcomes: tuple[tuple[State, "ActiveDiscriminationPlan"], ...] = ()

    def __post_init__(self) -> None:
        if len(self.response_types) == 1:
            if self.action is not None or self.outcomes:
                raise ValueError(
                    "terminal discrimination plans must have no action or outcomes"
                )
        elif self.action is None or not self.outcomes:
            raise ValueError(
                "nonterminal discrimination plans require an action and at least one outcome"
            )

    @property
    def worst_case_steps(self) -> int:
        return (
            0
            if self.action is None
            else 1 + max(child.worst_case_steps for _, child in self.outcomes)
        )


def shortest_active_discrimination_plan(
    family: CandidateLawFamily,
    state: State,
    response_types: Iterable[int] | None = None,
) -> ActiveDiscriminationPlan | None:
    """Return a shortest exact adaptive plan, or ``None`` when types cannot separate.

    The current macrostate is observed after every intervention. The search is exact
    for the declared finite family and minimizes the worst-case number of actions.
    """

    if state not in family.states:
        raise ValueError("unknown observable state")
    target = _validated_types(family, response_types)
    subsets = [
        tuple(combo)
        for size in range(1, family.response_type_count + 1)
        for combo in combinations(range(family.response_type_count), size)
    ]
    configurations = [
        (macrostate, subset) for macrostate in family.states for subset in subsets
    ]
    plans: dict[tuple[State, tuple[int, ...]], ActiveDiscriminationPlan] = {
        (macrostate, (response_type,)): ActiveDiscriminationPlan(
            macrostate, (response_type,)
        )
        for macrostate in family.states
        for response_type in range(family.response_type_count)
    }
    maximum_depth = len(configurations) - 1
    for _ in range(maximum_depth):
        additions: dict[tuple[State, tuple[int, ...]], ActiveDiscriminationPlan] = {}
        for macrostate, subset in configurations:
            key = (macrostate, subset)
            if key in plans:
                continue
            best: ActiveDiscriminationPlan | None = None
            for action in family.actions:
                grouped: dict[State, list[int]] = {}
                for response_type in subset:
                    successor_state, _ = family.typed_transition(
                        response_type, action, macrostate
                    )
                    grouped.setdefault(successor_state, []).append(response_type)
                children: list[tuple[State, ActiveDiscriminationPlan]] = []
                for observed_state in family.states:
                    group = grouped.get(observed_state)
                    if not group:
                        continue
                    child = plans.get((observed_state, tuple(group)))
                    if child is None:
                        break
                    children.append((observed_state, child))
                else:
                    candidate = ActiveDiscriminationPlan(
                        macrostate, subset, action, tuple(children)
                    )
                    if (
                        best is None
                        or candidate.worst_case_steps < best.worst_case_steps
                    ):
                        best = candidate
            if best is not None:
                additions[key] = best
        if not additions:
            break
        plans.update(additions)
        if (state, target) in plans:
            return plans[(state, target)]
    return plans.get((state, target))
