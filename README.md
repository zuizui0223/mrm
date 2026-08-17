# MRM — Mechanism-Robust Macro-Laws

MRM is a theorem-first mathematical-ecology repository for one uncertainty
question:

> When retained mechanisms agree on the visible state but disagree about future
> interventions, what is the strongest deterministic, typed, or set-valued law that
> can be reported honestly?

This repository **temporarily hosts** the cross-contract CREST synthesis unit and
its philosophy manuscript. Those assets are not part of the MRM mechanism theorem
family and are scheduled for extraction to `zuizui0223/crest`.

## MRM publication core

1. candidate-independent deterministic law iff retained response types agree;
2. exact typed and candidate-forgetting set-valued reports;
3. unique coarsest observation-preserving candidate-safe quotient;
4. sharp mechanism-memory / intervention frontier; and
5. exact finite active and positive-cost discrimination.

Observation updates and one-step VOI are conditional adapters. They do not transfer
CED's evidence/failure/calibration layer to MRM.

## CREST — separate synthesis unit, temporary physical host

CREST treats a state merge as a scientific commitment about which differences may
be ignored for a declared contract

\[
\mathcal C=(\Gamma,\mathcal H,\Theta,D;T).
\]

- **CCOC — future sufficiency:** what an enlarged legal future can expose;
- **MLTR — semantic coherence:** what an inherited law must split after change;
- **MRM — mechanism robustness:** what retained response disagreement prevents;
- **CED — evidential licensing:** what finite imperfect evidence permits reporting.

The J/O cross-contract results form a fifth logical research unit:

- [CREST synthesis unit charter](crest_synthesis/README.md)
- [Migration manifest](docs/crest_synthesis_migration_manifest_2026-08-18.md)
- [Canonical CREST theory](docs/contract_relative_ecological_state_theory.md)
- [Synthesis proof ledger](docs/crest_synthesis_proof_ledger_2026-08-17.md)

No new J/O theorem family may be added under the `mrm/` package path before the
physical extraction. Proof correction, complexity audit, regression testing, and
migration work remain allowed.

## Current CREST synthesis ladder

### Carrier gates

1. **J3 — universal common carrier.** Greatest compatible carrier closed under every
   declared legal transition, with finite elimination and coverage no-go
   certificates.
2. **J6 — controlled common carrier.** Greatest compatible carrier surviving every
   uncontrollable transition and retaining at least one safe controllable action at
   every world, with a memoryless selector or typed AND/OR no-go certificate.

### Typed repair gates

3. **J4 — universal-carrier repair characterization.** For a fixed retained subset,
   admission, transition-disable, and coverage-waiver operations are forced. The
   global value is the minimum over all nonempty subsets.
4. **J7 — controlled-carrier repair characterization.** For a fixed control-feasible
   retained subset, admission, uncontrollable-edge deletion, fallback installation,
   and coverage waiver are forced. The global value is the minimum over all feasible
   subsets, or a language-level no-repair result.

**Computational boundary:** the decision versions of both J4 and J7 are NP-complete
by direct weighted-set-cover reductions. The supplied solvers enumerate
`2^|W|-1` subsets and are exact exponential theorem oracles, not polynomial-time
algorithms. See
[the repair complexity boundary](docs/crest_repair_complexity_boundary_2026-08-18.md).

### State and lift results

5. **J1 — unique coarsest four-audit state.** Fair refinement on one admissible
   carrier reaches one least-information common fixed point `J`; evidence licenses
   full deterministic reporting iff it resolves `J`.
6. **J2 — faithful-lift invariance.** Scientifically invisible latent duplication
   leaves `J` and evidential licensing unchanged up to quotient isomorphism.
7. **J5 — one-sided lift bounds.** Added preserved obligations can only refine the
   pulled joint state; forgotten obligations can only coarsen it.

### Supporting obstruction

- **O1 — repair/evidence ordering obstruction.** The cheapest controlled-carrier
  repair need not be the cheapest repair whose downstream joint state is fully
  evidence-licensed.

```text
declared ambient synchronization
  -> choose carrier semantics: J3 or J6
  -> carrier or typed no-go
  -> choose matching repair semantics if needed: J4 or J7
  -> admissible carrier
  -> J1 joint state + evidence gate
  -> J2/J5 lift comparison
  -> O1 warning: structural and licensed optima can differ
```

## Claim firewall

The shared mathematics is established substrate:

- partition refinement, closure operators, and fixed points;
- invariant, viability, and safety kernels;
- finite safety games and memoryless safety policies;
- minimum-cost model repair, weighted set cover, and subset optimization;
- quotient naturality, simulation, and abstraction precision.

Ownership remains:

- CCOC — closed-vs-open interface lower bounds;
- MLTR — inherited-law transport, repair, defect, and history;
- MRM — retained mechanism disagreement and candidate-safe prediction;
- CED — finite evidence, observation failure, calibration, and risk-limited report;
- CREST synthesis unit — essential cross-contract carrier, repair, joint-state,
  evidence, and lift coupling.

J4/J7 are not MLTR semantic repair. J6/J7 do not infer which actions or fallbacks
are empirically controllable. J5 does not establish that a stronger contract is
normatively preferable. Exact J4/J7 values do not imply tractability.

## Proof and verification map

### MRM core

- [Recovered MRM core proofs](docs/mrm_core_proofs.md)
- [Minimal quotient and active discrimination](docs/minimal_quotient_active_discrimination.md)
- [Mechanism-ambiguity frontier](docs/mechanism_ambiguity_frontier.md)
- [Cost-aware discrimination](docs/cost_aware_active_discrimination.md)

### CREST synthesis — temporary host paths

- [J3 maximal universal common lift](docs/crest_maximal_common_lift_theorem_2026-08-17.md)
- [J6 controlled common-lift viability](docs/crest_controlled_common_lift_theorem_2026-08-18.md)
- [J4 universal repair characterization](docs/crest_minimum_common_lift_relaxation_theorem_2026-08-17.md)
- [J7 controlled repair characterization](docs/crest_minimum_controlled_lift_relaxation_theorem_2026-08-18.md)
- [J1 joint-state theorem](docs/crest_joint_state_theorem_2026-08-17.md)
- [J2 faithful-lift invariance](docs/crest_lift_invariance_theorem_2026-08-17.md)
- [J5 one-sided lift bounds](docs/crest_lax_lift_bounds_theorem_2026-08-18.md)
- [J4/J7 complexity boundary](docs/crest_repair_complexity_boundary_2026-08-18.md)
- [O1 repair/evidence obstruction](docs/crest_repair_evidence_noncommutation_2026-08-18.md)
- [Post-J7 novelty gate](docs/crest_next_proof_novelty_gate_2026-08-18.md)

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

MRM mathematics concerns finite declared mechanism families. CREST synthesis
mathematics is also finite and declared-model relative. Neither layer infers future
grammars, source-target relations, mechanism families, ambient synchronizations,
action controllability, fallback feasibility, evidence contracts, repair costs,
ecological targets, or empirical validity. J4/J7 are NP-hard global selection
problems despite their exact finite characterizations. Stochastic,
partial-observation, delayed-control, approximate, infinite, richer-repair, and
empirical common-lift inference remain outside the current proved scope.
