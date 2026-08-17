# CREST-J7 — exact objective characterization for failed controlled-carrier repair

> **Status:** conditional finite synthesis theorem with analytic proof and an
> exhaustive executable oracle. The fixed-witness repair formula is exact, but the
> global retained-subset selection problem is NP-complete. Weighted safety-game and
> model repair, set cover, and finite subset optimization are established substrate.
> CREST-J7 does not claim a new generic repair algorithm or tractability result.

## 1. Question

CREST-J6 returns the greatest finite carrier that:

- contains only statically compatible synchronized worlds;
- survives every legal uncontrollable transition; and
- admits at least one legal safe controllable transition at each retained world.

J6 can fail because the kernel is empty or because it omits a required component
label. J7 asks:

> Given explicit costs and explicitly available fallback controls, how is the
> minimum weakening characterized, and which control-feasible retained subsets
> realize it?

The theorem does not infer costs, invent ecological controls, or decide which
coverage requirement should be negotiable. Those are contract inputs. The supplied
oracle obtains a global optimum by exponential enumeration.

## 2. Declared repair language

Let the original J6 problem have finite worlds `W`, compatible subset `W0`,
uncontrollable actions `A_u`, controllable actions `A_c`, partial deterministic
transitions `tau_a`, component projections `p_k`, and required labels `R_k`.

J7 permits four operation types.

### A. Admit one incompatible world

For `w notin W0`, declare it compatible at cost `c_w`.

### B. Disable one uncontrollable transition

For one originally legal `(w,a)`, `a in A_u`, make the action illegal at that world
at cost `d_{w,a}`. Unsafe controllable transitions need not be disabled because the
controller may avoid them.

### C. Install one declared local fallback control

For each world `w`, the contract may provide one optional fallback successor
`f(w) in W` and installation cost `g_w`. Installing it makes a new globally named
fallback action legal at `w` with successor `f(w)`. If no fallback is declared, the
operation is unavailable.

### D. Waive one coverage obligation

For `ell in R_k`, waive `(k,ell)` at cost `r_{k,ell}`.

All executable costs are finite nonnegative integers. Positive-cost corollaries
assume every contract-changing operation has strictly positive cost.

## 3. Feasible retained witnesses and forced operations

Fix a nonempty subset `S subseteq W`. Define

\[
A(S)=S\setminus W_0,
\]

\[
U(S)=\{(w,a):w\in S,\ a\in A_u,\
\tau_a(w)\downarrow,\ \tau_a(w)\notin S\},
\]

and

\[
D(S)=\{(k,\ell):\ell\in R_k,\ \ell\notin p_k(S)\}.
\]

Let the control-deficient worlds be

\[
C(S)=\left\{w\in S:
\nexists a\in A_c\text{ with }\tau_a(w)\downarrow
\text{ and }\tau_a(w)\in S
\right\}.
\]

Call `S` **repair-feasible** when every `w in C(S)` has a declared fallback with
`f(w) in S`. If not, no operation in this repair language can give that retained
world a safe control.

For a repair-feasible `S`, define

\[
\boxed{
\begin{aligned}
R_c(S)=
&\sum_{w\in A(S)}c_w
+\sum_{(w,a)\in U(S)}d_{w,a}\\
&+\sum_{w\in C(S)}g_w
+\sum_{(k,\ell)\in D(S)}r_{k,\ell}.
\end{aligned}}
\]

## 4. Lemma 1 — fixed-witness necessity

Any repaired contract retaining `S` as a compatible, robustly
controlled-invariant, coverage-complete witness must perform every operation in
`A(S)`, `U(S)`, `C(S)`, and `D(S)`.

- retained incompatible worlds must be admitted;
- retained uncontrollable edges leaving `S` must be disabled;
- control-deficient retained worlds need their declared fallback into `S`; and
- unrepresented required labels must be waived.

These are disjoint operation types, so every repair with witness `S` costs at least
`R_c(S)`.

## 5. Lemma 2 — fixed-witness sufficiency

For repair-feasible `S`, performing exactly those operations makes every retained
world compatible, removes every uncontrollable exit, supplies at least one safe
control at every retained world, and satisfies every unwaived coverage obligation.
Thus `S` is a valid controlled witness, and the repaired J6 maximal kernel contains
it and is admissible.

The two lemmas give

\[
\boxed{
\text{minimum repair cost conditional on retaining }S=R_c(S).
}
\]

This equality concerns a **fixed** retained subset. It does not find the globally
best `S` or imply tractability.

## 6. Theorem — exact global objective characterization or language-level no-go

Let

\[
\mathcal F=\{S\subseteq W:S\neq\varnothing
\text{ and }S\text{ is repair-feasible}\}.
\]

If `F` is nonempty, the minimum controlled-carrier repair cost is

\[
\boxed{
R_c^*=\min_{S\in\mathcal F}R_c(S).
}
\]

Every minimizing subset yields an optimal repaired contract by its forced operation
sets. Conversely, every admissible repair has cost at least `R_c(K)`, where `K` is
its repaired J6 maximal kernel. If `F` is empty, no repair exists in the declared
language.

### Proof

For each feasible `S`, Lemma 2 constructs an admissible repair of cost exactly
`R_c(S)`, giving the upper bound.

For any admissible repaired contract, its nonempty maximal J6 kernel `K` is
controlled invariant and coverage complete. Lemma 1 shows that the repair contains
all operations forced by `K` and therefore costs at least `R_c(K)`. Because `K` has
a safe control at every world, supplied originally or through an installed declared
fallback, `K` belongs to `F`. The bounds coincide. If `F` is empty, every nonempty
subset contains an incurable control-deficient world, so no repair in the language
can be admissible. QED.

The theorem exactly characterizes the optimum value or no-repair outcome. It is not
an efficient algorithm for selecting the minimizing subset.

## 7. Complexity theorem — J7-REPAIR is NP-complete

Consider the decision problem:

> Given one J7 instance and budget `B`, does a repair-feasible nonempty `S` with
> `R_c(S) <= B` exist?

It belongs to NP because a proposed subset, its control feasibility, and its cost
can be checked in polynomial time.

For NP-hardness, reduce weighted set cover. Use one initially incompatible world
per weighted set and one binary required-label component per universe element, with
coverage-waiver cost `B+1`. Declare:

- no uncontrollable actions;
- one controllable action `stay`; and
- a self-loop `stay` transition at every world.

Every nonempty retained subset is then control-feasible without a fallback. For a
selected set family `J`,

\[
R_c(S_J)=
\sum_{j\in J}c_j
+(B+1)\left|U\setminus\bigcup_{j\in J}A_j\right|.
\]

Therefore `R_c(S_J) <= B` iff the selected sets cover the universe within budget.
The reduction is polynomial, so J7-REPAIR is NP-complete.

The hardness persists with no uncontrollable transitions, no fallback installation,
one controllable self-loop action, and binary component labels. It is therefore
already caused by the coverage-selection subproblem, not by safety-game structure.

Full details and the J4 reduction are in
`docs/crest_repair_complexity_boundary_2026-08-18.md`.

## 8. Corollaries

### Zero-cost equivalence

If every contract-changing operation has strictly positive cost, then

\[
\boxed{
R_c^*=0
\iff
\text{the original J6 problem is already admissible}.}
\]

### Nonuniqueness

Optimal repair need not be unique. The executable result returns every optimal
retained-subset witness and marks whether the optimum is unique. Its canonical plan
is only a deterministic representative.

### Cost monotonicity

Increasing one declared operation cost while keeping the repair language fixed
cannot reduce `R_c^*`, because each feasible subset cost is coordinatewise
nondecreasing.

## 9. Five-world witness

Use

\[
W=\{\mathsf{safe},\mathsf{choice},\mathsf{hazard},
\mathsf{trapped},\mathsf{bad}\},
\]

where `bad` is incompatible. `weather` is uncontrollable, and `protect` and
`exploit` are controllable. `hazard --weather--> bad`; `trapped` remains under
weather but its ordinary controls lead to `hazard` or `bad`.

Require the labels carried by `safe`, `choice`, and `trapped`. Declare:

- install `trapped --fallback--> safe`: cost 1;
- disable `hazard --weather--> bad`: cost 2;
- admit `bad`: cost 3;
- waive `trap`: cost 5.

The unique optimum is

\[
S^*=\{\mathsf{safe},\mathsf{choice},\mathsf{trapped}\},
\qquad
R_c^*=1,
\]

with one local fallback. If fallback installation and hazard-edge deletion both
cost 2, two optimal repairs tie. Admitting `bad` is feasible but costs 3; waiving
trap coverage costs 5.

## 10. Executable oracle

Files:

- `mrm/crest_controlled_lift_relaxation.py`
- `tests/test_crest_controlled_lift_relaxation.py`
- `tests/test_crest_repair_set_cover_reduction.py`

The solver enumerates all `2^|W|-1` nonempty subsets and rejects those that are not
repair-feasible. It is an exact finite oracle, not a polynomial-time claim. Because
J7-REPAIR is NP-complete, unless `P=NP` no polynomial-time algorithm solves every
instance.

The tests replay the fallback optimum, ties, zero-cost boundary, cost monotonicity,
forced subset operations, language-level infeasibility, validation, and an explicit
weighted-set-cover embedding. The executable reduction witness is not itself the
complexity proof.

## 11. Prior-art classification

Minimum-cost safety-game repair, controller synthesis, edge modification, weighted
set cover, and finite model repair are established substrate. J7 claims no generic
algorithmic novelty.

Its program role is the exact repair calculus attached to J6's structural failure
types—static incompatibility, uncontrollable escape, and absence of a safe
control—plus component-coverage loss, while preserving the distinction between
blocking an unavoidable transition and installing an available management fallback.

J7 is not MLTR repair. MLTR minimally refines one inherited semantic law after
replacement; J7 weakens a synchronized controlled-carrier contract before J1 state
construction.

## 12. Boundaries

J7 does not prove:

- empirical existence or acceptability of declared fallback controls;
- exhaustiveness of the four repair operations;
- arbitrary transition redirection or action-role reclassification;
- cost inference, reward optimality, or policy performance beyond safety;
- polynomial-time solvability or a tractable subclass classification;
- stochastic, partial-observation, delayed-control, infinite, or risk-limited
  repair; or
- that the mathematically cheapest repair is normatively preferable.

## 13. Synthesis placement

J7 is owned by the separate CREST synthesis unit, temporarily hosted in this
repository. It is not part of the MRM mechanism-robustness theorem family. See
`crest_synthesis/README.md` and
`docs/crest_synthesis_migration_manifest_2026-08-18.md`.
