"""Mechanism-Robust Macro-Laws (MRM).

Finite theory for reporting universal deterministic, typed deterministic, or
set-valued macro-laws when multiple retained mechanisms remain plausible.
"""

from .laws import CandidateLawFamily, candidate_safe_memory_bits
from .joint import JointUncertaintyFamily, joint_safe_memory_bits

__all__ = [
    "CandidateLawFamily",
    "candidate_safe_memory_bits",
    "JointUncertaintyFamily",
    "joint_safe_memory_bits",
]
