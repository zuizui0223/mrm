# CREST philosophy-of-ecology paper architecture — 信・達・雅 protocol

> **Status:** manuscript architecture only. This document does not add a theorem, claim philosophical priority, or promote CREST into a proved joint theory. It defines how the recovered mathematics may be translated into a philosophy-of-ecology argument.

## 1. Object of the paper

### Working title

> **What Counts as the Same Ecological State? A Contract-Relative Account of State-Representation Adequacy**

The title is intentionally broad. The actual object is narrower:

> **When may different ecological configurations safely be treated as the same coarse scientific state for prediction and reporting?**

This is a question about **state-representation adequacy**, not a complete metaphysics of ecological-system identity.

The working thesis is:

> A proposed coarse ecological state equivalence can be adequate under one scientific contract and inadequate under another. Four contracts are distinguished here: future operations, inherited semantics, retained mechanisms, and evidence.

Compact form:

\[
\boxed{
\text{usable coarse-state equivalence is contract-relative, not unconditional}.
}
\]

The older slogan

\[
\text{“ecological state identity is contract-relative”}
\]

may be used only as shorthand and must immediately be narrowed to **scientific coarse-state representation adequacy**.

CREST is therefore positioned as **philosophy of ecology grounded in mathematical ecology**:

- philosophy supplies the questions of sameness, representation, adequacy, and warranted assertion;
- mathematics supplies counterexamples, impossibility results, minimality results, and exact scope boundaries;
- ecology supplies the practice of using functional groups, community states, resilience classes, occupancy categories, ecosystem-condition states, and management states.

The canonical mathematical boundary is `docs/crest_proof_recovery_2026-08-17.md`.
The canonical prior-art boundary is `docs/crest_philosophy_literature_positioning_2026-08-17.md`.
The sentence-level firewall is `docs/crest_philosophy_claim_ledger_2026-08-17.md`.

---

## 2. Prior-art boundary

The paper must begin cumulatively rather than by claiming an empty field.

Existing work already owns major neighboring claims:

- ecosystem/system identity and dynamical continuity;
- multiple notions of ecological identity;
- ecological model adequacy and coarse graining;
- intervention-sensitive ecological states;
- pragmatic and perspectival representation;
- POMDP/adaptive management under state, model, and observation uncertainty;
- policy-relevant state abstraction;
- causal states, bisimulation, MDP abstraction, and causal abstraction;
- ecological model transferability;
- robustness/model pluralism;
- historical contingency and ecological memory;
- partial observability and evidence underdetermination.

Accordingly, CREST does **not** claim to invent ecological identity, model adequacy, intervention-relative state definition, task-relevant abstraction, causal abstraction, transferability, or uncertainty-aware decision theory.

Its remaining novelty hypothesis is deliberately narrower and remains **OPEN**:

> **CREST may provide a theorem-backed, failure-oriented metatheoretical decomposition of one coarse ecological state-equivalence adequacy problem into future-sufficiency, inherited-semantic, mechanism-robustness, and evidential-licensing audits.**

The novelty target is the **cross-contract diagnostic architecture**, not any individual quotient/minimization method.

---

## 3. 信 — fidelity protocol

Every philosophically important manuscript sentence must be tagged during drafting:

1. **FORMAL** — directly proved in CCOC, MLTR, MRM, or CED;
2. **INTERPRETIVE** — an ecological/philosophical reading of a formal result;
3. **OPEN** — a metatheoretical proposal, novelty hypothesis, or unproved extension;
4. **REJECT** — known overclaim or rediscovery of established prior art.

Hard rules:

- never turn a sufficient condition into an iff statement;
- never treat finite replay or CI as proof of a quantified theorem;
- never treat a required state distinction as one already observed;
- never add CCOC/MLTR/MRM/CED complexity quantities without a joint theorem;
- never claim that the four audits are exhaustive;
- never claim general audit independence or commutation;
- never claim one globally minimal simultaneous CREST state;
- never introduce a fifth “CREST theorem” merely by composing the four proof packages.

The claim ledger, not rhetorical convenience, decides what wording is admissible.

---

## 4. 達 — the argument spine

The manuscript should not read as four theories placed side by side. It should make one argument in six moves.

### Move 1 — Ecology already relies on coarse sameness

**Status:** INTERPRETIVE / established practice.

Ecological modelling routinely maps heterogeneous configurations to one state label:

\[
q:X\to Q.
\]

A label such as `pollination maintained`, `degraded state`, `occupied`, `resilient`, or `functional guild A` is therefore not only a description. It asserts that distinctions erased by `q` are irrelevant for the scientific work assigned to that state representation.

**Reader question:**

> Irrelevant for what?

This is the paper's entry point.

### Move 2 — “Adequate state” hides more than one obligation

**Status:** INTERPRETIVE / CREST architecture.

A single phrase such as “this is an adequate state variable” can hide several different claims. CREST isolates four that arise in the current theorem program:

1. the merge remains sufficient under the declared future operations;
2. the merge preserves inherited meaning after structural change;
3. the merge does not hide retained mechanism disagreement relevant to the requested future;
4. the distinction claimed in the report is licensed by the available evidence.

Do **not** call these four obligations exhaustive or mutually independent in general. The claim is only that they are **distinct in the present formalization**: they begin from different objects, use different quantifier orders, and have different failure outputs.

**Transition sentence:**

> The crucial issue is therefore not whether ecological states are “relative” in some generic sense, but which adequacy obligation a proposed equivalence is expected to satisfy.

### Move 3 — The four obligations can fail in mathematically different ways

**Status:** FORMAL anchors + INTERPRETIVE synthesis.

#### Future sufficiency

CCOC shows that small exact interfaces in each supplied closed future do not imply one comparably small exact interface for a jointly open future grammar.

Failure object:

> a future legal word or family of addressable futures that separates configurations previously merged.

Remedy / consequence:

> retain more interface information, or accept an open-future obstruction/lower bound.

#### Semantic coherence

MLTR fixes one inherited source law and asks whether its carried target partition remains exact. If not, it constructs the unique coarsest exact **source-relative** repair.

Failure object:

> inherited labels that no longer support well-defined target outputs/legal actions/successors.

Remedy / consequence:

> split only what target exactness forces while preserving inherited merges that remain valid; retain history context when incompatible inherited maps themselves must be preserved.

#### Mechanism robustness

MRM asks whether retained response types agree on the requested future behavior. Unsupported determinism is replaced by exact typed or set-valued reporting, and the candidate-safe quotient keeps only response distinctions that matter.

Failure object:

> retained response types with different declared future successors.

Remedy / consequence:

> retain target-relevant mechanism information or report ambiguity explicitly.

#### Evidential licensing

CED asks what a finite experiment/observation contract licenses. If one compatible evidence class contains multiple target values, one deterministic report is not justified. Its target-safe quotient is a **required resolution**, not an already observed state.

Failure object:

> an evidence-compatible class spanning multiple target values or target-safe blocks.

Remedy / consequence:

> retain ambiguity, strengthen the evidence contract, or choose a risk-limited experiment within the declared policy family.

**Transition sentence:**

> These are not four names for one failed abstraction: they diagnose different reasons why the same coarse state label can cease to do the scientific work expected of it.

This is an INTERPRETIVE synthesis, not a theorem of logical independence.

### Move 4 — Different failures require different remedies

**Status:** INTERPRETIVE, grounded in the four formal outputs.

The manuscript's strongest explanatory move is the remedy contrast:

```text
same proposed state equivalence
        |
        +-- future insufficiency
        |      -> remember more / interface lower bound
        |
        +-- semantic non-portability
        |      -> source-relative repair / defect / history
        |
        +-- mechanism non-robustness
        |      -> typed or set-valued report / candidate-safe state
        |
        +-- evidential non-resolvability
               -> ambiguity-retaining report / required additional evidence
```

A generic instruction to “use a better state abstraction” loses this diagnosis. A state may require more information because future operations expose hidden differences, because an inherited category changed meaning, because mechanism alternatives disagree, or because the evidence has not earned the distinction. Those are scientifically different problems even when all can be encoded inside one sufficiently rich decision model.

**Boundary:** CREST does not prove that a combined decision model cannot encode all four. The philosophical claim is diagnostic: encoding ingredients together does not erase the difference between the adequacy obligations.

### Move 5 — Contract-relative does not mean arbitrary

**Status:** INTERPRETIVE.

CREST need not choose between naive realism and unrestricted constructivism.

Whatever ontology one adopts for ecological systems, a **scientific coarse-state representation** can still be tested against explicit obligations. Once a contract is declared:

- a legal future can refute a proposed merge;
- a structural replacement can invalidate inherited semantics;
- retained mechanisms can disagree on a successor;
- an evidence class can contain incompatible target values.

Thus:

\[
\boxed{
\text{contract-relative}\neq\text{arbitrary}.
}
\]

The contract is a modelling commitment; the consequences under that contract are constrained.

### Move 6 — Philosophical conclusion

**Status:** INTERPRETIVE / preferred thesis.

Do not conclude that CREST has discovered the true ontology of ecological states.

Conclude instead:

> **Ecological state equivalence should be treated as an explicit scientific commitment rather than an invisible modelling default.**

To say that two configurations are “the same state” is to make commitments about what futures, meanings, mechanism alternatives, and evidence are relevant to that sameness.

The four CREST audits provide one theorem-backed way to make those commitments inspectable.

---

## 5. One recurring example — `pollination maintained`

The entire manuscript should use one ecological label rather than four unrelated examples.

Two configurations currently receive the same coarse label:

> **pollination maintained**.

### Future-sufficiency audit

A newly connected pollinator channel or intervention exposes a response distinction hidden under the present closed grammar.

Question:

> Were these configurations the same predictive state for the enlarged future?

### Semantic-coherence audit

After pollinator turnover, the inherited class may need to split according to substitute-response capacity.

Question:

> Does the old category preserve enough inherited operational meaning to support the same management semantics?

### Mechanism-robustness audit

Several retained mechanisms agree on current pollination but disagree about competitor removal or habitat restoration.

Question:

> Is one deterministic prediction warranted while those response alternatives remain possible?

### Evidential-licensing audit

Camera, visitation, eDNA, or experimental records may leave target-relevant alternatives compatible.

Question:

> Even if the distinction matters, has the evidence earned the right to report it?

The point is not that `pollination maintained` is false. It is that the **adequacy of treating configurations as equivalent under that label** depends on the contract.

---

## 6. Formal anchors — minimum mathematics in the philosophy paper

The philosophy paper needs only one formal anchor per audit.

### CCOC

Show the contrast

\[
\max_j K_{\mathrm{closed},j}=O(1),
\qquad
K_{\mathrm{open}}=\Omega(m)
\]

through the concrete future-addressability idea. Do not reproduce the full theorem family.

Philosophical payload:

> future repertoire can change minimum state requirements.

### MLTR

Show one inherited fiber that becomes invalid and the source-relative refinement idea.

Philosophical payload:

> state meaning can fail to transport even when a label remains syntactically available.

### MRM

Show one current observed state with two retained response types giving different successors.

Philosophical payload:

> current sameness does not license one predictive state when retained response laws disagree.

### CED

Show one evidence-compatible class containing two different target values.

Philosophical payload:

> a distinction can be required for prediction without being licensed by current evidence.

The mathematical goal of the philosophy paper is not proof reproduction. It is to make the four quantifier structures visibly non-identical.

---

## 7. Paragraph-level manuscript flow

### Introduction

**Paragraph 1 — established background.**
Acknowledge ecosystem identity, model adequacy, intervention-sensitive states, POMDP/state abstraction, causal abstraction, and transferability as existing literatures.

**Paragraph 2 — isolate the hidden commitment.**
Ecologists still routinely assign multiple configurations one coarse state label. Ask what that equivalence is required to preserve.

**Paragraph 3 — state the gap.**
Existing frameworks often optimize or assess a model under a chosen task; CREST instead separates four reasons why one proposed equivalence can fail.

**Paragraph 4 — thesis and non-claim.**
Introduce the four audits. State explicitly that the decomposition is not claimed exhaustive and CREST is not a fifth theorem.

### Main conceptual section

Use the `pollination maintained` example to pass through the four audits in the same order every time:

```text
future -> inherited meaning -> mechanism alternatives -> evidence
```

This order is explanatory only. It is **not** claimed to be a universal computational or causal order.

### Formal section

For each audit:

1. one setup sentence;
2. one minimal mathematical statement;
3. one failure witness;
4. one remedy;
5. one explicit non-claim.

### Synthesis section

Make the remedy contrast the center. Do not say “there are four kinds of ecological identity.” Say:

> there are at least four distinct adequacy questions that can be asked of the same coarse state equivalence in the current program.

### Discussion

Connect to existing philosophy as a diagnostic refinement of model adequacy/perspectivism rather than an alternative metaphysics.

### Conclusion

Return to the modelling commitment:

> when a state label merges configurations, the burden is to state what that merge is supposed to preserve.

---

## 8. 雅 — economy rules

The full manuscript must preserve:

- **one object:** one proposed coarse state equivalence;
- **one thesis:** its adequacy is contract-relative rather than unconditional;
- **four audits:** future, semantics, mechanism, evidence;
- **one recurring example:** `pollination maintained`;
- **one conclusion:** ecological sameness is an explicit scientific commitment.

Cut anything that does not serve that line.

Do not include:

- repository history;
- CI or implementation detail;
- a theorem catalogue;
- multiple competing umbrella metaphors;
- a survey of every abstraction framework;
- an argument that ecology was previously unaware of context, uncertainty, or identity;
- speculative fifth or sixth CREST axes in the main paper.

Literature belongs where it sharpens a boundary, not as a defensive bibliography dump.

---

## 9. Abstract skeleton

Do not finalize until the remaining exact prior-art question is sufficiently citation-chained.

**信:** Ecology routinely compresses heterogeneous configurations into shared states used for prediction and management. Existing work already treats ecosystem identity, model adequacy, intervention-sensitive states, and scientific representation as dynamic or purpose-sensitive. We ask a narrower question: when is one proposed coarse ecological state equivalence adequate for the scientific work assigned to it?

**達:** We distinguish four ways that equivalence can fail: future operations can expose erased distinctions; structural change can disrupt inherited state meaning; retained response mechanisms can agree on the present while disagreeing on future response; and finite evidence can fail to license a distinction required by the target prediction.

**雅:** These results motivate a contract-relative account of state-representation adequacy. The point is not that ecological states are arbitrary, but that a sameness claim should specify what it is expected to preserve. The four audits provide distinct formal failure tests while no claim is made that they are exhaustive, mutually independent, commuting, or jointly minimal.

---

## 10. Stop rule before full prose drafting

Full manuscript prose starts only when:

1. the exact four-contract novelty hypothesis has undergone the remaining citation-chain check;
2. every central sentence is admissible under the 信 claim ledger;
3. the argument can be stated without calling the audits independent or exhaustive;
4. one pollination example carries all four audits;
5. the manuscript contains no fifth theorem called “CREST theorem.”

At that point, drafting should proceed paragraph-by-paragraph from the argument spine above rather than from the repository histories.
