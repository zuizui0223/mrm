# CREST cross-repository proof recovery ledger — 2026-08-17

> **Status:** final proof-provenance audit after the 2026-08-17 recovery pass. This is not a new theorem. It separates quantified mathematical proof from finite replay, records the two claim/proof corrections found during recovery, and indexes the current proof surfaces of CCOC, MLTR, MRM, and CED.

## Proof-status scale

- **A — analytic + executable:** a quantified analytic proof is written and executable finite tests/replay check the implementation.
- **B — analytic only:** a quantified proof is written; no dedicated executable replay is required or currently linked.
- **C — finite oracle/replay only:** implementation or exhaustive finite cases exist, but no paper-ready quantified proof has been recovered.
- **D — statement only / proof gap:** a theorem-level statement is present but a paper-ready proof has not been recovered.
- **N/A — architecture:** program-level synthesis or routing rule, not itself a theorem with a proof obligation.

A green CI run shows that code/tests/builds pass. It is **not** by itself the proof of a quantified theorem.

## Post-recovery main baselines

- CCOC: `78891c557fe1a0bffea1489f14f4319cdaed8ab7`
- MLTR: `b1417c7f516d7f3ed3798e6ba31cd1270f363d38`
- MRM: `d29bb9464f7f876531bad6c51dc8e844a9297213`
- CED: `6af3baef11fb363c07d225f8b7dc72cd5dc64620`

CED required no proof-recovery code/document change because its current Paper B Supplement already contained the relevant analytic proofs.

---

## 1. CCOC — future sufficiency

### CORE-1 — exact grammar-aware dynamic interface

**Status: A.**

Analytic source:

- `docs/dynamic_boundary_blankets.md`
  - finite-horizon stabilization;
  - coarsest exact extension-stable interface;
  - finite dynamic-boundary upper bound;
  - uniform blanket obstruction.

Executable source:

- `causal_model/dynamic_boundary_blankets.py`
- `causal_model/grammar_aware_blankets.py`
- `causal_model/shared_grammar.py`
- corresponding tests.

Proof core: the all-legal-word trace relation is an exact right congruence; every exact deterministic interface fiber is contained in one trace-equivalence class, so the response quotient is coarsest.

### CORE-2 — extension–compression noncommutation lower bound

**Status: A. Headline theorem.**

Analytic source:

- `docs/extension_compression_noncommutation.md`
- `docs/portability_core_v1.md`
- the injection argument is mirrored in `causal_model/extension_compression_noncommutation.py`.

Proof core: any two distinct jointly realizable comparison states differ in some declared coordinate; a concrete legal future word decodes that coordinate and therefore separates their traces. The open exact interface is injective on the comparison family. Closed-context factorizations supply the closed upper bounds, giving the cross-grammar gap.

The lower bound is therefore a future-word injection argument, not a convention that partition sizes or memory contributions automatically add.

### CORE-3 — bounded-local extremal sharpness

**Status: A.**

Analytic all-`m` source:

- `docs/fixed_regular_extremal_theorem_2026-08-13.md`, Steps 1–7.

Executable finite-`m` source:

- `causal_model/fixed_regular_grammar_relay.py`
- `causal_model/extremal_open_composition.py`
- `causal_model/relay_tree_compilation.py`
- paper-core tests/replay.

The finite certificate for one supplied `m` is not the all-`m` proof; the explicit construction and induction in the theorem document are.

### CORE-4 — conservative exact portability boundary

**Status: A, supporting sufficient criterion.**

Analytic sources:

- `docs/coherent_portable_macrolaw.md`
- `docs/conservative_macro_schema.md`.

These prove sufficient positive portability conditions. They do not claim a necessary-and-sufficient global classification and do not solve MLTR's inherited-law repair problem.

### CORE-5 — future-word/new-action fiber split

**Status: A, supporting local obstruction.**

Proof: direct contradiction with deterministic exactness when one proposed macro fiber contains states producing different traces or quotient successors under the same legal future.

### Recovery action completed

Before this pass, `docs/claim_status_audit.md` and `docs/theorem_spine.md` still mixed retired theorem families with the current CCOC surface. PR #220 replaced them with current CORE-1–CORE-5 proof provenance and explicit proof/replay boundaries. No theorem code or registry identity changed.

---

## 2. MLTR — semantic coherence

### Operational portability and local obstruction

**Status: A.**

Analytic sources:

- `docs/master_theorem_proof.md`
- `manuscript/supplement_proofs.tex`
- statements in `docs/theorem_program.md`.

Uniformity of output, legal row, and successor carried label is necessary and sufficient for the specified carried target partition to be exact. Failure has a finite within-fiber witness.

### Unique coarsest source-relative repair / transport defect

**Status: A. Headline theorem.**

Analytic sources:

- `docs/transport_defect.md`
- `docs/master_theorem_proof.md`
- `manuscript/supplement_proofs.tex`.

Proof core: start from the carried partition and split by output, legal row, and successor block. Finite refinement stabilizes; the fixed point is exact; every exact target partition refining the inherited labels refines every iterate and hence the fixed point. This gives the unique coarsest source-relative repair and minimal state/bit defect.

### Path-label coherence

**Status: A for the proved sufficient semantic statement.**

If every root-to-terminal path induces the same carried terminal label map, one route-independent inherited label assignment exists; relative repair and defect are then route independent.

### Minimum history augmentation

**Status: A.**

When carried terminal maps differ, no single route-free carried label map can preserve all path-specific inherited assignments. One immutable history mode per distinct carried map is necessary and sufficient to preserve those inherited semantics before relative exact refinement.

### Claim correction found during recovery

The previous master proof and manuscript used a stronger phrase: route-independent carried/repaired partitions existed **iff** all carried maps were equal. The written proof did not establish the reverse statement for the final **unlabeled repaired partition**: different inherited label maps can in principle refine to the same unlabeled partition.

PR #34 therefore narrowed the claim to what is proved:

- equal carried maps are sufficient for route-independent inherited semantics, repair, and defect;
- unequal carried maps rule out one route-free inherited label map preserving all declared histories;
- the minimum-history theorem remains intact when path-specific inherited meanings must be preserved.

The Abstract, main History Coherence theorem, Discussion, master proof, and Supplement now use the same claim strength.

### MLTR boundary

Draft PR #30 remains on CREST hold. Its monitoring/set-cover layer is not part of the recovered MLTR proof core unless converted to a genuine cross-contract theorem; generic monitoring/evidence machinery belongs to CED.

---

## 3. MRM — mechanism robustness

### Pre-recovery gap

MRM already had theorem statements, executable modules, finite tests, a neutral quotient proof, and frontier notes, but no single paper-ready analytic proof spine covering the core Result I–IX chain.

### Recovered core

**Status: A for Results I–IX.**

Canonical analytic source:

- `docs/mrm_core_proofs.md`.

It now contains explicit proofs for:

1. universal deterministic law iff one response type;
2. exact typed and set-valued reporting;
3. candidate-safe product lower bound under uniform response separation;
4. conditional joint exterior–mechanism injection bound;
5. unique coarsest minimal candidate-safe quotient;
6. future-trajectory characterization of quotient classes;
7. minimum worst-case active-discrimination depth by finite configuration dynamic programming;
8. exact mechanism-memory and binary-probe intervention frontier;
9. minimum worst-case positive-cost discrimination by Bellman recursion and cycle removal.

Supporting sources:

- `docs/neutral_latent_world_quotient.md`
- `docs/minimal_quotient_active_discrimination.md`
- `docs/mechanism_ambiguity_frontier.md`
- `docs/cost_aware_active_discrimination.md`.

Executable sources include `mrm/laws.py`, `mrm/quotient.py`, `mrm/frontier.py`, `mrm/joint.py`, `mrm/costs.py`, tests, and `scripts/verify_mrm_core.py`.

### Proof/implementation correction found during recovery

The first recovered Result V proof said monotonicity held because the previous block identifier was explicitly retained in the next refinement signature. `mrm/quotient.py` does not do that. Its recurrence uses only

\[
\sigma_{n+1}(x)=\left(o(x),([T_a(x)]_{P_n})_{a\in A}\right).
\]

PR #16 corrected the proof rather than the implementation. Monotonicity is proved inductively:

- `P_1` refines the observation partition `P_0`;
- if `P_n` refines `P_{n-1}`, equality of `P_{n+1}` signatures implies equal successor `P_n` blocks, hence equal successor `P_{n-1}` blocks, hence equal `P_n` signatures;
- therefore `P_{n+1}` refines `P_n` for every `n` and finite stabilization follows.

The separate induction showing that every observation-preserving deterministic quotient refines every `P_n` then establishes unique coarseness. The theorem did not change; the proof is now aligned with the actual implementation.

### Observation/posterior/VOI adapters

**Status: not separate CREST headline proof obligations.**

- bounded-support update is exact filtering under a declared support relation;
- probabilistic update is Bayes' rule on the declared finite type family;
- one-step EIG is the standard posterior-entropy identity.

They remain adapters around the mechanism-report problem, not novelty claims for Bayesian inference or experimental design.

---

## 4. CED — evidential licensing

### Result 1 — experiment-induced information and honest reporting

**Status: A.**

Paper-ready source:

- `manuscript/paper_b_supplement.tex`, record factorization, deterministic report criterion, sharp set-valued fallback, and stochastic-support extension.

Executable source:

- `ced/experiment_quotient.py`
- `scripts/verify_experiment_quotient.py`
- theorem/story tests.

### Result 2 — unique coarsest target-safe quotient

**Status: A.**

Paper-ready source:

- `manuscript/paper_b_supplement.tex`, finite monotone refinement, unique coarsest target-safe quotient, and finite-action-word preservation.

Executable source:

- `ced/target_safe_quotient.py`
- exhaustive all-partition finite oracle in `tests/test_target_safe_quotient.py`.

The exhaustive oracle checks implementation/minimality on the witness; the analytic induction in the Supplement is the quantified proof.

CREST boundary: CED begins from an evidence-induced partition. MRM specializes worlds to observable-state × response-type pairs. Shared finite refinement is common substrate, not duplicate novelty.

### Result 3 — failure architecture / guarantee ceiling

**Status: A.**

Paper-ready source:

- `manuscript/paper_b_supplement.tex`, exact least-favourable frontier, monotonic coupling, and worst-case guarantee-ceiling limit.

Executable source:

- `ced/mode_detection.py`
- deterministic replay/figure tests.

The proved object is a worst-case **contract guarantee ceiling**, not a universal upper bound on realized detection probability.

### Result 4 — finite risk-limited policy existence

**Status: A for the stated finite existence theorem.**

Paper-ready source:

- `manuscript/paper_b_supplement.tex`: a nonempty finite feasible policy set has a cost minimizer.

The scientifically substantive reporting rule—unsupported records remain ambiguity-explicit/set-valued—is separate from this elementary finite minimization fact.

---

## 5. CREST itself

**Status: N/A — metatheoretical architecture, not a proved joint theorem.**

CREST's program principle

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

is a research architecture and routing rule. The current program does **not** prove that the four audits commute, that a unique globally minimal simultaneous state exists, or that their memory/defect/risk quantities combine mechanically.

A future CREST theorem must expose a genuinely coupled noncommutation, joint minimality statement, or impossibility. Merely composing the four recovered theorem packages is not a new proof.

---

## 6. Final proof-recovery verdict

The 2026-08-17 recovery pass closes the proof-provenance gaps of the current four-repository program:

- **CCOC:** CORE-1–CORE-5 now have a current analytic proof map aligned with the executable registry; stale theorem-sprawl proof navigation was removed.
- **MLTR:** source-relative portability/repair/history is explicitly proved; one route-coherence overclaim was found and narrowed across proof docs and manuscript without changing the minimum-history result.
- **MRM:** the previous documentation gap is closed by one Result I–IX analytic proof spine; a monotonicity justification was subsequently corrected to match the actual refinement implementation.
- **CED:** all four submission-facing result packages were already backed by explicit Supplement proofs, with finite replay/oracles serving as implementation guards.
- **CREST:** complete as a proof-indexed metatheoretical architecture, intentionally not promoted to a single joint theorem.

The next proof-control rule is simple: manuscript wording may not outrun the analytic proof indexed here, and CI/replay may not be cited as a substitute for a quantified argument.
