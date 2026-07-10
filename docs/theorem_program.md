# MRM theorem program

## Central question

Several retained ecological mechanisms can each support a compact exact
macro-law while disagreeing about the successor of the same observed macrostate
under a declared future action. MRM identifies the strongest honest report:
universal deterministic, typed deterministic, or set-valued.

## Result I — Universal deterministic law criterion

Let every candidate induce a deterministic transition map \(G_a^\theta:Q\to Q\)
on one common observable macrostate space. A candidate-independent deterministic
law exists exactly when every induced map agrees across candidates and actions.
Equivalently, the number \(R\) of distinct response types is one.

## Result II — Candidate-safe and set-valued reports

When \(R>1\), retaining response type gives a deterministic law on
\(Q\times R\). Forgetting it gives the exact set-valued successor

\[
F_a(q)=\{G_a^\theta(q):\theta\in C\}.
\]

No single deterministic candidate-forgetting law should be reported unless all
candidate maps agree.

## Result III — Candidate-safe product lower bound

If every pair of distinct response types can be separated by a declared future
action from every shared macrostate, an exact typed deterministic interface has
at least \(|Q|R\) states:

\[
K_{\mathrm{typed}}\ge\log_2|Q|+\log_2R.
\]

## Result IV — Joint exterior-mechanism uncertainty

Exterior completion uncertainty and response-type uncertainty add only under
joint operational separation of the full product. For a jointly addressable
family \(I\times E_1\times\cdots\times E_q\times R\),

\[
K_{\mathrm{joint}}\ge
\log_2|I|+\sum_j\log_2|E_j|+\log_2R.
\]

The condition is an injection premise over jointly realizable states, not an
arithmetic inference from two unrelated lower bounds.

## Result V — Minimal candidate-safe quotient

For the typed product \((q,r)\), require an exact deterministic interface to
preserve the currently observed macrostate \(q\). Starting from blocks with a
common \(q\), repeatedly refine by the blocks reached under every declared
action. The fixed point is the coarsest observation-preserving deterministic
quotient of \(Q\times R\), hence has the minimum number of states among exact
candidate-safe interfaces for the declared family.

The product lower bound is recovered under uniform separation. Without that
premise, response type may be locally irrelevant and the exact quotient can be
strictly smaller than \(|Q|R\).

## Result VI — Active discrimination under declared interventions

At observed macrostate \(q\), an action partitions the remaining response types
by their observed successor macrostate. Dynamic programming over
\(Q\times\{S:\varnothing\ne S\subseteq R\}\) returns a finite adaptive
discrimination tree with the minimum worst-case number of actions, or certifies
that no finite declared intervention policy separates the remaining types.

## Result VII — Canonical mechanism-ambiguity frontier

For every \(m\ge1\), let \(R_m=\{0,1\}^m\), \(Q=\{0,1\}\), and define
\(G^{r}_{\mathrm{probe}_i}(q)=r_i\). Each fixed response type has a two-state
macro-law. Yet every pair of response types is uniformly separable, so the minimal
candidate-safe quotient has exactly

\[
|Q||R_m|=2^{m+1}
\]

states and \(m+1\) memory bits. Relative to the fixed-candidate law, retained
mechanism ambiguity costs exactly \(m\) bits. Thus state cardinality grows
exponentially in the number of unresolved binary response dimensions, whereas the
memory surcharge grows linearly.

## Result VIII — Canonical active-identification frontier

Applying `probe_0, ..., probe_(m-1)` reads the complete response signature and
identifies the retained response type in \(m\) interventions. Any adaptive policy
of depth \(d\) has at most \(2^d\) observed leaves, so distinguishing \(2^m\)
types requires \(d\ge m\). The canonical schedule is therefore worst-case optimal.
After \(k\) distinct probes, exactly \(2^{m-k}\) response types remain.

## Result IX — Cost-aware exact active discrimination

Let every declared action have finite strictly positive cost \(c(a)\). For a
current macrostate \(q\) and compatible type subset \(S\), define
\(S_{a,q,x}=\{r\in S:G_a^r(q)=x\}\). The minimum worst-case total cost obeys

\[
V(q,\{r\})=0,\qquad
V(q,S)=\min_a\left[c(a)+\max_{x:S_{a,q,x}\ne\varnothing}
V(x,S_{a,q,x})\right].
\]

Finite dynamic programming over \(Q\times\{S:\varnothing\ne S\subseteq R\}
returns an exact minimum-cost adaptive plan, or no plan when the action grammar
cannot separate the remaining types. Strictly positive costs exclude beneficial
configuration cycles. When all costs are one, the objective agrees with the
minimum worst-case action count in Result VI.

## Result X — Robust observation update

Let bounded observation error be declared by nonempty supports \(N(x)\subseteq Q\),
where \(N(x)\) is the set of true successor macrostates compatible with observed
macrostate \(x\). For current known macrostate \(q\), action \(a\), observed
successor \(x\), and prior response-type set \(S\), the conservative update is

\[
S'=\{r\in S:G_a^r(q)\in N(x)\}.
\]

If \(|S'|=1\), the observation identifies a response type under the declared error
support. If \(|S'|>1\), MRM must retain ambiguity or report a set-valued successor
over \(S'\). If \(|S'|=0\), the observation contradicts the retained family and the
error-support declaration. Exact observation is recovered by \(N(x)=\{x\}\).

## Non-claims

MRM does not infer candidate mechanisms, response types, state alignment,
intervention grammar, action costs, or observation-error supports from field
observations. Its quotient, discrimination, frontier, cost-aware, and robust-update
results are finite, exact, and support-level; they do not yet optimize risk, handle
stochastic mechanism transitions, propagate hidden current-state uncertainty, or
incorporate Bayesian priors or hard budgets.
