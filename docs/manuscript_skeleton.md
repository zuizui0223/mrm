# Manuscript skeleton — Mechanism-Robust Macro-Laws

## Working title

**Mechanism-Robust Macro-Laws: honest ecological prediction under unresolved mechanism ambiguity**

## One-sentence claim

When multiple retained mechanisms imply different future macro-transitions, the
honest macro-law is not the most convenient deterministic candidate law, but one of
four explicitly justified reports: universal deterministic, typed deterministic,
minimal candidate-safe quotient, or set-valued / posterior-ambiguous forecast.

## Target paper type

A theory-first methods paper with executable finite witnesses. The repository is
not positioned as an empirical inference pipeline. It is a reporting and experiment
design calculus for declared finite candidate mechanism families.

## Abstract skeleton

Ecological macro-laws are often reported as if the mechanism responsible for a
pattern has already been resolved. Yet several retained mechanisms can agree on the
current macrostate while disagreeing about the effect of future interventions. We
formalize this problem using finite candidate macro-transition tables over a common
observable macrostate space. We prove a report trichotomy: if all retained
mechanisms induce the same transition maps, a universal deterministic law is
justified; if not, response type must be retained for deterministic prediction, or
the candidate-forgetting forecast must be set-valued. We then construct the minimal
candidate-safe quotient, showing exactly which response-type distinctions must be
kept at each macrostate. We extend the framework to active discrimination, action
costs, bounded observation error, probabilistic observation, and one-step
value-of-information scoring. Canonical witnesses show that unresolved binary
mechanism ambiguity can impose exponential state-cardinality growth while adding a
linear memory surcharge in bits, and that maximum information and maximum net
experimental value need not select the same intervention. The framework gives a
transparent standard for when deterministic ecological macro-laws may be reported,
when uncertainty must remain explicit, and which observations are worth collecting
next.

## Main narrative arc

### 1. Problem: deterministic macro-laws can smuggle in mechanism certainty

Start from the ecological situation, not the code. A visible community state can be
shared by multiple plausible mechanisms. A deterministic macro-law that forgets this
ambiguity is valid only if all retained mechanisms agree about every declared future
action. Otherwise, the forecast must either retain mechanism-response information or
be set-valued.

Core message: the problem is not stochasticity first; it is unjustified candidate
forgetting.

### 2. Finite setup and response types

Define:

- observable macrostate space \(Q\);
- declared actions \(A\);
- retained candidate mechanisms \(C\);
- induced maps \(G_a^\theta:Q\to Q\);
- response types as equivalence classes of candidates with identical full transition
  tables.

Explain that response type, not raw mechanism label, is the predictive unit.
Duplicate mechanisms with equal transition tables collapse.

### 3. Report trichotomy

Main-text theorem package:

- **Theorem 1 — Universal law criterion.** A candidate-independent deterministic
  law exists iff all retained response types induce identical maps.
- **Corollary 1 — Typed deterministic report.** If response type is retained,
  prediction is deterministic on \(Q\times R\).
- **Corollary 2 — Candidate-forgetting report.** If response type is omitted under
  disagreement, the honest forecast is the exact set-valued successor relation.

This is the conceptual core of the paper and should appear early.

### 4. Memory burden and minimal candidate-safe quotient

Main-text theorem package:

- **Theorem 2 — Product lower bound under uniform response separation.** If every
  pair of response types can be separated from every macrostate by a declared
  action, any exact typed deterministic interface needs \(|Q|R\) states.
- **Theorem 3 — Minimal candidate-safe quotient.** Partition refinement over
  \(Q\times R\), constrained to preserve observed \(q\), gives the coarsest exact
  observation-preserving deterministic interface.

Emphasize why the quotient is important: the full typed product can be too
pessimistic because some response-type distinctions are locally irrelevant.

### 5. Mechanism-ambiguity frontier

Main-text theorem package:

- **Theorem 4 — Canonical ambiguity frontier.** With \(m\) unresolved binary
  response dimensions, fixed-candidate laws have two observable states, but the
  candidate-safe interface has \(2^{m+1}\) states and \(m+1\) bits.
- **Corollary — Active identification lower bound.** \(m\) binary probes are
  necessary and sufficient to identify \(2^m\) response types.

This is the paper's sharp “why this matters” result. Say carefully:
state cardinality grows exponentially in unresolved binary response dimensions;
memory surcharge in bits grows linearly.

### 6. Active and cost-aware discrimination

Main-text methods/results package:

- **Theorem 5 — Shortest exact active discrimination.** Dynamic programming over
  \(Q\times\{S:\varnothing\ne S\subseteq R\}\) returns the minimum worst-case
  intervention depth, or no plan.
- **Theorem 6 — Minimum-cost exact active discrimination.** With positive action
  costs, the same finite configuration space gives the minimum worst-case total
  intervention cost.

Use the cost witness as the main figure or table: a one-step direct probe can be
shortest but not cheapest.

### 7. Observation error and posterior ambiguity

Keep as a main-text extension, not the opening theorem.

- **Theorem 7 — Robust support update.** With bounded observation support \(N(x)\),
  retain exactly response types whose predicted successor lies in \(N(x)\).
- **Theorem 8 — Probabilistic posterior update.** With likelihoods and priors,
  update response-type weights by Bayes' rule; MAP is not certainty.

Use this to show that MRM remains conservative under noisy observation: noisy data
can favor a mechanism without licensing a deterministic mechanism-resolved law.

### 8. One-step value-of-information design

Main-text design diagnostic, not full sequential policy.

- **Theorem 9 — Expected ambiguity reduction.** Score each action by expected
  posterior entropy reduction.
- **Corollary — Cost-adjusted design.** Raw information and net information value
  can select different actions.

This gives an applied bridge: what should we measure next, given declared
mechanism uncertainty?

### 9. Scope and non-claims

Make these explicit in the main text, not hidden in supplement:

- MRM does not infer mechanisms, candidate sets, priors, likelihoods, costs, or
  ecological validity from data.
- MRM assumes a declared common observable macrostate space.
- Most implemented results are finite, exact, and one-step where stated.
- VOI is one-step, not full sequential dynamic programming.
- Probabilistic observation is not stochastic mechanism dynamics.

## Result placement map

| Current result | Manuscript placement | Reason |
|---|---|---|
| Universal deterministic criterion | Main theorem 1 | central conceptual result |
| Typed / set-valued report | Main theorem 1 corollaries | defines honest reporting alternatives |
| Candidate-safe product lower bound | Main theorem 2 | memory-burden baseline |
| Joint exterior-mechanism uncertainty | Supplement or appendix | useful but secondary to core mechanism ambiguity |
| Minimal candidate-safe quotient | Main theorem 3 | strongest compression result |
| Active discrimination depth | Main theorem 5 | connects reporting to intervention |
| Mechanism-ambiguity frontier | Main theorem 4 | sharp headline complexity result |
| Cost-aware discrimination | Main theorem 6 | practical experimental burden |
| Robust support update | Main theorem 7 | observation-error guardrail |
| Probabilistic posterior update | Main theorem 8 | posterior ambiguity guardrail |
| One-step VOI design | Main theorem 9 | next-observation design bridge |

## Suggested figures

### Figure 1 — Report trichotomy

A flow diagram:

1. retained mechanisms;
2. collapse to response types;
3. do all response types agree?;
4. if yes, universal deterministic law;
5. if no, typed deterministic or set-valued forecast.

### Figure 2 — Minimal quotient versus full product

Show \(Q\times R\) full typed product and a quotient that merges locally irrelevant
response-type distinctions while preserving observed macrostates.

### Figure 3 — Ambiguity frontier

Plot \(m\) versus candidate-safe state cardinality \(2^{m+1}\), and optionally a
second panel for bits \(m+1\). The caption must avoid overclaiming: exponential in
state cardinality, linear in bits.

### Figure 4 — Cost versus information

A small table or bar chart:

| Action | Raw EIG | Cost | Net value | Selected by |
|---|---:|---:|---:|---|
| perfect | 2 | 3 | -1 | raw EIG |
| half_split | 1 | 0.25 | 0.75 | net value |
| uninformative | 0 | 0 | 0 | neither |

### Figure 5 — Observation uncertainty ladder

Exact observation → bounded-support robust update → probabilistic posterior update
→ VOI design.

## Paper section outline

1. Introduction
   - mechanism ambiguity in ecological macro-laws;
   - why deterministic laws require agreement across retained mechanisms;
   - overview of MRM report discipline.
2. Finite candidate macro-law framework
   - states, actions, candidates, response types;
   - report types.
3. Universal, typed, and set-valued macro-laws
   - theorem 1 and corollaries;
   - examples.
4. Candidate-safe memory and quotient structure
   - lower bound;
   - minimal quotient;
   - ambiguity frontier.
5. Active discrimination and experimental burden
   - shortest plans;
   - cost-aware plans.
6. Observation error and posterior ambiguity
   - robust support update;
   - posterior update;
   - thresholded resolution.
7. One-step value-of-information design
   - expected entropy reduction;
   - net value;
   - design witness.
8. Discussion
   - ecological interpretation;
   - how to use MRM with empirical candidate mechanisms;
   - non-claims and future extensions.

## Minimal empirical/ecological examples to mention

Use examples as motivating scenarios, not as claimed validated case studies:

- alternative pollinator-response mechanisms causing different effects of floral
  trait manipulation;
- disturbance mechanisms that agree under passive observation but disagree under
  management intervention;
- pathogen or mutualist pathways that share a current community state but predict
  different responses to removal/addition experiments;
- island systems where reduced interaction complexity may make several mechanisms
  plausible but not yet resolved.

## Supplement structure

1. Full finite definitions and notation.
2. Proofs of all theorem statements.
3. Exhaustive quotient checks and finite witnesses.
4. Replay artifact schema and reproducibility protocol.
5. Boundary cases and non-claims.
6. Relation to CCOC and MLTR provenance.

## Submission-readiness checklist

- [ ] Decide target journal type: theoretical ecology, ecological methods, or
      mathematical biology.
- [ ] Convert theorem program into formal notation with consistent symbols.
- [ ] Write proof sketches for all main theorems and move full proofs to supplement.
- [ ] Generate figures 1–5 from replay outputs or hand-checkable finite examples.
- [ ] Add one ecological worked example using declared candidate mechanisms.
- [ ] Keep all data-inference language out of theorems unless a separate inference
      layer is added.
- [ ] Cite automata minimization, set-valued prediction, active learning / decision
      trees, and value-of-information literature in the manuscript text.

## Current maturity assessment

The mathematical core is now strong enough for a manuscript outline. The repository
already contains executable witnesses for the main claims. What remains before a
paper draft is not another theorem by default, but prose discipline: tightening the
story, choosing notation, drawing figures, and writing proofs in a way that does not
oversell empirical inference.
