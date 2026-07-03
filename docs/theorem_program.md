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

## Non-claims

MRM does not infer candidate mechanisms, response types, state alignment, or
intervention grammar from field observations. Its quotient, discrimination, and
frontier results are finite, exact, and noiseless; they do not yet optimize cost or
risk, or handle stochastic transitions or observation error.
