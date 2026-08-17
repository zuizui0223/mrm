# CREST synthesis proof ledger — J1/J2/J3 — 2026-08-17

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

## 2. CREST-J1 — one unique coarsest state on a fixed common carrier

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

## 3. CREST-J2 — invariance across faithfully redundant lifts

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

## 4. Dependency structure

The proved synthesis chain is:

```text
declared ambient synchronization
  -> J3: maximal coherent/coverage-tested common carrier U*
  -> J1: unique coarsest four-audit joint partition J on U*
  -> J1: evidence licenses J, only a target, or neither
  -> J2: faithfully redundant refinements preserve the quotient and licensing
```

These are not three restatements of finite partition refinement.

- J3 is a greatest **carrier** problem under compatibility and transition closure.
- J1 is a least-information **partition** problem on a fixed carrier.
- J2 is a **morphism/invariance** problem across carriers.

Their order-theoretic directions, objects, and failure certificates differ.

## 5. Current strongest theorem-level statement

For one declared finite ambient synchronization:

1. compute `U*` by J3;
2. if `U*` is nonempty and coverage complete, declare the audit/evidence/target
   partitions on it;
3. compute the unique coarsest required state `J` by J1; and
4. report `J` deterministically exactly when the evidence partition refines it.

Across any faithfully redundant lift of this contract, J2 preserves the quotient
state and licensing result.

Compactly:

\[
\boxed{
\begin{aligned}
&U^*\neq\varnothing\text{ and coverage complete}
\\
&\Longrightarrow\text{ one unique coarsest required joint state }J,
\\
&\text{fully licensed deterministic state}
\Longleftrightarrow J\preceq E_D,
\\
&\pi\text{ faithful}
\Longrightarrow J_U=\pi^*J_V.
\end{aligned}}
\]

## 6. What “unique” now means

Proved uniqueness is:

- unique up to block renaming **inside one declared finite contract**;
- invariant across lifts connected by a CREST-faithful reduction; and
- based on the maximal carrier inside one declared ambient synchronization.

Not proved:

- one nature-given ambient synchronization;
- uniqueness across incompatible choices of component alignment, target, evidence,
  mechanism family, or future grammar;
- that every arbitrary four-repository model admits a coverage-complete common
  carrier;
- that the four axes exhaust all philosophical criteria of ecological state; or
- that cross-axis complexity/risk quantities add.

## 7. Prior-art firewall

The following are not CREST novelty claims:

- closure operators and least common fixed points;
- fair/chaotic iteration;
- finite partition refinement and strong preservation;
- quotient naturality under homomorphisms;
- greatest invariant or safety kernels;
- target reportability as factorization through an observation/evidence partition.

The candidate program contribution is the ecology-specific coupling and diagnostic
sequence, not the generic algebraic algorithms.

## 8. Philosophy-manuscript boundary

The current philosophy manuscript remains correct when it denies an **unconditional
universal** joint state. J1–J3 support a narrower formal statement:

> once an ambient synchronization is declared and survives the J3 carrier gate,
> the resulting finite common contract has one coarsest four-audit state, invariant
> under faithful redundant lifting and reportable only when evidence resolves it.

This conditional theorem may be added to the manuscript only after a fresh
claim-ledger and prior-art review. It must not be rewritten as a canonical ontology
of ecological states.

## 9. Next proof questions

High-value unresolved questions are now narrower:

1. minimum relaxation of compatibility, transition, or coverage constraints needed
   to make `U*` admissible;
2. lax/one-sided lift morphisms and upper/lower bounds on joint-state refinement;
3. controlled/existential rather than universal common-lift viability;
4. approximate, stochastic, infinite, and risk-limited variants; and
5. empirical inference/validation of ambient synchronization and contract choices.
