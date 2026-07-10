import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "verify_mrm_core.py"


def test_replay_report_matches_declared_witnesses():
    completed = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    report = json.loads(completed.stdout)
    assert report["schema_version"] == 6
    assert report["universal_law"] == {
        "response_type_count": 1,
        "report": "universal",
    }
    assert report["mechanism_disagreement"] == {
        "response_type_count": 2,
        "report": "typed-or-set-valued",
        "set_valued_successor": [0, 1],
        "candidate_safe_memory_bits": 2.0,
    }
    assert report["minimal_candidate_safe_quotient"] == {
        "full_typed_product_state_count": 4,
        "quotient_state_count": 3,
        "quotient_memory_bits": math.log2(3),
    }
    assert report["active_discrimination"] == {
        "response_type_count": 3,
        "start_state": 0,
        "root_action": "probe",
        "worst_case_steps": 2,
    }
    assert report["mechanism_ambiguity_frontier"] == [
        {
            "signature_width": 1,
            "response_type_count": 2,
            "fixed_candidate_state_count": 2,
            "candidate_safe_state_count": 4,
            "fixed_candidate_memory_bits": 1.0,
            "candidate_safe_memory_bits": 2.0,
            "ambiguity_memory_surcharge_bits": 1.0,
            "optimal_identification_steps": 1,
        },
        {
            "signature_width": 2,
            "response_type_count": 4,
            "fixed_candidate_state_count": 2,
            "candidate_safe_state_count": 8,
            "fixed_candidate_memory_bits": 1.0,
            "candidate_safe_memory_bits": 3.0,
            "ambiguity_memory_surcharge_bits": 2.0,
            "optimal_identification_steps": 2,
        },
        {
            "signature_width": 3,
            "response_type_count": 8,
            "fixed_candidate_state_count": 2,
            "candidate_safe_state_count": 16,
            "fixed_candidate_memory_bits": 1.0,
            "candidate_safe_memory_bits": 4.0,
            "ambiguity_memory_surcharge_bits": 3.0,
            "optimal_identification_steps": 3,
        },
        {
            "signature_width": 4,
            "response_type_count": 16,
            "fixed_candidate_state_count": 2,
            "candidate_safe_state_count": 32,
            "fixed_candidate_memory_bits": 1.0,
            "candidate_safe_memory_bits": 5.0,
            "ambiguity_memory_surcharge_bits": 4.0,
            "optimal_identification_steps": 4,
        },
    ]
    assert report["cost_aware_discrimination"] == {
        "response_type_count": 4,
        "start_state": 0,
        "shortest_root_action": "direct",
        "shortest_worst_case_steps": 1,
        "minimum_cost_root_action": "cheap_high_bit",
        "minimum_cost_worst_case_steps": 2,
        "minimum_worst_case_cost": 2.0,
    }
    assert report["robust_observation_update"] == {
        "exact_remaining_response_types": [2],
        "bounded_observed_state": 1,
        "bounded_compatible_true_states": [0, 1, 2],
        "bounded_remaining_response_types": [0, 1, 2],
        "bounded_eliminated_response_types": [3],
        "bounded_next_set_valued_successor": [1, 2, 3],
    }
    probabilistic = report["probabilistic_observation_update"]
    assert probabilistic["observed_state"] == 1
    assert math.isclose(probabilistic["evidence_probability"], 0.2875)
    assert probabilistic["map_response_types"] == [1]
    assert math.isclose(probabilistic["map_probability"], 0.60 / 1.15)
    assert probabilistic["resolved_at_050"] is True
    assert probabilistic["resolved_at_090"] is False
    assert probabilistic["credible_set_075"] == [1, 2, 0]
    assert probabilistic["positive_posterior_next_set_valued_successor"] == [0, 1, 2, 3]
    assert report["joint_uncertainty"] == {
        "joint_state_count": 128,
        "fixed_candidate_memory_bits": 5.0,
        "joint_safe_memory_bits": 7.0,
    }
