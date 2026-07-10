"""Write a deterministic finite replay report for the MRM theorem core."""

from __future__ import annotations

import json
from math import isclose
from pathlib import Path

from mrm.costs import minimum_cost_active_discrimination_plan
from mrm.frontier import binary_signature_frontier
from mrm.joint import JointUncertaintyFamily
from mrm.laws import CandidateLawFamily, candidate_safe_memory_bits
from mrm.probabilistic import (
    ProbabilisticObservationModel,
    posterior_observation_update,
    posterior_set_valued_successor,
)
from mrm.quotient import (
    minimal_candidate_safe_quotient,
    shortest_active_discrimination_plan,
)
from mrm.robust import (
    RobustObservationModel,
    robust_observation_update,
    robust_set_valued_successor,
)
from mrm.voi import rank_actions_by_value_of_information

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "artifacts" / "mrm_core_report.json"


def build_report() -> dict[str, object]:
    universal = CandidateLawFamily(
        states=(0, 1),
        actions=("act",),
        transitions=(((0, 1),), ((0, 1),)),
    )
    disagreement = CandidateLawFamily(
        states=(0, 1),
        actions=("passive", "intervene"),
        transitions=(((0, 1), (0, 1)), ((0, 1), (1, 0))),
    )
    joint = JointUncertaintyFamily(
        inside_cardinality=4,
        exterior_cardinalities=(2, 4),
        response_type_count=4,
    )
    local_irrelevance = CandidateLawFamily(
        states=(0, 1),
        actions=("act",),
        transitions=(((0, 1),), ((1, 1),)),
    )
    quotient = minimal_candidate_safe_quotient(local_irrelevance)
    discrimination = CandidateLawFamily(
        states=(0, 1),
        actions=("probe", "split"),
        transitions=(
            ((0, 0), (0, 0)),
            ((0, 0), (1, 0)),
            ((1, 1), (0, 0)),
        ),
    )
    plan = shortest_active_discrimination_plan(discrimination, 0)
    frontier = binary_signature_frontier(4)
    cost_tradeoff = CandidateLawFamily(
        states=(0, 1, 2, 3),
        actions=("direct", "cheap_high_bit", "cheap_low_bit"),
        transitions=tuple(
            (
                (response_type,) * 4,
                ((response_type >> 1) & 1,) * 4,
                (2 + (response_type & 1),) * 4,
            )
            for response_type in range(4)
        ),
    )
    shortest_cost_tradeoff = shortest_active_discrimination_plan(cost_tradeoff, 0)
    cheapest_cost_tradeoff = minimum_cost_active_discrimination_plan(
        cost_tradeoff,
        0,
        {"direct": 5.0, "cheap_high_bit": 1.0, "cheap_low_bit": 1.0},
    )
    robust_family = CandidateLawFamily(
        states=(0, 1, 2, 3),
        actions=("direct", "flip"),
        transitions=tuple(
            (
                (response_type,) * 4,
                ((response_type + 1) % 4,) * 4,
            )
            for response_type in range(4)
        ),
    )
    exact_observation = robust_observation_update(
        robust_family,
        RobustObservationModel.exact(robust_family.states),
        0,
        "direct",
        2,
    )
    bounded_observation = robust_observation_update(
        robust_family,
        RobustObservationModel(
            robust_family.states,
            {
                0: (0, 1),
                1: (0, 1, 2),
                2: (1, 2, 3),
                3: (2, 3),
            },
        ),
        0,
        "direct",
        1,
    )
    bounded_successor = robust_set_valued_successor(
        robust_family,
        bounded_observation.remaining_response_types,
        0,
        "flip",
    )
    probabilistic_model = ProbabilisticObservationModel(
        robust_family.states,
        {
            0: {0: 0.70, 1: 0.20, 2: 0.10, 3: 0.00},
            1: {0: 0.10, 1: 0.60, 2: 0.20, 3: 0.10},
            2: {0: 0.05, 1: 0.25, 2: 0.60, 3: 0.10},
            3: {0: 0.00, 1: 0.10, 2: 0.20, 3: 0.70},
        },
    )
    posterior_update = posterior_observation_update(
        robust_family,
        probabilistic_model,
        0,
        "direct",
        1,
    )
    if posterior_update is None:
        raise AssertionError("probabilistic witness unexpectedly contradicted")
    posterior_successor = posterior_set_valued_successor(
        robust_family,
        posterior_update,
        0,
        "flip",
    )
    voi_family = CandidateLawFamily(
        states=(0, 1, 2, 3),
        actions=("perfect", "half_split", "uninformative"),
        transitions=tuple(
            (
                (response_type,) * 4,
                ((response_type >> 1) & 1,) * 4,
                (0,) * 4,
            )
            for response_type in range(4)
        ),
    )
    voi_design = rank_actions_by_value_of_information(
        voi_family,
        ProbabilisticObservationModel.exact(voi_family.states),
        0,
        {"perfect": 3.0, "half_split": 0.25, "uninformative": 0.0},
        cost_per_bit=1.0,
        resolution_threshold=0.99,
    )
    voi_values = {value.action: value for value in voi_design.action_values}
    if (
        not universal.universal
        or disagreement.universal
        or not disagreement.response_separated()
        or not joint.verify()
        or quotient.state_count != 3
        or plan is None
        or plan.worst_case_steps != 2
        or not all(point.verify() for point in frontier)
        or shortest_cost_tradeoff is None
        or shortest_cost_tradeoff.action != "direct"
        or cheapest_cost_tradeoff is None
        or cheapest_cost_tradeoff.action != "cheap_high_bit"
        or not isclose(cheapest_cost_tradeoff.worst_case_cost, 2.0)
        or exact_observation.remaining_response_types != (2,)
        or bounded_observation.remaining_response_types != (0, 1, 2)
        or bounded_successor != frozenset({1, 2, 3})
        or posterior_update.map_response_types != (1,)
        or posterior_update.resolved_at(0.90)
        or not posterior_update.resolved_at(0.50)
        or posterior_update.credible_set(0.75) != (1, 2, 0)
        or posterior_successor != frozenset({0, 1, 2, 3})
        or voi_design.best_by_expected_information_gain.action != "perfect"
        or voi_design.best_by_net_information_gain.action != "half_split"
        or not isclose(voi_values["perfect"].expected_information_gain_bits, 2.0)
        or not isclose(voi_values["half_split"].expected_information_gain_bits, 1.0)
        or not isclose(voi_values["perfect"].net_information_gain_bits, -1.0)
        or not isclose(voi_values["half_split"].net_information_gain_bits, 0.75)
    ):
        raise AssertionError("MRM finite witness failed verification")
    return {
        "schema_version": 7,
        "scope": (
            "declared finite candidate macro-transition tables, exact, bounded-"
            "support, or probabilistic observed macrostates, declared intervention "
            "grammar, priors, likelihoods, and action costs"
        ),
        "non_claim": (
            "the replay does not infer ecological mechanisms, candidate sets, "
            "response types, action grammars, action costs, observation-error "
            "supports, likelihoods, priors, or noisy-risk-weighted experiment "
            "policies from data"
        ),
        "universal_law": {
            "response_type_count": universal.response_type_count,
            "report": universal.report_kind(),
        },
        "mechanism_disagreement": {
            "response_type_count": disagreement.response_type_count,
            "report": disagreement.report_kind(),
            "set_valued_successor": sorted(
                disagreement.set_valued_transition("intervene", 0)
            ),
            "candidate_safe_memory_bits": candidate_safe_memory_bits(disagreement),
        },
        "minimal_candidate_safe_quotient": {
            "full_typed_product_state_count": quotient.full_typed_product_state_count,
            "quotient_state_count": quotient.state_count,
            "quotient_memory_bits": quotient.memory_bits,
        },
        "active_discrimination": {
            "response_type_count": discrimination.response_type_count,
            "start_state": 0,
            "root_action": plan.action,
            "worst_case_steps": plan.worst_case_steps,
        },
        "mechanism_ambiguity_frontier": [
            point.replay_record() for point in frontier
        ],
        "cost_aware_discrimination": {
            "response_type_count": cost_tradeoff.response_type_count,
            "start_state": 0,
            "shortest_root_action": shortest_cost_tradeoff.action,
            "shortest_worst_case_steps": shortest_cost_tradeoff.worst_case_steps,
            "minimum_cost_root_action": cheapest_cost_tradeoff.action,
            "minimum_cost_worst_case_steps": cheapest_cost_tradeoff.worst_case_steps,
            "minimum_worst_case_cost": cheapest_cost_tradeoff.worst_case_cost,
        },
        "robust_observation_update": {
            "exact_remaining_response_types": list(
                exact_observation.remaining_response_types
            ),
            "bounded_observed_state": bounded_observation.observed_state,
            "bounded_compatible_true_states": list(
                bounded_observation.compatible_true_states
            ),
            "bounded_remaining_response_types": list(
                bounded_observation.remaining_response_types
            ),
            "bounded_eliminated_response_types": list(
                bounded_observation.eliminated_response_types
            ),
            "bounded_next_set_valued_successor": sorted(bounded_successor),
        },
        "probabilistic_observation_update": {
            "observed_state": posterior_update.observed_state,
            "evidence_probability": posterior_update.evidence_probability,
            "posterior": list(posterior_update.posterior),
            "map_response_types": list(posterior_update.map_response_types),
            "map_probability": posterior_update.map_probability,
            "entropy_bits": posterior_update.entropy_bits,
            "resolved_at_050": posterior_update.resolved_at(0.50),
            "resolved_at_090": posterior_update.resolved_at(0.90),
            "credible_set_075": list(posterior_update.credible_set(0.75)),
            "positive_posterior_next_set_valued_successor": sorted(
                posterior_successor
            ),
        },
        "value_of_information_design": {
            "best_by_expected_information_gain": (
                voi_design.best_by_expected_information_gain.action
            ),
            "best_by_net_information_gain": (
                voi_design.best_by_net_information_gain.action
            ),
            "perfect_expected_information_gain_bits": (
                voi_values["perfect"].expected_information_gain_bits
            ),
            "half_split_expected_information_gain_bits": (
                voi_values["half_split"].expected_information_gain_bits
            ),
            "uninformative_expected_information_gain_bits": (
                voi_values["uninformative"].expected_information_gain_bits
            ),
            "perfect_net_information_gain_bits": (
                voi_values["perfect"].net_information_gain_bits
            ),
            "half_split_net_information_gain_bits": (
                voi_values["half_split"].net_information_gain_bits
            ),
            "uninformative_net_information_gain_bits": (
                voi_values["uninformative"].net_information_gain_bits
            ),
            "perfect_resolution_probability": (
                voi_values["perfect"].resolution_probability
            ),
            "half_split_resolution_probability": (
                voi_values["half_split"].resolution_probability
            ),
        },
        "joint_uncertainty": {
            "joint_state_count": joint.joint_state_count,
            "fixed_candidate_memory_bits": joint.fixed_candidate_memory_bits,
            "joint_safe_memory_bits": joint.joint_safe_memory_bits,
        },
    }


def main() -> None:
    report = build_report()
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
