# MRM — Mechanism-Robust Macro-Laws

MRM is a theorem-first mathematical-ecology repository for one uncertainty
question:

> When retained mechanisms agree on the visible state but disagree about future
> interventions, what is the strongest deterministic, typed, or set-valued law that
> can be reported honestly?

MRM also maintains the program-level **Contract-Relative Ecological State Theory
(CREST)** synthesis connecting CCOC, MLTR, MRM, and CED. Companion theorem ownership
remains separate.

## MRM publication core

1. candidate-independent deterministic law iff retained response types agree;
2. exact typed and candidate-forgetting set-valued reports;
3. unique coarsest observation-preserving candidate-safe quotient;
4. sharp mechanism-memory / intervention frontier; and
5. exact finite active and positive-cost discrimination.

Observation updates and one-step VOI are conditional adapters. They do not transfer
CED's evidence/failure/calibration layer to MRM.

## CREST — one principle, four companion audits

CREST treats a state merge as a scientific commitment about which differences may
be ignored for a declared contract

\[
\mathcal C=(\Gamma,\mathcal H,\Theta,D;T).
\]

- **CCOC — future sufficiency:** what an enlarged legal future can expose;
- **MLTR — semantic coherence:** what an inherited law must split after change;
- **MRM — mechanism robustness:** what retained response disagreement prevents;
- **CED — evidential licensing:** what finite imperfect evidence permits reporting.

Canonical documents:

- [Contract-Relative Ecological State Theory](docs/contract_relative_ecological_state_theory.md)
- [CREST synthesis proof ledger](docs/crest_synthesis_proof_ledger_2026-08-17.md)

## Proved conditional synthesis ladder

CREST currently has six finite synthesis theorems. They do not form a nature-given
ontology; they operate after the synchronization, action roles, audits, evidence,
targets, and any repair costs are declared.

### Carrier gates

1. **J3 — universal common carrier.** Keep exactly the greatest compatible carrier
   closed under **every** declared legal transition. Return finite elimination and
   coverage no-go certificates when it fails.
2. **J6 — controlled common carrier.** Keep exactly the greatest compatible carrier
   that survives every uncontrollable transition and has at least one safe
   controllable transition at every retained world. Return a memoryless safe
   selector or a typed finite AND/OR no-go certificate.
3. **J4 — exact declared repair after carrier no-go.** Within the explicit language
   “admit one incompatible world / disable one transition / waive one coverage
   obligation,” minimize the forced weighted repair cost over all nonempty retained
   subsets. Tied optima remain explicit.

J3 and J6 answer different contracts. J3 requires safety under all actions; J6 asks
whether one control policy can remain safe against all uncontrollable moves.

### State and lift results

4. **J1 — unique coarsest four-audit state.** On one admissible finite carrier,
   fair refinement of the four audit closures reaches one least-information common
   fixed point `J`. Full deterministic reporting is licensed iff evidence resolves
   `J`; otherwise the sharp state report is set-valued. A requested target can still
   be reportable without the full state.
5. **J2 — faithful-lift invariance.** Scientifically invisible latent duplication
   leaves `J` and evidential licensing unchanged up to quotient isomorphism.
6. **J5 — one-sided lift bounds.** Adding preserved obligations can only refine the
   pulled joint state; forgetting obligations can only coarsen it. J2 is the equality
   case. Full-state licensing changes only in the corresponding one-sided direction.

```text
declared ambient synchronization
  -> choose action contract:
       J3 universal carrier
       J6 controlled carrier + safe selector
  -> carrier or finite no-go
  -> if needed: J4 exact least-cost declared relaxation
  -> admissible carrier
  -> J1 unique coarsest four-audit state + evidence gate
  -> compare alternate lifts/contracts:
       J2 exact faithful equality
       J5 one-sided refinement bounds
```

## Claim firewall

The shared mathematical tools are established substrate:

- partition refinement, closure operators, and fixed points;
- invariant, viability, and safety kernels;
- finite safety games and memoryless safety policies;
- minimum-cost model repair and subset optimization;
- quotient naturality, simulation, and abstraction precision.

The CREST claim is the ecology-specific contract architecture and its typed gates,
not invention of those generic algorithms.

Ownership remains:

- CCOC — closed-vs-open interface lower bounds;
- MLTR — inherited-law transport, repair, defect, and history;
- MRM — retained mechanism disagreement and candidate-safe prediction;
- CED — finite evidence, observation failure, calibration, and risk-limited report;
- CREST in MRM — conditional carrier, repair, joint-state, evidence, and
  cross-lift synthesis.

J4 is not MLTR semantic repair. J6 does not infer which actions are controllable.
J5 does not establish that a stronger contract is normatively preferable.

## Proof and verification map

### MRM core

- [Recovered MRM core proofs](docs/mrm_core_proofs.md)
- [Minimal quotient and active discrimination](docs/minimal_quotient_active_discrimination.md)
- [Mechanism-ambiguity frontier](docs/mechanism_ambiguity_frontier.md)
- [Cost-aware discrimination](docs/cost_aware_active_discrimination.md)

### CREST synthesis

- [J3 maximal universal common lift](docs/crest_maximal_common_lift_theorem_2026-08-17.md)
  — `mrm/crest_common_lift.py`, `tests/test_crest_common_lift.py`
- [J6 controlled common-lift viability](docs/crest_controlled_common_lift_theorem_2026-08-18.md)
  — `mrm/crest_controlled_lift.py`, `tests/test_crest_controlled_lift.py`
- [J4 minimum declared common-lift relaxation](docs/crest_minimum_common_lift_relaxation_theorem_2026-08-17.md)
  — `mrm/crest_common_lift_relaxation.py`, related tests
- [J1 joint-state theorem](docs/crest_joint_state_theorem_2026-08-17.md)
  — `mrm/crest_joint_state.py`, `tests/test_crest_joint_state.py`
- [J2 faithful-lift invariance](docs/crest_lift_invariance_theorem_2026-08-17.md)
  — `mrm/crest_lift_invariance.py`, `tests/test_crest_lift_invariance.py`
- [J5 one-sided lift bounds](docs/crest_lax_lift_bounds_theorem_2026-08-18.md)
  — `mrm/crest_lax_lift.py`, `tests/test_crest_lax_lift.py`

## Run

```bash
python -m pip install -e '.[dev]'
pytest
python scripts/verify_mrm_core.py
python scripts/verify_crest_philosophy_submission.py --write-report
```

CI runs the theorem suite on Python 3.10, 3.11, and 3.12. Python 3.12 also writes
deterministic replay and submission-control artifacts. Passing CI verifies the
implementation surface, not the analytic proofs by itself.

## Scope

The mathematics is finite and declared-model relative. It does not infer future
grammars, source-target relations, mechanism families, ambient synchronizations,
action controllability, evidence contracts, repair costs, ecological targets, or
empirical validity from data. Stochastic, partial-observation, delayed-control,
approximate, infinite, richer-repair, and empirical common-lift inference remain
open extensions.
