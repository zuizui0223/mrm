# CREST cross-repository final validation — 2026-08-17

## Status

This is a dated program-integration audit, not a new theorem. It verifies that the four repositories can be read as one Contract-Relative Ecological State Theory (CREST) program without collapsing their distinct quantifier orders, theorem outputs, or publication identities.

Audited main baselines before the final documentation synchronization:

- CCOC: `b4cdb994a0fb0eb7d1d5be410a267ea983287281`
- MLTR: `dc64cdfb29940d93072a586e48d55650496b4a5c`
- MRM: `4b7a38ed48d72286ae3694d6a9dae251aa539002`
- CED: `3ba95c0ac29f4c27248261b76f38b1dfa821766a`

The synchronization pass changes program-facing documentation only. It does not change theorem implementations, numerical witnesses, or empirical claims.

## 1. One upper principle, four audits

CREST uses the program-level contract notation

\[
\mathcal C=(\Gamma,\mathcal H,\Theta,D;T),
\]

with future grammar \(\Gamma\), inherited-semantic contract \(\mathcal H\), retained mechanism family \(\Theta\), evidence contract \(D\), and report/decision target \(T\).

The four repositories answer different questions about a proposed ecological state:

| Audit | Repository | Fixed / varied object | Characteristic failure | Core output |
|---|---|---|---|---|
| future sufficiency | CCOC | compare independently minimized closed interfaces with a jointly open future grammar | future insufficiency | exact open-interface lower bound + sharpness |
| semantic coherence | MLTR | fix one inherited source law and source–target relation | semantic non-portability | unchanged transport or unique coarsest source-relative repair |
| mechanism robustness | MRM | retain a family of candidate response laws on a common observed macrospace | mechanism non-robustness | deterministic/typed/set-valued report + minimal candidate-safe state |
| evidential licensing | CED | condition on a finite experiment/observation/failure/risk contract | evidential non-resolvability | compatible-world report, trustworthy target-safe refinement, risk-limited design |

Compact program rule:

> Remember distinctions that future operations can expose; preserve distinctions required by inherited meaning; retain mechanism distinctions that change requested predictions; and report only distinctions licensed by the evidence contract.

Passing one audit does not imply passing the other three.

## 2. Quantifier and ownership checks

### CCOC versus MLTR

Validated distinction:

- CCOC independently optimizes exact interfaces under each closed grammar and then compares them with the minimum under a jointly open grammar.
- MLTR fixes one inherited source partition first, carries it through structural change, and constrains every admissible target repair to refine the carried labels.

Therefore CCOC lower-bound inflation is not MLTR transport defect, and MLTR coarsest repair is not a CCOC open-future minimum.

### MRM versus CED

Validated distinction:

- CED equivalence begins from records or reliability-qualified compatible worlds under an evidence contract.
- MRM equivalence begins from retained response mechanisms and asks which mechanism distinctions change future target behavior.

A valid composition is directional but not mandatory:

```text
CED evidence class
  -> retained compatible worlds / response types
  -> MRM target agreement or candidate-safe refinement
  -> deterministic or ambiguity-explicit report
```

MRM observation/posterior/VOI modules are adapters around the mechanism-report target; CED remains owner of the broader finite-evidence, detection-failure, calibration, and risk-contract layer.

### Shared neutral refinement substrate

The finite target/action-stable refinement lemma is common substrate, not duplicate novelty.

- In CED, the initial partition is induced by evidence/records and the scientific question is target-safe reportability under observation reliability.
- In MRM, latent worlds specialize to `(observable macrostate, response type)` and the scientific question is mechanism-safe prediction under retained response ambiguity.

Both repositories explicitly avoid claiming generic partition refinement as new.

## 3. No universal audit order is claimed

CREST is a four-audit architecture, not a proved sequential pipeline.

A particular ecological analysis may apply CED before MRM, MLTR before CED, or another order depending on what is declared first. The present program does **not** claim that these audits commute or that intersecting their partitions automatically yields a unique globally minimal state.

A future synthesis theorem must prove a genuinely new coupling such as noncommutation, joint minimality, or impossibility. Merely composing existing quotients or adding existing bit bounds does not qualify.

## 4. Manuscript-routing consequences

The current repository-level publication identities remain distinct:

- **CCOC:** open-future exact-interface obstruction and bounded-local sharpness.
- **MLTR:** inherited-law transport, unique coarsest source-relative repair, defect, and history.
- **MRM:** honest prediction under unresolved mechanism ambiguity and minimal mechanism-relative state.
- **CED:** finite ecological reportability under evidence, failure, target, and risk contracts.

Cross-contract applications are allowed, but a companion layer must be labeled as an adapter/application unless a new coupling theorem is actually proved.

In particular, an MLTR-generated obstruction set may define what a monitoring system would need to distinguish, but generic sensor selection, set cover, detection failure, or risk-limited evidence is CED territory rather than a new MLTR theorem.

## 5. Final documentation synchronization required by this audit

The audit found no missing fifth scientific axis, but it found four documentation-generation mismatches:

1. CCOC already used CREST as a routing rule but lacked a direct link to the canonical four-audit synthesis.
2. MLTR had the correct CCOC quantifier firewall but still described CCOC mainly as frozen provenance and did not declare its CREST semantic-coherence role or CED/MRM boundaries.
3. MRM contained the canonical CREST synthesis but its README still over-emphasized observation/VOI extensions and historical frozen-CCOC wording.
4. CED's `program_synthesis_audit.md` and README reflected the pre-CREST manuscript architecture in which passive-closure non-certifiability was still a headline result; the current Paper B instead centers experiment-induced reportability, target-safe refinement, failure-aware trust, and risk-limited adaptive resolution.

The final synchronization branches correct only those narrative/control-plane mismatches.

## 6. Final scientific verdict

The four repositories **do form one complete CREST story at the program level**:

\[
\boxed{
\text{usable ecological state}
\Rightarrow
\begin{cases}
\text{future-sufficient},\\
\text{semantically coherent},\\
\text{mechanism-robust or ambiguity-explicit},\\
\text{evidentially licensed}.
\end{cases}}
\]

This is a research architecture rather than a single proved theorem. The completeness claim is therefore architectural: the four current repositories cover four distinct contract failures without requiring one to be reinterpreted as another. A theorem claiming simultaneous adequacy, audit commutation, or a globally minimal joint state remains future work and must not be implied by the present synthesis.
