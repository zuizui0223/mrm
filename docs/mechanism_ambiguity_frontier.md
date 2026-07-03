# Mechanism-ambiguity complexity frontier

## Canonical binary-signature family

For an integer \(m\ge 1\), let the retained response-type family be

\[
R_m=\{0,1\}^m,
\]

so that there are \(2^m\) candidate response types. Let the observable macrostate
space be \(Q=\{0,1\}\), and let the declared intervention grammar contain
`probe_0, ..., probe_(m-1)`. For response signature \(r=(r_0,\ldots,r_{m-1})\),
define

\[
G^{r}_{\mathrm{probe}_i}(q)=r_i\qquad \text{for every }q\in Q.
\]

Each fixed response type therefore has an exact two-state macro-law. The candidate
name has no role beyond its complete response signature: all distinct signatures
are distinct MRM response types.

## Result VII — Exact ambiguity frontier

Every pair of signatures differs in at least one bit, and the associated probe
separates that pair from either current macrostate. Therefore uniform response
separation holds. The observation-preserving minimal candidate-safe quotient is the
full typed product and has

\[
|Q||R_m|=2\cdot 2^m=2^{m+1}
\]

states. Its exact memory is

\[
K_{\mathrm{safe}}=\log_2(2^{m+1})=m+1
\]

bits, compared with one bit for the fixed-candidate two-state macro-law. Retaining
mechanism uncertainty therefore imposes an exact surcharge of \(m\) bits.

The state **cardinality** grows exponentially in the number of unresolved binary
response dimensions. The information-theoretic memory surcharge grows linearly in
that number. These are different statements and MRM reports both explicitly.

## Result VIII — Exact active-identification frontier

The canonical schedule applies every probe once. Its observed trajectory is exactly
the signature \(r\), so it identifies all \(2^m\) response types in \(m\)
interventions.

No exact adaptive policy can use fewer than \(m\) interventions in this family. At
each intervention the next observed macrostate has at most two values, hence a
depth-\(d\) adaptive intervention tree has at most \(2^d\) observable leaves.
Separating \(2^m\) response types requires \(2^d\ge2^m\), hence \(d\ge m\).
The canonical schedule attains this bound.

After \(k\) distinct probes, exactly \(2^{m-k}\) signatures remain compatible with
the observed bits. Thus the family supplies an exact information-removal path, not
only an endpoint lower bound.

## Why this is useful for MRM

The frontier is not a claim that finite automata minimization, binary decision
trees, or leaf-counting lower bounds are novel. Its role is to give MRM a transparent
witness family where all pieces of the reporting theory meet:

\[
\text{candidate mechanisms}
\to \text{response types}
\to \text{minimal candidate-safe law}
\to \text{optimal intervention identification}.
\]

It lets a manuscript say precisely when mechanism uncertainty is a small local
annotation and when it changes the exact state cardinality of every honest
candidate-safe macro-law.

## Verification boundary

`mrm.frontier.BinarySignatureFrontier` constructs the family, verifies uniform
response separation and full-product minimality, and records deterministic frontier
points. Tests verify widths one through five, exact residual candidate counts, and
that the generic active planner attains the \(m=3\) lower bound.

This is a finite, noiseless construction conditional on the declared intervention
grammar. It does not show that ecological mechanisms are binary, that field
experiments observe states without error, or that all interventions have equal cost,
risk, or feasibility.
