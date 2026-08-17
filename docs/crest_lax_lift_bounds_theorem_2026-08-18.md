# CREST-J5 — one-sided lift refinement bounds

> **Status:** conditional finite synthesis theorem with analytic proof and exhaustive
> finite witnesses. The generic mathematics is monotone closure comparison,
> simulation, and abstract-interpretation substrate. CREST-J5 does not claim a new
> general abstraction theorem. It extends CREST-J2 from exact faithful invariance to
> scientifically interpretable one-sided bounds when one common lift keeps strictly
> more or strictly fewer declared obligations than another.

## 1. Question left by CREST-J2

CREST-J2 proves equality

\[
J_U=\pi^*J_V
\]

when a surjective finite projection \(\pi:U\twoheadrightarrow V\) preserves the
baseline, evidence, target, audit labels, action legality, and successors exactly.
That result deliberately rejects an audit-visible duplicated world rather than
saying what can still be concluded.

The next question is:

> If the projection is not fully faithful because one lift declares additional or
> fewer future/semantic/mechanism/target obligations, can the two joint states still
> be ordered?

The answer is yes under explicit one-sided contract conditions.

## 2. Setup and order convention

Let \(U\) and \(V\) be finite CREST common-lift contracts and let

\[
\pi:U\twoheadrightarrow V
\]

be surjective. For a partition \(P\in\Pi(V)\), let \(\pi^*P\) be its pullback to
\(U\). Partitions are ordered by retained information:

\[
P\preceq Q
\quad\Longleftrightarrow\quad
Q\text{ refines }P.
\]

Thus a larger element retains more distinctions.

Both contracts declare the same audit names. Their evidence and report-target
partitions are required to be exact pullbacks:

\[
E_U=\pi^*E_V,
\qquad
T_U=\pi^*T_V.
\]

This keeps evidence change separate from audit-strength change. The condition is a
control choice, not a claim that every ecological comparison has equal evidence.

## 3. Two one-sided projection classes

### 3.1 Source-stronger projection

Call \(\pi\) **source-stronger** when:

1. the source baseline refines the pulled target baseline,
   \[
   \pi^*B_V\preceq B_U;
   \]
2. for every audit \(i\), the source audit-static partition refines the pulled
   target audit-static partition;
3. every target audit action also occurs in the source audit, while the source may
   add action columns; and
4. every shared action has exactly the pulled target legality row and commuting
   successor:
   \[
   \tau_i^U(u,a)\downarrow
   \Longleftrightarrow
   \tau_i^V(\pi u,a)\downarrow,
   \]
   and when legal,
   \[
   \pi(\tau_i^U(u,a))=\tau_i^V(\pi u,a).
   \]

The source can therefore retain additional static distinctions or expose additional
actions, but it cannot erase or reinterpret a target action.

### 3.2 Source-weaker projection

Call \(\pi\) **source-weaker** when:

1. the source baseline is coarser than the pulled target baseline,
   \[
   B_U\preceq\pi^*B_V;
   \]
2. every source audit-static partition is coarser than the corresponding pulled
   target partition;
3. every source audit action occurs in the target audit, while the target may add
   action columns; and
4. every shared action again has exactly factored legality and commuting successor.

The source has forgotten obligations but has not changed the meaning of the actions
that it retains.

These are transparent sufficient conditions. They are not asserted to be the
weakest possible simulation or categorical conditions.

## 4. Lemma — one-sided audit-closure inequalities

Let \(C_i^U\) and \(C_i^V\) be one corresponding audit closure.

### Source-stronger case

For every \(P\in\Pi(V)\),

\[
\boxed{
\pi^*C_i^V(P)
\preceq
C_i^U(\pi^*P).
}
\]

#### Proof

Start both finite refinement procedures from \(P\) and \(\pi^*P\). Assume at one
round that the source partition refines the pulled target partition. If two source
worlds have equal source signatures, then:

- equality of source current blocks implies equality of their pulled target blocks;
- equality of the finer source static labels implies equality of target static
  labels;
- every target action is a source action and shared legality is identical; and
- equality of source successor blocks implies equality of the corresponding pulled
  target successor blocks.

Hence equal source signatures imply equal target signatures. The next source round
therefore refines the pulled next target round. Induction over refinement rounds and
finite stabilization prove the displayed inequality. ∎

### Source-weaker case

For every \(P\in\Pi(V)\),

\[
\boxed{
C_i^U(\pi^*P)
\preceq
\pi^*C_i^V(P).
}
\]

#### Proof

Again compare the two refinement sequences. Assume the pulled target partition
refines the source partition. If two target images have equal target signatures,
then their source preimages have equal source signatures because:

- target current-block equality implies equality in the coarser source partition;
- target static-label equality implies equality in the coarser source static
  partition;
- every source action is present among the target actions; and
- shared legality and projected successors agree.

Thus the pulled target next round refines the source next round. Induction and
finite stabilization give the inequality. ∎

## 5. Theorem — one-sided joint-state bounds

Let \(J_U\) and \(J_V\) be the CREST-J1 unique coarsest common fixed points above
their respective baselines.

### Source-stronger bound

If \(\pi\) is source-stronger, then

\[
\boxed{
\pi^*J_V\preceq J_U.
}
\]

Consequently,

\[
|U/J_U|\ge |V/J_V|.
\]

#### Proof

Run the same fair audit-name schedule on both contracts. The baseline relation holds
by assumption. Suppose the source iterate refines the pulled target iterate. Source
audit monotonicity and the source-stronger closure lemma give

\[
\pi^*C_i^V(P)
\preceq
C_i^U(\pi^*P)
\preceq
C_i^U(Q),
\]

where \(Q\) is the current source iterate and \(\pi^*P\preceq Q\). Hence the
relation is preserved after every audit application. Both fair finite sequences
stabilize, yielding \(\pi^*J_V\preceq J_U\). Surjectivity ensures that pullback
preserves the number of target blocks, giving the cardinality bound. ∎

### Source-weaker bound

If \(\pi\) is source-weaker, then

\[
\boxed{
J_U\preceq\pi^*J_V.
}
\]

Consequently,

\[
|U/J_U|\le |V/J_V|.
\]

#### Proof

Use the same fair schedule. The pulled target baseline refines the source baseline.
Assume the pulled target iterate refines the source iterate. By the source-weaker
closure lemma and source-audit monotonicity,

\[
C_i^U(Q)
\preceq
C_i^U(\pi^*P)
\preceq
\pi^*C_i^V(P),
\]

where \(Q\preceq\pi^*P\). The relation persists through every audit application and
therefore at the fixed points. ∎

### Equality case

If both one-sided conditions hold, the relevant partitions are equal, the action
columns coincide, and shared action semantics are exact. The two inequalities give

\[
J_U=\pi^*J_V,
\]

recovering CREST-J2 faithful-lift invariance as the equality case.

## 6. Evidential consequences

Because evidence and target equality are exact pullbacks, target-only reportability
is invariant:

\[
T_U\text{ factors through }E_U
\Longleftrightarrow
T_V\text{ factors through }E_V.
\]

Full-state licensing is only one-sided.

### Source stronger

\[
E_U\text{ resolves }J_U
\Longrightarrow
E_V\text{ resolves }J_V.
\]

The converse can fail: the target evidence may resolve the reduced joint state while
remaining unable to distinguish a source-only audit-visible split.

### Source weaker

\[
E_V\text{ resolves }J_V
\Longrightarrow
E_U\text{ resolves }J_U.
\]

The converse can fail: evidence may resolve the weakened source state but not the
finer target state.

Thus evidence adequacy is monotone in the expected direction, but it is not
invariant once audit strength changes.

## 7. Strict witnesses

### 7.1 Added mechanism-visible detail

Let

\[
V=\{z,a,r\}
\]

have a baseline separating terminal \(z\) from live \(a,r\), and one future action
sending \(a\) to \(z\) and \(r\) to itself. Then

\[
J_V=\{\{z\},\{a\},\{r\}\}.
\]

Duplicate \(r\) in the source as \(r_0,r_1\), preserve the future action, and give
the duplicates different retained-mechanism labels. The projection
\(r_0,r_1\mapsto r\) is source-stronger and

\[
J_U=\{\{z\},\{a\},\{r_0\},\{r_1\}\}.
\]

The inequality is strict. If evidence still identifies only the pulled target world
\(r\), the target full state is licensed while the source full state is not.

### 7.2 Forgotten future action

On the identity carrier \(\{z,a,r\}\), let the target retain the distinguishing
future action above, while the source forgets that action and keeps only the
terminal/live baseline. Then

\[
J_U=\{\{z\},\{a,r\}\},
\qquad
J_V=\{\{z\},\{a\},\{r\}\}.
\]

The identity projection is source-weaker and the inequality is strict. Terminal/live
evidence resolves the source state but not the target state.

These examples show that J2 rejection of a nonfaithful projection need not end the
comparison: audit-visible additions and omissions produce opposite certified
bounds.

## 8. Executable verification

Files:

- `mrm/crest_lax_lift.py`
- `tests/test_crest_lax_lift.py`

The tests verify:

1. both closure inequalities for every audit and all five partitions of the
   three-world reduced carrier;
2. strict four-versus-three source-stronger refinement;
3. strict two-versus-three source-weaker coarsening;
4. J2 equality as the overlap of both directions;
5. one-sided full-state licensing and invariant target-only licensing; and
6. rejection of reversed action inclusion, noncommuting shared successors, and
   evidence changes disguised as audit-strength changes.

## 9. Prior-art classification

The generic order theory is established prior art.

- Cousot and Cousot develop closure-operator lattices, sound abstraction, and
  monotone fixed-point comparison.
- Ranzato and Tapparo relate strong preservation, behavioral equivalence, and
  minimal abstract-domain refinement.
- Simulation and abstraction maps routinely yield one-sided soundness or precision
  inequalities, with exact naturality as the equality/completeness case.

Accordingly, CREST-J5 does not claim that one-sided closure comparison is new. Its
program-level contribution is narrower:

> it gives a typed interpretation of the two inequality directions for CREST common
> lifts, separates added scientific obligations from forgotten obligations, and
> derives the corresponding evidence-licensing asymmetry.

## 10. Boundaries

CREST-J5 does not prove:

- that every nonfaithful projection satisfies either one-sided condition;
- comparison when shared action semantics only simulate rather than commute exactly;
- numerical bounds from a count of violated projection clauses;
- approximate, stochastic, infinite, or risk-limited lift comparison;
- that a stronger contract is scientifically preferable; or
- that the selected future, semantic, mechanism, evidence, or target contract is
  empirically correct.

The safe theorem-level extension of J2 is therefore:

\[
\boxed{
\text{additional preserved obligations can only refine }J,
\quad
\text{forgotten obligations can only coarsen }J,
\quad
\text{and exact faithfulness is the equality case.}
}
