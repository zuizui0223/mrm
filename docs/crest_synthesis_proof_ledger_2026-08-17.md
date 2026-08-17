# CREST synthesis proof ledger — J1/J2/J3/J4 — 2026-08-17

> **Status:** canonical proof ledger for the cross-contract CREST synthesis theorems.
> The earlier `crest_proof_recovery_2026-08-17.md` remains the detailed ledger for
> the four companion theorem programs before synthesis. This document records what
> is now proved across contracts, what is executable, and what remains conditional.

## Proof-status scale

- **A — analytic + executable:** quantified proof plus implementation/witness tests.
- **B — analytic only.**
- **C — executable finite evidence only.**
- **D — proof gap.**
- **N/A — philosophical or architectural claim, not a theorem.**

Green CI is an implementation/replay guard, not the proof of a quantified theorem.

## Theorem baselines

- **CREST-J1:** `96130b91c1f5b8d4512869545dd598af02e14361`
- **CREST-J2:** `f38d954a94eb76cf51f43144c7ace38c3c6b72c5`
- **CREST-J3:** `6b50d1334a62fb4c63c67fc0164f0dedb60ec21d`
- **CREST-J4:** `19ac2ede0b5c8311c36b03c350800e330e7b62fd`

## 1. CREST-J3 — maximal synchronized common carrier

**Status: A.**

Given:

- a finite ambient set of candidate joint tuples;
- a statically compatible subset `W0`;
- declared partial deterministic lifted actions; and
- required component-coverage labels,

define the universal transition-closure operator

\[
F(S)=\{w\in S\cap W_0:\tau_a(w)\downarrow\Rightarrow\tau_a(w)\in S
\text{ for every declared action }a\}.
\]

Descending iteration from `W0` stabilizes at the greatest fixed point `U*`.

Proved:

1. `U*` is the unique greatest statically compatible transition-closed subset;
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

The generic mathematics is greatest invariant/safety-kernel substrate. The CREST
result is the explicit common-carrier existence/coverage/no-go layer.

## 2. CREST-J4 — exact minimum declared relaxation after J3 no-go

**Status: A.**

Fix one J3 ambient problem and a finite weighted repair language:

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

1. every repair retaining `S` must contain all operations in `A(S)`, `E(S)`, and
   `D(S)`;
2. performing exactly those operations makes `S` a valid witness and forces the
   repaired J3 maximal kernel to be admissible;
3. the exact global optimum is
   \[
   R^*=\min_{\varnothing\neq S\subseteq W}R(S);
   \]
4. with strictly positive contract-changing costs, `R*=0` iff the original J3
   problem is admissible;
5. distinct repairs can tie, so the executable result returns all optimal
   retained-subset witnesses and reports whether the optimum is unique; and
6. increasing declared costs cannot reduce `R*`.

Analytic source:

- `docs/crest_minimum_common_lift_relaxation_theorem_2026-08-17.md`

Executable source:

- `mrm/crest_common_lift_relaxation.py`
- `tests/test_crest_common_lift_relaxation.py`
- `tests/test_crest_common_lift_relaxation_degenerate_ties.py`

The exhaustive solver checks all `2^|W|-1` nonempty subsets and reruns every selected
repair through the J3 kernel. It is an exact finite theorem oracle, not a polynomial
scalability claim.

Minimum-cost model repair and weighted subset optimization are prior substrate. The
CREST result is the exact repair calculus for J3's three scientifically typed
failure modes. J4 is not MLTR inherited-semantic repair.

## 3. CREST-J1 — one unique coarsest state on a fixed common carrier

**Status: A.**

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
3. a single pass through four separately minimized audits can be insufficient;
4. a deterministic full joint-state label is evidence-licensed iff the
   reliability-qualified evidence partition refines `J`;
5. otherwise the sharp state report is the set of `J` blocks compatible with the
   evidence class; and
6. a requested target may remain deterministically reportable even when the full
   joint state is unresolved.

Analytic source:

- `docs/crest_joint_state_theorem_2026-08-17.md`

Executable source:

- `mrm/crest_joint_state.py`
- `tests/test_crest_joint_state.py`

The least-common-fixed-point machinery is classical closure-operator substrate.
The CREST contribution is the conditional four-contract mapping, explicit
noncommuting witness, and evidence existence/no-go gate.

## 4. CREST-J2 — invariance across faithfully redundant lifts

**Status: A.**

Let `pi:U -> V` be a surjective finite contract projection preserving, by pullback:

- baseline, evidence, and target-equality partitions;
- audit-static distinctions;
- ordered action columns and action legality; and
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

Generic naturality/congruence/strong-preservation results are established substrate.
The CREST contribution is the explicit cross-contract faithful-lift condition and
its visibility obstruction.

## 5. Dependency structure

The proved synthesis chain is:

```text
declared ambient synchronization
  -> J3: maximal coherent/coverage-tested common carrier U* or finite no-go
  -> if no-go, J4: exact least-cost repair in a declared operation/cost language
  -> repaired J3 carrier
  -> J1: unique coarsest four-audit joint partition J
  -> J1: evidence licenses J, only a target, or neither
  -> J2: faithfully redundant refinements preserve the quotient and licensing
```

These are not four restatements of finite partition refinement.

- J3 is a greatest **carrier** problem under compatibility and transition closure.
- J4 is a minimum-cost **contract weakening** problem over candidate retained
  carriers.
- J1 is a least-information **partition** problem on a fixed carrier.
- J2 is a **morphism/invariance** problem across carriers.

Their order directions, mathematical objects, and failure certificates differ.

## 6. Current strongest theorem-level statement

For one declared finite ambient synchronization:

1. compute `U*` by J3;
2. if J3 fails, declare a J4 operation language and costs, then compute the exact
   minimum repair value and all optimal retained-subset witnesses;
3. rerun J3 on any selected optimal repair;
4. declare the audit/evidence/target partitions on the admissible carrier;
5. compute the unique coarsest required state `J` by J1; and
6. report `J` deterministically exactly when the evidence partition refines it.

Across any faithfully redundant lift of this contract, J2 preserves the quotient
state and licensing result.

Compactly:

\[
\boxed{
\begin{aligned}
&\mathrm{J3}(\mathcal A)=U^*\text{ or finite no-go},\\
&\mathrm{J3\ no\!\mbox{-}\!go}
\Longrightarrow
R^*=\min_{\varnothing\neq S\subseteq W}R(S),\\
&\text{admissible repaired carrier}
\Longrightarrow
\text{one unique coarsest required joint state }J,\\
&\text{fully licensed deterministic state}
\Longleftrightarrow J\preceq E_D,\\
&\pi\text{ faithful}
\Longrightarrow J_U=\pi^*J_V.
\end{aligned}}
\]

## 7. What “unique” now means

Proved uniqueness is:

- unique up to block renaming **inside one declared finite audit contract**;
- invariant across lifts connected by a CREST-faithful reduction; and
- based on the maximal carrier inside one declared ambient synchronization.

J4 does not add unconditional uniqueness of repair. It proves one exact minimum
value and returns all optimal retained-subset witnesses; ties are allowed.

Not proved:

- one nature-given ambient synchronization;
- uniqueness across incompatible component alignments, targets, evidence,
  mechanism families, future grammars, repair languages, or cost schedules;
- that every arbitrary four-repository model admits a coverage-complete common
  carrier;
- that the four axes exhaust all philosophical criteria of ecological state; or
- that cross-axis complexity/risk quantities add.

## 8. Prior-art firewall

The following are not CREST novelty claims:

- closure operators and least common fixed points;
- fair/chaotic iteration;
- finite partition refinement and strong preservation;
- quotient naturality under homomorphisms;
- greatest invariant or safety kernels;
- minimum-cost model repair, transition deletion, and exhaustive subset search;
- target reportability as factorization through an observation/evidence partition.

The candidate program contribution is the ecology-specific coupling and diagnostic
sequence, not the generic algebraic or optimization algorithms.

## 9. Philosophy-manuscript boundary

The current philosophy manuscript remains correct when it denies an **unconditional
universal** joint state and an objectively unique repair. J1–J4 support a narrower
formal statement:

> once an ambient synchronization and repair language are declared, J3 either
> returns a coherent carrier or a finite no-go; J4 can price the least declared
> weakening; J1 then gives one coarsest four-audit state on an admissible carrier;
> J2 removes faithfully redundant lift detail; evidence still controls what may be
> reported.

This theorem ladder may be added to the manuscript only after a fresh claim-ledger
and prior-art review. It must not be rewritten as a canonical ontology or as a
mathematical ranking of ecological values.

## 10. Next proof questions

High-value unresolved questions are now narrower:

1. richer repair languages and comparison of their optimal values;
2. lax/one-sided lift morphisms and upper/lower bounds on joint-state refinement;
3. controlled/existential rather than universal common-lift viability;
4. approximate, stochastic, infinite, and risk-limited variants; and
5. empirical inference/validation of ambient synchronization, costs, and contract
   choices.
