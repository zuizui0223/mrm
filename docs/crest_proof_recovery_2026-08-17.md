# CREST cross-repository proof recovery ledger — 2026-08-17

> **Status:** final proof-provenance audit after the 2026-08-17 recovery pass. This is not a new theorem. It separates quantified mathematical proof from finite replay and records every proof/claim correction found while auditing the current CCOC, MLTR, MRM, and CED publication surfaces.

## Proof-status scale

- **A — analytic + executable:** a quantified analytic proof is written and executable finite tests/replay check the implementation or witness.
- **B — analytic only:** a quantified proof is written; no dedicated executable replay is required or linked.
- **C — finite oracle/replay only:** implementation or exhaustive finite cases exist, but no paper-ready quantified proof has been recovered.
- **D — proof gap:** a theorem-level statement is present but a paper-ready proof has not been recovered.
- **N/A — architecture:** program-level synthesis/routing rule, not itself a theorem.

A green CI run shows that code, tests, or builds pass. It is **not** by itself the proof of a quantified theorem.

## Final audited theorem baselines

These are the theorem/proof baselines after the recovery corrections. The ledger-only synchronization that follows does not change theorem code.

- **CCOC:** `f360ed3ddb9a5a320e8132b03c51195ee14cb57a`
- **MLTR:** `b1417c7f516d7f3ed3798e6ba31cd1270f363d38`
- **MRM:** `0329c0b86fd72491d72d29f09df40ab341ae705f`
- **CED:** `440a1eda54ec948a6f2d88b3441af96e3388a611`

---

## 1. CCOC — future sufficiency

### CORE-1 — exact grammar-aware dynamic interface

**Status: A.**

For a declared finite deterministic controlled system and legal grammar, the all-legal-word trace relation is a right congruence. Its quotient is an exact deterministic interface, and every other exact interface fiber lies inside one trace-equivalence class. Hence the response quotient is coarsest.

Analytic source:

- `docs/dynamic_boundary_blankets.md`

Executable source:

- `causal_model/dynamic_boundary_blankets.py`
- `causal_model/grammar_aware_blankets.py`
- `causal_model/shared_grammar.py`
- corresponding tests.

Generic fixed-grammar minimization/right-congruence machinery is substrate, not the CCOC headline novelty claim.

### CORE-2 — extension–compression noncommutation

**Status: A. Headline theorem.**

For a jointly realizable comparison family with concrete legal future decoder words, any two distinct comparison states that differ in a decoded coordinate have distinct future traces. Therefore no exact open interface can merge them. In the product formulation,

\[
K_{\mathrm{open}}\ge \log_2|I|+\sum_j\log_2|E_j|.
\]

Supplied closed-context factorizations give

\[
K_{\mathrm{closed},j}\le \log_2|I|+\log_2|E_j|,
\]

and hence

\[
K_{\mathrm{open}}-\max_jK_{\mathrm{closed},j}
\ge
\sum_j\log_2|E_j|-\max_j\log_2|E_j|.
\]

Analytic source:

- `docs/extension_compression_noncommutation.md`
- `docs/portability_core_v1.md`.

The proof is an operational future-word injection. It does not assume that separate memory contributions automatically add.

### CORE-3 — bounded-local extremal sharpness

**Status: A.**

`docs/fixed_regular_extremal_theorem_2026-08-13.md` proves for every `m>=1` an explicit fixed-regular relay family with

\[
|P_C|=2,\qquad |P_O|=2^{m+1},\qquad K_O-K_C=m,
\]

while retaining one fixed four-symbol primitive alphabet, one newly legal primitive action, pairwise local communication, maximum degree three, a one-edge focal/exterior cut, and bounded local state/message alphabets.

Finite certificates check supplied values of `m`; the all-`m` construction/induction is the proof.

### CORE-4 / CORE-5 — positive portability and local split boundaries

**Status: A, supporting.**

Analytic sources:

- `docs/coherent_portable_macrolaw.md`
- `docs/conservative_macro_schema.md`.

These prove sufficient positive portability criteria and the direct local obstruction that a legal future word/action cannot give two distinct traces or quotient successors inside one exact macro fiber. They do not construct MLTR's unique source-relative repair.

### Retained CORE-2 strengthening: constrained codebooks

**Status: A, supporting strengthening.**

Analytic source:

- `docs/addressable_codebook_bound.md`.

Executable source:

- `causal_model/addressable_codebooks.py`
- `causal_model/codebook_families.py`
- `tests/test_addressable_codebooks.py`.

For an arbitrary finite jointly realizable codebook `C` with uniform legal coordinate decoders,

\[
K_{\mathrm{open}}(D_C)=\log_2|C|.
\]

If closed context `j` factors on the same comparison domain through `\pi_j(C)`, then

\[
K_{\mathrm{closed},j}(D_C)\le \log_2|\pi_j(C)|,
\]

so

\[
K_{\mathrm{open}}(D_C)-\max_jK_{\mathrm{closed},j}(D_C)
\ge
\log_2|C|-\max_j\log_2|\pi_j(C)|.
\]

This weakens Cartesian closure, not joint realizability or operational addressability. A codebook-domain factorization does **not** upper-bound the entire closed state space without an additional global closed-system contract.

The earlier document status still called this result a candidate even after analytic proof, finite certificates, and regression tests were in place. CCOC PR #221 corrected that status drift without promoting the result to a new headline theorem.

### Retained CORE-2 strengthening: approximate addressability

**Status: A, supporting companion.**

Analytic source:

- `docs/approximate_addressability.md`.

Executable source:

- `causal_model/approximate_addressability.py`
- `tests/test_approximate_addressability.py`.

For a uniform finite codebook, deterministic summary `Z`, and coordinate decoders with average errors `epsilon_j`, Fano plus conditional subadditivity gives

\[
\log_2|\operatorname{im}\phi|
\ge
\log_2|C|-\sum_j\left[h_2(\varepsilon_j)+\varepsilon_j\log_2(k_j-1)\right].
\]

For the binary full product and fixed `epsilon<1/2`, retained summary memory remains linear in the number of exterior coordinates. This is standard information-theoretic substrate used to show that the exact CCOC gap is not merely a zero-error artifact. It is not a new rate-distortion or approximate-state-abstraction theorem.

This approximation axis concerns **representation/future-response decoding error**, not CED's evidence/observation error.

### CCOC verdict

No current headline theorem or retained strengthening remains at C/D proof status. The current proof-control documents and executable tree agree.

---

## 2. MLTR — semantic coherence

### Operational portability and local obstruction

**Status: A.**

For the specified carried target partition, output, legal-action row, and successor carried labels being representative-independent inside each carried fiber is necessary and sufficient for exact portability. Failure yields a finite within-fiber witness.

Analytic sources:

- `docs/master_theorem_proof.md`
- `manuscript/supplement_proofs.tex`.

### Unique coarsest source-relative repair / transport defect

**Status: A. Headline theorem.**

Starting from the carried partition, finite refinement by output, legal row, and successor block stabilizes at an exact fixed point. Every exact target partition constrained to refine inherited labels refines every iterate and therefore the fixed point. Hence the fixed point is the unique coarsest **source-relative** exact repair.

Analytic sources:

- `docs/transport_defect.md`
- `docs/master_theorem_proof.md`
- `manuscript/supplement_proofs.tex`.

Transport defect is minimal inside this source-relative admissible class. It is not a claim of global minimality after inherited semantics are discarded.

### Path coherence and minimum history augmentation

**Status: A after claim correction.**

What is proved:

1. if all declared root-to-terminal paths carry the same terminal label map, inherited semantics, relative repair, and defect are route independent;
2. if carried maps differ, no single route-free **carried label map** can preserve all path-specific inherited assignments;
3. one immutable history mode per distinct carried map is necessary and sufficient to preserve all declared inherited meanings before history-aware relative refinement.

What is **not** proved: different carried maps do not necessarily force different final **unlabelled** repaired partitions. Two differently labelled inherited partitions can in principle refine to the same unlabelled final partition.

The earlier manuscript/master-proof wording used an unsupported iff statement about route-independent repair. MLTR PR #34 corrected the Abstract, Results theorem, Discussion, master proof, and Supplement to the actual semantic claim without changing the minimum-history theorem or executable results.

### MLTR verdict

No current headline MLTR result remains at C/D proof status. Draft PR #30 remains outside the canonical proof core under CREST hold because its generic monitoring/set-cover layer belongs to CED unless a genuinely new cross-contract theorem is proved.

---

## 3. MRM — mechanism robustness

### Results I–IX

**Status: A after proof recovery.**

Canonical analytic source:

- `docs/mrm_core_proofs.md`.

Recovered proofs cover:

1. candidate-independent deterministic law iff there is one response type;
2. exact typed and candidate-forgetting set-valued reports;
3. candidate-safe product lower bound under uniform response separation;
4. joint exterior–mechanism lower bound only under explicit joint realization/separation;
5. unique coarsest observation-preserving candidate-safe quotient;
6. finite-word trajectory characterization;
7. minimum worst-case active-discrimination depth over the declared finite configuration problem;
8. exact binary mechanism-memory and intervention frontier;
9. minimum worst-case positive-cost discrimination by Bellman recursion.

### Proof/implementation correction

The first recovered proof of Result V described a refinement signature that explicitly retained the old partition label. The actual `mrm/quotient.py` recurrence does not include that extra component:

\[
\sigma_{n+1}(x)=\left(o(x),([T_a(x)]_{P_n})_{a\in A}\right).
\]

Commit `d29bb9464f7f876531bad6c51dc8e844a9297213` corrected the proof rather than changing the implementation. Monotonicity is proved inductively: `P_1` refines the observation partition, and if `P_n` refines `P_{n-1}`, equality of the next signatures implies equality of the previous signatures. Thus `P_{n+1}` refines `P_n`; finite stabilization follows. A separate induction establishes coarseness among observation-preserving deterministic candidate-safe interfaces.

This correction matters: proof and implementation now establish the same recurrence.

### Admissible-class boundaries

- candidate-safe quotient minimality is among deterministic interfaces that preserve the current observed macrostate;
- active-discrimination optimality assumes exact current-macrostate observation, a fixed retained response type during the experiment, and the declared finite action grammar;
- positive-cost optimality assumes finite strictly positive action costs;
- the joint memory bound is not obtained by arithmetically adding separate CCOC and MRM bounds without the joint premise.

### Observation/posterior/VOI adapters

Bounded-support filtering, Bayes updating, and one-step EIG remain standard adapters around the mechanism-report target. They do not transfer CED's evidence-layer ownership to MRM and are not novelty claims for Bayesian inference or experimental design.

### MRM verdict

The main proof-recovery documentation gap is closed, and the subsequent proof/implementation mismatch was explicitly corrected. No current headline MRM result remains at C/D proof status.

---

## 4. CED — evidential licensing

### Result 1 — experiment-induced information and honest reporting

**Status: A.**

`manuscript/paper_b_supplement.tex` proves record factorization, the deterministic target-report iff criterion, the sharp compatible target set, and the stochastic-support analogue.

A singleton target report is licensed only when the declared compatible record/support class is target-constant.

### Result 2 — unique coarsest target-safe quotient

**Status: A, with the epistemic boundary now explicit.**

The Supplement proves finite monotone refinement, existence, unique coarseness, and preservation under every finite declared action word. The implementation is `ced/target_safe_quotient.py`, with an exhaustive finite all-partition oracle guarding the witness case.

Critical interpretation:

> the target-safe quotient is the **minimum additional refinement sufficient for deterministic target-safe state tracking**. It is not a claim that the current record has already identified the true refined block.

If one current compatible record class spans multiple target-safe blocks and the evidence contract has not resolved them, Result 1 still requires an ambiguity-retaining/set-valued report. Result 2 therefore gives a target-relative **resolution requirement**; Results 3–4 ask whether additional evidence can credibly earn the needed distinction.

CED PR #46 made this boundary explicit to prevent a self-contradictory reading in which an unresolved record partition is silently replaced by a finer “observed” state.

### Result 3 — failure architecture / worst-case guarantee ceiling

**Status: A under the declared probability contract.**

The Supplement proves the exact least-favourable joint-detection frontier under declared independent failure modes, availability lower bound, sensitivity lower bound, within-mode conditional independence, and zero false positives. The limiting quantity

\[
1-(1-a)^m
\]

is a ceiling on what the **lower-bound contract can guarantee**, not a universal ceiling on realized detection when true mode availability exceeds `a`.

The equal-effort one-mode versus independent-mode comparison is an explicit witness; it is not a universal theorem that every multi-mode allocation dominates every within-mode design.

### Result 4 — adaptive risk-limited target resolution

**Status: A for the declared finite-policy problem.**

The Supplement proves that a nonempty finite feasible policy family has at least one least-cost policy under the declared wrong-report, ambiguity, and other finite feasibility constraints. Exact finite enumeration evaluates the benchmark policies under one terminal reporting convention.

No global optimality claim is made over an undeclared infinite policy class.

### CED verdict

No Paper B headline result remains at C/D proof status. The important recovery correction was epistemic wording, not theorem mathematics: required target-safe resolution and currently licensed evidence are now kept distinct.

---

## 5. Shared mathematical substrate versus theorem ownership

The recovery audit confirms two intentional overlaps.

### Finite stable refinement

MLTR, MRM, and CED all use finite partition refinement, but over different objects and constraints:

- **MLTR:** target configurations constrained to refine an inherited source partition;
- **MRM:** observable-state × response-type worlds constrained to preserve the current observed macrostate;
- **CED:** latent worlds starting from an evidence-induced record partition, refined only to define the target/action-stable resolution requirement.

The generic refinement machinery is classical substrate and is not three independent novelty claims.

### Pair-separation / injection

CCOC and the conditional MRM joint bound both use operational separation/injection. The MRM bridge needs its own jointly realizable exterior × mechanism family; separate lower bounds do not add automatically.

---

## 6. CREST itself

**Status: N/A — metatheoretical architecture, not a proved fifth theorem.**

The program principle

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

is an organizing and routing principle supported by four separate theorem programs. The present work does **not** prove:

- that the four audits commute;
- that one unique globally minimal state simultaneously satisfies all four contracts;
- that CCOC memory, MLTR defect, MRM ambiguity cost, and CED risk quantities add;
- that passing three audits implies the fourth;
- that these four axes are philosophically exhaustive for every possible notion of ecological state.

A future CREST theorem must establish a genuinely coupled noncommutation, joint minimality statement, or impossibility rather than merely intersecting existing partitions.

---

## 7. Final proof-recovery verdict

The recovery was nontrivial and found real control-plane errors rather than merely relabelling green CI:

1. **CCOC:** stale theorem/proof navigation was synchronized with the cleaned CORE-1–CORE-5 tree; constrained-codebook status was promoted from stale “candidate” wording only after analytic proof/certificate/test review; approximate addressability was verified as a correct supporting Fano robustness result.
2. **MLTR:** an unsupported iff statement about route-independent final repair was narrowed to the actually proved statement about carried semantics and minimum history completion.
3. **MRM:** the missing Result I–IX analytic proof spine was recovered; then one proof argument was corrected because its stated refinement recurrence did not exactly match the implementation.
4. **CED:** the target-safe quotient was explicitly separated from what current evidence has already identified; finite-policy and failure-mode wording was narrowed to the precise proved contracts.

For the **current publication-facing theorem surfaces**, there is now no remaining C/D proof-status item known to this audit.

Therefore the safe current conclusion is

\[
\boxed{\text{four theorem programs are proof-recovered; CREST is their metatheoretical synthesis, not a proved fifth theorem}.}
\]

The remaining risks are different questions and must not be confused with proof closure:

- historical novelty / prior-art adjudication;
- ecological interpretation and selection of real-world contracts;
- empirical identification and validation;
- any future theorem coupling two or more CREST audits;
- philosophical claims of exhaustiveness or necessity beyond the four formal programs.
