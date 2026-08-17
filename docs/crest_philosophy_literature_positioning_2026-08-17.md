# CREST philosophy-of-ecology literature positioning — 2026-08-17

> **Status:** literature-positioning gate for a future philosophy-of-ecology manuscript. This document is not a novelty claim and does not alter the formal CREST proof ledger.

## 1. Immediate conclusion

Six broad novelty claims are now excluded.

### Not novel 1 — purpose/context relativity

The general idea that scientific representations are purpose-, perspective-, context-, or boundary-relative is already well developed in philosophy of science and philosophy of ecology.

Relevant traditions include pragmatic scientific representation, scientific perspectivism / perspectival realism, model pluralism, adequacy-for-purpose, and open-system/boundary-choice arguments.

CREST must not claim that it discovered purpose- or context-relative representation.

### Not novel 2 — ecological identity as a philosophical problem

Ecological and complex-system identity has a direct literature.

- Cumming & Collier (2005) analyze identity through system change, boundaries, and spatiotemporal continuity.
- Collier & Cumming (2011) argue for a dynamical approach to ecosystem identity because measurement, interaction, and intervention are themselves dynamic.
- Delettre (2021) explicitly distinguishes typological, numerical, global-state, and local-state ecological identity and notes that key-variable choice partly reflects scale, objectives, and researcher judgement.

CREST must not claim to be the first ecological-identity framework or the first four-way identity decomposition.

### Not novel 3 — ecological model adequacy as an explicit program

Getz et al. (2018), *Making ecological models adequate*, explicitly organize ecological model adequacy around state variables, control variables, data determinacy, sensitivity, validity, and coarse graining. They warn both against unsupported detail and against omitting mechanistic detail required to predict management response.

CREST must not claim that ecology lacked a model-adequacy framework.

### Not novel 4 — intervention-sensitive ecological state definitions

State-and-Transition Models already organize ecological states in relation to dynamics, reversibility, thresholds, and management intervention. In rangeland practice, community phases can be assigned to the same ecological state when reversible transitions remain possible without major restoration intervention and to different states when recovery requires stronger intervention or is not reversible.

Thus CREST must not claim that it first made ecological state classification dependent on intervention or future response.

### Not novel 5 — joint action, model uncertainty, and partial observability

Adaptive-management / MDP / POMDP ecology already integrates several ingredients that superficially resemble CREST:

- future management actions;
- uncertainty in ecological state;
- observation error / partial observability;
- structural or model uncertainty;
- learning from new observations;
- policy optimization under those uncertainties.

Fackler & Pacifici (2014) explicitly unify structural and observational uncertainty in resource management. Memarzadeh & Boettiger (2018) address ecological adaptive management under both model and state uncertainty. POMDP reviews in ecology treat belief states, observation models, management actions, and model uncertainty directly.

Nicol & Chadès (2012), *Which States Matter?*, go further toward state representation: they discretize a continuous ecological state space by retaining the states necessary to preserve an optimal management policy.

Therefore CREST must not claim that it first unifies action, mechanism/model uncertainty, observation, or task-relevant state compression.

### Not novel 6 — ecological model transferability/reuse

Ecological model transferability has a substantial literature. Existing work asks when pre-existing ecological models can be applied to new sites, times, or environmental conditions, how contextual differences affect generalizability, and how models should be adapted when transferred.

Examples include model application niche analysis, broad reviews of transferability challenges, and practical guidelines for adapting ecosystem models to new locations.

Therefore MLTR must not be philosophically sold as the discovery that ecological models or categories may fail to transfer.

Its narrower formal object is inherited state semantics under a declared source-target relation and the unique coarsest exact **source-relative** repair.

---

## 2. What remains distinctive enough to test

After the direct identity, adequacy, POMDP, state-abstraction, and transferability audits, the CREST novelty target is narrow.

CREST is **not**:

- a new metaphysics of ecosystem identity;
- a generic model-adequacy checklist;
- a new adaptive-management framework;
- a new POMDP/state-abstraction method;
- a generic transferability framework;
- a new statement that context, history, uncertainty, or evidence matter.

The remaining object is a **failure-oriented metatheory of one proposed coarse state equivalence**.

Given a proposed relation

\[
x\sim y
\]

meaning that two ecological configurations are to be treated as the same scientific state, CREST asks four logically different questions:

1. **future sufficiency:** can some declared future operation distinguish the merged configurations?
2. **semantic coherence:** after declared structural change, can inherited state meaning still be carried without additional splits?
3. **mechanism robustness:** do all retained response mechanisms agree on the requested future behavior at that state?
4. **evidential licensing:** has the evidence actually resolved the distinction needed for the requested deterministic report?

The important feature is the **diagnostic separation**:

```text
one proposed equivalence
        |
        +-- future failure      -> remember more / interface lower bound
        +-- semantic failure    -> source-relative repair / defect / history
        +-- mechanism failure   -> typed or set-valued prediction / candidate-safe state
        +-- evidence failure    -> ambiguity-retaining report / additional evidence requirement
```

POMDPs can combine actions, hidden states, model uncertainty, and observations in one decision process. CREST's claim is different: it asks **which adequacy obligation failed before or alongside policy optimization**, and it keeps inherited semantics as a separate contract rather than simply another latent variable.

---

## 3. Direct comparison with the closest prior frameworks

### 3.1 Cumming & Collier / Collier & Cumming — identity of the ecological system

Their target is system identity through change: what constitutes one system, how its boundaries and continuities are defined, and why ecosystem identity should be dynamic.

CREST's target is a state representation *within* a declared system/model:

> under which scientific contracts may two configurations safely share one state label?

```text
identity of the ecological system
    ≠
adequacy of a state equivalence used inside the system
```

### 3.2 Delettre — kinds of ecological identity

Delettre distinguishes typological, numerical, global-state, and local-state identity.

CREST distinguishes future sufficiency, semantic coherence, mechanism robustness, and evidential licensing.

The former are kinds/levels of ecological identity or persistence. The latter are failure tests for a chosen scientific equivalence relation. They can cross-classify rather than compete.

### 3.3 Getz et al. — ecological model adequacy

Getz et al. are the closest general adequacy precursor. Their protocol asks whether the whole model includes suitable state/control variables, is supported by data, and behaves validly/sensitively for its purpose.

CREST is narrower and more formal:

> take one coarse state equivalence as the object and ask which contract invalidates it.

Its theorem programs return different objects rather than one generic adequacy score.

### 3.4 State-and-Transition Models — intervention-sensitive states

STMs already connect ecological state classification to reversibility, disturbance, thresholds, and management pathways. This directly precedes any philosophical claim that state labels are related to intervention possibilities.

CCOC differs in formal question:

> if the admissible future grammar is enlarged, how much additional exact interface information can become necessary even when each closed future is individually compressible?

Thus CCOC is a lower-bound/representation theorem, not a first definition of intervention-relative ecological states.

### 3.5 POMDP / adaptive management — actions, uncertainty, and observations

Ecological POMDPs already represent:

- latent system states;
- actions;
- observation processes;
- belief states;
- model/structural uncertainty;
- adaptive learning and policy optimization.

This creates substantial overlap with the **ingredients** of CCOC, MRM, and CED.

The CREST distinction is architectural rather than ingredient-based:

- CCOC audits future-sufficiency of a proposed equivalence;
- MRM audits whether retained response alternatives license deterministic prediction;
- CED audits what evidence licenses reporting;
- MLTR audits inherited semantics after structural replacement.

CREST does not claim these must be modeled separately in every applied problem. It claims they are **logically distinct adequacy obligations** and should not be silently conflated because one decision framework can numerically encode all of them.

### 3.6 Nicol & Chadès — task-relevant state abstraction

Their CU-Tree/POMDP work explicitly asks which ecological states are necessary to preserve a management policy. This means task-relevant state compression is established practice.

CREST differs by asking why a proposed compression fails and by returning different remedies depending on the failure contract. It should not claim priority for “only retain task-relevant state.”

### 3.7 Ecological model transferability

Application-niche and transferability literatures already recognize that a model defensible in one context can be misapplied in another because of environmental novelty, nonstationarity, interactions, data bias, or changed conditions.

MLTR's formal distinction is that it fixes one inherited source macro-law and asks for exact transport relative to a declared relation. If the carried partition fails, it constructs the unique coarsest exact target refinement that preserves every inherited merge still compatible with target dynamics.

This is a semantics-preserving repair problem, not a general claim about transferability.

---

## 4. Claim matrix after the expanded prior-art audit

| Existing claim/framework | Already owns | CREST formal addition | Safe manuscript language |
|---|---|---|---|
| Pragmatic representation / perspectivism | purpose- and perspective-relative representation | four logically distinct contracts are attached to one coarse equivalence | “CREST decomposes one state-equivalence adequacy problem into four audits.” |
| Ecological identity literature | dynamic/system identity; multiple identity types | focuses on scientific state-equivalence adequacy rather than system identity | “CREST complements ecological identity theory with representation-level audits.” |
| Getz model adequacy | state/control/data/sensitivity/validity checks | theorem-backed failure objects for one state equivalence | “CREST is a formal specialization of state-representation adequacy.” |
| State-and-Transition Models | state classification tied to reversibility/intervention | exact future-grammar interface lower bounds | “CCOC quantifies one consequence of widening the future contract.” |
| POMDP/adaptive management | actions + latent state + observation + model uncertainty + policy optimization | separates adequacy obligations before/alongside optimization and adds inherited-semantic audit | “CREST is diagnostic, not another decision-process formalism.” |
| State abstraction in conservation | retain states relevant to optimal policy | distinguishes why a compression fails and which remedy follows | “CREST does not claim task-relevant abstraction as new.” |
| Model transferability | context-dependent model reuse/adaptation/generalization | unique source-relative exact repair of inherited macrostate semantics | “MLTR formalizes one constrained transfer problem, not transferability in general.” |
| Robustness/model pluralism | model convergence and robust conclusions | exact deterministic/typed/set-valued report under retained response disagreement | “MRM treats disagreement as a reporting/state problem.” |
| Partial observability / hidden states | belief-state inference and decision under imperfect observation | exact evidence-class reportability and required target-safe refinement | “CED is a report-licensing audit, not a replacement for POMDP inference.” |
| Historical contingency | legacies/path dependence | minimum context needed to preserve incompatible inherited semantic maps | “MLTR supplies one semantics-of-state history theorem.” |

---

## 5. Revised philosophical contribution

### Reject

> CREST discovers that ecological states are context-relative.

### Reject

> CREST is the first ecological identity, model adequacy, adaptive-management, state-abstraction, or transferability framework.

### Current safe working formulation

> Existing ecological and philosophical frameworks already address ecosystem identity, purpose-relative representation, model adequacy, intervention-sensitive states, adaptive management under model and observation uncertainty, state abstraction, model transferability, robustness, and historical contingency. CREST addresses a narrower logical problem. Given one proposed coarse equivalence among ecological configurations, four different scientific contracts can invalidate that equivalence in different ways, and the four associated theorem programs return different failure certificates and remedies.

### Strongest novelty hypothesis still worth testing

> **CREST may provide a new theorem-backed, failure-oriented decomposition of coarse ecological state-equivalence adequacy into future-sufficiency, inherited-semantic, mechanism-robustness, and evidential-licensing audits.**

The qualifiers **may**, **failure-oriented**, **coarse state-equivalence**, and **theorem-backed** are essential.

The novelty target is now the *decomposition and diagnostic architecture*, not any individual ingredient.

---

## 6. Why the mathematics still matters

The closest existing frameworks could otherwise make CREST look like a verbal relabeling. The mathematical anchors prevent that.

### CCOC

Not merely “interventions matter.”

It gives an exact future-word injection showing that a wider future grammar can force a larger exact interface, including families with constant-size closed interfaces and growing open-interface memory.

### MLTR

Not merely “transfer can fail.”

It fixes inherited source semantics and constructs the unique coarsest exact source-relative repair, with a precise history-context lower/upper bound when incompatible carried maps must be preserved.

### MRM

Not merely “model uncertainty matters.”

It asks when retained response laws license one deterministic report, when typed/set-valued reporting is exact, and what minimum mechanism-relative state must remain.

### CED

Not merely “states are partially observed.”

It asks what may be **reported** from a compatible evidence class, distinguishes current evidence from required target-safe resolution, and ties trusted refinement to explicit failure/risk contracts.

---

## 7. Revised opening for the manuscript

> Ecology already has mature ways to define ecosystem states, assess model adequacy, optimize decisions under partial observability and model uncertainty, aggregate states for management, and test model transferability. These frameworks solve different scientific problems. A more specific logical question remains implicit across them: when several ecological configurations are assigned the same coarse state label, what exactly is being assumed about their future behavior, inherited meaning, mechanism dependence, and evidential distinguishability? CREST treats these as four distinct adequacy obligations of one proposed state equivalence.

This opening makes the paper cumulative rather than priority-seeking.

---

## 8. Remaining exact search question

The search has now become very narrow:

> **Is there already a philosophy/ecology/decision-theory framework that explicitly takes one coarse ecological state equivalence as its object and separately audits (i) future-action sufficiency, (ii) semantic portability across structural replacement, (iii) robustness to retained response mechanisms, and (iv) evidence-licensed reportability, with distinct failure outputs?**

The targeted searches so far have found frameworks that combine several of these ingredients, especially POMDP/adaptive management, but not one that gives this same four-way adequacy decomposition. This remains a provisional negative search result, not proof of novelty.

---

## 9. Bibliographic anchors for citation chaining

Priority anchors now include:

- Cumming & Collier (2005), *Change and Identity in Complex Systems*;
- Collier & Cumming (2011), *A Dynamical Approach to Ecosystem Identity*;
- Delettre (2021), *Identity of Ecological Systems and the Meaning of Resilience*;
- Getz et al. (2018), *Making Ecological Models Adequate*;
- Nicol & Chadès (2012), *Which States Matter?*;
- Fackler & Pacifici (2014), structural + observational uncertainty in resource management;
- Memarzadeh & Boettiger (2018), adaptive management under partial observability/model uncertainty;
- Williams & Brown / Chadès POMDP ecology reviews;
- state-and-transition model literature;
- Moon et al. model application niche / transferability literature;
- Yates et al. transferability challenges;
- Giere; Massimi; Bokulich & Parker;
- Odenbaugh; Justus; Plutynski;
- Levins / Wimsatt / Weisberg;
- historical contingency and ecological memory literature.

---

## 10. Current decision

Proceed under this hierarchy:

```text
existing ecology/philosophy/decision theory:
  system identity
  + model adequacy
  + intervention-sensitive states
  + POMDP/adaptive management
  + state abstraction
  + transferability
  + robustness/history/evidence
        ↓
CREST contribution under test:
  theorem-backed failure diagnosis for one coarse state equivalence
  across future / semantics / mechanism / evidence contracts
        ↓
formal anchors:
  CCOC / MLTR / MRM / CED
```

No stronger novelty language is currently justified.
