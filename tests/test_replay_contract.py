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
    assert report["schema_version"] == 2
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
    assert report["joint_uncertainty"] == {
        "joint_state_count": 128,
        "fixed_candidate_memory_bits": 5.0,
        "joint_safe_memory_bits": 7.0,
    }
