# MRM — Mechanism-Robust Macro-Laws

MRM is a theorem-first mathematical-ecology repository for one uncertainty question:

> When retained mechanisms agree on the visible state but disagree about future interventions, what must an honest macro-law remember, and how many interventions are fundamentally required to resolve the ambiguity?

## Publication center

The paper is now organized around the paired mechanism-ambiguity frontier in `docs/mrm_core_proofs.md` and `docs/mechanism_ambiguity_frontier.md`.

1. **Honest reporting:** a candidate-independent deterministic law exists exactly when retained response types agree on the declared transition maps; otherwise deterministic prediction must retain response-relevant type information or the candidate-forgetting report remains set-valued.
2. **Minimal state:** the unique coarsest observation-preserving candidate-safe quotient retains only response-type distinctions that can change declared future observations.
3. **Theorem 7 — exact memory frontier:** in the canonical `m`-bit response family the candidate-safe law has `2^(m+1)` states and `m+1` bits, an exact `m`-bit surcharge relative to a fixed two-state candidate law.
4. **Theorem 8 — exact intervention frontier:** exactly `m` binary probes are necessary and sufficient in the worst case to identify one of the `2^m` response signatures; after `k` distinct probes exactly `2^(m-k)` signatures remain compatible.
5. **General finite discrimination:** dynamic programming returns the shortest exact active-discrimination policy when one exists, and the minimum worst-case total intervention cost under positive declared action costs.

Theorem 8 is the manuscript headline. Theorem 7 supplies its paired representational burden: unresolved mechanism ambiguity has both a state-memory price and an experimental price.

Observation updates, posterior summaries, and one-step value-of-information calculations are **downstream adapters** around this mechanism-report target. Bayesian preference for a response type is not exact mechanism resolution, and posterior/VOI machinery is not renumbered as Theorem 8.

## CREST role: mechanistic insufficiency of a present-state merge

The cross-contract synthesis lives in the dedicated [CREST repository](https://github.com/zuizui0223/crest). The current hierarchy is fixed in the [trajectory-first program architecture](https://github.com/zuizui0223/crest/blob/main/docs/trajectory_first_program_architecture_2026-08-22.md).

Within that hierarchy, MRM is the **mechanistic obstruction theory**. Two ecological worlds may share the same visible present state while retaining different response mechanisms. Those differences become state-relevant exactly when they change a future response required by the declared scientific contract.

\[
\boxed{
\text{same visible present state}
\not\Rightarrow
\text{same required state when retained mechanisms disagree on a relevant future}.
}
\]

MRM does not identify ecological state with full mechanism identity. Its minimal candidate-safe quotient preserves only **response-relevant mechanism distinctions**.

Within the trajectory-first CREST hierarchy:

- **CCOC** handles future/composition distinctions exposed by a wider future grammar;
- **MLTR** handles inherited meaning and structural replacement;
- **MRM** handles retained mechanism disagreement;
- **CED** is downstream evidence licensing: whether observations identify distinctions the required state needs.

CREST's finite joint-carrier, joint-state, lift, repair, philosophy, and representational-stability results are not part of the MRM publication API. Extraction provenance is recorded in `docs/crest_extraction_provenance.md`.

## Proof and verification map

- [Recovered MRM core proofs](docs/mrm_core_proofs.md) — authoritative theorem numbering, including Theorems 7–9.
- [Mechanism-ambiguity frontier](docs/mechanism_ambiguity_frontier.md) — paired Result VII/VIII witness family.
- [Minimal quotient and active discrimination](docs/minimal_quotient_active_discrimination.md)
- [Cost-aware discrimination](docs/cost_aware_active_discrimination.md)
- [Robust observation update](docs/robust_observation_update.md) — supporting adapter.
- [Probabilistic observation update](docs/probabilistic_observation_update.md) — supporting adapter.
- [Value-of-information design](docs/value_of_information_design.md) — supporting design diagnostic.
- [Theorem-8-centered manuscript architecture](docs/manuscript_skeleton.md)

## Run

```bash
python -m pip install -e '.[dev]'
pytest
python scripts/verify_mrm_core.py
```

CI runs the theorem suite on Python 3.10, 3.11, and 3.12. Python 3.12 also writes the deterministic MRM replay artifact. Passing CI verifies the implementation surface; analytic proofs remain the theorem basis.

## Scope

MRM concerns declared finite candidate mechanism families on a common observable macrostate space. It does not infer candidate sets, mechanisms, response types, alignments, observation models, priors, likelihoods, action costs, or empirical validity from data. The canonical Theorem 7–8 frontier is finite and noiseless, conditional on a declared binary probe grammar. Cross-contract carrier, repair, joint-state, lift, trajectory-level interpretation, and philosophy results belong to CREST rather than MRM.
