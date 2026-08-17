# CREST philosophy-of-ecology paper architecture — 信・達・雅 protocol

> **Status:** manuscript architecture only. This document does not add a theorem, claim philosophical priority, or promote CREST into a proved joint theory. It is the bridge from the recovered mathematics to a philosophy-of-ecology paper.

## 1. Paper identity

### Working title/question

> **What Counts as the Same Ecological State?**

The title is deliberately broad, but the paper's actual object is narrower:

> **When may different ecological configurations safely be treated as the same coarse state representation for prediction and reporting?**

This distinction matters because philosophy of ecology already contains direct accounts of ecosystem identity, dynamical identity, resilience-linked identity, system boundaries, and model adequacy. CREST should complement those literatures, not redescribe them as absent.

### Working thesis

> The adequacy conditions of a usable coarse ecological state representation are contract-relative. A proposed state equivalence may be adequate for one scientific contract and fail another because of future operations, inherited semantics, retained mechanisms, or finite evidence.

A compact form is

\[
\boxed{
\text{usable coarse-state equivalence is contract-relative, not unconditional}.
}
\]

The older phrase

\[
\text{“ecological state identity is contract-relative”}
\]

may still be used as an interpretive slogan, but the paper must immediately clarify that it concerns **scientific state-representation adequacy**, not a claim that CREST supplies the first or exhaustive metaphysics of ecological-system identity.

### Intended field position

The paper is **philosophy of ecology grounded in mathematical ecology**:

- philosophy asks what sameness, representation, adequacy, and warranted assertion mean in ecological practice;
- mathematics supplies counterexamples, impossibility results, minimality results, and explicit scope boundaries;
- ecology supplies the practice of using functional groups, community states, resilience classes, occupancy categories, ecosystem-condition states, and management states.

The paper should be presented as a formal sharpening of existing ecological-identity and model-adequacy discussions.

Direct predecessors include work on dynamic ecosystem identity (Cumming & Collier; Collier & Cumming), multiple notions of ecological identity (Delettre), and explicit ecological model-adequacy protocols (Getz et al.). Broader conceptual neighbors include pragmatic representation, perspectivism, adequacy-for-purpose, model pluralism, robustness analysis, open-system ecology, historical contingency, and partial observability.

The paper's target is therefore not “four new quotient theories.” It is one representational question with four theorem-backed ways to fail.

---

## 2. 信・達・雅 as the writing protocol

The classical translation triad is used as an **editorial discipline**, not as a scientific novelty claim.

### 信 — fidelity

Every philosophically important sentence must have one label during drafting:

1. **FORMAL** — directly proved in CCOC, MLTR, MRM, or CED;
2. **INTERPRETIVE** — an ecological/philosophical reading of a proved result;
3. **OPEN** — a metatheoretical proposal or conjecture not established by the current mathematics.

Rules:

- never turn a sufficient condition into an iff claim;
- never treat finite replay/CI as proof of a quantified theorem;
- never treat a required state distinction as one already observed;
- never add complexity/defect/risk quantities from different axes without a joint theorem;
- never say the four CREST audits exhaust all legitimate ecological state criteria;
- never say the four audits commute or yield one globally minimal state unless separately proved;
- never claim that purpose-relative representation, ecological identity, ecosystem openness, or model adequacy began with CREST.

Canonical proof boundary: `docs/crest_proof_recovery_2026-08-17.md`.

Canonical literature boundary: `docs/crest_philosophy_literature_positioning_2026-08-17.md`.

### 達 — intelligibility without dilution

Each axis begins with an ecological question before notation.

- **Future sufficiency / CCOC:** Could a distinction irrelevant in every presently closed context become necessary after a future connection or intervention becomes legal?
- **Semantic coherence / MLTR:** Does an inherited ecological category retain its operational meaning after turnover, replacement, or rewiring?
- **Mechanism robustness / MRM:** Can one deterministic prediction be reported when several retained response mechanisms imply different intervention outcomes?
- **Evidential licensing / CED:** Has the evidence actually resolved the distinction that the requested prediction requires?

Each section follows:

```text
ordinary ecological practice
  -> proposed state equivalence
  -> hidden adequacy assumption
  -> formal failure mode
  -> theorem/counterexample
  -> philosophical consequence
  -> explicit non-claim
```

The main text should minimize repository names. Use the four audit names in the philosophical flow and introduce CCOC/MLTR/MRM/CED once as mathematical anchors.

### 雅 — conceptual economy

The paper has **one object, four audits, one recurring example**.

One object:

> a proposed coarse equivalence relation saying which ecological configurations count as the same scientific state.

Four audits:

1. future sufficiency;
2. semantic coherence;
3. mechanism robustness;
4. evidential licensing.

One recurring example:

> **pollination maintained**.

Avoid theorem catalogues, repository history, multiple umbrella metaphors, CI/code detail, and a fifth “CREST theorem.”

Preferred recurring sentence:

> A coarse state equivalence can be adequate under one contract and inadequate under another.

---

## 3. Relation to existing ecological identity and adequacy frameworks

This section is mandatory because the nearest prior art is direct.

### System identity is not the same problem as state-representation adequacy

Cumming & Collier and Collier & Cumming ask how an ecological/complex system retains identity through change and why ecosystem identity should be understood dynamically.

CREST asks a different question *inside a declared system/model*:

> When may two configurations share one coarse scientific state label?

So the manuscript must preserve:

```text
identity of the ecological system
    ≠
adequacy of a coarse state representation within that system
```

### Identity types are not CREST audits

Delettre distinguishes typological, numerical, global-state, and local-state ecological identity.

CREST does not propose four competing identity types. It asks whether a chosen state equivalence survives four scientific contracts.

The two decompositions can cross-classify each other.

### Model adequacy is not new with CREST

Getz et al. explicitly evaluate ecological model adequacy through state variables, control variables, data determinacy, sensitivity, validity, and coarse graining.

CREST should be presented as a **formal specialization of the state-representation part of adequacy**. Its distinctive move under test is to turn four different sources of inadequacy into four different mathematical problems and outputs.

---

## 4. Formal-to-philosophical claim ladder

### F1. Future sufficiency — CCOC

**FORMAL:** Exact compression under separately closed future grammars need not imply comparably small exact compression under a jointly open future grammar. Concrete future words can force an interface lower bound, with sharp bounded-local witnesses. Constrained-codebook and Fano results are supporting strengthenings.

**INTERPRETIVE:** Present functional equivalence need not be predictive equivalence under an enlarged future repertoire.

**UNSAFE:** Ecosystems cannot possess stable macro-laws.

### F2. Semantic coherence — MLTR

**FORMAL:** For a fixed inherited source law, the carried target partition can be tested for exactness. If it fails, finite refinement yields the unique coarsest exact source-relative repair. Equal carried terminal maps are sufficient for route-independent inherited semantics/repair; unequal maps rule out one route-free carried label map preserving all inherited assignments. One history mode per distinct carried map is necessary and sufficient when those inherited path-specific meanings must be retained.

**INTERPRETIVE:** An ecological category can keep its name while losing enough operational meaning to support the same intervention or prediction after structural change.

**UNSAFE:** Different histories always produce different final unlabeled state partitions.

### F3. Mechanism robustness — MRM

**FORMAL:** A universal deterministic law exists exactly when retained response types agree everywhere. Typed/set-valued reports are exact alternatives under disagreement. The candidate-safe quotient is the unique coarsest observation-preserving deterministic quotient on the declared typed system. Active/cost-aware discrimination is conditional on the declared finite response family, actions, and costs.

**INTERPRETIVE:** Presently identical configurations need not constitute one predictive state when retained mechanisms disagree about the requested future response.

**UNSAFE:** Full mechanism identity must always be retained.

### F4. Evidential licensing — CED

**FORMAL:** Deterministic target reporting is licensed exactly when the target is constant on the compatible evidence class. Otherwise the sharp report remains ambiguity-explicit. The target-safe quotient is the unique coarsest **required refinement** preserving records, targets, and declared successors; it is not automatically a state identified by the current evidence. Failure architecture constrains which nominal distinctions can be credited, and finite policy optimality is relative to the declared finite policy family.

**INTERPRETIVE:** A distinction may be real and prediction-relevant without yet being one that available evidence licenses us to report.

**UNSAFE:** The target-safe quotient is what the current experiment has already observed.

---

## 5. The central philosophical move

CREST should distinguish **ontological identity** from **representational adequacy**.

It does not need to decide whether ecological states are fundamentally real, conventional, processual, individual, or perspectival. The stronger and safer claim is:

> Whatever ontological account of ecological systems one adopts, a coarse scientific state representation has identity conditions determined by what it is required to preserve, predict, distinguish, and justify.

This permits a realist reading:

\[
\boxed{
\text{contract-relative}\neq\text{arbitrary}.
}
\]

Contracts are declared by scientific practice, but their consequences are not arbitrary:

- a future legal operation can refute a proposed merge;
- a replacement can invalidate inherited semantics;
- retained mechanisms can disagree on a successor;
- an evidence class can contain multiple target values.

Thus CREST does not infer “anything can be a state.” It says that scientific sameness claims have explicit adequacy obligations.

---

## 6. One recurring example — “pollination maintained”

Two ecological configurations currently receive the same coarse label: **pollination maintained**.

### Future-sufficiency audit

A newly connected pollinator channel or intervention exposes a response distinction hidden under the present closed grammar.

Question:

> Were these configurations the same predictive state for the enlarged future?

### Semantic-coherence audit

After pollinator turnover, the inherited functional class may need to split according to substitute-response capacity.

Question:

> Does the old category preserve enough of its inherited meaning to support the same management semantics?

### Mechanism-robustness audit

Several retained mechanisms agree on current pollination but disagree about competitor removal or habitat restoration.

Question:

> Is one deterministic prediction warranted before the mechanism ambiguity is resolved?

### Evidential-licensing audit

Camera, visitation, eDNA, or experimental records may leave target-relevant alternatives compatible.

Question:

> Even if the distinction matters, has the evidence earned the right to report it?

The point is not that “pollination maintained” is false. It is that the **adequacy of treating configurations as equivalent under that label** depends on the contract.

---

## 7. Proposed manuscript structure

### Title

Preferred working title:

> **What Counts as the Same Ecological State? A Contract-Relative Account of State-Representation Adequacy**

This keeps the broad philosophical hook while making the technical object explicit.

### Section 1 — From ecosystem identity to state-representation adequacy

Acknowledge direct predecessors immediately:

- ecosystem/system identity and dynamic continuity;
- plural kinds of ecological identity;
- model adequacy and coarse graining;
- perspectival/purpose-relative representation.

Then isolate the remaining question:

> Given a coarse ecological state equivalence, what must it survive to support prediction and reporting?

### Section 2 — Four independent adequacy audits

Introduce future sufficiency, semantic coherence, mechanism robustness, and evidential licensing conceptually.

### Section 3 — Formal anchors

Use one theorem/counterexample per axis, only enough mathematics to establish that the audits differ in quantifier order, starting object, minimization constraint, and honest failure output.

### Section 4 — Contract-relative does not mean arbitrary

Explain the realism-compatible position and why a declared contract can generate objective failure certificates.

### Section 5 — Consequences for ecological explanation, transfer, and measurement

Keep conceptual:

- state variables should be indexed to future/action context;
- transferring categories requires semantic audit;
- mechanism disagreement should not be hidden if it changes the target future;
- measurement should earn target-relevant distinctions rather than maximize latent resolution indiscriminately.

### Section 6 — Limits

State explicitly:

- the four audits are not proved exhaustive;
- no universal audit order is proved;
- no commutation theorem is proved;
- no globally minimal simultaneous CREST state is proved;
- CREST does not infer the contracts from ecological data;
- exact finite results are conceptual benchmarks, not automatic empirical laws.

End with:

> Ecological state equivalence should be treated as an explicit scientific commitment rather than an invisible modelling default.

---

## 8. Abstract skeleton under 信・達・雅

Do not finalize until the remaining exact-prior-art search is complete.

### 信

Ecology routinely compresses heterogeneous configurations into shared states used for prediction and management. Previous work has shown that ecosystem identity, model boundaries, and model adequacy are dynamic and purpose-sensitive. We ask a narrower question: when is a proposed coarse ecological state equivalence adequate for the scientific work assigned to it?

### 達

We distinguish four ways such equivalence can fail: future operations can expose erased distinctions; structural change can alter inherited state meaning; retained mechanisms can agree on the present yet disagree on future response; and finite evidence can fail to license a distinction required by the target prediction.

### 雅

These results motivate a contract-relative account of state-representation adequacy. A state equivalence is indexed to future, semantic, mechanism, and evidence contracts rather than treated as unconditionally sufficient. This is not unrestricted relativism: each contract supports explicit mathematical failure tests, while no claim is made that the four audits are exhaustive or jointly minimal.

---

## 9. Remaining literature gate

The broad literature gate has already ruled out novelty claims for:

- purpose/context relativity;
- ecological identity as a philosophical problem;
- four-way ecological identity taxonomies in general;
- ecological model adequacy;
- ecosystem openness and boundary choice;
- model pluralism/robustness;
- historical contingency;
- evidence underdetermination.

The remaining search is extremely narrow:

> **Has an existing framework already treated one coarse ecological state equivalence as separately constrained by future operations, inherited semantics, retained mechanism alternatives, and evidence/reportability?**

Only if that search remains negative after citation chaining should the paper use language such as:

> CREST may provide a new theorem-backed four-contract decomposition of coarse ecological state-representation adequacy.

---

## 10. Stop rule

Do not write the full paper until:

1. direct citation chains from Cumming & Collier, Delettre, Getz et al., Giere, Massimi, Bokulich & Parker, and robustness/model-pluralism work have been checked;
2. every central sentence can be tagged FORMAL / INTERPRETIVE / OPEN;
3. no sentence exceeds the final proof ledger;
4. one pollination example carries the whole argument;
5. there is no fifth theorem called “CREST theorem.”

The next task remains literature positioning, not theorem generation.
