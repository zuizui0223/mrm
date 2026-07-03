from scripts.verify_mrm_core import build_report


def test_replay_report_matches_declared_witnesses():
    report = build_report()
    assert report["schema_version"] == 1
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
    assert report["joint_uncertainty"] == {
        "joint_state_count": 128,
        "fixed_candidate_memory_bits": 5.0,
        "joint_safe_memory_bits": 7.0,
    }
