# CREST-J3 — maximal synchronized common lift and coverage no-go

> **Status:** conditional program-level theorem with analytic proof and executable
> finite certificates. Greatest invariant subsets, safety kernels, and descending
> fixed-point pruning are established dynamical-systems and verification substrate.
> CREST-J3 does not claim those generic constructions as new. It supplies the
> missing existence/no-go layer between four separately specified audit components
> and the fixed-lift joint-state theorem CREST-J1.

## 1. Problem

CREST-J1 begins after a finite common latent-world lift has been declared. CREST-J2
shows that faithfully redundant refinements of such a lift do not change its joint
quotient. Neither theorem decides whether a proposed cross-component synchronization
contains any dynamically coherent common lift in the first place.

CREST-J3 answers that question relative to a declared finite ambient
synchronization.

## 2. Ambient synchronization contract

Let `A` be a finite ambient set of candidate joint tuples. A tuple may contain the
component states needed by CCOC, MLTR, MRM, and CED. Let

\[
W_0\subseteq A
\]

be the tuples satisfying the static compatibility relation—for example, agreement
on shared observable configuration, time, site, or declared source/target
correspondence.

Let `Act` be the union of all lifted audit actions. Each action is partial and
deterministic on `A`:

\[
\tau_a:A\rightharpoonup A.
\]

Undefined means that the action is illegal at that tuple. Restricting the common
lift is not allowed to make a previously legal action disappear. Therefore a subset
`L` is dynamically admissible only when

\[
w\in L,\ \tau_a(w)\text{ defined}
\quad\Longrightarrow\quad
\tau_a(w)\in L.
\]

Finally, each companion component may declare local labels that a **coverage-complete**
common lift must represent. These are projection-surjectivity obligations, not new
transitions.

## 3. Universal invariant-kernel operator

For `S subseteq A`, define

\[
F(S)=
\left\{
 w\in S\cap W_0:
 \forall a,\
 \tau_a(w)\text{ defined}
 \Rightarrow
 \tau_a(w)\in S
\right\}.
\]

`F` is monotone and deflationary. Start from

\[
S_0=W_0,
\qquad
S_{n+1}=F(S_n).
\]

The sequence removes every compatible tuple whose legal future leaves the current
candidate set.

## 4. Theorem 1 — unique maximal common lift

### Statement

The descending sequence stabilizes after finitely many strict rounds at a unique set

\[
U^*=\bigcap_{n\ge 0}S_n.
\]

`U*` is the greatest statically compatible subset closed under every declared legal
action. Equivalently:

1. `U* subseteq W0`;
2. every legal successor of a world in `U*` also belongs to `U*`; and
3. every other subset satisfying 1–2 is contained in `U*`.

A nonempty common lift exists if and only if

\[
\boxed{U^*\ne\varnothing.}
\]

### Proof

Because `A` is finite and `F(S) subseteq S`, the descending sequence stabilizes at
some `U*`. At stabilization, `F(U*)=U*`, which is exactly static compatibility plus
closure under all legal transitions.

Let `L` be any other compatible transition-closed subset. Then `L subseteq S0`.
Assume inductively that `L subseteq Sn`. If `w in L`, every legal successor of `w`
is in `L`, hence in `Sn`; therefore `w in F(Sn)=S(n+1)`. Thus

\[
L\subseteq S_n
\]

for every `n`, so `L subseteq U*`. Hence `U*` is the unique greatest admissible
common lift. The existence equivalence follows because `U*` itself is admissible
when nonempty, while every admissible lift must be a subset of it. ∎

This is a maximal-carrier theorem, not the CREST-J1 minimal-state theorem. CREST-J3
first determines which joint worlds can coexist under the declared transitions;
CREST-J1 then compresses those worlds as far as all four audit closures permit.

## 5. Theorem 2 — coverage-complete existence criterion

For component `k`, let `R_k` be the finite set of local labels that the common lift
must represent, and let

\[
p_k:A\to X_k
\]

be the declared component label/projection.

### Statement

A coverage-complete common lift exists if and only if

\[
\boxed{
R_k\subseteq p_k(U^*)
\quad\text{for every component }k.
}
\]

### Proof

If `U*` covers every required label, then `U*` itself is a compatible,
transition-closed, coverage-complete lift.

Conversely, suppose some required label is absent from `p_k(U*)`. Every admissible
lift `L` is contained in `U*` by Theorem 1, so

\[
p_k(L)\subseteq p_k(U^*).
\]

No admissible subset can recover the missing label. Therefore no coverage-complete
lift exists. ∎

This condition distinguishes two different no-go results:

- **empty-kernel no-go:** no dynamically coherent common lift exists at all;
- **coverage no-go:** some coherent joint worlds survive, but none can represent all
  required companion states.

## 6. Theorem 3 — finite elimination certificates

Assign rank `0` to every statically incompatible ambient tuple. At pruning round
`r>=1`, remove a current tuple when one legal successor already lies outside the
current set and record that action and successor.

### Statement

Every eliminated compatible tuple has a finite witness chain

\[
w_0\xrightarrow{a_0}w_1
\xrightarrow{a_1}\cdots
\xrightarrow{a_{m-1}}w_m
\]

such that:

1. `w_m` is statically incompatible;
2. elimination ranks strictly decrease along the chain; and
3. `m < |A|`.

For a missing component label, collecting the chains of all statically compatible
candidate tuples carrying that label is a finite coverage-impossibility
certificate.

### Proof

A tuple removed at round `r>0` has a recorded legal successor outside the set present
at the start of round `r`. Because removals inside one round are simultaneous, that
successor was either statically incompatible or removed in an earlier round. Its
rank is therefore strictly smaller. Repeating the recorded successor step gives a
strictly decreasing sequence of nonnegative integer ranks, which must terminate at
rank `0`. No world repeats, so the chain length is less than `|A|`. ∎

## 7. Cascade witness

Let

\[
A=\{w_0,w_1,w_2,s,b\},
\qquad
W_0=\{w_0,w_1,w_2,s\},
\]

where `b` is statically incompatible. One action has transitions

\[
w_0\to w_1,
\quad
w_1\to w_2,
\quad
w_2\to b,
\quad
s\to s.
\]

Pruning proceeds as follows:

1. round 1 removes `w2` because it enters `b`;
2. round 2 removes `w1` because it enters removed `w2`;
3. round 3 removes `w0` because it enters removed `w1`;
4. `s` survives.

Thus

\[
U^*=\{s\}.
\]

The chain

\[
w_0\to w_1\to w_2\to b
\]

certifies why `w0` cannot belong to any common lift. Exhaustive enumeration of all
subsets of `W0` leaves only the empty set and `{s}` as transition-closed subsets, so
`{s}` is the unique maximal common lift.

If one component requires both labels represented by `w0` and `s`, a nonempty lift
exists but no coverage-complete lift exists. If it requires only the label carried
by `s`, `{s}` is coverage complete. If the transition `s -> s` is changed to
`s -> b`, the maximal kernel is empty.

## 8. Connection to CREST-J1 and CREST-J2

The current synthesis chain is now:

```text
declared ambient component synchronization
    -> CREST-J3 maximal compatible transition-closed carrier U*
    -> if nonempty and coverage-complete, declare audit/evidence/target partitions
    -> CREST-J1 unique coarsest joint state J on U*
    -> CREST-J1 evidence licensing gate
    -> CREST-J2 invariance under faithfully redundant refinements of U*
```

The stages answer different questions:

- J3: **which joint worlds can coherently exist together under the contract?**
- J1: **which surviving worlds must remain distinct?**
- J2: **which added latent detail is scientifically redundant?**

No stage substitutes for empirical justification of the ambient compatibility
relation or transition maps.

## 9. Executable verification

Files:

- `mrm/crest_common_lift.py`
- `tests/test_crest_common_lift.py`

The tests verify:

1. exhaustive maximality over every subset of a four-world compatible set;
2. three-round cascade elimination and rank-decreasing witness chains;
3. the coverage-complete necessary-and-sufficient condition;
4. empty-kernel no-go;
5. preservation of worlds with illegal, rather than escaping, actions; and
6. containment of every declared closed common lift in the maximal kernel.

## 10. Prior-art classification

The generic construction is standard.

- Viability and invariant-kernel theory studies the largest subset of a constraint
  set from which trajectories can remain admissible.
- Safety verification uses greatest fixed points and backward elimination of states
  whose successors violate the safety set.
- Saint-Pierre's discrete viability-kernel work and the broader Aubin viability
  tradition are direct mathematical neighbors.

The present operator is **universal** over every declared legal action, closer to a
robust positively invariant/safety kernel than to an existential controlled
viability kernel. CREST-J3 does not claim to invent invariant-set pruning.

Its program-level contribution is to expose a previously implicit prerequisite of
the four-audit synthesis:

> a joint state can be minimized only after the declared component alignments admit
> a nonempty, transition-closed, coverage-adequate common carrier.

## 11. Remaining open problems

- constructing the ambient compatibility relation directly from arbitrary CCOC,
  MLTR, MRM, and CED model objects;
- existential/control-selective rather than universal action closure;
- stochastic and risk-limited common-lift kernels;
- approximate compatibility and quantitative deletion cost;
- minimum relaxation of component coverage or transitions needed to make `U*`
  admissible; and
- empirical inference and validation of the synchronization contract.

CREST-J3 therefore supplies a conditional canonical carrier, not a canonical
ontology of ecological worlds.
