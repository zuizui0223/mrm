# CREST-J2 — faithful-lift invariance and visibility obstruction

> **Status:** conditional program-level theorem with analytic proof and executable
> finite witnesses. Naturality of closure/refinement under a structure-preserving
> surjection is classical quotient and abstract-interpretation substrate. No generic
> novelty is claimed for that machinery. CREST-J2 answers when two choices of
> finite common lift encode the same scientific joint state and when extra latent
> detail can change it.

## 1. Problem left by CREST-J1

CREST-J1 proves that one declared finite common lift has a unique coarsest joint
state satisfying all four audit closures. It deliberately leaves open whether two
different common lifts produce the same state.

Unconditionally they need not. A second lift may add a latent distinction that is
visible to the future grammar, inherited semantics, retained mechanisms, evidence,
or target. Such a distinction can force a finer joint state.

The correct invariance statement is therefore relative to a map showing that the
additional latent detail is invisible to every declared contract.

## 2. Faithful contract projection

Let

\[
\pi:U\twoheadrightarrow V
\]

be a surjection from a detailed finite common lift `U` to a reduced finite common
lift `V`. For a partition `P` of `V`, write `pi^*P` for its pullback to `U`:

\[
u\equiv_{\pi^*P}u'
\quad\Longleftrightarrow\quad
\pi(u)\equiv_P\pi(u').
\]

Call `pi` **CREST-faithful** when the following conditions hold.

1. The baseline, reliability-qualified evidence, and target-equality partitions on
   `U` are pullbacks of those on `V`.
2. The two contracts declare the same audit names and action columns.
3. Every audit-static distinction on `U` is the pullback of the corresponding
   distinction on `V`.
4. Action legality factors through `pi`.
5. Every legal partial successor commutes with `pi`:

\[
\pi(\tau_i^U(u,a))=\tau_i^V(\pi(u),a).
\]

Thus worlds inside one `pi`-fiber may be distinct as raw latent descriptions, but
no declared CREST audit, evidence class, or target can distinguish them.

These conditions are sufficient and deliberately strict. They are not claimed to
be the weakest possible categorical formulation.

## 3. Lemma — each audit closure commutes with pullback

### Statement

For every CREST-faithful projection, every audit `i`, and every partition `P` of
`V`,

\[
\boxed{
C_i^U(\pi^*P)=\pi^*C_i^V(P).
}
\]

### Proof

Fix one audit. Its refinement step assigns each world a signature consisting of:

1. its current partition block;
2. its audit-static label;
3. its legal-action row; and
4. the current blocks of all legal successors.

Assume the current partition on `U` is `pi^*P`. By condition 3, the static label of
`u` depends only on `pi(u)`. By condition 4, legality depends only on `pi(u)`. By
condition 5, a legal successor of `u` projects to the corresponding legal successor
of `pi(u)`. Because the current partition is a pullback, the source successor block
is exactly the pulled-back target successor block.

Therefore two source worlds have equal refinement signatures exactly when their
target images have equal target refinement signatures. One refinement step on `U`
is the pullback of one refinement step on `V`.

Induction gives the same equality after every finite refinement round. Both
refinements stabilize because the carriers are finite. Their fixed points therefore
satisfy

\[
C_i^U(\pi^*P)=\pi^*C_i^V(P).
\]

∎

## 4. Theorem — joint minimal state is invariant under faithful lifting

Let `J_U` and `J_V` be the CREST-J1 unique coarsest common fixed points above the
respective baselines.

### Statement

If `pi:U -> V` is CREST-faithful, then

\[
\boxed{J_U=\pi^*J_V.}
\]

Consequently the quotient state sets are canonically bijective:

\[
U/J_U\cong V/J_V.
\]

The detailed lift may contain more latent worlds, but it contains no additional
CREST-visible joint state.

### Proof by fair iteration

Choose the same fair cyclic audit-name schedule on both lifts. The baseline on `U`
is the pullback of the baseline on `V`. The lemma shows inductively that after each
audit application, the source partition is the pullback of the target partition.
Thus the two fair sequences remain related by pullback at every stage.

The target sequence stabilizes at `J_V`. Its pullback is fixed by every source
audit, so the source sequence stabilizes at `pi^*J_V`. CREST-J1 uniqueness on `U`
then gives

\[
J_U=\pi^*J_V.
\]

Because `pi` is surjective, every `J_V` block has a nonempty preimage, and distinct
`J_V` blocks have disjoint preimages. The pulled-back blocks therefore give a
bijection between `U/J_U` and `V/J_V`. ∎

### Equivalent fixed-point proof

The pullback map embeds the partition lattice of `V` into the partition lattice of
`U` because `pi` is surjective. Audit naturality maps common fixed points above the
target baseline to common fixed points above the source baseline. Minimality in
both lattices yields the same equality.

## 5. Corollary — two lifts with one faithful reduction have the same joint state

Suppose two common lifts `U_1` and `U_2` admit CREST-faithful surjections to one
reduced contract `V`:

\[
U_1\twoheadrightarrow V\longleftarrow U_2.
\]

Then

\[
U_1/J_{U_1}
\cong
V/J_V
\cong
U_2/J_{U_2}.
\]

Hence uniqueness across lift choices is recovered **up to faithful reduction**.
The theorem does not say that all possible lifts admit such a common reduction.

## 6. Evidence and target licensing are invariant

Because the evidence and target-equality partitions are also pullbacks,

\[
J_U\text{ factors through }E_U
\quad\Longleftrightarrow\quad
J_V\text{ factors through }E_V,
\]

and

\[
T_U\text{ factors through }E_U
\quad\Longleftrightarrow\quad
T_V\text{ factors through }E_V.
\]

The forward implications use surjectivity: any target pair witnessing failure has
source preimages that witness the corresponding failure upstairs. The reverse
implications follow directly by pullback.

Therefore a faithful latent-world duplication cannot create or destroy either:

- licensing of the full joint state; or
- licensing of the requested target without the full state.

This preserves the CREST-J1 distinction between required joint-state resolution and
currently licensed target reporting.

## 7. Visibility obstruction witness

The invariance conditions are scientifically substantive rather than bookkeeping.
Consider the reduced lift

\[
V=\{z,a,r\},
\]

with a baseline separating terminal world `z` from the two live worlds. A future
action sends `a` to `z` and `r` to itself, so the joint state is

\[
J_V=\{\{z\},\{a\},\{r\}\}.
\]

Now duplicate `r` into `r_0,r_1` to obtain

\[
U=\{z,a,r_0,r_1\},
\]

and project both duplicates to `r`.

### Audit-invisible duplication

If all audit labels, evidence labels, targets, legal rows, and projected successors
agree on `r_0,r_1`, the projection is faithful and

\[
J_U=\{\{z\},\{a\},\{r_0,r_1\}\}.
\]

The quotient still has three states and is isomorphic to `V/J_V`.

### Audit-visible duplication

Give `r_0` and `r_1` different retained-mechanism static labels. The proposed
projection is no longer faithful. The source joint state becomes

\[
J_U'=\{\{z\},\{a\},\{r_0\},\{r_1\}\},
\]

which has four states. Thus a lift choice can change the joint state precisely when
its added detail is visible to at least one declared contract; faithful-lift
invariance does not hide such a distinction.

This is a witness of possible failure, not a claim that every violation of one
syntactic sufficient condition must change the quotient.

## 8. Executable verification

Files:

- `mrm/crest_lift_invariance.py`
- `tests/test_crest_lift_invariance.py`

The tests verify:

1. audit naturality for every audit and all five partitions of a three-world
   reduced carrier;
2. equality `J_U = pi^*J_V` for a redundant world duplication;
3. quotient-state isomorphism for two different detailed lifts with one faithful
   reduction;
4. preservation of full-state and target-only evidential licensing;
5. rejection of an audit-visible mechanism split and the resulting three-versus-four
   state witness; and
6. rejection of non-surjective and evidence-nonfactoring projections.

## 9. Prior-art classification

The mathematical substrate is established.

- Congruence-preserving quotients and homomorphism-compatible behavioral
  equivalence are standard.
- Abstract interpretation and strong-preservation theory characterize minimally
  refined abstract models and their behavior under sound/complete abstraction
  maps.
- Naturality statements of the form `closure after pullback = pullback after
  closure` are standard structure-preservation conditions.

Relevant neighboring formal sources include Cousot and Cousot's lattice/fixpoint
framework and Ranzato and Tapparo's abstract-interpretation account of minimally
strongly preserving abstract models. CREST-J2 does not claim a new generic closure
or quotient theorem.

Its program-level result is narrower:

> it identifies an explicit sufficient contract morphism under which the choice of
> CREST common lift is scientifically inert, and separates that case from a concrete
> audit-visible lift obstruction.

## 10. What is now recovered and what remains open

### Recovered

- joint-state invariance under a finite CREST-faithful surjective lift;
- quotient-state isomorphism despite redundant latent-world duplication;
- invariance of full-state and target-only evidential licensing;
- equivalence of two lifts that share one faithful reduction; and
- an explicit visible-fiber obstruction witness.

### Still open

- existence of a canonical faithful reduction for arbitrary four-repository models;
- weakest possible morphism conditions for invariance;
- comparison under lax simulation rather than exact transition commutation;
- quantitative bounds when a lift is only approximately faithful;
- infinite, stochastic, and risk-limited lift invariance; and
- empirical justification for any particular common lift or reduction.

CREST-J1 plus CREST-J2 therefore yields the current strongest safe statement:

\[
\boxed{
\text{one unique coarsest joint state per finite common contract, and one invariant}
\text{ quotient across all faithfully equivalent finite lifts.}
}
\]
