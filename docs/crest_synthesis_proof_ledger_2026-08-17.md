# CREST synthesis proof ledger — J1/J2/J3/J4/J5/J6/J7

> **Status:** canonical cross-contract proof ledger. Last synchronized
> 2026-08-18. `crest_proof_recovery_2026-08-17.md` remains the detailed audit of
> CCOC, MLTR, MRM, and CED before synthesis.

## Status convention

- **A:** quantified analytic proof plus executable witness/tests.
- **B:** analytic proof only.
- **C:** finite replay/oracle only.
- **D:** proof gap.
- **N/A:** architecture or philosophical interpretation rather than theorem.

Green CI guards implementation and replay. It is not itself the proof of a
quantified theorem.

## Theorem baselines

- **J1:** `96130b91c1f5b8d4512869545dd598af02e14361`
- **J2:** `f38d954a94eb76cf51f43144c7ace38c3c6b72c5`
- **J3:** `6b50d1334a62fb4c63c67fc0164f0dedb60ec21d`
- **J4:** `19ac2ede0b5c8311c36b03c350800e330e7b62fd`
- **J5:** `e96b99cea6a217fefdbfab62025595c85fffed94`
- **J6:** `2b687d3797a4403cb0eadb939328cb2d97939496`
- **J7:** `59b521d4c9a4bfa5e11bc057d835e61de96079ae`

All seven current synthesis results are **Status A**.

## 1. Carrier gates

### J3 — maximal universal common carrier

For finite ambient worlds `W`, compatible set `W0`, partial deterministic legal
actions, and component-coverage requirements, descending iteration of

\[
F(S)=\{w\in S\cap W_0:
\tau_a(w)\downarrow\Rightarrow\tau_a(w)\in S
\text{ for every declared action }a\}
\]

returns the unique greatest compatible transition-closed carrier `U*`.

Proved:

1. a nonempty universal common lift exists iff `U*` is nonempty;
2. a coverage-complete lift exists iff `U*` represents every required component
   label; and
3. each eliminated world has a finite rank-decreasing action-chain certificate.

Sources:

- `docs/crest_maximal_common_lift_theorem_2026-08-17.md`
- `mrm/crest_common_lift.py`
- `tests/test_crest_common_lift.py`

### J6 — maximal controlled common carrier

Partition actions into uncontrollable `A_u` and controllable `A_c`. Define

\[
\begin{aligned}
G(S)=\{w\in S\cap W_0:\;&
\forall a\in A_u,
\tau_a(w)\downarrow\Rightarrow\tau_a(w)\in S,\\
&\exists a\in A_c,
\tau_a(w)\downarrow\text{ and }\tau_a(w)\in S\}.
\end{aligned}
\]

Descending iteration returns the unique greatest robustly controlled-invariant
carrier `K*`.

Proved:

1. a nonempty controlled lift exists iff `K*` is nonempty;
2. a coverage-complete controlled lift exists iff `K*` represents every required
   label;
3. every nonempty `K*` admits a deterministic memoryless safe selector;
4. every eliminated world has a finite AND/OR certificate for static
   incompatibility, uncontrollable escape, or failure of every control choice; and
5. under explicit control nonblocking, the corresponding J3 carrier is contained
   in the J6 carrier, with strict inclusion witnessed.

Sources:

- `docs/crest_controlled_common_lift_theorem_2026-08-18.md`
- `mrm/crest_controlled_lift.py`
- `tests/test_crest_controlled_lift.py`

The executable witness gives

\[
U^*_{J3}=\{\mathsf{safe}\}
\subsetneq
K^*_{J6}=\{\mathsf{safe},\mathsf{choice}\}.
\]

J3 and J6 answer different action quantifiers; neither supersedes the other.

## 2. Typed carrier-repair gates

### J4 — exact repair of a failed universal J3 contract

The declared operation language permits:

1. admitting an originally incompatible world;
2. disabling an originally legal transition; and
3. waiving one component-coverage obligation.

For nonempty retained subset `S`, define

\[
\begin{aligned}
A(S)&=S\setminus W_0,\\
E(S)&=\{(w,a):w\in S,\tau_a(w)\downarrow,
                  \tau_a(w)\notin S\},\\
D(S)&=\{(k,\ell):\ell\in R_k,\ell\notin p_k(S)\}.
\end{aligned}
\]

The exact fixed-witness cost is

\[
R(S)=\sum_{w\in A(S)}c_w+
\sum_{(w,a)\in E(S)}d_{w,a}+
\sum_{(k,\ell)\in D(S)}r_{k,\ell},
\]

and the global optimum is

\[
\boxed{R^*=\min_{\varnothing\neq S\subseteq W}R(S).}
\]

Necessity and sufficiency coincide. With strictly positive changing costs,
`R*=0` iff the original J3 problem is admissible. Optimal repairs may tie.

Sources:

- `docs/crest_minimum_common_lift_relaxation_theorem_2026-08-17.md`
- `mrm/crest_common_lift_relaxation.py`
- related tests

### J7 — exact repair of a failed controlled J6 contract

J7 preserves the uncontrollable/controllable distinction. Its declared operation
language permits:

1. admitting an originally incompatible world;
2. disabling an **uncontrollable** transition;
3. installing one declared local fallback control; and
4. waiving one component-coverage obligation.

For nonempty retained subset `S`, let `A(S)` and `D(S)` be as above, and define

\[
U(S)=\{(w,a):w\in S,\ a\in A_u,
\tau_a(w)\downarrow,\tau_a(w)\notin S\},
\]

\[
C(S)=\{w\in S:\nexists a\in A_c
\text{ with }\tau_a(w)\downarrow\text{ and }\tau_a(w)\in S\}.
\]

A subset is repair-feasible only if every `w` in `C(S)` has a declared fallback
successor `f(w)` lying in `S`. For feasible `S`,

\[
R_c(S)=
\sum_{w\in A(S)}c_w+
\sum_{(w,a)\in U(S)}d_{w,a}+
\sum_{w\in C(S)}g_w+
\sum_{(k,\ell)\in D(S)}r_{k,\ell}.
\]

If `F` is the family of repair-feasible nonempty subsets, then

\[
\boxed{R_c^*=\min_{S\in\mathcal F}R_c(S)}
\]

when `F` is nonempty. If `F` is empty, no repair exists in the declared language.

Proved:

1. the four operation sets are forced for every fixed feasible witness `S`;
2. applying exactly those operations makes `S` controlled-invariant and satisfies
   every unwaived coverage obligation;
3. the displayed minimum is the exact global optimum in the declared language;
4. with strictly positive changing costs, `R_c*=0` iff the original J6 problem is
   admissible;
5. optimal repair may tie and all optimal retained-subset witnesses are returned;
6. increasing declared operation costs cannot lower the optimum; and
7. a repair language with no feasible retained subset returns an exact no-repair
   result rather than silently weakening the theorem.

Sources:

- `docs/crest_minimum_controlled_lift_relaxation_theorem_2026-08-18.md`
- `mrm/crest_controlled_lift_relaxation.py`
- `tests/test_crest_controlled_lift_relaxation.py`

The canonical witness has three scientifically different repair routes:

- install one local safe fallback;
- block one uncontrollable hazard edge; or
- waive the missing coverage obligation.

Declared costs select the optimum; equal costs can produce multiple optimal
repairs. J7 does not infer action roles, fallback feasibility, or ecological costs.

J4 and J7 are not interchangeable, and neither is MLTR semantic repair. J4/J7
weaken cross-component carrier contracts before J1 constructs a state. MLTR repairs
one inherited macro-law after structural replacement.

## 3. Joint state and evidence

### J1 — unique coarsest four-audit state

On one admissible finite carrier `U`, with baseline `B` and monotone inflationary
idempotent audit closures,

\[
J=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B)
\]

is the unique least-information common fixed point.

Proved:

1. fair iteration reaches `J` without pairwise commutation;
2. one pass through separately minimized audits can be insufficient;
3. full deterministic state reporting exists iff `J\preceq E_D`;
4. failure gives the sharp set of compatible `J` blocks; and
5. target reporting may remain deterministic without full-state identification.

Sources:

- `docs/crest_joint_state_theorem_2026-08-17.md`
- `mrm/crest_joint_state.py`
- `tests/test_crest_joint_state.py`

## 4. Lift and contract comparison

### J2 — faithful-lift invariance

For a surjective contract projection `pi:U -> V` preserving baseline, evidence,
target, audit labels, action legality, and successors exactly,

\[
C_i^U(\pi^*P)=\pi^*C_i^V(P),
\]

so

\[
\boxed{J_U=\pi^*J_V,\qquad U/J_U\cong V/J_V.}
\]

Full-state and target-only licensing are invariant. Audit-visible latent duplication
can break the condition and refine the state.

Sources:

- `docs/crest_lift_invariance_theorem_2026-08-17.md`
- `mrm/crest_lift_invariance.py`
- `tests/test_crest_lift_invariance.py`

### J5 — one-sided lift-refinement bounds

With exact evidence/target pullback and exact shared-action semantics:

\[
\boxed{
\text{source stronger}\Rightarrow\pi^*J_V\preceq J_U,
}
\]

\[
\boxed{
\text{source weaker}\Rightarrow J_U\preceq\pi^*J_V.
}
\]

Both directions recover J2 equality. Target-only licensing is invariant. Full-state
licensing is one-sided in the corresponding direction. Strict four-versus-three
and two-versus-three witnesses are executable.

Sources:

- `docs/crest_lax_lift_bounds_theorem_2026-08-18.md`
- `mrm/crest_lax_lift.py`
- `tests/test_crest_lax_lift.py`

## 5. Dependency structure

```text
declared ambient synchronization
  -> choose action quantification:
       J3 universal safety under every legal action
       J6 robust safety under every uncontrollable move + one safe control
  -> maximal carrier or finite typed no-go
  -> choose matching repair language if declared:
       J4 exact universal-carrier repair
       J7 exact controlled-carrier repair
  -> admissible carrier
  -> J1 unique coarsest four-audit state + evidence gate
  -> alternate lift/contract comparison:
       J2 exact faithful equality
       J5 one-sided refinement/coarsening bounds
```

The mathematical objects differ:

- J3/J6 — greatest **carrier** problems;
- J4/J7 — minimum-cost **typed contract-repair** problems;
- J1 — least-information **partition** problem;
- J2 — exact **morphism/invariance** problem; and
- J5 — one-sided **morphism/order-comparison** problem.

## 6. Current strongest safe statement

For one declared finite synchronization and action contract:

\[
\boxed{
\begin{aligned}
&\mathrm{J3}\text{ or }\mathrm{J6}
\Longrightarrow
\text{one maximal carrier or finite typed no-go},\\
&\mathrm{J6}\text{ nonempty}
\Longrightarrow
\text{one memoryless safe selector exists},\\
&\mathrm{J3\ no\mbox{-}go}+\text{declared J4 language/costs}
\Longrightarrow
\text{exact universal repair optimum},\\
&\mathrm{J6\ no\mbox{-}go}+\text{declared J7 language/costs}
\Longrightarrow
\text{exact controlled repair optimum or no feasible repair},\\
&\text{admissible carrier}
\Longrightarrow
\text{one unique coarsest joint state }J,\\
&\text{fully licensed state}
\Longleftrightarrow J\preceq E_D,\\
&\pi\text{ faithful}
\Longrightarrow J_U=\pi^*J_V,\\
&\pi\text{ one-sided}
\Longrightarrow
\text{the corresponding J5 partition bound.}
\end{aligned}}
\]

## 7. Remaining boundaries

Not proved:

- a nature-given synchronization, action-role assignment, fallback, or cost scale;
- that every companion model admits a coverage-complete J3 or J6 carrier;
- reward/cost optimality of a J6 selector beyond safety;
- exhaustiveness of the J4/J7 repair languages;
- arbitrary transition redirection or action-role reclassification;
- comparison under partial or approximate action simulation;
- stochastic, partial-observation, delayed-control, infinite, or risk-limited forms;
- philosophical exhaustiveness of the four audits; or
- empirical validity of any declared contract.

A stronger contract is not thereby normatively better. J3 is not superseded by J6,
and J4 is not superseded by J7; they answer different action quantifications.

## 8. Prior-art firewall

The following are not CREST novelty claims:

- closure operators, fair iteration, and partition refinement;
- invariant, viability, and safety kernels;
- finite safety games and memoryless safety policies;
- minimum-cost model/safety-game repair and exhaustive subset search;
- quotient naturality, simulation, and abstraction precision; and
- target reportability as evidence factorization.

The candidate contribution is the ecology-specific contract coupling and typed
diagnostic chain, not the generic algorithms.

## 9. Next-proof gate

The remaining directions are broader and should not be opened automatically:

1. partial-observation and finite-memory control;
2. stochastic/adversarial risk-limited safety and repair;
3. weakest or approximate lift simulation;
4. richer repair-language comparison; and
5. empirical inference of synchronization, action roles, fallbacks, costs, and
   evidence.

Any next theorem must change a coupled premise or prove a new impossibility,
noncommutation, or minimality result. A relabelled viability, repair, or refinement
algorithm does not qualify.
