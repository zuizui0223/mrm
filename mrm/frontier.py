"""Canonical finite witnesses for the mechanism-ambiguity complexity frontier."""

from __future__ import annotations

from dataclasses import dataclass
from math import isclose, log2

from .laws import CandidateLawFamily
from .quotient import minimal_candidate_safe_quotient


@dataclass(frozen=True)
class BinarySignatureFrontier:
    """A width-``m`` family with ``2**m`` retained mechanism response types.

    A response type is a binary signature ``r``. The observable macrostate space is
    ``Q = {0, 1}``, and action ``probe_i`` sets the next observed macrostate to the
    ``i``-th signature bit, independently of the present macrostate. Thus every
    fixed candidate has a two-state macro-law, whereas retaining all response types
    requires the full typed product. The prescribed probe schedule reads the full
    signature in exactly ``m`` interventions.
    """

    signature_width: int

    def __post_init__(self) -> None:
        if (
            not isinstance(self.signature_width, int)
            or isinstance(self.signature_width, bool)
            or self.signature_width < 1
        ):
            raise ValueError("signature_width must be a positive integer")

    @property
    def candidate_count(self) -> int:
        return 1 << self.signature_width

    @property
    def observable_state_count(self) -> int:
        return 2

    @property
    def actions(self) -> tuple[str, ...]:
        return tuple(f"probe_{index}" for index in range(self.signature_width))

    @property
    def fixed_candidate_memory_bits(self) -> float:
        return log2(self.observable_state_count)

    @property
    def candidate_safe_state_count(self) -> int:
        return self.observable_state_count * self.candidate_count

    @property
    def candidate_safe_memory_bits(self) -> float:
        return log2(self.candidate_safe_state_count)

    @property
    def ambiguity_memory_surcharge_bits(self) -> float:
        return log2(self.candidate_count)

    @property
    def information_lower_bound_steps(self) -> int:
        """Binary-observation leaf-count lower bound for exact identification."""
        return self.signature_width

    @property
    def canonical_probe_schedule(self) -> tuple[str, ...]:
        return self.actions

    def signature(self, response_type: int) -> tuple[int, ...]:
        if (
            not isinstance(response_type, int)
            or isinstance(response_type, bool)
            or not 0 <= response_type < self.candidate_count
        ):
            raise ValueError("response type outside binary signature family")
        return tuple(
            (response_type >> index) & 1 for index in range(self.signature_width)
        )

    def family(self) -> CandidateLawFamily:
        """Return the declared finite response-type family for this witness."""
        return CandidateLawFamily(
            states=(0, 1),
            actions=self.actions,
            transitions=tuple(
                tuple((bit, bit) for bit in self.signature(response_type))
                for response_type in range(self.candidate_count)
            ),
        )

    def observations(self, response_type: int) -> tuple[int, ...]:
        """Observed outcomes under the canonical one-probe-per-bit schedule."""
        family = self.family()
        state = 0
        outcomes: list[int] = []
        for action in self.canonical_probe_schedule:
            state, _ = family.typed_transition(response_type, action, state)
            outcomes.append(state)
        return tuple(outcomes)

    def remaining_candidate_count_after_probes(self, distinct_probe_count: int) -> int:
        """Residual candidates after observing that many distinct canonical probes."""
        if (
            not isinstance(distinct_probe_count, int)
            or isinstance(distinct_probe_count, bool)
            or not 0 <= distinct_probe_count <= self.signature_width
        ):
            raise ValueError(
                "distinct_probe_count must be between zero and signature_width"
            )
        return 1 << (self.signature_width - distinct_probe_count)

    def replay_record(self) -> dict[str, int | float]:
        return {
            "signature_width": self.signature_width,
            "response_type_count": self.candidate_count,
            "fixed_candidate_state_count": self.observable_state_count,
            "candidate_safe_state_count": self.candidate_safe_state_count,
            "fixed_candidate_memory_bits": self.fixed_candidate_memory_bits,
            "candidate_safe_memory_bits": self.candidate_safe_memory_bits,
            "ambiguity_memory_surcharge_bits": self.ambiguity_memory_surcharge_bits,
            "optimal_identification_steps": self.information_lower_bound_steps,
        }

    def verify(self) -> bool:
        """Verify the finite witness identities claimed by the frontier."""
        family = self.family()
        quotient = minimal_candidate_safe_quotient(family)
        observations = tuple(
            self.observations(response_type)
            for response_type in range(self.candidate_count)
        )
        return (
            family.response_type_count == self.candidate_count
            and family.response_separated()
            and quotient.state_count == self.candidate_safe_state_count
            and len(set(observations)) == self.candidate_count
            and isclose(
                self.fixed_candidate_memory_bits
                + self.ambiguity_memory_surcharge_bits,
                self.candidate_safe_memory_bits,
                rel_tol=0.0,
                abs_tol=1e-12,
            )
        )


def binary_signature_frontier(maximum_width: int) -> tuple[BinarySignatureFrontier, ...]:
    """Return canonical frontier points from width one through ``maximum_width``."""
    if (
        not isinstance(maximum_width, int)
        or isinstance(maximum_width, bool)
        or maximum_width < 1
    ):
        raise ValueError("maximum_width must be a positive integer")
    return tuple(BinarySignatureFrontier(width) for width in range(1, maximum_width + 1))
