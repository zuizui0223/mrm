# Minimal candidate-safe quotient and active discrimination

## Finite setup

Let `Q` be the common observed macrostate set and `R` the response-type quotient
of a declared finite candidate family. Each response type `r` induces a deterministic
transition `G_a^r: Q -> Q` for every declared action `a`. The full typed interface is
therefore the product system

\[
T_a(q,r) = (G_a^r(q), r), \qquad o(q,r)=q.
\]

The observation map is deliberately fixed: an exact interface must still reveal the
current observed macrostate, not only a hidden predictive class.

## Result V — Minimal candidate-safe quotient

A **candidate-safe quotient** is an observation-preserving deterministic quotient of
the typed product: members of one quotient class have the same current macrostate,
and each declared action sends the whole class to one successor class.

Starting from classes with the same observed macrostate and repeatedly refining by
the successor classes under every action yields the coarsest stable partition. Its
classes are exactly the pairs `(q, r)` that have identical observed trajectories for
every finite declared action word. Consequently, the resulting quotient has the
fewest states among exact deterministic interfaces that preserve the current
macrostate for the declared family.

This sharpens the earlier product lower-bound regime. Uniform one-step response
separation forces every `(q, r)` pair apart and recovers the full `|Q| |R|` product.
Without that premise, response type can be locally irrelevant at some observed states;
the minimal quotient quantifies the exact retained memory rather than incorrectly
applying the full product bound.

## Result VI — Exact active discrimination

For a current observed macrostate and a remaining subset of response types, an action
partitions types by the next observed macrostate. The planner constructs an adaptive
intervention tree whose branches are those observations. A terminal branch contains
one response type.

The implementation performs finite dynamic programming over

\[
Q \times \{S: \varnothing \ne S \subseteq R\}.
\]

It returns a plan with the minimum worst-case number of actions, or `None` when no
finite declared intervention policy can identify the response type from that current
state. The plan is adaptive because later actions may depend on earlier observed
macrostate outcomes.

## Relation to existing formalisms

The construction deliberately uses established finite-state ideas rather than claiming
that partition refinement or distinguishing sequences are new. The MRM contribution is
the **reporting problem under retained ecological mechanism uncertainty**: response
types first arise by collapsing candidate macro-transition tables; quotient states must
preserve the observed ecological macrostate; and a failed discrimination plan licenses a
set-valued rather than unsupported deterministic report. Classical automata minimization
and adaptive distinguishing-sequence methods supply the finite computational machinery,
not the mechanism-robust reporting rule.

## What the code verifies

`mrm.quotient.minimal_candidate_safe_quotient` verifies a finite quotient witness by
checking output preservation and deterministic successors of every quotient class.
`shortest_active_discrimination_plan` returns a finite worst-case-optimal plan for the
declared family. The test suite additionally exhausts all two-state, one-action pairs
of deterministic candidate maps and compares quotient equality with finite future
trajectory equality.

## Boundaries

These are exact finite, noiseless results conditional on a declared common macrostate
space, response-type family, and intervention grammar. They do not infer candidates
from data, align different state spaces, optimize experiment costs or risks, or handle
stochastic transitions and observation error. Those require a separate evidence-design
extension rather than being silently folded into the deterministic theorem.
