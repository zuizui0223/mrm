# MRM standalone verification audit

## Purpose

MRM was reconstructed from frozen CCOC legacy mechanism-uncertainty assets. This
audit records the exact standalone theorem surface and the boundary between
analytic statements and finite replay.

## Source-to-successor map

| CCOC legacy asset | MRM public core | Status |
|---|---|---|
| candidate-safe universal laws | `mrm.laws.CandidateLawFamily` | migrated as response-type quotient and report trichotomy |
| joint exterior–candidate laws | `mrm.joint.JointUncertaintyFamily` | migrated as a declared joint-separation cardinality witness |
| no legacy implementation | `mrm.quotient` | new finite quotient construction and active discrimination planner on the declared response-type core |

The CCOC open-composition manuscript theorem and MLTR replacement transport
results are not MRM dependencies.

## What the checks establish

The standalone tests and replay verify that:

1. duplicate candidates with equal complete macro-transition tables collapse to
   one response type;
2. disagreement produces an exact set-valued successor when response type is not
   retained;
3. retaining a response type gives a deterministic typed successor;
4. response-type cardinality is invariant to candidate ordering and duplication;
5. the candidate-safe product quantity is used only after the declared uniform
   response-separation condition has been checked;
6. the joint cardinality identity is numerically stable for both binary and
   nonbinary finite cardinalities;
7. the minimal candidate-safe quotient preserves observed macrostates and has
   deterministic successors while merging locally irrelevant response types; and
8. a finite adaptive intervention tree has the claimed minimum worst-case depth
   on the declared discrimination witness, while an inseparable current state
   returns no plan.

The quotient test also exhausts every pair of two-state, one-action deterministic
candidate maps and compares quotient equality with future observed-trajectory
equality.

## Analytic theorem versus replay

The universal-law criterion follows from equality of the declared induced maps.
The typed product lower bound and joint lower bound require their stated
operational separation assumptions. The minimal quotient follows from finite
observation-preserving partition refinement, and the planner is exact over its
finite state/subset search space. A replay verifies selected finite witnesses and
small exhaustive cases; it does not prove all-family statements or identify
candidate mechanisms from data.

## Explicit boundaries

MRM currently assumes a common observable macrostate space, finite deterministic
candidate maps, exact macrostate observations, and a declared action grammar. It
does not infer or align candidate state spaces, choose candidate sets from data,
or treat noisy, stochastic, cost-weighted, or risk-weighted candidate
disagreement.
