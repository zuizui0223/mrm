"""Write a deterministic finite replay report for the MRM theorem core."""

from __future__ import annotations

import json
from pathlib import Path

from mrm.joint import JointUncertaintyFamily
from mrm.laws import CandidateLawFamily, candidate_safe_memory_bits
from mrm.quotient import (
    minimal_candidate_safe_quotient,
    shortest_active_discrimination_plan,
)

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
    if (
        not universal.universal
        or disagreement.universal
        or not disagreement.response_separated()
        or not joint.verify()
        or quotient.state_count != 3
        or plan is None
        or plan.worst_case_steps != 2
    ):
        raise AssertionError("MRM finite witness failed verification")
    return {
        "schema_version": 2,
        "scope": (
            "declared finite candidate macro-transition tables, exact observed "
            "macrostates, and declared intervention grammar"
        ),
        "non_claim": (
            "the replay does not infer ecological mechanisms, candidate sets, "
            "response types, action grammars, or noisy-risk-weighted experiment "
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
