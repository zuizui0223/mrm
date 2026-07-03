"""Universal, typed, and set-valued macro-laws under mechanism uncertainty.

This module rescues CCOC legacy ID-2. Each retained mechanism induces a
macro-transition table on the same observable macrostate set. The exact report
is determined by whether those induced tables agree after duplicate response
types are collapsed.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import log2
from typing import Hashable, Iterable

State = Hashable
Action = Hashable


def _canonical(values: Iterable[object]) -> tuple[int, ...]:
    labels: dict[object, int] = {}
    result: list[int] = []
    for value in values:
        if value not in labels:
            labels[value] = len(labels)
        result.append(labels[value])
    return tuple(result)


@dataclass(frozen=True)
class CandidateLawFamily:
    """Finite candidate mechanisms with a common observable macrostate space.

    ``transitions[candidate][action][state]`` is the candidate-specific successor.
    Candidate names are deliberately not used as memory types: two candidates are
    equivalent whenever their complete induced macro transition tables agree.
    """

    states: tuple[State, ...]
    actions: tuple[Action, ...]
    transitions: tuple[tuple[tuple[State, ...], ...], ...]

    def __post_init__(self) -> None:
        if not self.states or len(set(self.states)) != len(self.states):
            raise ValueError("states must be a nonempty tuple of unique values")
        if not self.actions or len(set(self.actions)) != len(self.actions):
            raise ValueError("actions must be a nonempty tuple of unique values")
        if not self.transitions:
            raise ValueError("at least one candidate is required")
        state_set = set(self.states)
        for candidate in self.transitions:
            if len(candidate) != len(self.actions):
                raise ValueError("candidate action rows must match actions")
            for row in candidate:
                if len(row) != len(self.states) or any(target not in state_set for target in row):
                    raise ValueError("transition rows must map every state to the common state set")

    @property
    def candidate_count(self) -> int:
        return len(self.transitions)

    def successor(self, candidate: int, action: Action, state: State) -> State:
        if not isinstance(candidate, int) or isinstance(candidate, bool) or not 0 <= candidate < self.candidate_count:
            raise ValueError("candidate index outside family")
        try:
            action_index = self.actions.index(action)
            state_index = self.states.index(state)
        except ValueError as error:
            raise ValueError("unknown action or state") from error
        return self.transitions[candidate][action_index][state_index]

    @property
    def response_type_labels(self) -> tuple[int, ...]:
        """One type label per candidate, collapsing identical full tables."""
        return _canonical(self.transitions)

    @property
    def response_type_count(self) -> int:
        return max(self.response_type_labels) + 1

    @property
    def universal(self) -> bool:
        return self.response_type_count == 1

    def universal_transition(self, action: Action, state: State) -> State:
        if not self.universal:
            raise ValueError("candidate family has no universal deterministic macro-law")
        return self.successor(0, action, state)

    def set_valued_transition(self, action: Action, state: State) -> frozenset[State]:
        return frozenset(self.successor(candidate, action, state) for candidate in range(self.candidate_count))

    def typed_transition(self, response_type: int, action: Action, state: State) -> tuple[State, int]:
        if not isinstance(response_type, int) or isinstance(response_type, bool) or not 0 <= response_type < self.response_type_count:
            raise ValueError("response type outside family")
        candidate = self.response_type_labels.index(response_type)
        return self.successor(candidate, action, state), response_type

    def response_separated(self) -> bool:
        """Uniform one-step response separation on the common macrostate set."""
        labels = self.response_type_labels
        representatives = [labels.index(response_type) for response_type in range(self.response_type_count)]
        for left_offset, left_candidate in enumerate(representatives):
            for right_candidate in representatives[left_offset + 1 :]:
                for state in self.states:
                    if not any(
                        self.successor(left_candidate, action, state)
                        != self.successor(right_candidate, action, state)
                        for action in self.actions
                    ):
                        return False
        return True

    def report_kind(self) -> str:
        return "universal" if self.universal else "typed-or-set-valued"


def candidate_safe_memory_bits(family: CandidateLawFamily) -> float:
    """Exact candidate-safe product lower bound when response types separate."""
    if not family.response_separated():
        raise ValueError("uniform response separation is required for the product bound")
    return log2(len(family.states)) + log2(family.response_type_count)
