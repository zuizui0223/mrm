# CREST final proof-recovery ledger — 2026-08-17

> **Status:** program-level proof audit, not a new theorem. This ledger separates quantified analytic proof, executable replay, interpretation, and unresolved synthesis claims.

## 1. Final audited main baselines

After proof recovery and claim-boundary corrections:

- **CCOC:** `f360ed3ddb9a5a320e8132b03c51195ee14cb57a`
- **MLTR:** `b1417c7f516d7f3ed3798e6ba31cd1270f363d38`
- **MRM:** `99e2455a521d6182df8d9d1241ba833783f455db`
- **CED:** `440a1eda54ec948a6f2d88b3441af96e3388a611`

Proof status uses:

- **A — analytic + executable:** a quantified proof is written and finite tests/replay verify the implementation or witness;
- **B — analytic only:** a proof is written but no dedicated executable surface is required;
- **C — executable/oracle only:** finite checks exist without a recovered paper-ready quantified proof;
- **D — proof gap:** a theorem-level claim lacks a recovered proof;
- **N/A — architecture:** synthesis/routing statement, not itself a theorem.

A green CI run is not itself a proof of a quantified theorem.

---

## 2. CCOC — future sufficiency

### CORE-1: exact grammar-aware dynamic interface — **A**

Claim: for a declared finite deterministic controlled system and finite legal grammar, the legal-word trace quotient is the coarsest exact deterministic interface.

Analytic proof:

- `docs/dynamic_boundary_blankets.md` — right-congruence, coarseness, finite-horizon stabilization, blanket upper bound.

Executable surface:

- `causal_model/dynamic_boundary_blankets.py`
- `causal_model/grammar_aware_blankets.py`
- `causal_model/shared_grammar.py`
- dedicated tests.

Boundary: generic fixed-grammar minimization/right-congruence machinery is substrate, not the headline novelty claim.

### CORE-2: extension–compression noncommutation — **A**

Claim: a jointly realizable comparison family with concrete future decoder words forces an injective exact open interface; supplied closed-context factorizations give the cross-grammar gap.

Analytic proof:

- `docs/extension_compression_noncommutation.md`
- `docs/portability_core_v1.md`.

Proof core:

\[
K_{\mathrm{open}}\ge \log_2|I|+\sum_j\log_2|E_j|
\]

from coordinate-wise future separation, and

\[
K_{\mathrm{open}}-\max_jK_{\mathrm{closed},j}
\ge
\sum_j\log_2|E_j|-\max_j\log_2|E_j|
\]

when the declared closed factorizations provide the required upper bounds.

Boundary: the memory terms do not add without joint realizability and operational separation.

### CORE-3: bounded-local extremal sharpness — **A**

Analytic all-`m` proof:

- `docs/fixed_regular_extremal_theorem_2026-08-13.md`.

It establishes for every `m>=1` the fixed-regular relay family with

\[
|P_C|=2,\qquad |P_O|=2^{m+1},\qquad K_O-K_C=m,
\]

while keeping bounded degree, bounded local alphabets, pairwise local communication, and one newly legal primitive action in the grammar.

Finite certificates replay supplied `m`; they are not the quantified proof.

### CORE-4 / CORE-5: positive portability and local split boundaries — **A, supporting**

Analytic proofs:

- `docs/coherent_portable_macrolaw.md`
- `docs/conservative_macro_schema.md`.

These are sufficient positive conditions and local obstructions. They do not provide MLTR's source-relative unique repair.

### Retained CORE-2 strengthenings — **A, supporting**

**Constrained codebooks:** `docs/addressable_codebook_bound.md` proves the pair-separation lower bound for an arbitrary finite jointly realizable codebook. It weakens Cartesian closure but does not remove joint realizability or coordinate addressability. The full-state closed gap needs an additional full-state closed upper-bound contract; a codebook-only factorization is not enough.

**Approximate addressability:** `docs/approximate_addressability.md` proves the Fano robustness bound

\[
\log_2|\operatorname{im}\phi|
\ge
\log_2|C|-\sum_j\left[h_2(\varepsilon_j)+\varepsilon_j\log_2(k_j-1)\right].
\]

For the binary full-product family and fixed `epsilon<1/2`, the retained memory remains linear in the number of exterior coordinates. This is classical information-theoretic substrate used as a robustness companion, not a new rate-distortion or approximate-abstraction theorem.

### CCOC verdict

No current CCOC headline or retained strengthening is left at C/D proof status. Current proof-control documents now match the post-cleanup tree.

---

## 3. MLTR — semantic coherence

### Operational portability criterion — **A**

A carried target partition is exact iff output, legal-action row, and successor carried labels are representative-independent inside each carried fiber.

Proof sources:

- `docs/master_theorem_proof.md`
- `manuscript/supplement_proofs.tex`.

### Local obstruction + unique coarsest source-relative repair — **A**

Proof sources:

- `docs/transport_defect.md`
- `docs/master_theorem_proof.md`
- `manuscript/supplement_proofs.tex`.

Finite monotone refinement from the carried partition terminates at the unique coarsest exact target partition constrained to refine inherited labels. Therefore transport defect is minimal **within the source-relative admissible class**, not among all target abstractions after source semantics are discarded.

### Route coherence and history — **A after wording correction**

Recovered proof supports:

1. if all declared root-to-terminal paths carry the same terminal label map, inherited semantics, relative repair, and defect are route independent;
2. if carried maps differ, no single route-free **carried label map** can preserve all path-specific inherited assignments;
3. one immutable history mode per distinct carried map is necessary and sufficient to preserve all declared carried semantics before history-aware relative refinement.

The earlier wording “route-independent repair exists iff carried maps agree” was too strong because different carried maps can in principle refine to the same **unlabelled** final partition. That overclaim was removed from the master proof, supplement, abstract, results, and discussion in commit `b1417c7...`.

### MLTR verdict

No current headline MLTR theorem remains at C/D proof status. The only open manuscript branch with generic monitoring/set-cover material remains held outside the canonical MLTR proof core under CREST routing.

---

## 4. MRM — mechanism robustness

### Results I–IX — **A after proof recovery**

The recovered paper-ready proof spine is:

- `docs/mrm_core_proofs.md`.

It explicitly proves:

1. universal deterministic law iff one response type;
2. exact typed and set-valued candidate-forgetting reports;
3. candidate-safe product lower bound under uniform response separation;
4. joint exterior–mechanism injection only under joint operational separation;
5. unique coarsest observation-preserving candidate-safe quotient;
6. finite-word trajectory characterization of its classes;
7. exact minimum worst-case active-discrimination depth by finite configuration dynamic programming;
8. the binary mechanism-ambiguity memory/intervention frontier;
9. minimum worst-case positive-cost discrimination via Bellman recursion and removal of positive-cost configuration cycles.

Key admissible-class boundaries:

- the candidate-safe quotient is minimal among deterministic interfaces that **preserve the current observed macrostate**;
- active-discrimination optimality assumes exact observation of the current macrostate, a fixed retained response type through the experiment, and the declared finite action grammar;
- positive-cost optimality assumes every declared action cost is finite and strictly positive;
- the joint memory bound is not the sum of separate CCOC/MRM bounds unless the full joint family is realizable and separable.

### Observation/posterior/VOI modules — **supporting adapters, not headline theorem novelty**

- bounded-support update is exact set filtering under a declared support contract;
- probabilistic update is Bayes' rule on the declared finite response-type family;
- one-step EIG is the standard posterior-entropy identity.

They are not evidence-layer replacements for CED and are not novelty claims for Bayesian inference or experimental design.

### MRM verdict

The main proof-recovery gap found across CREST was MRM's missing consolidated analytic proof package. That gap is closed at `99e2455...`. No current MRM headline result remains at C/D proof status.

---

## 5. CED — evidential licensing

### Result 1: experiment-induced information and honest reporting — **A**

`manuscript/paper_b_supplement.tex` proves record factorization, the deterministic target-report iff criterion, the sharp compatible target set, and the stochastic support analogue.

Current evidence licenses a singleton target report only when the target is constant on the compatible record/support class.

### Result 2: unique coarsest target-safe quotient — **A, with explicit epistemic boundary**

The supplement proves the finite monotone refinement theorem, uniqueness/coarseness, and preservation under finite declared action words.

Crucial interpretation fixed in commit `440a1eda...`:

> the target-safe quotient is the **minimum refinement sufficient for deterministic target-safe tracking**, not a claim that the current record has already identified its refined block.

If a current compatible record class spans multiple target-safe blocks and the observation contract has not resolved them, Result 1 still requires ambiguity/set-valued reporting. Result 2 supplies the **resolution requirement** for subsequent design.

### Result 3: failure architecture — **A under the declared probability contract**

The least-favourable independent-mode proof in the supplement gives the exact worst-case joint-detection frontier under declared mode independence, availability lower bound, sensitivity lower bound, within-mode conditional independence, and zero false positives.

The uniform guarantee ceiling

\[
1-(1-a)^m
\]

is a ceiling on what the **lower-bound contract can guarantee**, not a universal ceiling on realized detection when true availability exceeds `a`.

The equal-effort independent-mode comparison is an explicit witness, not a theorem that every allocation across more modes universally dominates every within-mode design.

### Result 4: adaptive risk-limited target resolution — **A for the finite declared policy problem**

The supplement proves existence of a least-cost feasible policy in a nonempty **finite declared policy family**, under explicit wrong-report and ambiguity constraints. Exact finite enumeration evaluates the benchmark strategies under one shared terminal reporting rule.

No claim is made of global optimization over an undeclared infinite policy space.

### CED verdict

The epistemic self-consistency gap was wording, not mathematics: a required target-safe refinement had to be distinguished from a currently observed refinement. That boundary is now explicit. No current Paper B headline result remains at C/D proof status.

---

## 6. Shared substrate versus distinct theorem ownership

Two overlaps are intentional and no longer treated as duplicate novelty:

### Finite refinement substrate

MLTR repair, MRM candidate-safe quotient, and CED target-safe quotient all use finite stable refinement machinery. The common fixed-point/partition-refinement substrate is classical. Their scientific objects differ:

- MLTR: refinement constrained by an inherited source partition;
- MRM: refinement of observable-state × response-type worlds while preserving the current observed macrostate;
- CED: refinement of an evidence-induced record partition to identify the minimum target/action-stable resolution requirement.

### Injection/lower-bound substrate

CCOC's addressability lower bound and MRM's conditional joint exterior–mechanism bound both use pair separation/injection. MRM does not inherit CCOC additivity without a separately declared joint product/separation premise.

---

## 7. CREST itself — **N/A: metatheoretical architecture**

CREST currently has **no single joint theorem** claiming simultaneous adequacy. The program-level statement

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

is an organizing principle supported by four separate theorem programs, not a theorem obtained by intersecting their quotients.

Still unproved and therefore prohibited as present CREST claims:

- that the four audits commute;
- that there is a unique globally minimal joint state satisfying all four contracts;
- that CCOC memory, MLTR defect, MRM ambiguity cost, and CED risk quantities add;
- that passing three audits implies the fourth;
- that the four axes are philosophically exhaustive for all possible ecological state concepts.

A future CREST theorem must establish a genuinely new coupling, noncommutation, joint minimality, or impossibility rather than rename one companion theorem.

---

## 8. Final theory-recovery verdict

For the **current CREST story and current publication-facing theorem surfaces**, the recovery audit found no remaining logical contradiction after three control-plane corrections:

1. CCOC stale proof/status documents were synchronized with the cleaned current tree and the two retained strengthenings were explicitly classified as proved supporting results;
2. MLTR route/history wording was narrowed from an unsupported iff on final repairs to the actually proved statement about carried semantics plus minimum history completion;
3. CED target-safe refinement was made explicitly a required resolution, not an already observed state, and finite-policy optimality language was narrowed to the declared finite policy family.

MRM's missing consolidated analytic proof spine was also recovered.

Therefore the current safe status is:

\[
\boxed{\text{four theorem programs recovered; CREST remains a metatheoretical synthesis, not a proved fifth theorem}.}
\]

Remaining risks are **not proof-recovery gaps**:

- prior-art / historical novelty adjudication;
- ecological interpretation and choice of real-world contracts;
- empirical identification/validation;
- any future theorem coupling multiple CREST audits.
