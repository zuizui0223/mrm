# MRM latent-mechanism responsibility at a temporal cut — definition firewall

## Purpose

This note fixes the mathematical meaning of the **latent present / mechanism** side used when MRM is projected into CREST. It is a claim-control note, not a new theorem.

The essential distinction is between:

1. a primitive retained candidate mechanism `theta`; and
2. the response type induced by that candidate under the declared observable space and intervention grammar.

The response type is derived from the candidate mechanism. It is not the definition of the candidate mechanism itself.

## Primitive objects

Fix a finite observable macrostate set `Q`, finite declared action set `A`, and finite retained candidate-mechanism family

\[
C=\{\theta\}.
\]

Each candidate mechanism `theta` is a declared latent controlled law that induces deterministic transitions

\[
G_a^\theta:Q\to Q
\qquad(a\in A).
\]

The candidate family and the maps `G_a^theta` are inputs to the MRM contract. They are not inferred from the candidate-safe quotient that MRM later constructs.

## Response-type equivalence

Two candidate mechanisms are response-equivalent exactly when their complete declared transition tables agree:

\[
\theta\equiv_\Theta\theta'
\iff
\forall q\in Q,\ \forall a\in A,
G_a^\theta(q)=G_a^{\theta'}(q).
\]

Let

\[
R=C/\!\equiv_\Theta
\]

be the response-type set.

This is a quotient **of primitive mechanism candidates**. It removes mechanism-name differences that have no declared response consequence.

The typed latent state space used by MRM is then

\[
X=Q\times R,
\]

with

\[
T_a(q,r)=(G_a^r(q),r),
\qquad
o(q,r)=q.
\]

The candidate-safe quotient is constructed only after these objects have been fixed.

## Why this is non-circular

The dependency order is

\[
Q,A,C,\{G_a^\theta\}
\longrightarrow
\equiv_\Theta
\longrightarrow
R
\longrightarrow
Q\times R
\longrightarrow
\text{candidate-safe quotient}.
\]

The final quotient does not define the candidate family, the mechanism laws, or the response-type relation. It only determines how much of the already declared latent response-law variation must remain in an honest deterministic macrostate representation.

## Mechanism is not the same coordinate as future

MRM and CCOC both evaluate future responses, but they quantify over different primitive coordinates.

MRM fixes the visible state space and intervention grammar and varies the latent law:

\[
\text{MRM:}\qquad
q\ \text{fixed/observed},\quad
A\ \text{fixed},\quad
\theta,\theta'\ \text{vary}.
\]

CCOC fixes one controlled law and compares raw configurations under a declared or enlarged future grammar:

\[
\text{CCOC:}\qquad
\mathcal M\ \text{fixed},\quad
s,s'\ \text{vary},\quad
\mathcal L\ \text{declared/compared}.
\]

Thus MRM's latent coordinate is the **law index** behind the cut; CCOC's future responsibility is the **right-of-cut query family** applied under a fixed law.

These coordinates need not be statistically or ontologically independent. CREST does not require such independence. It only requires that the primitive objects and the responsibility maps be declared before the final state quotient.

## Why response relevance does not make the definition circular

MRM intentionally does not preserve full mechanism identity. It preserves only mechanism distinctions that can change declared responses. This is a relevance quotient, not a circular definition:

\[
\theta
\longrightarrow
\text{declared response law}
\longrightarrow
[\theta]_\Theta.
\]

The arrow starts from a primitive candidate mechanism. The quotient class `[theta]_Theta` is the output of the relevance criterion.

For CREST wording, **latent response structure** is therefore more precise than an unrestricted claim about complete causal mechanism identity.

## Relation to the temporal cut

For a CREST world `omega` at cut `t`, let `theta_t(omega)` be the retained latent candidate law compatible with the same visible observation. A fixed MRM contract induces the latent responsibility map

\[
\Theta_t(\omega)=[\theta_t(\omega)]_\Theta.
\]

Two worlds can share the same visible cut value while requiring different latent-present state information when their response types differ.

## Scope

This note does not claim that candidate mechanisms are uniquely identifiable causal structures, that the retained candidate family is inferred from data, or that response-type equivalence exhausts every biologically meaningful mechanism distinction. It fixes the finite non-circular dependency order already used by the MRM core proofs.
