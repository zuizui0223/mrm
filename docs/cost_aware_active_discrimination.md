# Cost-aware active discrimination

## Finite setup

Let a declared finite response-type family induce deterministic macro transitions
\(G_a^r:Q\to Q\). Every declared intervention \(a\) has a finite strictly positive
cost \(c(a)>0\). At current observed macrostate \(q\), let \(S\subseteq R\) be the
remaining response types consistent with the observed history. An intervention
partitions \(S\) by its next observed macrostate,

\[
S_{a,q,x}=\{r\in S:G_a^r(q)=x\}.
\]

## Result IX — Minimum-cost exact discrimination

Define the value of exact identification by

\[
V(q,\{r\})=0,
\]

and, for non-singleton \(S\),

\[
V(q,S)=\min_a\left[c(a)+\max_{x:S_{a,q,x}\ne\varnothing}
V(x,S_{a,q,x})\right].
\]

Actions whose nonempty outcome branch has no finite value are unavailable. The
resulting policy is adaptive: its next action may depend on the macrostate observed
after earlier interventions.

Because the family and the configuration space
\(Q\times\{S:\varnothing\ne S\subseteq R\}\) are finite, and every cost is
strictly positive, an optimal policy can be chosen without revisiting a
configuration on a branch. Finite dynamic programming therefore returns the exact
minimum worst-case total cost, or returns no plan when the declared grammar cannot
identify the remaining response types.

When all action costs equal one, this objective reduces to the minimum worst-case
number of interventions from Result VI.

## Cost-versus-length witness

Take four response types \(r\in\{0,1,2,3\}\), observable states
\(Q=\{0,1,2,3\}\), and three actions:

- `direct`, cost 5: maps every current state to \(r\), identifying the type in one
  action;
- `cheap_high_bit`, cost 1: maps to the high binary bit of \(r\), leaving two
  response types per observed branch;
- `cheap_low_bit`, cost 1: maps to state \(2+\) the low binary bit of \(r\).

The shortest exact policy uses `direct` and has one step, but its worst-case cost
is 5. The minimum-cost policy first applies `cheap_high_bit` and then
`cheap_low_bit` on either observed branch; it has two steps and worst-case total
cost 2. Thus minimising intervention count and minimising experimental burden are
different reporting problems even with deterministic observations.

## MRM interpretation

The cost layer does not choose ecological mechanisms or estimate a budget from
data. It asks a conditional design question: after a retained response-type family
and action costs have been explicitly declared, what is the least expensive exact
way to turn a typed or set-valued report into a mechanism-resolved deterministic
one? If no finite policy exists, MRM still licenses only the candidate-safe
quotient or the set-valued forecast.

## Verification boundary

`minimum_cost_active_discrimination_plan` verifies finite, exact, positive-cost
witnesses. Tests compare a one-step expensive probe against a two-step cheap
policy, show unit-cost agreement with the shortest-depth objective, and reject
missing, extra, zero, negative, infinite, and Boolean action costs.

This extension does not model failure probability, risk, ethical constraints,
partial observability, stochastic responses, Bayesian priors, or budget-limited
approximation. Those require a separate noisy or risk-aware evidence-design
layer.
