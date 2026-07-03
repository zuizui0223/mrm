"""Mechanism-Robust Macro-Laws (MRM).

Finite theory for reporting universal deterministic, typed deterministic, or
set-valued macro-laws when multiple retained mechanisms remain plausible.
"""

from .costs import (
    CostAwareDiscriminationPlan,
    minimum_cost_active_discrimination_plan,
)
from .frontier import BinarySignatureFrontier, binary_signature_frontier
from .joint import JointUncertaintyFamily, joint_safe_memory_bits
from .laws import CandidateLawFamily, candidate_safe_memory_bits
from .quotient import (
    ActiveDiscriminationPlan,
    CandidateSafeQuotient,
    minimal_candidate_safe_quotient,
    shortest_active_discrimination_plan,
)

__all__ = [
    "CandidateLawFamily",
    "candidate_safe_memory_bits",
    "JointUncertaintyFamily",
    "joint_safe_memory_bits",
    "CandidateSafeQuotient",
    "ActiveDiscriminationPlan",
    "minimal_candidate_safe_quotient",
    "shortest_active_discrimination_plan",
    "BinarySignatureFrontier",
    "binary_signature_frontier",
    "CostAwareDiscriminationPlan",
    "minimum_cost_active_discrimination_plan",
]
