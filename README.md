# MRM — Mechanism-Robust Macro-Laws

MRM is a theorem-first mathematical-ecology repository for one uncertainty
question:

> When multiple retained mechanisms support compact exact instance laws but
> disagree about future macro transitions, what is the strongest law that can be
> reported without pretending the mechanism uncertainty has vanished?

MRM also maintains the program-level **Contract-Relative Ecological State Theory
(CREST)** synthesis connecting CCOC, MLTR, MRM, and CED. Companion theorem ownership
remains separate.

## MRM publication core

1. **Universal deterministic law.** A candidate-independent macro-law exists exactly
   when all retained candidates induce the same transition maps.
2. **Typed or set-valued law.** When candidates disagree, retaining response type
   gives an exact deterministic law; forgetting it gives the exact set-valued
   successor relation.
3. **Minimal candidate-safe quotient.** The coarsest observation-preserving
   deterministic quotient retains only response-type distinctions that declared
   future actions can expose.
4. **Mechanism-ambiguity frontier.** A canonical binary family gives an exact
   mechanism-memory and intervention-depth frontier.
5. **Active and cost-aware discrimination.** Finite dynamic programs minimize
   worst-case intervention depth or positive action cost under the declared family.

Product/joint bounds are supporting mechanism results. Robust/probabilistic
observation updates and one-step VOI are conditional adapters; they do not make MRM
the owner of CED's broader evidence, failure, calibration, or risk-contract layer.

## Ecological reading

Retained mechanisms can represent alternative pollination responses, disturbance
effects, pathogen pathways, colonization dynamics, or management responses. They
may agree on the visible community now but disagree about what a future intervention
does. MRM formalizes when one deterministic forecast is justified, when a
response-type distinction must remain, when ambiguity should be typed or set-valued,
and when declared interventions can resolve it.

## CREST — program-level synthesis

Canonical synthesis:

- [Contract-Relative Ecological State Theory](docs/contract_relative_ecological_state_theory.md)
- [CREST J1/J2/J3 synthesis proof ledger](docs/crest_synthesis_proof_ledger_2026-08-17.md)

The four companion audits are:

- **CCOC / future sufficiency:** which distinctions an enlarged legal future can
  make necessary;
- **MLTR / semantic coherence:** which distinctions an inherited source law must add
  after structural change;
- **MRM / mechanism robustness:** which retained mechanism distinctions change the
  requested future prediction;
- **CED / evidential licensing:** which distinctions finite imperfect evidence can
  legitimately resolve and report.

### Proved synthesis chain

CREST now has three conditional finite synthesis theorems:

1. **CREST-J3 — maximal synchronized common carrier.** From a declared finite
   ambient component synchronization, compute the unique greatest compatible
   transition-closed carrier `U*`. A common lift exists iff `U*` is nonempty; a
   coverage-complete lift exists iff `U*` represents every required component
   label. Removed tuples carry finite action-chain no-go certificates.
2. **CREST-J1 — unique coarsest joint state.** On one finite common carrier with four
   monotone inflationary audit closures, fair refinement produces the unique
   coarsest common fixed point `J`. Full deterministic state reporting is licensed
   exactly when the evidence partition refines `J`; otherwise the sharp state report
   remains set-valued. A target may still be reportable without the full state.
3. **CREST-J2 — faithful-lift invariance.** If a detailed finite lift projects
   surjectively to a reduced lift while preserving all audit/evidence/target
   structure, then `J_U = pi^* J_V` and the quotient states are isomorphic. Raw
   latent detail invisible to every declared contract cannot change the scientific
   state.

```text
declared ambient synchronization
  -> J3 maximal coherent carrier U*
  -> J1 unique coarsest four-audit state J + evidence gate
  -> J2 invariance across faithfully redundant lifts
```

This is a conditional theorem ladder, not a claim that nature supplies one universal
state partition. Uniqueness is within one declared finite contract and across
faithfully equivalent lifts—not across different grammars, inherited meanings,
mechanism families, evidence contracts, targets, or ambient alignments.

## Claim firewall

Shared refinement/fixed-point machinery is classical substrate.

- independently optimized closed-vs-open interface lower bounds belong to CCOC;
- inherited-law transport, repair, defect, and history belong to MLTR;
- retained mechanism disagreement and candidate-safe state belong to MRM;
- finite/noisy evidence, failure architecture, calibration, and risk-limited
  reportability belong to CED;
- conditional carrier/joint-state/lift synthesis is maintained here as CREST.

Do not add a theorem family merely because it can be described using `state`,
`quotient`, `refinement`, `uncertainty`, or `adequacy`.

## Proof and verification map

### MRM companion proofs

- [Recovered MRM core proofs](docs/mrm_core_proofs.md)
- [Minimal quotient and active discrimination](docs/minimal_quotient_active_discrimination.md)
- [Mechanism-ambiguity frontier](docs/mechanism_ambiguity_frontier.md)
- [Cost-aware discrimination](docs/cost_aware_active_discrimination.md)
- [Robust observation update](docs/robust_observation_update.md)
- [Probabilistic observation update](docs/probabilistic_observation_update.md)
- [Value-of-information design](docs/value_of_information_design.md)

### CREST synthesis proofs

- [J3 maximal common lift](docs/crest_maximal_common_lift_theorem_2026-08-17.md)
  — `mrm/crest_common_lift.py`, `tests/test_crest_common_lift.py`
- [J1 joint-state theorem](docs/crest_joint_state_theorem_2026-08-17.md)
  — `mrm/crest_joint_state.py`, `tests/test_crest_joint_state.py`
- [J2 faithful-lift invariance](docs/crest_lift_invariance_theorem_2026-08-17.md)
  — `mrm/crest_lift_invariance.py`, `tests/test_crest_lift_invariance.py`
- [Synthesis proof ledger](docs/crest_synthesis_proof_ledger_2026-08-17.md)
- [Companion proof-recovery ledger](docs/crest_proof_recovery_2026-08-17.md)
- [Cross-repository validation](docs/crest_final_validation_2026-08-17.md)

### Philosophy manuscript controls

- `manuscript/crest_philosophy_biology_philosophy.md`
- `manuscript/biology_philosophy_submission_handoff.md`
- `docs/crest_biology_philosophy_submission_audit_2026-08-17.md`

The current journal manuscript retains the safe claim that no **unconditional
universal** ecological state has been proved. J1–J3 may be integrated only after a
fresh manuscript claim/prior-art audit.

## Run

```bash
python -m pip install -e '.[dev]'
pytest
python scripts/verify_mrm_core.py
python scripts/verify_crest_philosophy_submission.py --write-report
```

CI runs the theorem suite on Python 3.10, 3.11, and 3.12; Python 3.12 also writes
deterministic replay and submission-control artifacts. Passing CI verifies the
implementation surface, not the quantified analytic proofs by itself.

## Scope

The current mathematics is finite and declared-model relative. It does not infer
future grammars, source-target relations, mechanism families, synchronization
relations, observation-error contracts, priors, action costs, ecological targets,
or empirical validity from data. Stochastic, approximate, infinite, controlled
viability, and empirical common-lift inference remain open extensions.
