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
| no legacy implementation | `mrm.quotient` | finite quotient construction and active discrimination planner on the declared response-type core |
| no legacy implementation | `mrm.frontier.BinarySignatureFrontier` | canonical exponential-cardinality / linear-memory-surcharge witness with exact probe-depth frontier |
| no legacy implementation | `mrm.costs` | exact finite minimum-worst-case-cost discrimination under declared positive action costs |
| no legacy implementation | `mrm.robust` | conservative response-type update under declared bounded observation-error support |

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
   deterministic successors while merging locally irrelevant response types;
8. a finite adaptive intervention tree has the claimed minimum worst-case depth
   on the declared discrimination witness, while an inseparable current state
   returns no plan;
9. canonical binary-signature families of widths one through five have the stated
   response-type counts, full-product minimal quotients, exact memory surcharge,
   unique probe trajectories, and residual-candidate path. The generic planner
   attains the width-three information lower bound;
10. declared positive action costs can change the exact optimal policy: the
    cost-aware planner selects a two-step cost-2 branch plan over a one-step
    cost-5 direct probe, agrees with the shortest-depth planner under unit costs,
    and rejects incomplete, extraneous, zero, negative, infinite, and Boolean
    cost assignments; and
11. bounded observation-error supports can prevent false mechanism identification:
    exact observations recover a singleton response type, wider supports retain
    every compatible type, contradictions return an empty retained set, and robust
    set-valued successors continue over the retained type subset.

The quotient test also exhausts every pair of two-state, one-action deterministic
candidate maps and compares quotient equality with future observed-trajectory
equality.

## Analytic theorem versus replay

The universal-law criterion follows from equality of the declared induced maps.
The typed product lower bound and joint lower bound require their stated
operational separation assumptions. The minimal quotient follows from finite
observation-preserving partition refinement, and the planner is exact over its
finite state/subset search space. The binary-signature frontier combines these
facts with a binary decision-tree leaf count. The cost-aware planner adds finite
positive-cost minimax dynamic programming. The robust update adds support-level
filtering under a declared observation-error relation. A replay verifies selected
finite witnesses and small exhaustive cases; it does not prove all-family
statements or identify candidate mechanisms, action costs, or observation-error
supports from data.

## Explicit boundaries

MRM currently assumes a common observable macrostate space, finite deterministic
candidate maps, declared action grammar, finite strictly positive action costs,
and exact or bounded-support macrostate observations. It does not infer or align
candidate state spaces, choose candidate sets, intervention costs, observation
supports, or risks from data, or treat stochastic mechanism transitions,
probabilistic observation error, Bayesian updating, risk-weighted design, or
hard-budget candidate disagreement. The canonical frontier does not assert that
ecological mechanisms are intrinsically binary or that all field interventions have
equal feasibility.
