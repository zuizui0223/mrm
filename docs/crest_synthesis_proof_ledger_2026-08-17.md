# CREST synthesis proof ledger — J1/J2/J3/J4/J5/J6/J7 + O1

> **Status:** canonical cross-contract proof ledger. Last synchronized
> 2026-08-18. The J/O series is owned by the separate CREST synthesis unit,
> temporarily hosted in the MRM repository. `crest_proof_recovery_2026-08-17.md`
> remains the detailed audit of CCOC, MLTR, MRM, and CED before synthesis.

## Status convention

- **A:** quantified analytic proof plus executable witness/tests.
- **B:** analytic proof only.
- **C:** finite replay/oracle only.
- **D:** proof gap.
- **N/A:** architecture or philosophical interpretation rather than theorem.

Green CI guards implementation and replay. It is not itself the proof of a
quantified theorem.

## Ownership and freeze

J1–J7 and O1 are not part of the MRM mechanism theorem family. They form a fifth
logical unit because their statements essentially couple multiple companion
contracts. See:

- `crest_synthesis/README.md`;
- `docs/crest_synthesis_migration_manifest_2026-08-18.md`; and
- `docs/crest_next_proof_novelty_gate_2026-08-18.md`.

No J8 or new O-family may be added under `mrm/` before extraction to the dedicated
CREST repository.

## Theorem baselines

- **J1:** `96130b91c1f5b8d4512869545dd598af02e14361`
- **J2:** `f38d954a94eb76cf51f43144c7ace38c3c6b72c5`
- **J3:** `6b50d1334a62fb4c63c67fc0164f0dedb60ec21d`
- **J4:** `19ac2ede0b5c8311c36b03c350800e330e7b62fd`
- **J5:** `e96b99cea6a217fefdbfab62025595c85fffed94`
- **J6:** `2b687d3797a4403cb0eadb939328cb2d97939496`
- **J7:** `59b521d4c9a4bfa5e11bc057d835e61de96079ae`

All seven theorem results remain **Status A**. O1 is a proved executable obstruction,
not a new theorem-family baseline.

## 1. Carrier gates

### J3 — maximal universal common carrier — Status A

Descending iteration of

\[
F(S)=\{w\in S\cap W_0:
\tau_a(w)\downarrow\Rightarrow\tau_a(w)\in S
\text{ for every declared action }a\}
\]

returns the unique greatest compatible transition-closed carrier `U*`.

Proved:

1. nonempty universal common lift iff `U*` is nonempty;
2. coverage-complete lift iff `U*` represents every required label; and
3. each eliminated world has a finite rank-decreasing action-chain certificate.

Sources:

- `docs/crest_maximal_common_lift_theorem_2026-08-17.md`
- `mrm/crest_common_lift.py`
- `tests/test_crest_common_lift.py`

### J6 — maximal controlled common carrier — Status A

Descending iteration of

\[
\begin{aligned}
G(S)=\{w\in S\cap W_0:\;&
\forall a\in A_u,
\tau_a(w)\downarrow\Rightarrow\tau_a(w)\in S,\\
&\exists a\in A_c,
\tau_a(w)\downarrow\text{ and }\tau_a(w)\in S\}
\end{aligned}
\]

returns the unique greatest robustly controlled-invariant carrier `K*`.

Proved:

1. nonempty controlled lift iff `K*` is nonempty;
2. coverage-complete controlled lift iff `K*` represents every required label;
3. every nonempty `K*` admits a deterministic memoryless safe selector;
4. eliminated worlds have finite typed AND/OR certificates; and
5. under control nonblocking, the corresponding J3 carrier is contained in the J6
   carrier, with strict inclusion witnessed.

Sources:

- `docs/crest_controlled_common_lift_theorem_2026-08-18.md`
- `mrm/crest_controlled_lift.py`
- `tests/test_crest_controlled_lift.py`

J3 and J6 answer different action quantifiers; neither supersedes the other.

## 2. Typed carrier-repair gates

### J4 — universal J3 repair characterization — Status A

For fixed nonempty retained subset `S`,

\[
R(S)=\sum_{w\in A(S)}c_w+
\sum_{(w,a)\in E(S)}d_{w,a}+
\sum_{(k,\ell)\in D(S)}r_{k,\ell}
\]

is both necessary and sufficient. The global value is

\[
\boxed{R^*=\min_{\varnothing\neq S\subseteq W}R(S).}
\]

Proved:

1. the operation set is forced conditional on `S`;
2. those operations make `S` a valid J3 witness;
3. every admissible repair is lower-bounded by its repaired kernel's fixed-witness
   cost;
4. positive-cost zero iff the original J3 problem is admissible;
5. tied optima are retained explicitly; and
6. the J4-REPAIR decision problem is NP-complete by weighted set cover.

The NP-hardness holds with no transitions and binary component labels. The solver's
`2^|W|-1` enumeration is therefore an exact exponential oracle, not a tractability
claim.

Sources:

- `docs/crest_minimum_common_lift_relaxation_theorem_2026-08-17.md`
- `docs/crest_repair_complexity_boundary_2026-08-18.md`
- `mrm/crest_common_lift_relaxation.py`
- J4 and set-cover reduction tests

### J7 — controlled J6 repair characterization — Status A

For a repair-feasible retained subset `S`,

\[
R_c(S)=
\sum_{w\in A(S)}c_w+
\sum_{(w,a)\in U(S)}d_{w,a}+
\sum_{w\in C(S)}g_w+
\sum_{(k,\ell)\in D(S)}r_{k,\ell}
\]

is necessary and sufficient. If `F` is the family of feasible nonempty subsets,

\[
\boxed{R_c^*=\min_{S\in\mathcal F}R_c(S)}
\]

when `F` is nonempty; otherwise the declared language admits no repair.

Proved:

1. fixed-witness operations are forced;
2. applying them makes the witness controlled invariant and coverage complete;
3. every admissible repair is lower-bounded by its repaired J6 kernel;
4. positive-cost zero iff the original J6 problem is admissible;
5. ties, monotonicity, and language-level infeasibility are explicit; and
6. the J7-REPAIR decision problem is NP-complete by weighted set cover.

The hardness already holds with no uncontrollable transitions and one controllable
self-loop per world. The global exponential search cannot be attributed only to
safety-game structure.

Sources:

- `docs/crest_minimum_controlled_lift_relaxation_theorem_2026-08-18.md`
- `docs/crest_repair_complexity_boundary_2026-08-18.md`
- `mrm/crest_controlled_lift_relaxation.py`
- J7 and set-cover reduction tests

J4/J7 are not MLTR semantic repair. They weaken cross-component carrier contracts
before J1 state construction.

## 3. Joint state and evidence

### J1 — unique coarsest four-audit state — Status A

On one admissible finite carrier `U`, with baseline `B` and monotone inflationary
idempotent audit closures,

\[
J=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B)
\]

is the unique least-information common fixed point.

Proved:

1. fair iteration reaches `J` without pairwise commutation;
2. one pass through separately minimized audits can be insufficient;
3. full deterministic state reporting iff `J\preceq E_D`;
4. failure gives the sharp compatible-block set; and
5. a target may remain deterministic without full-state identification.

Sources:

- `docs/crest_joint_state_theorem_2026-08-17.md`
- `mrm/crest_joint_state.py`
- `tests/test_crest_joint_state.py`

The generic least-common-fixed-point result is classical substrate. J1's claim must
remain the conditional four-contract mapping and evidence gate, not a priority claim
for partition refinement.

## 4. Lift and contract comparison

### J2 — faithful-lift invariance — Status A

For a surjective faithful projection `pi:U -> V`,

\[
C_i^U(\pi^*P)=\pi^*C_i^V(P),
\qquad
J_U=\pi^*J_V,
\qquad
U/J_U\cong V/J_V.
\]

Full-state and target-only licensing are invariant. Audit-visible duplication can
break the condition and refine the state.

### J5 — one-sided lift-refinement bounds — Status A

With exact evidence/target pullback and exact shared-action semantics,

\[
\text{source stronger}\Rightarrow\pi^*J_V\preceq J_U,
\]

\[
\text{source weaker}\Rightarrow J_U\preceq\pi^*J_V.
\]

Both directions recover J2 equality. Target-only licensing is invariant;
full-state licensing follows the corresponding one-sided implication.

Sources:

- J2: `docs/crest_lift_invariance_theorem_2026-08-17.md`, implementation, tests
- J5: `docs/crest_lax_lift_bounds_theorem_2026-08-18.md`, implementation, tests

## 5. O1 — repair/evidence ordering obstruction

O1 proves by finite executable witness that

\[
\boxed{R_{\mathrm{struct}}^*=1<R_{\mathrm{licensed}}^*=2.}
\]

The cheapest J7 carrier repair can yield a J1 state not resolved by the declared
evidence, while a costlier repair is fully licensed. The target remains reportable
under the cheaper repair. O1 therefore refutes automatic commutation of structural
repair optimization and downstream full-state licensing.

Sources:

- `docs/crest_repair_evidence_noncommutation_2026-08-18.md`
- `tests/test_crest_repair_evidence_noncommutation.py`

O1 is a supporting obstruction, not J8.

## 6. Dependency structure

```text
declared ambient synchronization
  -> choose action quantification: J3 or J6
  -> maximal carrier or finite typed no-go
  -> choose matching repair language: J4 or J7
  -> exact objective characterization + NP-hard global subset selection
  -> admissible carrier
  -> J1 joint state + evidence gate
  -> J2/J5 lift comparison
  -> O1 warns that structural and fully licensed optima can differ
```

The mathematical objects differ:

- J3/J6 — greatest carrier problems;
- J4/J7 — fixed-witness exactness plus NP-hard global contract-repair selection;
- J1 — least-information partition problem;
- J2 — exact morphism/invariance problem;
- J5 — one-sided morphism/order problem; and
- O1 — cross-gate noncommutation witness.

## 7. Prior-art firewall

Not CREST novelty:

- closure operators, fair iteration, and partition refinement;
- invariant, viability, and safety kernels;
- finite safety games and memoryless policies;
- minimum-cost model repair, weighted set cover, and exhaustive subset search;
- quotient naturality, simulation, and abstraction precision; and
- target reportability as evidence factorization.

The candidate contribution is the ecology-specific contract coupling and typed
failure/repair sequence, not generic algorithms or their complexity classes.

## 8. Remaining boundaries

Not proved:

- nature-given synchronization, action roles, fallbacks, or costs;
- guaranteed coverage-complete J3/J6 carriers for arbitrary companion models;
- reward optimality beyond safety;
- exhaustive J4/J7 repair languages;
- polynomial algorithms or tractable subclass classifications for J4/J7;
- arbitrary redirection or action-role reclassification;
- stochastic, partial-observation, delayed-control, approximate, infinite, or
  risk-limited forms;
- philosophical exhaustiveness of the four audits; or
- empirical validity of declared contracts.

## 9. Development gate

The active line is consolidation and physical extraction, not theorem count. A new
cross-contract result must prove a genuinely new coupled impossibility,
noncommutation, necessary-and-sufficient boundary, or minimality statement. No J8
or new O-family may be implemented under `mrm/`.
