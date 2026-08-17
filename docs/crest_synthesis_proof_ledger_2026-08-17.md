# CREST synthesis proof ledger — J1/J2/J3/J4/J5/J6

> **Status:** canonical cross-contract proof ledger. Last synchronized
> 2026-08-18. `crest_proof_recovery_2026-08-17.md` remains the detailed proof audit
> for CCOC, MLTR, MRM, and CED before synthesis.

## Status convention

- **A:** quantified analytic proof plus executable witness/tests.
- **B:** analytic proof only.
- **C:** finite replay/oracle only.
- **D:** proof gap.
- **N/A:** architecture or philosophical interpretation rather than theorem.

Green CI guards the implementation surface; it is not itself a mathematical proof.

## Theorem baselines

- **J1:** `96130b91c1f5b8d4512869545dd598af02e14361`
- **J2:** `f38d954a94eb76cf51f43144c7ace38c3c6b72c5`
- **J3:** `6b50d1334a62fb4c63c67fc0164f0dedb60ec21d`
- **J4:** `19ac2ede0b5c8311c36b03c350800e330e7b62fd`
- **J5:** `e96b99cea6a217fefdbfab62025595c85fffed94`
- **J6:** `2b687d3797a4403cb0eadb939328cb2d97939496`

All six current synthesis results are **Status A**.

## J3 — maximal universal common carrier

For a finite ambient synchronization with compatible worlds \(W_0\), partial
deterministic actions, and component-coverage requirements, descending iteration of

\[
F(S)=\{w\in S\cap W_0:
\tau_a(w)\downarrow\Rightarrow\tau_a(w)\in S
\text{ for every declared action }a\}
\]

returns the unique greatest compatible transition-closed carrier \(U^*\).

Proved:

1. nonempty common lift exists iff \(U^*\neq\varnothing\);
2. coverage-complete lift exists iff \(U^*\) represents all required labels; and
3. each eliminated world has a finite rank-decreasing action-chain certificate.

Sources:

- `docs/crest_maximal_common_lift_theorem_2026-08-17.md`
- `mrm/crest_common_lift.py`
- `tests/test_crest_common_lift.py`

Generic invariant/safety-kernel mathematics is prior substrate.

## J6 — maximal controlled common carrier

Partition actions into uncontrollable \(A_u\) and controllable \(A_c\). Define

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
carrier \(K^*\).

Proved:

1. nonempty controlled common lift exists iff \(K^*\neq\varnothing\);
2. coverage-complete controlled lift exists iff \(K^*\) represents all required
   labels;
3. every nonempty \(K^*\) admits a deterministic memoryless safe selector;
4. every eliminated world has a finite typed AND/OR certificate for static
   incompatibility, uncontrollable escape, or failure of every control choice; and
5. under explicit control nonblocking, the corresponding J3 universal carrier is a
   subset of the J6 carrier, with strict inclusion witnessed.

Sources:

- `docs/crest_controlled_common_lift_theorem_2026-08-18.md`
- `mrm/crest_controlled_lift.py`
- `tests/test_crest_controlled_lift.py`

The five-world witness gives

\[
U^*_{\mathrm{J3}}=\{\mathsf{safe}\}
\subsetneq
K^*_{\mathrm{J6}}=\{\mathsf{safe},\mathsf{choice}\}.
\]

Greatest controlled-invariant kernels and memoryless finite safety policies are
prior substrate. J6's CREST role is the typed carrier gate and finite ecology-facing
failure certificate.

## J4 — exact declared relaxation after J3 no-go

For the repair language

- admit incompatible world \(w\) at cost \(c_w\);
- disable transition \((w,a)\) at cost \(d_{w,a}\); and
- waive coverage requirement \((k,\ell)\) at cost \(r_{k,\ell}\),

define for every nonempty retained subset \(S\):

\[
\begin{aligned}
A(S)&=S\setminus W_0,\\
E(S)&=\{(w,a):w\in S,\tau_a(w)\downarrow,
                  \tau_a(w)\notin S\},\\
D(S)&=\{(k,\ell):\ell\in R_k,\ell\notin p_k(S)\}.
\end{aligned}
\]

The forced fixed-witness cost is

\[
R(S)=\sum_{w\in A(S)}c_w+
\sum_{(w,a)\in E(S)}d_{w,a}+
\sum_{(k,\ell)\in D(S)}r_{k,\ell},
\]

and

\[
\boxed{R^*=\min_{\varnothing\neq S\subseteq W}R(S).}
\]

Necessity and sufficiency coincide. With strictly positive changing costs,
\(R^*=0\) iff the original J3 problem is admissible. Optimal repair may tie.

Sources:

- `docs/crest_minimum_common_lift_relaxation_theorem_2026-08-17.md`
- `mrm/crest_common_lift_relaxation.py`
- related tests

This theorem currently repairs the J3 universal contract. It is not yet an exact
repair theorem for J6 policy/action-role failures.

## J1 — unique coarsest four-audit state

On one finite carrier \(U\), with baseline \(B\) and monotone inflationary idempotent
audit closures,

\[
J=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B)
\]

is the unique least-information common fixed point.

Proved:

1. fair iteration reaches \(J\) without pairwise commutation;
2. one pass through separately minimized audits can be insufficient;
3. full deterministic state reporting exists iff \(J\preceq E_D\);
4. failure gives the sharp set of compatible `J` blocks; and
5. target reporting may remain deterministic without full-state identification.

Sources:

- `docs/crest_joint_state_theorem_2026-08-17.md`
- `mrm/crest_joint_state.py`
- `tests/test_crest_joint_state.py`

Least common closure fixed points are prior substrate.

## J2 — faithful-lift invariance

For a surjective contract projection \(\pi:U\twoheadrightarrow V\) preserving all
baseline, evidence, target, audit, legality, and successor structure,

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

## J5 — one-sided lift refinement bounds

With exact evidence/target pullback and exact shared-action semantics:

- **source stronger:** finer baseline/static obligations and all target actions,
  possibly more actions;
- **source weaker:** coarser obligations and a subset of target actions.

Proved:

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
licensing is one-sided in the corresponding direction. Strict four-versus-three and
two-versus-three witnesses are executable.

Sources:

- `docs/crest_lax_lift_bounds_theorem_2026-08-18.md`
- `mrm/crest_lax_lift.py`
- `tests/test_crest_lax_lift.py`

Simulation/abstraction precision order is prior substrate.

## Dependency structure

```text
declared ambient synchronization
  -> choose action quantification:
       J3 universal safety under every legal action
       J6 robust safety under every uncontrollable move + one safe control
  -> maximal carrier or finite typed no-go
  -> if using the current universal repair language:
       J4 exact least-cost J3 relaxation
  -> admissible carrier
  -> J1 unique coarsest four-audit state + evidence gate
  -> alternate lift comparison:
       J2 exact faithful equality
       J5 one-sided refinement/coarsening bounds
```

The objects and order directions differ:

- J3/J6 — greatest **carrier** problems;
- J4 — minimum-cost **contract weakening**;
- J1 — least-information **partition**;
- J2 — exact **morphism/invariance**;
- J5 — one-sided **morphism/order comparison**.

## Current strongest safe statement

For one declared finite synchronization and action contract:

\[
\boxed{
\begin{aligned}
&\mathrm{J3}\text{ or }\mathrm{J6}
\Longrightarrow
\text{one maximal carrier or finite no-go},\\
&\mathrm{J6}\text{ nonempty}
\Longrightarrow
\text{one memoryless safe selector exists},\\
&\mathrm{J3\ no\mbox{-}go}+\text{declared J4 costs}
\Longrightarrow
\text{exact minimum repair value},\\
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

## What remains conditional

Not proved:

- a nature-given synchronization or controllability classification;
- that every companion model admits a coverage-complete J3 or J6 carrier;
- cost/reward optimality of a J6 selector;
- exact minimum repair for a failed controlled-J6 contract;
- comparison under partial or approximate action simulation;
- stochastic, partial-observation, delayed-control, infinite, or risk-limited forms;
- philosophical exhaustiveness of the four audits; or
- empirical validity of any declared contract.

A stronger contract is not thereby normatively better, and J3 is not superseded by
J6. They answer different quantifications over future actions.

## Prior-art firewall

The following are not CREST novelty claims:

- closure operators, fair iteration, and partition refinement;
- invariant, viability, and safety kernels;
- finite safety games and memoryless safety policies;
- minimum-cost model repair and exhaustive subset search;
- quotient naturality, simulation, and abstraction precision;
- target reportability as evidence factorization.

The candidate contribution is the ecology-specific contract coupling and typed
diagnostic chain, not the generic algorithms.

## Next proof questions

1. exact minimum repair of a failed controlled-J6 contract;
2. partial-observation and finite-memory control;
3. stochastic/adversarial risk-limited safety;
4. weakest/approximate lift simulations; and
5. empirical inference of synchronization, action roles, costs, and evidence.
