# MRM — Mechanism-Robust Macro-Laws

MRM is a theorem-first mathematical-ecology repository for one uncertainty
question:

> When multiple retained mechanisms support compact exact instance laws but
> disagree about future macro transitions, what is the strongest law that can be
> reported without pretending the mechanism uncertainty has vanished?

MRM is the standalone successor of CCOC legacy `ID-2` and `ID-3`. CCOC remains
frozen provenance; this repository contains the active mechanism-uncertainty
core.

## Theorem core

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

## Ecological reading

Different retained mechanisms can represent alternative pollination responses,
disturbance effects, pathogen pathways, colonization dynamics, or management
responses. They may agree on the current visible community but disagree about
what a future intervention does. MRM formalizes when one deterministic ecological
macro-law is justified, when a mechanism type must be retained, when only part of
that type information is needed at a state, when finite interventions can identify
it at an explicitly declared cost, and when a set-valued forecast is the honest
output.

## Provenance

The initial standalone core is reconstructed from the frozen CCOC legacy source
at `zuizui0223/ccoc`, especially:

- `docs/candidate_safe_universal_laws.md`; and
- `docs/joint_open_candidate_laws.md`.

The migration keeps mechanism uncertainty separate from CCOC's open-composition
paper and from MLTR's non-nested replacement theory.

## Verification

- [Standalone verification audit](docs/standalone_verification_audit.md) —
  source-to-successor mapping, replay boundary, and added invariants.
- [Minimal quotient and active discrimination](docs/minimal_quotient_active_discrimination.md)
  — finite theorem statements, witnesses, and boundaries.
- [Mechanism-ambiguity complexity frontier](docs/mechanism_ambiguity_frontier.md)
  — exact state-cardinality, memory-surcharge, and intervention-depth witness.
- [Cost-aware active discrimination](docs/cost_aware_active_discrimination.md)
  — exact positive-cost dynamic program and cost-versus-length witness.
- `pytest` checks candidate quotient behavior, finite witnesses, response-type
  invariants, minimal quotient behavior, active discrimination, frontier scaling,
  cost-aware planning, and replay-report values.
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
macrostate space, exact macrostate observations, and declared action grammar and
positive action costs. It does not infer candidate sets, mechanisms, response
types, state alignments, action costs, or ecological validation from data, or treat
noisy, stochastic, risk-weighted, or budget-limited intervention design.
