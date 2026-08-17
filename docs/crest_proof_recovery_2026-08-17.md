# CREST cross-repository proof recovery ledger — 2026-08-17

> **Status:** proof-provenance audit, not a new theorem. The purpose is to distinguish mathematical proof from executable replay and to identify any theorem that is only implemented or narrated.

## Proof-status scale

- **A — analytic + executable:** a quantified analytic proof is written and an executable finite replay/test surface checks the implementation.
- **B — analytic only:** a quantified proof is written; no dedicated executable replay is required or currently linked.
- **C — finite oracle/replay only:** implementation or exhaustive finite cases exist, but no paper-ready quantified proof has been recovered.
- **D — statement only / proof gap:** a theorem-level statement is present but a paper-ready proof has not been recovered.
- **N/A — architecture:** program-level synthesis or routing rule, not itself a theorem with a proof obligation.

A green CI run is evidence that code and tests pass; it is **not** by itself a proof of a quantified theorem.

## Audited baselines

Proof locations were audited on the current post-CREST main branches:

- CCOC: `5298f63cb648c042c01c45790f9946a86d1dc65c`
- MLTR: `183672478f877db521cdf46c9fb1afdb0b4686ec`
- MRM: `9348eca4db3b8012077d8365c3ba5f6b943fed6a`
- CED: `6af3baef11fb363c07d225f8b7dc72cd5dc64620`

The proof-recovery branches add or synchronize proof documentation only unless explicitly stated otherwise.

---

## 1. CCOC — future sufficiency

### CORE-1 — exact grammar-aware dynamic interface

**Status: A.**

Analytic proof:

- `docs/dynamic_boundary_blankets.md`
  - finite horizon stabilization;
  - coarsest exact extension-stable interface;
  - dynamic boundary-blanket upper bound;
  - uniform blanket obstruction.

Executable surface:

- `causal_model/dynamic_boundary_blankets.py`
- `causal_model/grammar_aware_blankets.py`
- `causal_model/shared_grammar.py`
- `tests/test_dynamic_boundary_blankets.py`
- `tests/test_grammar_aware_blankets.py`
- `tests/test_shared_grammar.py`

Proof core: the all-word trace relation is a right congruence; every exact deterministic interface fiber lies inside one trace-equivalence class, so the trace quotient is coarsest.

### CORE-2 — extension–compression noncommutation lower bound

**Status: A.**

Analytic proof:

- `docs/extension_compression_noncommutation.md`
- `docs/portability_core_v1.md`
- the injection proof is also stated directly in `causal_model/extension_compression_noncommutation.py`.

Executable surface:

- `causal_model/extension_compression_noncommutation.py`
- `causal_model/operational_addressability.py`
- `tests/test_extension_compression.py`
- `tests/test_operational_addressability.py`

Proof core: any two distinct jointly realizable product states differ in a coordinate; the declared decoder word for that coordinate separates their future traces. Hence the exact open quotient is injective on the comparison product. Supplied closed factorizations give the closed upper bounds needed for the noncommutation inequality.

This matches the original proof design recovered from the RACH/Causal Interface Inflation work: the lower bound is a concrete future-word injection, not a partition-counting convention.

### CORE-3 — bounded-local extremal sharpness

**Status: A.**

Analytic all-`m` proof:

- `docs/fixed_regular_extremal_theorem_2026-08-13.md`, Steps 1–7.

Executable finite-`m` aggregation:

- `causal_model/extremal_open_composition.py`
- `causal_model/fixed_regular_grammar_relay.py`
- `causal_model/relay_tree_compilation.py`
- corresponding tests and paper-core replay.

Important proof/replay boundary: the executable certificate checks one supplied finite `m`; the induction/construction in the theorem document proves the quantified family for every `m>=1`.

### CORE-4 — conservative exact portability boundary

**Status: A, supporting theorem.**

Analytic proofs:

- `docs/coherent_portable_macrolaw.md`
- `docs/conservative_macro_schema.md`

Executable surface:

- `causal_model/coherent_portable_macrolaw.py`
- `causal_model/conservative_macro_schema.py`
- dedicated tests.

These are sufficient positive criteria, not a necessary-and-sufficient global classification and not an inherited-law repair theorem.

### CORE-5 — future-word/new-action fiber split

**Status: A, supporting local obstruction.**

Proof is direct contradiction with exactness: one macro fiber cannot admit one deterministic future trace/successor label if a legal word/action produces two different traces/successor labels inside it. The same documents and tests as CORE-4 carry the executable witness.

### CCOC proof-provenance correction required

The mathematical proof spine is recovered, but two older navigation documents on the audited main still enumerate physically retired/non-CCOC theorem families:

- `docs/claim_status_audit.md`
- `docs/theorem_spine.md`

They are not valid current proof ledgers after CREST cleanup. The CCOC proof-recovery branch rewrites them around CORE-1–CORE-5 and the current proof locations without changing theorem code.

---

## 2. MLTR — semantic coherence

### Operational portability and local obstruction

**Status: A.**

Paper-ready proofs:

- `manuscript/supplement_proofs.tex`, sections “Operational portability” and “Local obstruction”.

Program statements:

- `docs/theorem_program.md`.

The sufficiency proof constructs quotient output, legal rows, and successors from quantities constant inside carried fibers. The obstruction is the converse witness to failure of those factorization conditions for the specified carried partition.

### Unique coarsest source-relative repair / transport defect

**Status: A.**

Analytic proof:

- `docs/transport_defect.md`
- `manuscript/supplement_proofs.tex`.

Proof core: finite refinement from the carried partition terminates; the fixed point is exact; every exact partition refining the carried source labels refines every iteration and therefore refines the fixed point. This proves unique coarseness relative to inherited semantics.

Executable/reproducibility surface is covered by the transport-core tests and deterministic replay.

### Path-label coherence

**Status: A.**

Analytic proof:

- `docs/path_coherence.md`
- `manuscript/supplement_proofs.tex`.

Path equality gives the same carried terminal tuple; relative repair is a deterministic function of the terminal system plus that tuple, so repair and defect are route independent.

### Minimum history augmentation

**Status: A.**

Analytic proof:

- `docs/history_augmentation.md`
- `manuscript/supplement_proofs.tex`.

Lower bound: two distinct carried terminal maps cannot share one immutable history mode. Upper bound: one mode per distinct carried map represents all declared histories. Relative exact refinement then supplies the coarsest history-aware exact repair.

### MLTR boundary

The open draft PR #30 contains a monitoring-realization/set-cover layer. Under CREST that is not part of the recovered MLTR proof core. It remains on hold until generic monitoring/evidence content is split or demoted as a CED adapter. The proof ledger therefore treats the source-relative portability/repair/history hierarchy above as the canonical MLTR proof package.

---

## 3. MRM — mechanism robustness

### State before recovery

On the audited baseline, MRM had theorem statements, executable modules, finite tests, a neutral quotient proof, and an explicit frontier proof, but no single paper-ready proof spine covering the central Result I–IX chain. This was the main proof-recovery gap across the four repositories.

### Recovered MRM core

**Status after this branch: A for Results I–IX.**

New analytic proof spine:

- `docs/mrm_core_proofs.md`.

It now gives explicit proofs for:

1. universal deterministic law iff one response type;
2. exact typed and set-valued reporting;
3. candidate-safe product lower bound under uniform response separation;
4. conditional joint exterior–mechanism injection bound;
5. unique coarsest minimal candidate-safe quotient;
6. future-trajectory characterization of quotient classes;
7. minimum worst-case active-discrimination depth by finite configuration DP;
8. exact mechanism-memory and intervention frontier for the binary signature family;
9. minimum worst-case positive-cost discrimination by Bellman recursion and cycle removal.

Existing supporting proof documents remain:

- `docs/neutral_latent_world_quotient.md`
- `docs/minimal_quotient_active_discrimination.md`
- `docs/mechanism_ambiguity_frontier.md`
- `docs/cost_aware_active_discrimination.md`.

Executable surface:

- `mrm/laws.py`
- `mrm/quotient.py`
- `mrm/frontier.py`
- `mrm/joint.py`
- `mrm/costs.py`
- tests plus `scripts/verify_mrm_core.py`.

### Observation/posterior/VOI adapters

**Status: not separate CREST headline proof obligations.**

- bounded-support update is exact set filtering under a declared observation support;
- probabilistic update is Bayes' rule on the declared finite type family;
- one-step EIG is the standard posterior-entropy identity.

They remain executable adapters around the mechanism-report problem and are explicitly not novelty claims for Bayesian inference or experimental design.

---

## 4. CED — evidential licensing

### Result 1 — experiment-induced information and honest reporting

**Status: A.**

Paper-ready proof:

- `manuscript/paper_b_supplement.tex`, “Record factorization and deterministic report criterion”, sharp set-valued corollary, and stochastic-support extension.

Executable surface:

- `ced/experiment_quotient.py`
- `scripts/verify_experiment_quotient.py`
- theorem/story tests.

### Result 2 — unique coarsest target-safe quotient

**Status: A.**

Paper-ready proof:

- `manuscript/paper_b_supplement.tex`, monotone finite refinement lemma, unique coarsest target-safe quotient theorem, finite-word preservation corollary.

Executable surface:

- `ced/target_safe_quotient.py`
- exhaustive five-world all-partition oracle in `tests/test_target_safe_quotient.py`.

The exhaustive oracle is an implementation guard, not the proof. The analytic induction in the Supplement is the proof.

CREST boundary: this refinement lemma is shared finite substrate with MRM, but CED starts from an evidence-induced partition and asks what target-safe distinction the evidence architecture must support. MRM specializes latent worlds to observable-state × response-type pairs and asks a different mechanism-robustness question.

### Result 3 — failure architecture / guarantee ceiling

**Status: A.**

Paper-ready proof:

- `manuscript/paper_b_supplement.tex`, exact least-favourable joint-detection frontier by inclusion–exclusion, monotonic coupling lower-bound proof, and worst-case guarantee ceiling limit.

Executable surface:

- `ced/mode_detection.py`
- deterministic figure/replay tests.

The proof correctly distinguishes a worst-case **contract guarantee ceiling** from a universal realized-probability ceiling.

### Result 4 — finite risk-limited policy existence

**Status: A for the stated finite existence theorem.**

Paper-ready proof:

- `manuscript/paper_b_supplement.tex`: a nonempty finite feasible policy set has a cost minimizer.

The scientifically substantive report rule—unsupported records remain set-valued—is separate from this elementary finite minimization fact and is tested by the common benchmark/reporting contract.

---

## 5. CREST itself

**Status: N/A — architecture, not proved theorem.**

CREST's statement

\[
\text{usable ecological state}
\Rightarrow
\begin{cases}
\text{future-sufficient},\\
\text{semantically coherent},\\
\text{mechanism-robust or ambiguity-explicit},\\
\text{evidentially licensed}
\end{cases}
\]

is a metatheoretical research principle and routing architecture. It is **not** currently a theorem claiming that the four audits commute, that one globally minimal simultaneous quotient exists, or that four proof obligations can be combined mechanically.

A future CREST theorem would need a genuinely coupled statement—e.g. audit noncommutation, joint minimality, or impossibility—not merely the juxtaposition of the four recovered theorem packages.

---

## 6. Final proof-recovery verdict

After the MRM proof recovery and CCOC proof-ledger synchronization in this pass:

- **CCOC:** headline and supporting current CORE-1–5 claims have analytic proofs plus executable verification.
- **MLTR:** the source-relative portability/repair/history spine has explicit manuscript/document proofs plus transport replay.
- **MRM:** the previous main gap is closed by an explicit Result I–IX proof spine; executable tests remain replay rather than proof substitutes.
- **CED:** all four submission-facing Result packages have explicit Supplement proofs, with exhaustive or deterministic replay as implementation guards.
- **CREST:** complete as a proof-indexed metatheoretical architecture, but intentionally not promoted to a single proved joint theorem.

The remaining work after this ledger is not to invent more theorem families. It is to keep manuscript statements exactly aligned with these recovered proofs and to refuse any claim whose proof status falls below the level required by its wording.
