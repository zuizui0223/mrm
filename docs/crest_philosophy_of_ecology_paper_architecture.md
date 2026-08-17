# CREST philosophy-of-ecology paper architecture — 信・達・雅 protocol

> **Status:** manuscript architecture only. This document does not add a theorem, does not claim philosophical novelty, and does not promote CREST from a program-level metatheoretical framework into a proved joint theory. It is the bridge from the recovered mathematics to a philosophy-of-ecology paper.

## 1. Paper identity

### Working question

> **What counts as the same ecological state?**

### Working thesis

> Ecological state identity is not intrinsic to a presently visible configuration. It is relative to the contracts under which the state is expected to support future intervention, preserve inherited meaning, remain robust to retained mechanism alternatives, and justify reports from finite evidence.

Compact form:

\[
\boxed{\text{ecological state identity is contract-relative, not intrinsic}.}
\]

This is a **metatheoretical thesis** supported by four formally distinct theorem programs. It is not itself a fifth theorem.

### Intended field position

The paper should be written as **philosophy of ecology grounded in mathematical ecology**:

- philosophy supplies the question of state identity, sameness, representation, and warranted assertion;
- mathematics supplies counterexamples, impossibility results, minimality results, and explicit scope boundaries;
- ecology supplies the domain in which state variables, functional classes, monitoring categories, and management states are actually used.

The paper should not be framed as “four new quotient theories.” The philosophical object is the relation between ecological state identity and the contracts that make a state representation usable.

---

## 2. 信・達・雅 as the writing protocol

The classical translation triad is used here as an **editorial discipline**, not as a scientific analogy claimed to be novel.

### 信 — fidelity to the formal results

Every philosophical statement must be traceable to one of three statuses:

1. **FORMAL:** directly proved in CCOC, MLTR, MRM, or CED;
2. **INTERPRETIVE:** a philosophical/ecological reading of a proved result;
3. **OPEN:** a metatheoretical proposal or philosophical conjecture not proved by the current mathematics.

Rules:

- never turn a sufficient condition into an iff statement;
- never treat a finite replay as proof of a quantified theorem;
- never treat a required state distinction as one already observed;
- never add CCOC, MLTR, MRM, or CED complexity quantities without a joint theorem;
- never say that the four CREST audits are exhaustive of all possible notions of ecological state adequacy;
- never say that the four audits commute or yield one globally minimal joint state unless that is separately proved.

The canonical proof boundary is `docs/crest_proof_recovery_2026-08-17.md`.

### 達 — intelligibility without mathematical dilution

Each formal axis should be introduced through one ecological question before notation.

- **CCOC:** “Could a distinction that is irrelevant in every presently closed context become necessary after a future connection becomes legal?”
- **MLTR:** “Does an ecological category retain the same operational meaning after turnover or rewiring?”
- **MRM:** “Can one deterministic prediction be reported when several retained mechanisms imply different intervention responses?”
- **CED:** “Has the evidence actually resolved the distinction that the prediction requires?”

Every section should follow the same explanatory order:

```text
ordinary ecological practice
  -> hidden assumption
  -> formal failure mode
  -> theorem/counterexample
  -> philosophical consequence
  -> explicit non-claim
```

The paper should minimize repository names in the main philosophical flow. CCOC/MLTR/MRM/CED can appear once as formal anchors and then be referred to by the four audits.

### 雅 — conceptual economy and elegance

The paper should have **one thesis, four failure modes, one recurring example**.

Avoid:

- theorem catalogues;
- multiple competing umbrella metaphors;
- historical repository narrative;
- code/CI details in the main text;
- claiming that every ecological modelling problem is a CREST problem;
- excessive terminology for variants already handled by the same formal axis.

Preferred recurring sentence structure:

> A state can be adequate relative to one contract and inadequate relative to another.

Preferred recurring ecological example: **pollination maintained** under turnover, intervention, mechanism ambiguity, and finite observation. The same example should carry all four audits rather than introducing four unrelated case studies.

---

## 3. Formal-to-philosophical claim ladder

The paper must keep these levels visibly separate.

### Level F — formal results already recovered

#### F1. Future sufficiency — CCOC

Formal result:

- exact state compression under separately closed future grammars need not imply comparably small exact compression under a jointly open future grammar;
- concrete future words can force an open-interface lower bound;
- the gap can be sharp under bounded-local, fixed-regular constructions;
- constrained-codebook and Fano-based approximate results are supporting strengthenings, not additional philosophical axes.

Safe philosophical reading:

> Present functional equivalence does not guarantee causal equivalence under an enlarged future repertoire.

Unsafe reading:

> No ecosystem has a stable macro-law.

#### F2. Semantic coherence — MLTR

Formal result:

- a carried source macro-law is portable exactly when the specified carried partition remains operationally exact;
- if it fails, finite refinement yields the unique coarsest exact target repair constrained to preserve inherited labels;
- equal carried terminal label maps are sufficient for route-independent inherited semantics and relative repair;
- unequal carried maps rule out one route-free carried label map preserving all declared histories;
- one history mode per distinct carried map is necessary and sufficient when path-specific inherited meanings themselves must be preserved.

Safe philosophical reading:

> Ecological categories can be historically and structurally conditional even when their names remain unchanged.

Unsafe reading:

> Different histories always imply different final ecological state partitions.

#### F3. Mechanism robustness — MRM

Formal result:

- a universal deterministic macro-law exists exactly when retained response types agree everywhere;
- typed and set-valued reports are exact fallbacks under disagreement;
- the minimal candidate-safe quotient is the unique coarsest observation-preserving deterministic quotient on the declared typed system;
- active discrimination and cost-aware discrimination are finite conditional design problems after the response-type family and costs are declared.

Safe philosophical reading:

> A presently identical ecological configuration need not determine one predictive state when retained mechanisms disagree about future response.

Unsafe reading:

> Mechanism identity must always be retained in full.

#### F4. Evidential licensing — CED

Formal result:

- deterministic target reporting is licensed exactly when the target is constant on the compatible evidence class;
- otherwise the sharp report remains ambiguity-retaining/set-valued;
- the target-safe quotient is the unique coarsest **required refinement** preserving current records, target values, and declared action successors;
- it is not automatically a state already identified by the current evidence;
- failure architecture constrains which nominal distinctions can be credited;
- finite risk-limited experiment choice is optimized only inside the declared finite policy family.

Safe philosophical reading:

> A distinction may be real and prediction-relevant without yet being a distinction that available evidence licenses us to report.

Unsafe reading:

> The target-safe quotient is what the current experiment has already observed.

---

## 4. The central philosophical move

The paper should distinguish **state existence** from **state adequacy**.

CREST does not need to claim that ecological states are unreal or merely conventional. The stronger and more defensible position is:

> Whatever ontological status one assigns to underlying ecological configurations, the identity conditions of a *usable ecological state representation* depend on what that representation is required to preserve, predict, distinguish, and justify.

This avoids an unnecessary choice between naive realism and constructivism.

A state representation is therefore not “relative” in the sense that anything goes. It is constrained by explicit contracts and can fail them mathematically.

This yields a useful philosophical asymmetry:

\[
\boxed{\text{contract-relative} \neq \text{arbitrary}.}
\]

The contracts expose objective failure conditions:

- a future legal action can separate a proposed merge;
- a structural replacement can invalidate inherited semantics;
- retained mechanisms can disagree on successors;
- an evidence class can contain multiple target values.

Thus CREST is compatible with realism about ecological processes while rejecting the idea that one intrinsic coarse-grained state identity is automatically adequate for every scientific purpose.

---

## 5. One recurring example: “pollination maintained”

Use one ecological label throughout the paper.

### Present description

Two configurations are both labelled **pollination maintained**.

### Future-sufficiency failure

A future pollinator connection or intervention exposes a response distinction hidden under the presently closed grammar.

Question:

> Were the two configurations really the same predictive state for the enlarged future?

### Semantic-coherence failure

After pollinator turnover, an inherited class may need to split according to substitute-response capacity.

Question:

> Does the old label still mean enough to support the same intervention semantics?

### Mechanism-robustness failure

Several retained mechanisms agree on current pollination but disagree about response to competitor removal or habitat restoration.

Question:

> Is one deterministic forecast justified before the mechanism ambiguity is resolved?

### Evidential-licensing failure

Camera, visitation, eDNA, or experimental records may leave both target-relevant worlds compatible.

Question:

> Even if the distinction matters, has the evidence earned the right to report it?

The philosophical point is not that “pollination maintained” is false. It is that its adequacy depends on the contract under which it is being used.

---

## 6. Proposed manuscript structure

### Title candidates

Use as working titles only until the literature gate is complete.

1. **What Counts as the Same Ecological State? A Contract-Relative Account of Ecological Representation**
2. **Ecological States Are Contract-Relative: Future, Meaning, Mechanism, and Evidence**
3. **The Same State for What? A Formal Philosophy of Ecological State Identity**

Preferred current title: **What Counts as the Same Ecological State?** because it states the philosophical problem without overselling CREST as a finished universal theory.

### Section 1 — The hidden identity assumption in ecological state variables

Start from ordinary practice:

- functional groups;
- community states;
- resilience classes;
- occupancy states;
- management categories.

Problem:

> These variables implicitly say which configurations count as “the same” for a scientific purpose.

Do not begin with quotient notation.

### Section 2 — Four ways ecological sameness can fail

Introduce the four audits conceptually:

1. future sufficiency;
2. semantic coherence;
3. mechanism robustness;
4. evidential licensing.

End with the CREST thesis.

### Section 3 — Formal anchors: why the four failures are not merely verbal distinctions

Give one theorem/counterexample per axis, at minimum mathematical detail sufficient to show that the four failures have different quantifier structures.

Do **not** reproduce every theorem.

The main formal point is:

> the four failures are supported by different mathematical objects and different minimization constraints, not by relabeling one partition theorem.

### Section 4 — Contract-relative does not mean arbitrary

Address the likely philosophical objection.

Explain that contracts are declared but consequences are constrained:

- wrong compression can be refuted;
- inherited meaning can fail exactness;
- mechanism disagreement can make deterministic reports unsupported;
- evidence can fail to license a target distinction.

This section is the bridge from mathematical ecology to philosophy of science.

### Section 5 — Implications for ecological explanation and measurement

Keep this conceptual, not a methods catalogue.

Consequences:

- “same state” should be indexed to future/action context;
- transferring ecological categories requires semantic audit;
- mechanism uncertainty should not be hidden by one state label when it changes the requested future;
- measurement design should be target-relative rather than oriented toward resolving every latent detail.

### Section 6 — Limits and open problems

State explicitly:

- the four audits are not proved exhaustive;
- no universal audit order is proved;
- no commutation theorem is proved;
- no globally minimal simultaneous CREST state is currently proved;
- CREST does not infer the contracts from ecological data;
- exact finite theorems are conceptual benchmarks, not automatic empirical laws.

End not with “CREST solves ecological state representation,” but with:

> Ecological state identity should be treated as an explicit scientific commitment rather than an invisible modelling default.

---

## 7. Abstract skeleton under 信・達・雅

Do not finalize until the literature audit is complete.

### 信 — sentence 1–2: state the actual problem

Ecology routinely compresses heterogeneous configurations into shared states used for prediction, comparison, and management. Such compression silently assumes criteria for when two ecological configurations count as the same state.

### 達 — sentence 3–5: state the four failures plainly

We distinguish four ways that this assumption can fail: future operations can expose previously irrelevant distinctions; structural change can alter the meaning of inherited state categories; retained mechanisms can agree on the present but disagree on future response; and finite evidence can fail to resolve distinctions required by the prediction.

### 雅 — sentence 6–8: give one principle

These results motivate a contract-relative account of ecological state identity. On this view, state sameness is indexed to declared future, semantic, mechanism, and evidence contracts rather than treated as an intrinsic property of a present configuration. The account is not relativism without constraint: each contract supports explicit mathematical failure tests, while no claim is made that the four audits are exhaustive or jointly minimal.

---

## 8. Literature gates before drafting prose

The philosophy manuscript must not claim novelty until it is compared against at least these neighboring traditions:

1. philosophy of ecology on ecological individuality, communities, and state variables;
2. scientific perspectivism / perspectival realism;
3. model pluralism and pragmatic/functional accounts of representation;
4. interventionist and causal accounts of variables;
5. state abstraction, lumpability, bisimulation, and sufficient-state concepts;
6. observability, identifiability, partial identification, and evidence-relative reporting;
7. open-systems and boundary-choice discussions in ecology and philosophy of science;
8. historical contingency / path dependence in ecological explanation;
9. mechanism pluralism and robust prediction under model uncertainty.

For every literature family, record:

- what problem it already owns;
- whether it already says “state identity is purpose/context relative”;
- whether it supplies a formal impossibility/minimality result comparable to one CREST axis;
- what CREST adds, if anything, beyond recombining familiar philosophical positions.

Novelty may ultimately lie in the **four-contract integration plus theorem-backed failure architecture**, not in the generic idea that models or state variables are purpose-relative.

---

## 9. Stop rules

Do not write the full philosophy manuscript until all of the following are true:

1. the literature gate is complete enough to avoid rediscovering perspectivism/pluralism under new vocabulary;
2. every main philosophical sentence can be labelled FORMAL / INTERPRETIVE / OPEN;
3. no sentence attributes a stronger theorem to a repository than the final proof ledger supports;
4. one recurring ecological example carries the whole paper;
5. the manuscript contains no fifth theorem called “CREST theorem.”

If the literature audit shows that “contract-relative state identity” is already an established philosophical thesis, the paper should pivot from priority to **formal unification and diagnostic articulation** rather than defend a novelty claim for the thesis itself.

---

## 10. Current next task

The next research task is **literature positioning, not theorem generation**.

The output of that task should be a claim matrix with three columns:

```text
existing philosophical claim
CREST formal contribution
safe manuscript claim
```

Only after that matrix is stable should the full prose manuscript be drafted under the 信・達・雅 protocol.
