# What Counts as the Same Ecological State?
## A Contract-Relative Account of State-Representation Adequacy

> **Development draft — 信・達・雅 controlled.** This is a philosophy-of-ecology synthesis/perspective grounded in the recovered CCOC, MLTR, MRM, and CED theorem programs. It does not claim that CREST is a fifth theorem, that the four audits are exhaustive, or that generic representational adequacy, state abstraction, ecological identity, or model transferability is new.

## Abstract

<!-- INTERPRETIVE: C36 / established ecological modelling practice -->
Ecology routinely compresses heterogeneous configurations into shared states used for prediction, comparison, and management.

<!-- PRIOR ART BOUNDARY: C33–C35 -->
Existing work already provides mature accounts of ecosystem identity, ecological model adequacy, intervention-sensitive states, predictive state abstraction, partial observability, causal abstraction, and purpose-sensitive scientific representation.

<!-- INTERPRETIVE: C1 -->
We ask a narrower question: when several ecological configurations are assigned the same coarse state, what scientific commitments are being made by that equivalence?

<!-- INTERPRETIVE ARCHITECTURE: C27, no independence/exhaustiveness claim -->
We distinguish four adequacy questions in the current program: whether the equivalence remains sufficient under declared future operations, preserves inherited meaning after structural change, supports prediction across retained mechanism alternatives, and is licensed by the available evidence.

<!-- FORMAL ANCHORS: C4, C10, C15/C18, C21/C23 -->
These questions are anchored respectively by an open-future interface lower bound, a unique coarsest source-relative repair, mechanism-safe deterministic/typed/set-valued reporting, and an evidence-relative reportability criterion with a required target-safe refinement.

<!-- INTERPRETIVE: remedy contrast -->
The same coarse state can therefore fail for different reasons, and the appropriate response differs: retain additional predictive information, repair inherited semantics, preserve or resolve mechanism ambiguity, or withhold a distinction that the evidence has not earned.

<!-- INTERPRETIVE: C3 -->
Contract-relative adequacy is not unrestricted relativism: once a scientific contract is declared, proposed state merges can be tested and can fail for explicit formal reasons.

<!-- POSITIONING: C35 OPEN, priority-independent -->
We present CREST as a theorem-grounded synthesis for making ecological state-equivalence commitments explicit; no claim is made that these four audits are exhaustive, commuting, jointly minimal, or the first general theory of representational adequacy.

---

## 1. From ecosystem identity to state-representation adequacy

<!-- PRIOR ART: do not claim an empty field -->
Ecologists have long had to decide what counts as a system, a state, a regime, or a functionally equivalent configuration. Philosophy of ecology has examined the identity and continuity of ecological systems, including dynamical accounts of ecosystem identity and distinctions among different senses of ecological identity (Cumming & Collier; Collier & Cumming; Delettre). Ecological modelling has likewise developed explicit adequacy protocols, intervention-sensitive State-and-Transition Models, adaptive-management and POMDP approaches to hidden state and model uncertainty, methods for task-relevant state aggregation, and extensive work on model transferability. In adjacent formal fields, causal states, bisimulation, state abstraction, and causal abstraction already provide mature accounts of prediction- or intervention-preserving coarse representations. CREST begins from this literature rather than from the claim that ecological representation was previously treated as context-free.

<!-- INTERPRETIVE: C1/C36 -->
A narrower commitment is nevertheless easy to leave implicit. Let a coarse state representation assign configurations \(x\in X\) to labels \(q(x)\in Q\). Whenever \(q(x)=q(y)\), the model is licensed to ignore at least some differences between \(x\) and \(y\). The important question is not simply whether this is a useful simplification. It is **which differences the state variable promises can safely be ignored for the scientific work assigned to it**. A state label used to summarize the present, forecast future interventions, transfer an inherited ecological classification, average over mechanism uncertainty, and support an empirical report is being asked to satisfy more than one kind of adequacy.

<!-- INTERPRETIVE ARCHITECTURE: distinct, not generally independent -->
CREST separates four such questions in the present theorem program. **Future sufficiency** asks whether an enlarged legal future can expose a distinction that the coarse state erased. **Semantic coherence** asks whether an inherited state meaning remains operationally valid after structural replacement. **Mechanism robustness** asks whether retained response mechanisms agree on the future prediction requested from the state. **Evidential licensing** asks whether the available experiment and observation contract actually justify reporting the distinction that the prediction requires. These are not asserted to be an exhaustive taxonomy of ecological adequacy. They are kept separate because the current formalizations start from different objects, quantify over different alternatives, and return different failure certificates and remedies.

<!-- INTERPRETIVE: C3/C36 -->
The resulting position is contract-relative without being arbitrary. Scientists choose which futures, inherited meanings, candidate mechanisms, observations, and targets belong to a model contract; CREST does not prove that one such contract is uniquely correct for nature. But once a contract is declared, the proposed state equivalence is no longer protected by convenience alone. A legal future can distinguish two merged configurations; a structural replacement can make an inherited label operationally incoherent; retained mechanisms can disagree on a successor; and an evidence class can contain multiple target values. Our philosophical claim is therefore modest: **ecological state equivalence should be treated as an explicit scientific commitment rather than an invisible modelling default.**

---

## 2. One state label, four different tests

Consider the coarse ecological state **pollination maintained**. Suppose two configurations currently receive this same label because both sustain adequate pollination under the present community and management repertoire. CREST does not ask whether that label is simply true or false. It asks what follows when the same label is used for different scientific purposes.

### 2.1 Future sufficiency

<!-- FORMAL anchor: C4; INTERPRETIVE: C5 -->
Two configurations can be equivalent under every supplied closed future yet require different state information once future colonization, reconnection, dispersal, or intervention possibilities are jointly opened. CCOC formalizes this as a cross-grammar compression problem: concrete legal future words can make previously dormant distinctions operationally addressable, forcing a larger exact interface. The ecological lesson is not that open systems lack macrolaws, but that **present or closed-context functional equivalence need not be sufficient for an enlarged future repertoire**.

### 2.2 Semantic coherence

<!-- FORMAL anchor: C9/C10/C13; reject C12 -->
After pollinator turnover, the inherited label `pollination maintained` may still be syntactically available while no longer grouping states with the same legal actions or future responses. MLTR fixes the inherited source classification rather than replacing it with an unconstrained target abstraction. If the carried classification fails exactness, its unique coarsest source-relative repair adds only the distinctions forced by the target dynamics. Historical context is retained when incompatible inherited terminal meanings themselves must be preserved. The point is not that different histories always produce different final partitions; it is that **semantic reuse imposes a constraint that ordinary target-only re-abstraction can ignore**.

### 2.3 Mechanism robustness

<!-- FORMAL anchor: C15/C16/C18; reject C17/C20 -->
The same visible pollination state can also be compatible with several retained response mechanisms. If those response types disagree about competitor removal, habitat restoration, or another declared intervention, a single deterministic forecast is not uniformly supported. MRM does not require full mechanism identity to remain in the state. It retains only response distinctions that can change the declared future behavior, and otherwise permits exact typed or set-valued reporting. **Mechanism ambiguity is therefore a predictive-state issue only where retained alternatives make different predictions under the declared action and target contract.**

### 2.4 Evidential licensing

<!-- FORMAL anchor: C21/C23; reject C24/C25 -->
Finally, a distinction can be prediction-relevant without being one that current observations license us to report. Camera records, visitation observations, eDNA, or experiments may leave multiple target-relevant worlds compatible. CED licenses a deterministic target report exactly when the target is constant on the compatible evidence class. Its target-safe quotient describes the minimum additional resolution that would be sufficient for deterministic target tracking; it is **not** a state already identified by the present data. Evidence failure therefore calls for ambiguity-retaining reporting or a stronger evidence contract, not for silently promoting a required distinction into an observed fact.

---

## 3. Why the failure diagnosis matters

<!-- INTERPRETIVE, no universal independence theorem -->
A sufficiently rich decision model could encode future actions, structural changes, mechanism alternatives, and observations together. CREST does not claim otherwise. The reason to keep the four audits conceptually visible is diagnostic. A coarse state can be inadequate because it forgot a future-relevant distinction, because an inherited category changed meaning, because retained mechanisms disagree, or because the evidence has not resolved what the report requires. Calling all four cases “bad abstraction” hides what should happen next.

```text
future insufficiency
    -> retain more predictive information / accept an interface obstruction

semantic non-portability
    -> source-relative repair / defect / required history context

mechanism non-robustness
    -> typed or set-valued prediction / candidate-safe state / discrimination

evidential non-resolvability
    -> ambiguity-retaining report / required additional evidence
```

<!-- OPEN boundaries: C28-C31 -->
This diagnosis does not yet supply a universal order for applying the audits. We have not proved that the audits commute, that their complexity measures add, that passing three implies the fourth, or that one unique globally minimal representation satisfies all four. Those are possible future synthesis questions, not premises of the present philosophical account.

---

## 4. Contract-relative does not mean arbitrary

<!-- INTERPRETIVE: C3 -->
The most natural philosophical objection is that a contract-relative account makes state identity merely conventional: choose a different purpose and obtain a different state. That conclusion does not follow. CREST concerns the adequacy of a **scientific representation**, not the claim that underlying ecological processes depend on our descriptions. The contracts specify which consequences a representation is expected to preserve. Given those commitments, failure can be objective relative to the model: two merged configurations produce different legal future traces; a carried label fails to factor target dynamics; two retained response types disagree; or one evidence class supports incompatible target values.

This allows CREST to remain compatible with realist approaches to ecological systems while also taking perspectival and pragmatic representation seriously. A coarse state need not mirror a unique intrinsic partition of nature to be scientifically constrained. Conversely, the fact that a state variable is useful in one context does not authorize its unqualified reuse in another. The philosophical burden shifts from asking whether a coarse state is simply “real” to asking **what invariances and reporting rights its use commits us to**.

---

## 5. Position relative to existing adequacy and abstraction theories

<!-- PRIOR ART firewall -->
The account is intentionally cumulative. Ecological identity theory already analyzes what makes a system the same through change. Ecological model-adequacy work already asks whether state variables, controls, data, and validation are sufficient for a modelling purpose. State-and-Transition Models already connect ecological states to thresholds and intervention. POMDP and adaptive-management theory already combine hidden state, observations, actions, and model uncertainty. Causal states, bisimulation, and causal abstraction already formalize predictive or interventional coarse graining. Recent general theories of representational adequacy additionally study minimal adequate representations, certification, regime-dependent obsolescence, and repair.

<!-- POSITIONING: C35 OPEN -->
CREST should therefore not be judged by whether any one of these ingredients is new. Its potential contribution is narrower: an ecology-specific synthesis in which one proposed coarse state equivalence is subjected to four differently structured adequacy questions, each linked to a **separate recovered theorem program** and a different response to failure. Whether this exact four-contract mapping warrants a priority claim remains open; the argument does not depend on that priority.

---

## 6. Limits

The current framework is finite and theorem-guided. It does not infer the correct future grammar, source-target relation, mechanism family, evidence model, or report target from ecological data. It does not establish that the four audits exhaust all legitimate criteria for ecological representation. It does not establish a universal joint state, an audit order, or a single combined complexity measure. The exact theorems function here as conceptual benchmarks that make several hidden commitments visible; empirical adequacy still requires domain-specific modelling and evidence.

CREST is therefore best read at present as a **metatheoretical synthesis with formal anchors**, not as a completed general theory of ecology and not as a replacement for ecological identity theory, model adequacy, causal abstraction, adaptive management, or representational-adequacy theory.

---

## 7. Conclusion

<!-- INTERPRETIVE: C36 -->
When ecologists assign different configurations the same state label, the merge does scientific work. It says, implicitly or explicitly, that some differences can be ignored. The four CREST audits ask four different questions about that permission: will the ignored difference matter under the declared future; does the inherited category still mean the same thing after structural change; do retained mechanisms support the same prediction; and has the evidence actually licensed the distinction the report claims? The answer need not be the same in all four cases. **Ecological state equivalence should therefore be treated as an explicit scientific commitment rather than an invisible modelling default.**

---

## Draft-control notes

- Every central sentence above is constrained by `docs/crest_philosophy_claim_ledger_2026-08-17.md`.
- The formal proof boundary is `docs/crest_proof_recovery_2026-08-17.md`.
- Prior-art boundaries are maintained in `docs/crest_philosophy_literature_positioning_2026-08-17.md`.
- Full citations and journal-specific formatting are intentionally deferred until the argument survives another specialist literature pass.
