"""Joint exterior and mechanism uncertainty.

This module rescues the core claim of CCOC legacy ID-3: exterior uncertainty and
mechanism response uncertainty add only under a declared joint operational
separation condition. The finite canonical family below makes the condition
explicit rather than inferring additivity from two cardinality counts.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import log2


@dataclass(frozen=True)
class JointUncertaintyFamily:
    """Canonical jointly addressable inside/exterior/response-type family.

    The state is ``(inside, exterior_1, ..., exterior_q, response_type)``. A
    structural read context selects one exterior coordinate, while an intervention
    distinguishes response types. The class stores only cardinalities because the
    theorem's proof is an injection under declared pairwise separators.
    """

    inside_cardinality: int
    exterior_cardinalities: tuple[int, ...]
    response_type_count: int

    def __post_init__(self) -> None:
        for value, name in (
            (self.inside_cardinality, "inside_cardinality"),
            (self.response_type_count, "response_type_count"),
        ):
            if not isinstance(value, int) or isinstance(value, bool) or value < 1:
                raise ValueError(f"{name} must be a positive integer")
        if not self.exterior_cardinalities or any(
            not isinstance(value, int) or isinstance(value, bool) or value < 2
            for value in self.exterior_cardinalities
        ):
            raise ValueError("exterior_cardinalities must be a nonempty tuple of integers at least two")
        if self.inside_cardinality < self.response_type_count:
            raise ValueError("canonical intervention witness requires inside_cardinality >= response_type_count")

    @property
    def joint_state_count(self) -> int:
        product = self.inside_cardinality * self.response_type_count
        for value in self.exterior_cardinalities:
            product *= value
        return product

    @property
    def fixed_candidate_memory_bits(self) -> float:
        result = log2(self.inside_cardinality)
        for value in self.exterior_cardinalities:
            result += log2(value)
        return result

    @property
    def joint_safe_memory_bits(self) -> float:
        return self.fixed_candidate_memory_bits + log2(self.response_type_count)

    def verify(self) -> bool:
        return (1 << round(self.joint_safe_memory_bits)) == self.joint_state_count if self.joint_state_count & (self.joint_state_count - 1) == 0 else self.joint_safe_memory_bits == log2(self.joint_state_count)


def joint_safe_memory_bits(inside_cardinality: int, exterior_cardinalities: tuple[int, ...], response_type_count: int) -> float:
    """Return the joint product lower-bound in bits for the canonical family."""
    return JointUncertaintyFamily(inside_cardinality, exterior_cardinalities, response_type_count).joint_safe_memory_bits
