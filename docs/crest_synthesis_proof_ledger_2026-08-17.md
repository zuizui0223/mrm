# CREST synthesis proof ledger — J1/J2/J3/J4/J5

> **Status:** canonical cross-contract proof ledger. Last synchronized
> 2026-08-18. The companion ledger `crest_proof_recovery_2026-08-17.md` remains the
> detailed proof audit for CCOC, MLTR, MRM, and CED before synthesis.

## Proof-status scale

- **A — analytic + executable:** quantified proof plus implementation/witness tests.
- **B — analytic only.**
- **C — executable finite evidence only.**
- **D — proof gap.**
- **N/A — philosophical or architectural claim, not a theorem.**

Green CI guards implementation and replay. It is not by itself the proof of a
quantified theorem.

## Theorem baselines

- **CREST-J1:** `96130b91c1f5b8d4512869545dd598af02e14361`
- **CREST-J2:** `f38d954a94eb76cf51f43144c7ace38c3c6b72c5`
- **CREST-J3:** `6b50d1334a62fb4c63c67fc0164f0dedb60ec21d`
- **CREST-J4:** `19ac2ede0b5c8311c36b03c350800e330e7b62fd`
- **CREST-J5:** `e96b99cea6a217fefdbfab62025595c85fffed94`

All five current synthesis results are **Status A**.

## 1. CREST-J3 — maximal synchronized common carrier

Given a finite ambient set of candidate joint tuples, a statically compatible subset
`W0`, declared partial deterministic lifted actions, and component-coverage
obligations, define

\[
F(S)=\{w\in S\cap W_0:\tau_a(w)\downarrow\Rightarrow\tau_a(w)\in S
\text{ for every declared action }a\}.
\]

Descending iteration from `W0` stabilizes at the greatest fixed point `U*`.

Proved:

1. `U*` is the unique greatest compatible transition-closed subset;
2. a nonempty common lift exists iff `U*` is nonempty;
3. a coverage-complete common lift exists iff `U*` represents every required
   component label; and
4. every eliminated tuple has a finite rank-decreasing action chain ending at a
   statically incompatible tuple.

Analytic source:

- `docs/crest_maximal_common_lift_theorem_2026-08-17.md`

Executable source:

- `mrm/crest_common_lift.py`
- `tests/test_crest_common_lift.py`

Generic greatest invariant/safety-kernel mathematics is prior substrate. The CREST
result is the explicit common-carrier existence, coverage, and no-go layer.

## 2. CREST-J4 — exact minimum declared relaxation after J3 no-go

Fix one J3 ambient problem and a weighted finite repair language:

- admit an originally incompatible world `w` at cost `c_w`;
- disable an originally legal transition `(w,a)` at cost `d_{w,a}`; and
- waive one required component label `(k,l)` at cost `r_{k,l}`.

For every nonempty retained subset `S`, define

\[
\begin{aligned}
A(S)&=S\setminus W_0,\\
E(S)&=\{(w,a):w\in S,\tau_a(w)\downarrow,
                  \tau_a(w)\notin S\},\\
D(S)&=\{(k,\ell):\ell\in R_k,
                  \ell\notin p_k(S)\}.
\end{aligned}
\]

The exact fixed-witness cost is

\[
R(S)=
\sum_{w\in A(S)}c_w
+
\sum_{(w,a)\in E(S)}d_{w,a}
+
\sum_{(k,\ell)\in D(S)}r_{k,\ell}.
\]

Proved:

1. every repair retaining `S` must include all operations in `A(S)`, `E(S)`, and
   `D(S)`;
2. performing exactly those operations makes `S` a valid witness and makes the
   repaired J3 kernel admissible;
3. the exact global optimum is
   \[
   R^*=\min_{\varnothing\neq S\subseteq W}R(S);
   \]
4. with strictly positive contract-changing costs, `R*=0` iff the original J3
   problem is admissible;
5. distinct repairs can tie, so all optimal retained-subset witnesses are returned;
   and
6. increasing declared costs cannot reduce `R*`.

Analytic source:

- `docs/crest_minimum_common_lift_relaxation_theorem_2026-08-17.md`

Executable source:

- `mrm/crest_common_lift_relaxation.py`
- `tests/test_crest_common_lift_relaxation.py`
- `tests/test_crest_common_lift_relaxation_degenerate_ties.py`

The exhaustive solver checks all `2^|W|-1` nonempty subsets and reruns every selected
repair through J3. This is an exact finite theorem oracle, not a polynomial
scalability claim. Minimum-cost model repair is prior substrate. J4 is not MLTR
inherited-semantic repair.

## 3. CREST-J1 — unique coarsest state on a fixed common carrier

Given a finite common carrier `U`, baseline partition `B`, and four monotone,
inflationary, idempotent audit closures

\[
C_\Gamma,C_\mathcal H,C_\Theta,C_{D,T}:\Pi(U)\to\Pi(U),
\]

their join closure has a unique least common fixed point above `B`:

\[
J=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B).
\]

Proved:

1. `J` is the unique coarsest partition satisfying all four representational
   obligations;
2. fair cyclic refinement converges to `J` without pairwise audit commutation;
3. one pass through separately minimized audits can be insufficient;
4. a deterministic full joint-state label is evidence-licensed iff the
   reliability-qualified evidence partition refines `J`;
5. otherwise the sharp state report is the set of `J` blocks compatible with the
   evidence class; and
6. a requested target may be deterministic even when the full joint state is not.

Analytic source:

- `docs/crest_joint_state_theorem_2026-08-17.md`

Executable source:

- `mrm/crest_joint_state.py`
- `tests/test_crest_joint_state.py`

Least common fixed points and fair closure iteration are prior substrate. The CREST
result is the conditional four-contract mapping, noncommuting witness, and evidence
existence/no-go gate.

## 4. CREST-J2 — faithful-lift invariance

Let `pi:U -> V` be a surjective finite contract projection preserving by pullback:

- baseline, evidence, and target-equality partitions;
- audit-static distinctions;
- action columns and action legality; and
- projected partial successors.

Then every audit closure is natural:

\[
C_i^U(\pi^*P)=\pi^*C_i^V(P).
\]

Consequently,

\[
J_U=\pi^*J_V,
\qquad
U/J_U\cong V/J_V.
\]

Proved:

1. redundant latent-world duplication cannot change the joint quotient;
2. full-state and target-only evidence licensing are preserved;
3. two lifts with a shared faithful reduction have isomorphic joint quotients; and
4. an audit-visible duplicate can break the projection and strictly enlarge the
   joint state.

Analytic source:

- `docs/crest_lift_invariance_theorem_2026-08-17.md`

Executable source:

- `mrm/crest_lift_invariance.py`
- `tests/test_crest_lift_invariance.py`

Generic quotient naturality and strong preservation are prior substrate. J2 gives
the explicit cross-contract faithful-lift condition and its visibility obstruction.

## 5. CREST-J5 — one-sided lift refinement bounds

J5 compares lifts when exact J2 faithfulness fails in a controlled direction.
Evidence and report-target partitions remain exact pullbacks, and every shared action
retains exact legality and projected successor semantics.

### Source-stronger projection

The source baseline and audit-static partitions refine the pulled target partitions,
and every target action is retained while the source may add actions. For every
audit closure,

\[
\pi^*C_i^V(P)
\preceq
C_i^U(\pi^*P).
\]

Fair joint iteration yields

\[
\boxed{
\pi^*J_V\preceq J_U,
\qquad
|U/J_U|\ge |V/J_V|.
}
\]

### Source-weaker projection

The source baseline and audit-static partitions are coarser than the target
pullbacks, and every source action occurs in the target while the target may add
actions. Then

\[
C_i^U(\pi^*P)
\preceq
\pi^*C_i^V(P),
\]

and

\[
\boxed{
J_U\preceq\pi^*J_V,
\qquad
|U/J_U|\le |V/J_V|.
}
\]

Proved:

1. added preserved obligations can only refine the joint state;
2. forgotten obligations can only coarsen it;
3. satisfying both directions recovers J2 equality;
4. target-only licensing is invariant under exact evidence/target pullback;
5. in the stronger-source case, source full-state licensing implies target
   licensing, with converse failure witnessed; and
6. in the weaker-source case, target full-state licensing implies source licensing,
   with converse failure witnessed.

Analytic source:

- `docs/crest_lax_lift_bounds_theorem_2026-08-18.md`

Executable source:

- `mrm/crest_lax_lift.py`
- `tests/test_crest_lax_lift.py`

The tests exhaustively verify both closure inequalities for every audit and all five
partitions of a three-world target carrier. Strict witnesses give four-versus-three
states after adding a mechanism-visible duplicate and two-versus-three states after
forgetting a future action.

One-sided closure comparison, simulation, abstraction soundness, and precision
ordering are prior substrate. J5's program role is the explicit CREST direction of
fit and the corresponding evidence-licensing asymmetry.

## 6. Dependency structure

```text
declared ambient synchronization
  -> J3: maximal coherent/coverage-tested carrier U* or finite no-go
  -> if no-go, J4: exact least-cost repair in a declared operation/cost language
  -> repaired J3 carrier
  -> J1: unique coarsest four-audit joint partition J
  -> J1: evidence licenses J, only a target, or neither
  -> compare alternate lifts/contracts:
       J2: exact faithful equality and quotient isomorphism
       J5: one-sided refinement/coarsening bounds
```

The results concern distinct objects:

- J3 — greatest **carrier**;
- J4 — minimum-cost **contract weakening**;
- J1 — least-information **partition**;
- J2 — exact **morphism/invariance**;
- J5 — one-sided **morphism/order comparison**.

They are not five renamed partition-refinement claims.

## 7. Current strongest theorem-level statement

For one declared finite ambient synchronization:

1. compute `U*` by J3;
2. if J3 fails, declare a J4 operation language and costs, compute the exact minimum
   value, and retain all optimal witnesses;
3. rerun J3 on a selected optimal repair;
4. declare audit/evidence/target partitions on the admissible carrier;
5. compute the unique coarsest required state `J` by J1; and
6. report `J` deterministically exactly when the evidence partition refines it.

Across other lifts:

\[
\boxed{
\begin{aligned}
&\pi\text{ faithful}
\Longrightarrow J_U=\pi^*J_V,\\
&\pi\text{ source-stronger}
\Longrightarrow \pi^*J_V\preceq J_U,\\
&\pi\text{ source-weaker}
\Longrightarrow J_U\preceq\pi^*J_V.
\end{aligned}}
\]

## 8. What remains conditional

Proved uniqueness is inside one declared finite audit contract, with equality across
faithfully equivalent lifts and order bounds across J5-comparable lifts.

Not proved:

- one nature-given ambient synchronization;
- uniqueness across incompatible component alignments, targets, evidence,
  mechanism families, future grammars, repair languages, or cost schedules;
- that every nonfaithful projection satisfies one J5 direction;
- comparison when shared action semantics only simulate rather than commute exactly;
- that every arbitrary four-repository model admits a coverage-complete carrier;
- that the four axes exhaust all philosophical criteria of ecological state; or
- that cross-axis complexity/risk quantities add.

J4 does not prove a unique repair under ties. J5 does not say that a stronger
contract is scientifically better; it only orders the required distinctions after
the contracts are declared.

## 9. Prior-art firewall

The following are not CREST novelty claims:

- closure operators and least common fixed points;
- fair/chaotic iteration;
- finite partition refinement and strong preservation;
- quotient naturality under homomorphisms;
- simulation and abstraction precision inequalities;
- greatest invariant or safety kernels;
- minimum-cost model repair, transition deletion, and exhaustive subset search;
- target reportability as factorization through an evidence partition.

The candidate program contribution is the ecology-specific coupling and diagnostic
sequence, not the generic algebraic or optimization algorithms.

## 10. Philosophy-manuscript boundary

The current philosophy manuscript correctly denies an **unconditional universal**
joint state and an objectively unique repair. J1–J5 support the narrower statement:

> after an ambient synchronization, repair language, audit contract, evidence, and
> comparison map are declared, CREST can return a maximal carrier or no-go, price the
> least declared repair, construct one coarsest four-audit state, identify what the
> evidence licenses, and distinguish exact lift equivalence from one-sided changes
> in required state resolution.

This theorem ladder must not be rewritten as a canonical ontology, a proof that one
contract is normatively best, or a mathematical ranking of ecological values.

## 11. Next proof questions

1. controlled/existential rather than universal common-lift viability;
2. weakest simulation conditions when shared actions do not commute exactly;
3. quantitative bounds from approximate lift faithfulness;
4. richer repair languages and comparison of their optima;
5. stochastic, approximate, infinite, and risk-limited variants; and
6. empirical inference/validation of synchronization, costs, and contracts.
