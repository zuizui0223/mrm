# MRM — Mechanism-Robust Macro-Laws

MRM is a theorem-first mathematical-ecology repository for one uncertainty question:

> When retained mechanisms agree on the visible state but disagree about future interventions, what is the strongest deterministic, typed, or set-valued law that can be reported honestly?

## Publication core

1. A candidate-independent deterministic law exists exactly when retained response types agree on the declared transition maps.
2. Otherwise typed deterministic and candidate-forgetting set-valued reports preserve unresolved mechanism ambiguity.
3. The unique coarsest observation-preserving candidate-safe quotient retains only response-type distinctions that can affect declared future behavior.
4. The mechanism-ambiguity frontier gives sharp state-memory and intervention-depth witnesses.
5. Finite active and positive-cost discrimination identify response type when the declared action grammar permits it.

Observation updates, posterior summaries, and one-step value-of-information calculations are conditional adapters around the mechanism-report target. They do not transfer CED's evidence, failure, calibration, or risk-contract layer to MRM.

## CREST role: mechanistic insufficiency of a present-state merge

The cross-contract synthesis lives in the dedicated [CREST repository](https://github.com/zuizui0223/crest). The current hierarchy is fixed in the [trajectory-first program architecture](https://github.com/zuizui0223/crest/blob/main/docs/trajectory_first_program_architecture_2026-08-22.md).

CREST now starts from temporally extended ecological worlds and asks when a present snapshot is sufficient for a declared scientific state. Within that hierarchy, MRM is the **mechanistic obstruction theory**.

Two ecological worlds may share the same visible present state while retaining different response mechanisms. MRM asks whether those mechanism differences can be forgotten. They become state-relevant exactly when retained mechanisms disagree on a future response required by the contract.

\[
\boxed{
\text{same visible present state}
\not\Rightarrow
\text{same required state when retained mechanisms disagree on a relevant future}.
}
\]

MRM therefore does not identify ecological state with full mechanism identity. Its minimal candidate-safe quotient preserves only **response-relevant mechanism distinctions**.

Within the trajectory-first CREST hierarchy:

- **CCOC** handles future/composition distinctions exposed by a wider future grammar;
- **MLTR** handles inherited meaning and structural replacement;
- **MRM** handles retained mechanism disagreement;
- **CED** is downstream evidence licensing: whether observations actually identify the distinctions that the required state needs.

CREST's finite joint-carrier, joint-state, lift, repair, philosophy, and representational-stability results are not part of the MRM publication API.

The audited extraction provenance is recorded in `docs/crest_extraction_provenance.md`.

## Proof and verification map

- [Recovered MRM core proofs](docs/mrm_core_proofs.md)
- [Minimal quotient and active discrimination](docs/minimal_quotient_active_discrimination.md)
- [Mechanism-ambiguity frontier](docs/mechanism_ambiguity_frontier.md)
- [Cost-aware discrimination](docs/cost_aware_active_discrimination.md)
- [Robust observation update](docs/robust_observation_update.md)
- [Probabilistic observation update](docs/probabilistic_observation_update.md)
- [Value-of-information design](docs/value_of_information_design.md)

## Run

```bash
python -m pip install -e '.[dev]'
pytest
python scripts/verify_mrm_core.py
```

CI runs the theorem suite on Python 3.10, 3.11, and 3.12. Python 3.12 also writes the deterministic MRM replay artifact. Passing CI verifies the implementation surface; the analytic proofs remain the theorem basis.

## Scope

MRM concerns declared finite candidate mechanism families on a common observable macrostate space. It does not infer candidate sets, mechanisms, response types, alignments, observation models, priors, likelihoods, action costs, or empirical validity from data. Cross-contract carrier, repair, joint-state, lift, trajectory-level interpretation, and philosophy results belong to CREST rather than MRM.
