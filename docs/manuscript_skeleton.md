# Manuscript architecture — Mechanism-Robust Macro-Laws

## Working title

**How many interventions does unresolved mechanism ambiguity cost? Exact state and experiment frontiers for ecological macro-laws**

Alternative:

**Mechanism ambiguity has an exact experimental price: state memory and intervention depth in ecological macro-laws**

## One-sentence thesis

When several retained mechanisms agree on the visible present state but encode `m` unresolved binary response dimensions, an honest deterministic macro-law must retain exactly `m` additional bits in the canonical frontier family, and exact mechanism identification requires exactly `m` binary interventions in the worst case.

## Paper identity

MRM is a finite mathematical-ecology paper about the **price of unresolved response mechanism**. It is not an empirical mechanism-selection pipeline, a Bayesian model-selection paper, or a general active-learning paper.

The manuscript should be organized around the paired canonical frontier proved in `docs/mrm_core_proofs.md`:

- **Theorem 7 — exact memory frontier:** `2^(m+1)` candidate-safe states, `m+1` bits, hence an exact `m`-bit surcharge relative to a fixed two-state law;
- **Theorem 8 — exact intervention frontier:** exactly `m` binary probes are necessary and sufficient in the worst case to identify one of `2^m` response signatures.

Theorem 8 is the manuscript center. The surrounding results explain why the experimental lower bound is scientifically relevant and when it applies.

## Core question

> If current ecological state is known but the response mechanism is not, how much additional state information must an honest predictive law retain, and how many interventions are fundamentally required to resolve the ambiguity?

This is sharper than the generic statement that mechanism uncertainty matters. The paper returns exact finite burdens under a declared mechanism family and action grammar.

## Abstract spine

1. Ecological mechanisms can be observationally indistinguishable in the present yet predict different responses to intervention.
2. A deterministic candidate-forgetting macro-law is justified only when retained response types agree; otherwise prediction must retain response-relevant type information or remain set-valued.
3. The unique coarsest candidate-safe quotient retains only mechanism distinctions that can change declared future observations.
4. In the canonical `m`-bit response family, unresolved mechanism ambiguity imposes an exact `m`-bit state-memory surcharge and an exact `m`-intervention identification burden. These two quantities are attained by the same transparent family.
5. General finite dynamic programming extends the intervention result beyond the canonical family to shortest and minimum-cost exact discrimination when such a policy exists.
6. Observation-error, posterior, and one-step value-of-information modules are downstream adapters and are not part of the headline theorem claim.

## Main theorem architecture

### Result 1 — Honest reporting under mechanism disagreement

Use Theorem 1 and Proposition 2 from `docs/mrm_core_proofs.md`.

A candidate-independent deterministic macro-law exists exactly when retained response types agree on all declared transition maps. When they disagree:

- retaining response type gives a deterministic typed law;
- forgetting type gives the exact set-valued successor relation.

This result establishes why mechanism ambiguity cannot simply be omitted from the state description.

### Result 2 — What mechanism distinctions must the state remember?

Use Theorem 5 and Corollary 5.1.

The minimal candidate-safe quotient is the unique coarsest observation-preserving deterministic quotient of observable-state × response-type worlds. Two typed states can be merged exactly when all finite declared action words yield the same observed trajectories.

This prevents the paper from equating honest prediction with full mechanism identity: only response-relevant distinctions survive.

### Result 3 — Exact ambiguity burden in state space

Use Theorem 7.

For the canonical family `R_m = {0,1}^m`, each fixed mechanism has a two-state observable macro-law, but the minimal candidate-safe law has

`2^(m+1)` states and `m+1` bits.

Relative to a fixed-candidate law, the exact information surcharge is `m` bits.

Report the two scales separately:

- state cardinality grows exponentially in `m`;
- required memory in bits grows linearly in `m`.

### Result 4 — Theorem 8: exact intervention frontier

This is the headline result.

For the same canonical family, exactly `m` binary probes are necessary and sufficient in the worst case to identify one of the `2^m` response signatures.

**Upper bound:** probe each response coordinate once.

**Lower bound:** a depth-`d` binary intervention tree has at most `2^d` leaves. Exact discrimination among `2^m` response types therefore requires `d >= m`.

After `k` distinct probes, exactly `2^(m-k)` signatures remain compatible. This gives an exact ambiguity-removal trajectory, not only an endpoint bound.

The ecological interpretation is deliberately narrow: if the declared mechanism uncertainty contains `m` independently response-relevant binary distinctions and each declared probe reveals at most one binary outcome, no adaptive cleverness can beat the `m`-intervention worst-case bound.

### Result 5 — Beyond the canonical family: shortest exact discrimination

Use Theorem 6.

Dynamic programming over configurations `(q,S)` returns the minimum worst-case intervention depth for any finite declared response family, or `None` exactly when no finite exact discrimination policy exists.

Theorem 8 should be presented first as the sharp closed-form frontier; Theorem 6 then shows that the same question is executable for arbitrary finite families.

### Result 6 — Unequal intervention costs

Use Theorem 9.

With strictly positive declared action costs, finite Bellman recursion returns the minimum worst-case total cost. Unit costs recover the shortest-depth problem.

This belongs after Theorem 8 because it relaxes equal intervention cost, not because it is a stronger headline theorem.

## Supporting results and placement

### Product lower bound — Theorem 3

Keep as a short lemma/corollary supporting Result 3. Under uniform response separation, the full typed product is minimal.

### Joint exterior × mechanism bound — Proposition 4

Supplement only. It requires an explicit joint operational-separation premise and should not distract from the mechanism-only paper.

### Robust observation update

Methods/Supplement adapter. Bounded observation support filters compatible response types but does not alter the mechanism-report target.

### Probabilistic posterior update

Methods/Supplement adapter. Bayesian weights may favor one response type but do not convert posterior preference into exact mechanism resolution.

**Do not call this Theorem 8 in the manuscript.** The canonical analytic numbering in `docs/mrm_core_proofs.md` is authoritative: Theorem 8 is the exact intervention frontier.

### One-step value of information

Discussion/Methods adapter. It may help choose among observations under a declared prior/likelihood/cost model, but it is neither the proof nor the generalization of the exact intervention frontier.

## Main narrative order

1. **Same present, different intervention response.** Motivate response-mechanism ambiguity.
2. **What can be reported honestly?** Universal versus typed versus set-valued law.
3. **What must the state remember?** Minimal candidate-safe quotient.
4. **How large can the burden become?** Theorem 7 memory frontier.
5. **How many interventions are unavoidable?** Theorem 8 intervention frontier — manuscript peak.
6. **Can arbitrary finite families be solved?** Shortest and cost-aware discrimination.
7. **What changes under noisy evidence?** Observation/posterior/VOI adapters, explicitly downstream.
8. **Discussion.** Mechanism uncertainty has both a representational and an experimental price.

## Suggested figures

### Figure 1 — Same observed state, different responses

Two or more retained response types share current `q` but map one intervention to different successors. End with the reporting fork: deterministic if agreement, typed/set-valued if disagreement.

### Figure 2 — Minimal candidate-safe quotient

Show the full `Q × R` product and a smaller quotient in which response-type distinctions irrelevant to every declared future word are merged.

### Figure 3 — Paired ambiguity frontiers

This should be the visual center of the paper.

Panel A: `m` versus candidate-safe state count `2^(m+1)` and memory `m+1` bits.

Panel B: `m` versus minimum worst-case intervention depth `m`.

Panel C or inset: after `k` distinct probes, residual compatible response types `2^(m-k)`.

The visual message is not “everything is exponential.” State cardinality is exponential, whereas memory surcharge and intervention depth are linear.

### Figure 4 — Adaptive discrimination outside the canonical family

A small decision tree showing a family where different first actions yield different worst-case depths. Use the verified generic planner output.

### Figure 5 — Cost changes the preferred exact plan

Show shortest-depth versus minimum-cost exact discrimination under unequal positive action costs.

Posterior/VOI figures are optional Supplement material unless they materially improve the final journal fit.

## Ecological interpretation

Use one recurring hypothetical ecological system rather than a catalogue. A good form is:

- current macrostate: one observed community or habitat state;
- retained mechanisms: alternative limiting pathways that make identical present-state predictions;
- interventions: manipulations that separately expose response coordinates;
- target: future macrostate response, not historical mechanism identity for its own sake.

Pollinator limitation, restoration response, or disturbance-response mechanisms are suitable examples only if described as finite declared candidate models, not empirical validation.

## Novelty boundary

Do not claim novelty for:

- finite-state minimization or partition refinement;
- deterministic decision trees or the binary leaf-counting lower bound;
- active learning in general;
- Bayesian updating;
- value of information;
- generic dynamic programming.

The contribution is the ecology-specific coupling:

`retained mechanism family -> honest macro-law -> minimal response-relevant state -> exact state-memory burden -> exact intervention burden`.

## Journal decision after reorganization

Evaluate journal fit only after this architecture is implemented and a full manuscript exists.

Likely fits:

- **Theoretical Ecology** if the ecological interpretation and general finite theorem package carry the paper;
- **Journal of Theoretical Biology** if the emphasis is finite mathematical structure and mechanism-response discrimination;
- **Ecological Modelling** if implementation and model-comparison workflow dominate.

A methods journal is less natural unless the observation/experimental-design implementation becomes the primary contribution.

## Development freeze

Do not add a new theorem family by default. Remaining work is:

1. synchronize README and publication controls with the Theorem 7/8 center;
2. add manuscript-story regression tests so Theorem 8 cannot again be renamed as posterior updating;
3. strengthen the canonical frontier executable oracle beyond widths one through five if useful;
4. create one integrated manuscript draft and figures;
5. run a nearest-neighbour literature audit for ecological mechanism uncertainty, model discrimination, active experiment design, automata/minimal-state results, and decision-tree lower bounds;
6. choose the journal only after that audit.

## Submission gate

The paper is not submission-ready merely because the theorem suite is green. Submission requires:

- a manuscript centered on Theorems 7–8;
- consistent theorem numbering with the analytic proof spine;
- an ecological worked interpretation;
- primary-source literature boundaries;
- figures generated from deterministic theorem witnesses where quantitative;
- an explicit non-empirical scope statement;
- full CI/replay consistency at the submission commit.
