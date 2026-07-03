"""Write a deterministic finite replay report for the MRM theorem core."""

from __future__ import annotations

import json
from pathlib import Path

from mrm.joint import JointUncertaintyFamily
from mrm.laws import CandidateLawFamily, candidate_safe_memory_bits

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
    joint = JointUncertaintyFamily(inside_cardinality=4, exterior_cardinalities=(2, 4), response_type_count=4)
    if not universal.universal or disagreement.universal or not disagreement.response_separated() or not joint.verify():
        raise AssertionError("MRM finite witness failed verification")
    return {
        "schema_version": 1,
        "scope": "declared finite candidate macro-transition tables and declared joint operational separation",
        "non_claim": "the replay does not infer ecological mechanisms, candidate sets, response types, or action grammars from data",
        "universal_law": {
            "response_type_count": universal.response_type_count,
            "report": universal.report_kind(),
        },
        "mechanism_disagreement": {
            "response_type_count": disagreement.response_type_count,
            "report": disagreement.report_kind(),
            "set_valued_successor": sorted(disagreement.set_valued_transition("intervene", 0)),
            "candidate_safe_memory_bits": candidate_safe_memory_bits(disagreement),
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
