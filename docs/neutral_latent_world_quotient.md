# Candidate-safe quotient in neutral latent-world notation

## Neutral setup

Let `W` be a finite latent-world set. Each world has a currently observed ecological state `o(w)`. For every declared action `a`, the world has a deterministic successor world `tau_a(w)`. A requested report target is a finite-valued map `T(w)`.

The initial observation partition groups worlds with the same current observation.

## Future-action-stable target-safe refinement

Starting from the observation partition, repeatedly split worlds whenever either:

1. their report targets differ; or
2. for some declared action, their successors lie in different current blocks.

The resulting fixed point is the coarsest partition that:

- preserves current observation;
- supports a deterministic target report in every block; and
- has deterministic successor blocks under every declared action.

## Relation to MRM

For MRM, latent worlds are pairs

```text
(observable macrostate, response type).
```

The current observation forgets response type. The declared actions are candidate interventions, and the successor map is the typed transition. The report target may be the next observable state, a management response category, or the complete future-action transition row.

When the report target is the full future-action behavior, this neutral refinement is exactly the existing minimal candidate-safe quotient.

## Relation to CED

CED may supply an experiment-induced partition before future-action refinement. A noisy experiment may leave a compatible set rather than one exact record class. MRM then answers whether the requested target is constant across the retained response possibilities and, if not, which declared intervention can refine the mechanism-relative ambiguity.

A valid bridge is therefore:

```text
latent worlds
  -> CED experiment / evidence classes
  -> reliability-qualified compatible worlds
  -> MRM future-action-stable target-safe refinement
  -> deterministic or ambiguity-explicit report.
```

This is a **composition of distinct audits**, not a claim that CED and MRM define one quotient theorem. CED equivalence is record/evidence-relative; MRM refinement is future-response/target-relative. Their current manuscripts should remain separable even when one finite example uses both layers.

See `contract_relative_ecological_state_theory.md` for the broader program-level distinction among future, inherited-semantic, mechanism, and evidence contracts.

## Minimality proof

Let `P0` be the current observation or experiment-induced partition. Let `F` split blocks by target value and successor block under every declared action.

The sequence `P0, F(P0), F^2(P0), ...` stabilizes because `W` is finite. Its fixed point is target-constant and action-stable.

Any deterministic interface preserving `P0`, supporting the target report, and having deterministic action successors must separate every split introduced by `F`. By induction it refines every iterate and therefore refines the fixed point. The fixed point is the unique coarsest target-safe deterministic quotient.

## Target resolution rather than full mechanism identification

The active objective should be to reach a class on which `T` is constant, not necessarily a singleton latent world. Response types that remain behaviorally different but induce the same requested management report need not be identified.

This distinction is essential for the cross-repository bridge: experimental effort is justified by report resolution, not by mechanism labeling for its own sake.
