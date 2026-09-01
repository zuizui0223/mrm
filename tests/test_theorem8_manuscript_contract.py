from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
SKELETON = ROOT / "docs" / "manuscript_skeleton.md"
PROOFS = ROOT / "docs" / "mrm_core_proofs.md"
FRONTIER = ROOT / "docs" / "mechanism_ambiguity_frontier.md"


def test_authoritative_theorem_8_is_the_exact_intervention_frontier():
    proofs = PROOFS.read_text(encoding="utf-8")
    marker = "### Theorem 8 — exact intervention frontier"
    assert marker in proofs
    section = proofs.split(marker, 1)[1].split("---", 1)[0]
    assert "Exactly `m` binary probes are necessary and sufficient" in section
    assert "2^d" in section
    assert "d>=m" in section


def test_manuscript_architecture_centers_theorem_7_8_pair():
    text = SKELETON.read_text(encoding="utf-8")
    assert "Theorem 8 is the manuscript center" in text
    assert "Theorem 7 — exact memory frontier" in text
    assert "Theorem 8 — exact intervention frontier" in text
    assert text.index("Theorem 7 — exact memory frontier") < text.index(
        "Theorem 8 — exact intervention frontier"
    )
    assert "Result 4 — Theorem 8: exact intervention frontier" in text
    assert "intervention identification burden" in text
    assert "Do not call this Theorem 8 in the manuscript" in text
    assert "Theorem 8 — Probabilistic posterior update" not in text


def test_readme_and_frontier_keep_state_and_experiment_burdens_distinct():
    readme = README.read_text(encoding="utf-8")
    frontier = FRONTIER.read_text(encoding="utf-8")

    assert "Theorem 8 — exact intervention frontier" in readme
    assert "Theorem 7 — exact memory frontier" in readme
    assert "state-memory price and an experimental price" in readme
    assert "Result VII — Exact ambiguity frontier" in frontier
    assert "Result VIII — Exact active-identification frontier" in frontier
    assert "state **cardinality** grows exponentially" in frontier
    assert "memory surcharge grows linearly" in frontier


def test_posterior_and_voi_are_downstream_adapters_not_headline_theorems():
    readme = README.read_text(encoding="utf-8")
    skeleton = SKELETON.read_text(encoding="utf-8")
    assert "downstream adapters" in readme.lower()
    assert "Probabilistic posterior update" in skeleton
    assert "Methods/Supplement adapter" in skeleton
    assert "One-step value of information" in skeleton
    assert "Discussion/Methods adapter" in skeleton
