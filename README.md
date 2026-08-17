# MRM — Mechanism-Robust Macro-Laws

MRM is a theorem-first mathematical-ecology repository for one uncertainty
question:

> When multiple retained mechanisms support compact exact instance laws but
> disagree about future macro transitions, what is the strongest law that can be
> reported without pretending the mechanism uncertainty has vanished?

MRM is the standalone successor of CCOC legacy `ID-2` and `ID-3`. CCOC now retains
its own independent open-future theorem program and also preserves the historical
provenance from which the MRM mechanism-uncertainty core was separated.

## Executable theorem and design surface

1. **Universal deterministic law.** A candidate-independent macro-law exists
   exactly when all retained candidates induce the same transition maps.
2. **Typed or set-valued law.** When candidates disagree, retaining response type
   yields a deterministic law; omitting it yields the exact set-valued successor
   relation rather than one unsupported deterministic law.
3. **Candidate-safe product lower bound.** Under uniform response separation, an
   exact typed law needs at least the observable macrostate information plus the
   response-type information.
4. **Joint uncertainty.** Exterior completion and mechanism uncertainty add only
   when the full joint product is operationally separable under the declared
   grammar.
5. **Minimal candidate-safe quotient.** Without uniform separation, response type
   can be locally irrelevant. The coarsest observation-preserving deterministic
   quotient retains exactly the type information that future declared actions can
   expose.
6. **Active discrimination.** From a current macrostate, a finite adaptive action
   tree either identifies response type with the fewest worst-case interventions or
   certifies that the declared grammar cannot separate it.
7. **Mechanism-ambiguity frontier.** A canonical family with \(2^m\) response
   types has a two-state fixed-candidate law but requires \(2^{m+1}\) states for
   an exact candidate-safe law: state cardinality grows exponentially in the
   unresolved binary response dimensions, while the memory surcharge is exactly
   \(m\) bits and \(m\) binary probes are necessary and sufficient for identification.
8. **Cost-aware discrimination.** When declared actions have positive costs, the
   exact design target is the minimum worst-case total cost, not necessarily the
   fewest interventions. A costly one-shot probe can be dominated by a longer,
   cheaper adaptive sequence.
9. **Robust observation update.** With bounded observation error, an observed
   successor eliminates only response types whose predicted successor is outside
   the declared compatible true-state set. Ambiguous or noisy observations keep a
   set-valued report rather than falsely identifying a mechanism.
10. **Probabilistic observation update.** With declared likelihoods and priors,
    an observation produces posterior response-type weights, entropy, credible
    sets, and thresholded resolution checks rather than silently treating the MAP
    mechanism as certain.
11. **Value-of-information design.** Before choosing an action, declared priors,
    likelihoods, and costs can score each one-step intervention by expected entropy
    reduction, net information value, and probability of crossing a resolution
    threshold.

CREST hierarchy is narrower than this executable inventory. The publication identity is
**honest prediction under unresolved mechanism ambiguity**: universal/typed/set-valued
reporting, minimal candidate-safe state, the ambiguity frontier, and target-relevant
discrimination. The product/joint bounds and cost-aware planner are supporting
mechanism results. Items 9–11 are conditional observation/design adapters and do not
make MRM the owner of the broader evidence, failure, calibration, or risk-contract
layer.

## Ecological reading

Different retained mechanisms can represent alternative pollination responses,
disturbance effects, pathogen pathways, colonization dynamics, or management
responses. They may agree on the current visible community but disagree about
what a future intervention does. MRM formalizes when one deterministic ecological
macro-law is justified, when a mechanism type must be retained, when only part of
that type information is needed at a state, when finite interventions can identify
it at an explicitly declared cost, how bounded or probabilistic observation error
changes the retained type set, which next action is expected to reduce ambiguity,
and when a set-valued or posterior-ambiguous forecast is the honest output.

## Program-level synthesis: contract-relative ecological state

MRM maintains the canonical program-level synthesis
[Contract-Relative Ecological State Theory (CREST)](docs/contract_relative_ecological_state_theory.md).

The upper principle is that ecological state identity is not intrinsic to the
present visible configuration. It is indexed by distinct declared contracts:

- **CCOC / future sufficiency:** which distinctions can matter under future composition / action;
- **MLTR / semantic coherence:** which distinctions must preserve inherited meaning across structural change;
- **MRM / mechanism robustness:** which distinctions must remain because retained mechanisms disagree about future response;
- **CED / evidential licensing:** which distinctions finite evidence can legitimately resolve and report.

CREST is a program-level architecture, not a claim that the four repositories share
one quotient theorem or should be merged. The audits are logically distinct and no
universal order or commutation theorem is currently claimed.

A shared finite refinement lemma can appear in more than one repository without
becoming duplicate novelty. In particular, CED's target-safe refinement begins from
an evidence-induced class, while MRM's candidate-safe quotient specializes the
latent worlds to observable-state × response-type worlds. The neutral refinement
machinery is common substrate; the indexed uncertainty and scientific output are
different.

MRM remains responsible for mechanism-robust reporting and candidate-safe state.
Its observation-update and VOI modules are conditional adapters around that target;
they do not replace CED's broader finite-evidence and risk-contract theory.

## Provenance

The initial standalone core is reconstructed from the historical CCOC source at
`zuizui0223/ccoc`, especially:

- `docs/candidate_safe_universal_laws.md`; and
- `docs/joint_open_candidate_laws.md`.

The migration keeps mechanism uncertainty separate from CCOC's open-composition
paper and from MLTR's non-nested replacement theory.

## Verification and manuscript planning

- [Contract-relative ecological state synthesis](docs/contract_relative_ecological_state_theory.md)
  — canonical program-level relation among CCOC, MLTR, MRM, and CED, with explicit
  claim firewalls and future synthesis questions.
- [CREST final cross-repository validation](docs/crest_final_validation_2026-08-17.md)
  — dated integration audit across the four repository baselines and the shared
  substrate/ownership checks.
- [Manuscript skeleton](docs/manuscript_skeleton.md) — paper title, abstract
  skeleton, theorem placement, figure plan, supplement structure, and submission
  checklist.
- [Standalone verification audit](docs/standalone_verification_audit.md) —
  source-to-successor mapping, replay boundary, and added invariants.
- [Minimal quotient and active discrimination](docs/minimal_quotient_active_discrimination.md)
  — finite theorem statements, witnesses, and boundaries.
- [Mechanism-ambiguity complexity frontier](docs/mechanism_ambiguity_frontier.md)
  — exact state-cardinality, memory-surcharge, and intervention-depth witness.
- [Cost-aware active discrimination](docs/cost_aware_active_discrimination.md)
  — exact positive-cost dynamic program and cost-versus-length witness.
- [Robust observation update](docs/robust_observation_update.md) — bounded-error
  support updates and conservative set-valued continuation.
- [Probabilistic observation update](docs/probabilistic_observation_update.md) —
  posterior response-type weights, entropy, credible sets, and thresholded
  resolution checks.
- [Value-of-information design](docs/value_of_information_design.md) — one-step
  expected entropy reduction, net information value, and threshold-crossing
  probability.
- `pytest` checks candidate quotient behavior, finite witnesses, response-type
  invariants, minimal quotient behavior, active discrimination, frontier scaling,
  cost-aware planning, robust and probabilistic observation updates, VOI scoring,
  and replay-report values.
- `scripts/verify_mrm_core.py` writes a deterministic JSON artifact.

## Run

```bash
python -m pip install -e '.[dev]'
pytest
python scripts/verify_mrm_core.py
```

The replay writes `artifacts/mrm_core_report.json`.

## Scope

MRM concerns declared finite candidate families with a common observable
macrostate space, exact, bounded-support, or probabilistic macrostate observations,
and declared action grammar, priors, likelihoods, and action costs. It does not
infer candidate sets, mechanisms, response types, state alignments,
observation-error supports, likelihoods, priors, action costs, or ecological
validation from data, or treat stochastic mechanism transitions, full sequential
risk-weighted design, or hard-budget intervention design.
