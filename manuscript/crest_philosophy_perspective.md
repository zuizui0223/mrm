# What Counts as the Same Ecological State?
## A Contract-Relative Account of State-Representation Adequacy

> **Development draft — 信・達・雅 controlled.** This is a philosophy-of-ecology synthesis/perspective grounded in the recovered CCOC, MLTR, MRM, and CED theorem programs. It does not claim that CREST is a fifth theorem, that the four audits are exhaustive, or that generic representational adequacy, state abstraction, ecological identity, or model transferability is new.

## Abstract

Ecology routinely compresses heterogeneous configurations into shared states used for prediction, comparison, and management. Existing work already provides mature accounts of ecosystem identity, ecological model adequacy, intervention-sensitive states, predictive state abstraction, partial observability, causal abstraction, and purpose-sensitive scientific representation. We ask a narrower question: when several ecological configurations are assigned the same coarse state, what scientific commitments are being made by that equivalence? We distinguish four adequacy questions in the current program: whether the equivalence remains sufficient under declared future operations, preserves inherited meaning after structural change, supports prediction across retained mechanism alternatives, and is licensed by the available evidence. These questions are anchored respectively by an open-future interface lower bound, a unique coarsest source-relative repair, mechanism-safe deterministic/typed/set-valued reporting, and an evidence-relative reportability criterion with a required target-safe refinement. The same coarse state can therefore fail for different reasons, and the appropriate response differs: retain additional predictive information, repair inherited semantics, preserve or resolve mechanism ambiguity, or withhold a distinction that the evidence has not earned. Contract-relative adequacy is not unrestricted relativism: once a scientific contract is declared, proposed state merges can be tested and can fail for explicit formal reasons. We present CREST as a theorem-grounded synthesis for making ecological state-equivalence commitments explicit; no claim is made that these four audits are exhaustive, commuting, jointly minimal, or the first general theory of representational adequacy.

---

## 1. From ecosystem identity to state-representation adequacy

Ecologists have long had to decide what counts as a system, a state, a regime, or a functionally equivalent configuration. Philosophy of ecology has examined the identity and continuity of ecological systems, including dynamical accounts of ecosystem identity and distinctions among different senses of ecological identity (Cumming & Collier, 2005; Collier & Cumming, 2011; Delettre, 2021). Ecological modelling has likewise developed explicit adequacy protocols (Getz et al., 2018), intervention-sensitive State-and-Transition Models (Stringham et al., 2003), adaptive-management and POMDP approaches to hidden state and model uncertainty, and methods for task-relevant state aggregation (Nicol & Chadès, 2012; Fackler & Pacifici, 2014), alongside extensive work on ecological model transferability (Yates et al., 2018). In adjacent formal fields, causal states and causal abstraction already provide mature accounts of prediction- or intervention-preserving coarse representations (Shalizi & Crutchfield, 2001; Beckers & Halpern, 2019). CREST begins from this literature rather than from the claim that ecological representation was previously treated as context-free.

A narrower commitment is nevertheless easy to leave implicit. Let a coarse state representation assign configurations \(x\in X\) to labels \(q(x)\in Q\). Whenever \(q(x)=q(y)\), the representation treats at least some differences between \(x\) and \(y\) as irrelevant to the work assigned to that label. The important question is not simply whether this is a useful simplification. It is **which differences the state variable commits us to ignoring for the scientific work assigned to it**. A state label used to summarize the present, forecast future interventions, transfer an inherited ecological classification, average over mechanism uncertainty, and support an empirical report is being asked to satisfy more than one kind of adequacy.

CREST separates four such questions in the present theorem program. **Future sufficiency** asks whether an enlarged legal future can expose a distinction that the coarse state erased. **Semantic coherence** asks whether an inherited state meaning remains operationally valid after structural replacement. **Mechanism robustness** asks whether retained response mechanisms agree on the future prediction requested from the state. **Evidential licensing** asks whether the available experiment and observation contract actually justify reporting the distinction that the prediction requires. These are not asserted to be an exhaustive taxonomy of ecological adequacy. They are kept separate because the current formalizations start from different objects, quantify over different alternatives, and return different failure certificates and remedies.

The resulting position is contract-relative without being arbitrary. Scientific representation and model evaluation are already widely understood as purpose-sensitive rather than reducible to one context-free measure of accuracy or fidelity (Giere, 2010; Parker, 2020; Bokulich & Parker, 2021), and perspectival accounts need not abandon realism (Massimi, 2022). CREST adds no priority claim here. Scientists choose which futures, inherited meanings, candidate mechanisms, observations, and targets belong to a model contract; CREST does not prove that one such contract is uniquely correct for nature. But once a contract is declared, the proposed state equivalence is no longer protected by convenience alone. A legal future can distinguish two merged configurations; a structural replacement can make an inherited label operationally incoherent; retained mechanisms can disagree on a successor; and an evidence class can contain multiple target values. Our philosophical claim is therefore modest: **ecological state equivalence should be treated as an explicit scientific commitment rather than an invisible modelling default.**

---

## 2. One state label, four different tests

Consider the coarse ecological state **pollination maintained**. Suppose two configurations currently receive this same label because both sustain adequate pollination under the present community and management repertoire. CREST does not ask whether that label is simply true or false. It asks what follows when the same label is used for different scientific purposes.

### 2.1 Future sufficiency

Two configurations can be equivalent under every supplied closed future yet require different state information once future colonization, reconnection, dispersal, or intervention possibilities are jointly opened. CCOC formalizes this as a cross-grammar compression problem: concrete legal future words can make previously dormant distinctions operationally addressable, forcing a larger exact interface. The ecological lesson is not that open systems lack macrolaws, but that **present or closed-context functional equivalence need not be sufficient for an enlarged future repertoire**.

### 2.2 Semantic coherence

After pollinator turnover, the inherited label `pollination maintained` may still be syntactically available while no longer grouping states with the same legal actions or future responses. MLTR fixes the inherited source classification rather than replacing it with an unconstrained target abstraction. If the carried classification fails exactness, its unique coarsest source-relative repair adds only the distinctions forced by the target dynamics. Historical context is retained when incompatible inherited terminal meanings themselves must be preserved. The point is not that different histories always produce different final partitions; it is that **semantic reuse imposes a constraint that ordinary target-only re-abstraction can ignore**. This is a narrower claim than ecological model transferability in general, whose limitations under novel conditions are already well established (Yates et al., 2018).

### 2.3 Mechanism robustness

The same visible pollination state can also be compatible with several retained response mechanisms. If those response types disagree about competitor removal, habitat restoration, or another declared intervention, a single deterministic forecast is not uniformly supported. MRM does not require full mechanism identity to remain in the state. It retains only response distinctions that can change the declared future behavior, and otherwise permits exact typed or set-valued reporting. **Mechanism ambiguity is therefore a predictive-state issue only where retained alternatives make different predictions under the declared action and target contract.** This is not the claim that ecology previously lacked decision frameworks combining structural and observational uncertainty; such combinations already exist in resource management and POMDP-based approaches (Fackler & Pacifici, 2014).

### 2.4 Evidential licensing

Finally, a distinction can be prediction-relevant without being one that current observations license us to report. Camera records, visitation observations, eDNA, or experiments may leave multiple target-relevant worlds compatible. CED licenses a deterministic target report exactly when the target is constant on the compatible evidence class. Its target-safe quotient describes the minimum additional resolution that would be sufficient for deterministic target tracking; it is **not** a state already identified by the present data. Evidence failure therefore calls for ambiguity-retaining reporting or a stronger evidence contract, not for silently promoting a required distinction into an observed fact. This emphasis on reportability is compatible with, rather than a replacement for, broader adequacy-for-purpose and partial-observability frameworks (Parker, 2020; Nicol & Chadès, 2012).

---

## 3. Why the failure diagnosis matters

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

This diagnosis does not yet supply a universal order for applying the audits. We have not proved that the audits commute, that their complexity measures add, that passing three implies the fourth, or that one unique globally minimal representation satisfies all four. Those are possible future synthesis questions, not premises of the present philosophical account.

---

## 4. Contract-relative does not mean arbitrary

The most natural philosophical objection is that a contract-relative account makes state identity merely conventional: choose a different purpose and obtain a different state. That conclusion does not follow. CREST concerns the adequacy of a **scientific representation**, not the claim that underlying ecological processes depend on our descriptions. The contracts specify which consequences a representation is expected to preserve. Given those commitments, failure can be objective relative to the model: two merged configurations produce different legal future traces; a carried label fails to factor target dynamics; two retained response types disagree; or one evidence class supports incompatible target values.

This allows CREST to remain compatible with realist approaches to ecological systems while also taking perspectival and pragmatic representation seriously (Giere, 2010; Massimi, 2022). A coarse state need not mirror a unique intrinsic partition of nature to be scientifically constrained. Conversely, the fact that a state variable is useful in one context does not authorize its unqualified reuse in another. The philosophical burden shifts from asking whether a coarse state is simply “real” to asking **what invariances and reporting rights its use commits us to**.

---

## 5. Position relative to existing adequacy and abstraction theories

The account is intentionally cumulative. Ecological identity theory already analyzes what makes a system the same through change (Cumming & Collier, 2005; Delettre, 2021). Ecological model-adequacy work already asks whether state variables, controls, data, and validation are sufficient for a modelling purpose (Getz et al., 2018), while general philosophy of modelling explicitly evaluates models and data for adequacy to purpose (Parker, 2020; Bokulich & Parker, 2021). State-and-Transition Models already connect ecological states to thresholds and intervention (Stringham et al., 2003). POMDP and adaptive-management theory already combine hidden state, observations, actions, and model uncertainty (Nicol & Chadès, 2012; Fackler & Pacifici, 2014). Causal states and causal abstraction already formalize predictive or interventional coarse graining (Shalizi & Crutchfield, 2001; Beckers & Halpern, 2019). Recent general theories of representational adequacy additionally study minimal adequate representations, certification, regime-dependent obsolescence, and repair (Swanson, 2026; Huang, 2026).

CREST should therefore not be judged by whether any one of these ingredients is new. Its potential contribution is narrower: an ecology-specific synthesis in which one proposed coarse state equivalence is subjected to four differently structured adequacy questions, each linked to a **separate recovered theorem program** and a different response to failure. Whether this exact four-contract mapping warrants a priority claim remains open; the argument does not depend on that priority.

---

## 6. Limits

The current framework is finite and theorem-guided. It does not infer the correct future grammar, source-target relation, mechanism family, evidence model, or report target from ecological data. It does not establish that the four audits exhaust all legitimate criteria for ecological representation. It does not establish a universal joint state, an audit order, or a single combined complexity measure. The exact theorems function here as conceptual benchmarks that make several hidden commitments visible; empirical adequacy still requires domain-specific modelling and evidence.

CREST is therefore best read at present as a **metatheoretical synthesis with formal anchors**, not as a completed general theory of ecology and not as a replacement for ecological identity theory, model adequacy, causal abstraction, adaptive management, or representational-adequacy theory.

---

## 7. Conclusion

When ecologists assign different configurations the same state label, the merge does scientific work. It says, implicitly or explicitly, that some differences can be ignored. The four CREST audits ask four different questions about that permission: will the ignored difference matter under the declared future; does the inherited category still mean the same thing after structural change; do retained mechanisms support the same prediction; and has the evidence actually licensed the distinction the report claims? The answer need not be the same in all four cases. **Ecological state equivalence should therefore be treated as an explicit scientific commitment rather than an invisible modelling default.**

---

## References

Beckers, S., & Halpern, J. Y. (2019). Abstracting Causal Models. *Proceedings of the AAAI Conference on Artificial Intelligence*, 33(01), 2678–2685. https://doi.org/10.1609/aaai.v33i01.33012678

Bokulich, A., & Parker, W. (2021). Data models, representation and adequacy-for-purpose. *European Journal for Philosophy of Science*, 11(1), Article 31. https://doi.org/10.1007/s13194-020-00345-2

Collier, J., & Cumming, G. S. (2011). A Dynamical Approach to Ecosystem Identity. In *Philosophy of Ecology*, Handbook of the Philosophy of Science, Vol. 11, pp. 201–218. Elsevier. https://doi.org/10.1016/B978-0-444-51673-2.50008-X

Cumming, G. S., & Collier, J. (2005). Change and identity in complex systems. *Ecology and Society*, 10(1), Article 29. https://doi.org/10.5751/ES-01252-100129

Delettre, O. (2021). Identity of ecological systems and the meaning of resilience. *Journal of Ecology*, 109, 3147–3156. https://doi.org/10.1111/1365-2745.13655

Fackler, P., & Pacifici, K. (2014). Addressing structural and observational uncertainty in resource management. *Journal of Environmental Management*, 133, 27–36. https://doi.org/10.1016/j.jenvman.2013.11.004

Getz, W. M., Marshall, C. R., Carlson, C. J., Giuggioli, L., Ryan, S. J., Romañach, S. S., Boettiger, C., Chamberlain, S. D., Larsen, L., D'Odorico, P., & O'Sullivan, D. (2018). Making ecological models adequate. *Ecology Letters*, 21(2), 153–166. https://doi.org/10.1111/ele.12893

Giere, R. N. (2010). An Agent-Based Conception of Models and Scientific Representation. *Synthese*, 172(2), 269–281. https://doi.org/10.1007/s11229-009-9506-z

Huang, Z. (2026). Self-Certification of Representation Adequacy: Sequential Certification at Minimum Task Loss. arXiv:2608.02267.

Massimi, M. (2022). *Perspectival Realism*. Oxford University Press.

Nicol, S., & Chadès, I. (2012). Which States Matter? An Application of an Intelligent Discretization Method to Solve a Continuous POMDP in Conservation Biology. *PLoS ONE*, 7(2), e28993. https://doi.org/10.1371/journal.pone.0028993

Parker, W. S. (2020). Model Evaluation: An Adequacy-for-Purpose View. *Philosophy of Science*, 87(3), 457–477. https://doi.org/10.1086/708691

Shalizi, C. R., & Crutchfield, J. P. (2001). Computational Mechanics: Pattern and Prediction, Structure and Simplicity. *Journal of Statistical Physics*, 104, 817–879.

Stringham, T. K., Krueger, W. C., & Shaver, P. L. (2003). State and transition modeling: An ecological process approach. *Journal of Range Management*, 56(2), 106–113. https://doi.org/10.2307/4003893

Swanson, D. T. (2026). *Carriers and Adequacy for Purpose: A Formal Framework for Representation-Constrained Adequacy*. PhilArchive manuscript, archived 21 May 2026.

Yates, K. L., Bouchet, P. J., Caley, M. J., Mengersen, K., Randin, C. F., Parnell, S., Fielding, A. H., Bamford, A. J., Ban, S., Barbosa, A. M., et al. (2018). Outstanding Challenges in the Transferability of Ecological Models. *Trends in Ecology & Evolution*, 33(10), 790–802. https://doi.org/10.1016/j.tree.2018.08.001

---

## Draft-control notes

- Every central sentence is constrained by `docs/crest_philosophy_claim_ledger_2026-08-17.md`.
- The formal proof boundary is `docs/crest_proof_recovery_2026-08-17.md`.
- Prior-art boundaries are maintained in `docs/crest_philosophy_literature_positioning_2026-08-17.md`.
- Citation selection is controlled by `docs/crest_philosophy_citation_ledger_2026-08-17.md`.
- Journal-specific formatting is intentionally deferred until journal positioning is audited.
