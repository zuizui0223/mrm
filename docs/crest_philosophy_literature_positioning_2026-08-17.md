# CREST philosophy-of-ecology literature positioning — 2026-08-17

> **Status:** literature-positioning gate for a future philosophy-of-ecology manuscript. This document is not a novelty claim and does not alter the formal CREST proof ledger.

## 1. Immediate conclusion

Seven broad novelty claims are now excluded.

### Not novel 1 — purpose/context relativity

Scientific representation is already widely treated as purpose-, perspective-, context-, or boundary-relative in pragmatic representation, perspectivism, model pluralism, adequacy-for-purpose, and philosophy of modelling.

### Not novel 2 — ecological identity as a philosophical problem

Cumming & Collier, Collier & Cumming, and Delettre directly analyze ecological/complex-system identity, dynamical continuity, boundaries, resilience-linked identity, and multiple kinds of ecological identity.

CREST is not the first ecological-identity framework and not the first four-way identity taxonomy.

### Not novel 3 — ecological model adequacy

Getz et al. (2018), *Making ecological models adequate*, explicitly organize adequacy around state variables, control variables, data determinacy, sensitivity, validity, and coarse graining.

CREST is not the first ecological model-adequacy framework.

### Not novel 4 — intervention-sensitive ecological state definitions

State-and-Transition Models already define ecological states in relation to dynamics, reversibility, thresholds, and management intervention. State classifications can depend on whether transitions are reversible without major restoration or require stronger interventions.

CREST is not the first account in which intervention possibilities matter to ecological state classification.

### Not novel 5 — action + model uncertainty + partial observability

Adaptive-management / MDP / POMDP ecology already combines management actions, latent states, observation error, model/structural uncertainty, belief updating, learning, and policy optimization.

Fackler & Pacifici unify structural and observational uncertainty. Memarzadeh & Boettiger treat both model and state uncertainty in adaptive management. POMDP reviews in ecology formalize belief states and decisions under imperfect observation.

Nicol & Chadès (2012), *Which States Matter?*, retain only the discretized states needed to preserve an optimal management policy.

CREST is not the first integration of actions, model uncertainty, observations, or task-relevant state compression.

### Not novel 6 — ecological model transferability/reuse

Ecological model-transfer literature already studies when models can be reused across sites/times/novel conditions, how environmental dissimilarity and nonstationarity reduce performance, and how transferred models should be adapted.

MLTR therefore cannot be sold as the discovery that ecological models or categories can fail to transfer.

### Not novel 7 — minimal predictive/behavioral state abstraction

The formal substrate of coarse state equivalence is also mature.

- Computational mechanics defines **causal states** as equivalence classes of histories with the same predictive future distribution and proves a unique minimal predictive representation.
- Bisimulation / MDP model-minimization theory groups states when all actions preserve the relevant reward/output and transition behavior and studies coarsest reduced models.
- Predictive/causal state representations under partial observability learn or characterize coarsest action-observation history partitions.
- State aggregation and approximate abstraction have extensive literatures in decision theory and reinforcement learning.

Therefore CREST must not claim novelty for:

- defining states by future behavior;
- constructing a coarsest future-preserving quotient;
- using partition refinement;
- using action-conditioned behavioral equivalence;
- deriving generic state-abstraction minimality.

These are formal substrates used by individual CREST axes.

---

## 2. What remains distinctive enough to test

After the identity, adequacy, intervention, POMDP, transferability, and state-abstraction audits, CREST's novelty target is narrow and explicitly **metatheoretical**.

Take one proposed coarse ecological equivalence

\[
x\sim y,
\]

meaning that two configurations are to count as one scientific state.

CREST does not ask only whether this is a good predictive abstraction. It separates four different adequacy obligations:

1. **future sufficiency** — can a declared future operation expose a distinction erased by the equivalence?
2. **semantic coherence** — after structural replacement, does an inherited state meaning survive, and if not what is the least source-relative repair?
3. **mechanism robustness** — do all retained response mechanisms agree on the requested future prediction, or must mechanism ambiguity remain explicit?
4. **evidential licensing** — has the evidence licensed the distinction needed for the requested deterministic report?

The candidate contribution is the **failure diagnosis**:

```text
one proposed coarse equivalence
        |
        +-- future failure
        |      -> interface obstruction / lower bound
        |
        +-- inherited-semantic failure
        |      -> source-relative repair / defect / history context
        |
        +-- mechanism failure
        |      -> typed or set-valued report / candidate-safe state
        |
        +-- evidence failure
               -> ambiguity-retaining report / required additional resolution
```

Existing state abstraction usually specifies one behavioral/task criterion and constructs a representation adequate for that criterion. CREST's remaining claim is that **different scientific inadequacies should not be collapsed into one abstraction objective merely because they can all be encoded in a large decision model**.

---

## 3. Direct comparison with the closest prior frameworks

### 3.1 Ecological-system identity — Cumming/Collier and Delettre

Their primary object is the identity/persistence of an ecological or complex system.

CREST's object is the adequacy of a **coarse state equivalence used within a declared model/system**.

```text
system identity
    ≠
scientific adequacy of a chosen state equivalence
```

Delettre's typological/numerical/global/local identities are identity types; CREST's future/semantic/mechanism/evidence axes are adequacy audits. They can cross-classify.

### 3.2 Ecological model adequacy — Getz et al.

Getz et al. already ask whether a whole ecological model contains suitable state/control variables, is data-determined, and is sufficiently valid/sensitive for its task.

CREST is narrower: it takes one equivalence relation among configurations as its object and separates four mathematically different ways that equivalence can become scientifically inadequate.

### 3.3 State-and-Transition Models

STMs already tie ecological state categories to disturbance, reversibility, thresholds, and restoration pathways.

CCOC does not originate intervention-relative state classification. Its formal addition is a cross-grammar lower-bound question: how much exact state information can become necessary when the allowed future operations are enlarged?

### 3.4 Adaptive management and POMDPs

POMDP/adaptive-management frameworks can jointly encode actions, hidden states, model uncertainty, observation models, and learning.

This is a serious neighbor, not a minor analogy.

CREST differs by **diagnostic target**:

- POMDPs primarily define a decision problem and optimize a policy under uncertainty;
- CREST asks which scientific obligation of a proposed state equivalence has failed.

CREST also makes inherited semantics after structural replacement a separate contract rather than simply another latent variable or model parameter.

### 3.5 Policy-relevant state abstraction — Nicol & Chadès

Their work shows that not every ecological detail needs to be preserved: a compact discretization can retain only the states needed for an optimal management policy.

CREST therefore cannot claim “retain only task-relevant distinctions” as new.

Its narrower question is whether the failure comes from future sufficiency, semantic reuse, mechanism disagreement, or evidence licensing, because the remedy differs.

### 3.6 Model transferability

Application-niche and transferability frameworks already ask whether a model developed under one context remains defensible in another.

MLTR's narrower object is one accepted source macro-law carried by a declared source-target relation. Its unique coarsest **source-relative** exact repair preserves inherited merges whenever target exactness permits them.

### 3.7 Causal states / bisimulation / predictive state representations

These formal theories are the closest neighbors to the quotient language used in CCOC/MRM/CED.

They already own generic future-predictive or action-conditioned minimal-state representation.

CREST should therefore say:

> the quotient/refinement machinery is inherited substrate; the philosophical issue is which contract supplies the relevant equivalence criterion and what kind of failure is being diagnosed.

This is exactly why CREST keeps the four theorem programs separate rather than calling one generic behavioral quotient a new ecological theory.

---

## 4. Expanded claim matrix

| Existing framework | Already owns | CREST addition under test | Safe language |
|---|---|---|---|
| Pragmatic representation / perspectivism | purpose-sensitive representation | four distinct adequacy obligations on one equivalence | “CREST decomposes one state-equivalence adequacy question.” |
| Ecological identity theory | system identity, continuity, multiple identity types | state-representation rather than system-identity object | “CREST complements ecological identity theory.” |
| Getz model adequacy | state/control/data/sensitivity/validity adequacy | theorem-backed failure outputs for one coarse equivalence | “CREST is a formal specialization of state-representation adequacy.” |
| State-and-Transition Models | intervention/reversibility-sensitive states | cross-grammar information lower bound | “CCOC quantifies a future-sufficiency failure.” |
| POMDP/adaptive management | action + hidden state + model uncertainty + observation + policy | separates adequacy failures rather than optimizing one encoded decision process | “CREST is diagnostic, not another POMDP.” |
| Conservation state abstraction | policy-relevant state compression | distinguishes four reasons a proposed compression may be inadequate | “Task relevance itself is not a CREST novelty.” |
| Model transferability | contextual model reuse/adaptation | source-relative semantic repair of inherited state labels | “MLTR formalizes one constrained transfer problem.” |
| Causal states / bisimulation / MDP abstraction | minimal future-/action-preserving state representations | asks which scientific contract defines the equivalence and what remedy follows failure | “Generic quotient minimality is substrate.” |
| Robustness/model pluralism | robust conclusions across models | mechanism disagreement as exact report/state problem | “MRM returns ambiguity-explicit alternatives.” |
| Partial observability / HMM/POMDP | hidden-state inference under observation error | reportability criterion + required target resolution | “CED is an evidential-licensing audit.” |
| Historical contingency | legacies/path dependence | inherited-semantic history requirement | “MLTR supplies a semantics-of-state history theorem.” |

---

## 5. Revised philosophical contribution

### Explicitly reject

> CREST discovers context-relative ecological states.

> CREST invents ecological identity, model adequacy, task-relevant state compression, behavioral state abstraction, adaptive uncertainty integration, or model transferability.

### Current safe working formulation

> Existing ecology, philosophy, and decision theory already provide accounts of ecological-system identity, model adequacy, intervention-sensitive states, adaptive management under uncertainty, task-relevant state abstraction, model transferability, predictive causal states, bisimulation, robustness, and partial observability. CREST addresses a narrower representational question: given one proposed coarse equivalence among ecological configurations, which scientific obligation has been violated when that equivalence ceases to support prediction or reporting? It separates future sufficiency, inherited-semantic coherence, mechanism robustness, and evidential licensing because the formal failure objects and remedies differ.

### Strongest novelty hypothesis still worth testing

> **CREST may provide a new theorem-backed, failure-oriented metatheoretical decomposition of coarse ecological state-equivalence adequacy into future-sufficiency, inherited-semantic, mechanism-robustness, and evidential-licensing audits.**

The novelty target is the **cross-contract diagnostic architecture**. No individual mathematical minimization principle is claimed as new merely by appearing inside CREST.

---

## 6. Why the mathematics still matters

### CCOC

Uses existing behavioral/state-abstraction substrate but asks a different comparative question: independently small closed-context interfaces can require a sharply larger interface when future grammars are jointly opened.

### MLTR

Uses refinement substrate but constrains repair to preserve one inherited source semantics. The object is not a fresh target abstraction but the least exact **repair of an inherited law**.

### MRM

Uses behavioral equivalence substrate but indexes hidden variation by retained response types and distinguishes unsupported determinism from exact typed/set-valued reporting.

### CED

Uses partition/refinement substrate but separates what current evidence identifies from what additional target-safe resolution would be sufficient for a deterministic report.

The philosophy paper should make these differences in quantifier order and starting objects visible, rather than present four copies of state minimization.

---

## 7. Revised opening

> Ecology already has mature accounts of ecosystem identity, model adequacy, intervention-sensitive states, adaptive decision-making under partial observability and model uncertainty, state aggregation, model transferability, and predictive state abstraction. These frameworks answer different questions. A narrower representational issue remains easy to hide: when several ecological configurations are assigned the same coarse state label, which scientific obligation is that sameness supposed to satisfy? CREST separates four obligations—future sufficiency, inherited-semantic coherence, mechanism robustness, and evidential licensing—and uses distinct mathematical results to diagnose their failure.

---

## 8. Remaining exact prior-art question

The remaining search question is now deliberately difficult to satisfy accidentally:

> **Is there already a framework that takes one coarse ecological state equivalence as its object, explicitly separates future-action sufficiency, inherited semantic portability, retained-mechanism robustness, and evidence-licensed reportability, and treats failures as requiring distinct formal remedies rather than one unified policy/abstraction objective?**

Targeted searches have found frameworks combining multiple ingredients, especially POMDP/adaptive management and behavioral state abstraction, but not this exact four-contract failure architecture. This is a provisional negative search result, not proof of novelty.

---

## 9. Citation-chain anchors

Priority anchors:

- Cumming & Collier (2005); Collier & Cumming (2011); Delettre (2021);
- Getz et al. (2018);
- State-and-Transition Model literature;
- Nicol & Chadès (2012), *Which States Matter?*;
- Fackler & Pacifici (2014);
- Memarzadeh & Boettiger (2018);
- ecological POMDP reviews;
- Moon et al. model application niche / transferability work;
- Yates et al. model-transferability review;
- Shalizi & Crutchfield on causal states;
- bisimulation/MDP model-minimization and state-abstraction literature;
- predictive/causal state representations under partial observability;
- Giere; Massimi; Bokulich & Parker;
- Odenbaugh; Justus; Plutynski;
- Levins / Wimsatt / Weisberg;
- historical contingency/ecological memory literature.

---

## 10. Current decision

Proceed only with this hierarchy:

```text
existing theory:
  system identity
  + model adequacy
  + intervention-sensitive states
  + POMDP/adaptive management
  + state aggregation / causal states / bisimulation
  + model transferability
  + robustness / history / evidence
        ↓
CREST contribution under test:
  failure-oriented metatheory for one coarse ecological state equivalence
  across future / inherited semantics / mechanisms / evidence
        ↓
formal anchors:
  CCOC / MLTR / MRM / CED
```

No stronger novelty language is currently justified.
