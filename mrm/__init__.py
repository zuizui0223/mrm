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
from .probabilistic import (
    PosteriorObservationUpdate,
    ProbabilisticObservationModel,
    posterior_observation_update,
    posterior_set_valued_successor,
)
from .quotient import (
    ActiveDiscriminationPlan,
    CandidateSafeQuotient,
    minimal_candidate_safe_quotient,
    shortest_active_discrimination_plan,
)
from .robust import (
    RobustObservationModel,
    RobustObservationUpdate,
    robust_observation_update,
    robust_set_valued_successor,
)
from .voi import (
    ActionInformationValue,
    ValueOfInformationDesign,
    rank_actions_by_value_of_information,
    score_action_information_value,
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
    "RobustObservationModel",
    "RobustObservationUpdate",
    "robust_observation_update",
    "robust_set_valued_successor",
    "ProbabilisticObservationModel",
    "PosteriorObservationUpdate",
    "posterior_observation_update",
    "posterior_set_valued_successor",
    "ActionInformationValue",
    "ValueOfInformationDesign",
    "rank_actions_by_value_of_information",
    "score_action_information_value",
]
