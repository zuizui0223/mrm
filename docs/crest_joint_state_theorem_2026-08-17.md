# CREST-J1 — conditional joint-state existence, noncommutation, and evidence gate

> **Status:** conditional program-level theorem with analytic proof and executable
> finite witnesses. The generic least-common-fixed-point result is classical
> closure-operator substrate; no novelty is claimed for that machinery. CREST-J1
> records exactly what follows when the four audits are placed on one declared
> finite common lift, and exactly what still can fail.

## 1. Decision

The unrestricted sentence

> “There is always one unique minimal ecological state satisfying all four CREST
> axes”

is false as stated because the current companion theories do not automatically
share one carrier, one transition structure, or one evidence relation.

A precise conditional theorem is available:

\[
\boxed{
\begin{minipage}{0.88\linewidth}
On a declared finite common latent-world lift, if each CREST audit induces a
monotone inflationary refinement closure on the same partition lattice, then there
is a unique coarsest partition fixed by all four audit closures. Pairwise audit
commutation is not required. A fully evidentially licensed deterministic joint
state exists if and only if the reliability-qualified evidence partition resolves
that coarsest required partition.
\end{minipage}}
\]

The first sentence is a common-fixed-point/minimality theorem. The second is an
existence-or-no-go gate joining the representational requirements to CED-style
evidential licensing.

## 2. Common-lift contract

Let \(U\) be a finite set of joint latent worlds. A world in \(U\) may contain, as
needed by the application,

- the ecological configuration used by the future grammar;
- the carried source label or history class used by MLTR;
- the retained response type used by MRM;
- the latent variables and record-support identity used by CED; and
- the requested report target.

The theorem is relative to this declared lift. It does **not** prove that one
canonical lift is forced by nature.

Let \(\Pi(U)\) be the finite lattice of partitions of \(U\), ordered by information:

\[
P\preceq Q
\quad\Longleftrightarrow\quad
Q\text{ refines }P.
\]

Thus moving upward retains more distinctions. Let \(B\in\Pi(U)\) be the baseline
partition containing every distinction that must be preserved before the four
audits are applied.

Assume four closure operators

\[
C_\Gamma,\ C_\mathcal H,\ C_\Theta,\ C_{D,T}:\Pi(U)\to\Pi(U).
\]

For each \(i\), \(C_i\) is:

1. **inflationary:** \(P\preceq C_i(P)\);
2. **monotone:** \(P\preceq Q\Rightarrow C_i(P)\preceq C_i(Q)\); and
3. **idempotent:** \(C_i(C_i(P))=C_i(P)\).

Its fixed points are the partitions satisfying that audit on the common lift.

The intended mapping is:

| closure | companion meaning on the common lift |
|---|---|
| \(C_\Gamma\) | CCOC future-grammar exactness / legal-row and successor stability |
| \(C_\mathcal H\) | MLTR inherited-label-preserving target exactness |
| \(C_\Theta\) | MRM candidate-safe deterministic stability over retained response types |
| \(C_{D,T}\) | CED target-constant, action-stable required resolution |

Let \(E_D\in\Pi(U)\) be the **reliability-qualified evidence partition**: worlds
inside one \(E_D\)-block remain observationally compatible under the declared
experiment, detection, failure, and risk contract. It need not itself be fixed by
the representational closures.

## 3. Theorem 1 — unique coarsest required joint state

### Statement

There is a unique partition \(J\in\Pi(U)\) such that:

1. \(B\preceq J\);
2. \(C_i(J)=J\) for every
   \(i\in\{\Gamma,\mathcal H,\Theta,(D,T)\}\); and
3. for every other partition \(P\) satisfying 1–2,
   \(J\preceq P\).

Thus \(J\) is the unique coarsest / least-information partition satisfying all
four representational obligations, unique up to renaming its blocks.

### Proof

The partition lattice \(\Pi(U)\) is finite and complete. Closure operators on a
complete lattice themselves form a complete lattice. Let

\[
C_* = C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T}
\]

be their join in the closure-operator lattice. Its fixed-point set is

\[
\operatorname{Fix}(C_*)
=
\bigcap_i\operatorname{Fix}(C_i).
\]

Define

\[
J=C_*(B).
\]

Because \(C_*\) is inflationary, \(B\preceq J\). Because it is idempotent, \(J\)
is a fixed point of \(C_*\), hence of every \(C_i\). If \(P\) is any common fixed
point above \(B\), monotonicity gives

\[
J=C_*(B)\preceq C_*(P)=P.
\]

Therefore \(J\) is the unique least common fixed point above \(B\). ∎

### Constructive fair iteration

The joint state does not require the audits to commute. Choose any cyclic order
containing every audit and start with \(P_0=B\). Apply the four closures repeatedly:

\[
P_{n+1}=C_{i_n}(P_n),
\]

where the schedule is fair. Every strict update increases the number of partition
blocks. Therefore a finite carrier gives at most

\[
|U|-|B|
\]

strict block-increasing updates before stabilization. Monotonicity shows by
induction that every iterate is below every common fixed point above \(B\), so the
stable result is \(J\), independent of the fair audit order.

Order can change the intermediate partitions and number of passes; it cannot change
the final least common fixed point.

## 4. Theorem 2 — evidential licensing dichotomy

### Statement

A deterministic full joint-state label, computable from the evidence class and
satisfying all four representational closures, exists if and only if

\[
\boxed{J\preceq E_D,}
\]

that is, the evidence partition refines the required joint-state partition.

When this condition holds, \(J\) itself is the unique coarsest fully licensed joint
state.

When it fails, no deterministic evidence-based state satisfying all four
representational obligations exists. The sharp honest report for evidence class
\(e\) is then

\[
\mathcal S(e)
=
\{[u]_J:[u]_{E_D}=e\},
\]

a set of still-compatible joint-state blocks.

### Proof

If \(J\preceq E_D\), every evidence block lies inside one \(J\)-block, so the
quotient label \([u]_J\) factors through the evidence record. By Theorem 1, \(J\)
is already the unique coarsest common fixed point above \(B\).

Conversely, suppose a partition \(P\) is fixed by all four closures, lies above
\(B\), and is a deterministic function of the evidence class. Theorem 1 gives
\(J\preceq P\). Evidence measurability gives \(P\preceq E_D\). Hence
\(J\preceq E_D\). If that relation fails, no such \(P\) can exist. The set-valued
report lists exactly the \(J\)-blocks intersecting an evidence class and is therefore
sharp. ∎

## 5. Target-level corollary

Failure to identify the full joint state does not automatically prohibit every
report. For a finite target map \(T:U\to Y\), a deterministic target report exists
exactly when

\[
u\equiv_{E_D}v\Rightarrow T(u)=T(v).
\]

Therefore it is possible that

\[
J\not\preceq E_D
\quad\text{but}\quad
T\text{ factors through }E_D.
\]

In that case the evidence licenses the requested target without licensing the full
CREST joint-state block. This preserves the CED boundary between **required state
resolution** and **currently licensed reporting**.

## 6. Proposition — one-pass intersection is insufficient

The unique joint state is not, in general, obtained by computing each audit's
minimum once from the same baseline and intersecting those four outputs.

### Seven-world cascade witness

Let

\[
U=\{z,a,b,c,d,r,s\}
\]

and let the baseline distinguish \(z\) from all other worlds. Give each audit one
partial deterministic transition, with all unspecified live worlds mapping to
\(r\), \(z\mapsto z\), and \(r,s\mapsto r\):

| audit | distinguishing transition |
|---|---|
| future | \(a\mapsto z\) |
| inherited semantics | \(b\mapsto a\) |
| mechanism | \(c\mapsto b\) |
| target/action | \(d\mapsto c\) |

From the baseline, only the future closure can initially distinguish a new world:
it splits \(a\). That split makes the semantic closure able to distinguish \(b\),
which makes the mechanism closure distinguish \(c\), which makes the target closure
distinguish \(d\).

A reverse one-pass order stops after the first split. Fair repeated iteration gives

\[
J=\{\{z\},\{a\},\{b\},\{c\},\{d\},\{r,s\}\}.
\]

The executable oracle enumerates all 877 partitions of the seven-world carrier.
Exactly two refine the baseline and are fixed by all four closures: \(J\) and the
discrete partition. Hence \(J\) is the unique coarsest common fixed point.

This witness establishes audit **noncommutation at the construction level** while
preserving final order-independent minimality.

## 7. What has and has not been recovered

### Recovered

- conditional existence of one unique coarsest required state on a finite common
  lift;
- a constructive, fair, order-independent refinement algorithm;
- no need for pairwise audit commutation;
- a necessary-and-sufficient evidence condition for a fully reportable joint state;
- a sharp set-valued fallback when evidence is too coarse;
- an explicit witness showing that one-pass intersection of separately minimized
  audit outputs can miss the joint state.

### Not recovered

- a canonical common lift for arbitrary CCOC, MLTR, MRM, and CED models;
- uniqueness across different choices of \(U\), contracts, targets, or mechanism
  families;
- an unconditional empirical claim that current observations resolve \(J\);
- a theorem that the four axes are exhaustive or logically independent;
- pairwise commutation, a universal audit order, or additive cross-axis costs;
- an infinite, approximate, stochastic, or risk-limited version without additional
  completeness/continuity assumptions.

The theorem is therefore **conditional but non-vacuous**: it identifies the exact
mathematical assumptions under which “one minimal CREST state” is meaningful and the
exact evidence obstruction under which that state cannot be reported.

## 8. Prior-art classification

The generic order theory is established prior art.

- Cousot and Cousot (1977), *Abstract interpretation: a unified lattice model for
  static analysis of programs by construction or approximation of fixpoints*,
  provides the classic lattice/fixpoint framework.
- Dacar, *Closure operators on dcpos* (arXiv:1709.06170; current 2026 revision),
  proves collective results for preclosure/closure maps and that closure operators
  form a complete lattice; the join has the intersection of the constituent
  fixed-point sets.
- Fair or chaotic iteration of monotone inflationary maps is standard fixed-point
  computation substrate.

Accordingly, CREST-J1 does not claim to invent least common fixed points. Its role is
to determine whether the four existing audit contracts can be put into that
substrate without erasing their different scientific meanings, and to expose the
additional common-lift and evidence gates.

## 9. Executable sources

- `mrm/crest_joint_state.py`
- `tests/test_crest_joint_state.py`

The executable witness checks:

1. final partition equality under forward and reverse fair schedules;
2. different pass counts under noncommuting schedules;
3. failure of one reverse pass;
4. exhaustive unique-coarseness over all seven-world partitions;
5. full-state evidence success and failure;
6. target reportability despite failure to identify the full joint state; and
7. preservation of partial legal-action rows.
