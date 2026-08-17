# CREST-J4 — exact objective characterization for failed common-lift repair

> **Status:** conditional finite synthesis theorem with analytic proof and an
> exhaustive executable oracle. The fixed-witness repair formula is exact, but the
> global retained-subset selection problem is NP-complete. Generic weighted model
> repair, set cover, edge deletion, and finite subset optimization are established
> substrate. CREST-J4 does not claim a new general repair algorithm or tractability
> result.

## 1. Question

CREST-J3 returns a unique maximal compatible transition-closed carrier `U*` for one
declared ambient synchronization. Two no-go outcomes are possible:

1. `U*` is empty; or
2. `U*` is nonempty but fails one or more component-coverage obligations.

CREST-J4 asks:

> Within an explicitly declared repair language and cost contract, how is the
> minimum weakening characterized, and which retained subsets realize it?

The theorem does not decide which ecological commitments should be cheap to relax.
Those costs are inputs. It characterizes the optimum after they are declared; the
supplied executable oracle obtains it by exponential enumeration.

## 2. Finite repair language

Let `W` be the finite ambient world set, `W0 subset W` the statically compatible
worlds, and

\[
\tau_a:W\rightharpoonup W
\]

one partial deterministic lifted transition for each declared action `a`.
For each component `k`, let

\[
p_k:W\to L_k
\]

be its label projection and let `R_k subset L_k` be the labels that a complete lift
must represent.

CREST-J4 permits only three operation types.

### A. Static-compatibility relaxation

Admit a world `w notin W0` at cost `c_w`.

### B. Transition-contract relaxation

Disable one originally legal transition `(w,a)` at cost `d_{w,a}`. The action
becomes illegal only at that retained world; the transition is not redirected.

### C. Coverage relaxation

Waive one obligation `(k,l)` with `l in R_k` at cost `r_{k,l}`.

All executable costs are finite nonnegative integers. Positive-cost corollaries
require every contract-changing operation to have strictly positive cost.

A repaired problem is **admissible** when its J3 maximal kernel is nonempty and
represents every coverage obligation not waived by the repair.

## 3. Forced cost of one retained witness

For any nonempty subset `S subset W`, define

\[
\begin{aligned}
A(S)
  &= S\setminus W_0,\\
E(S)
  &= \{(w,a):w\in S,\ \tau_a(w)\downarrow,
                    \ \tau_a(w)\notin S\},\\
D(S)
  &= \{(k,\ell):\ell\in R_k,
                    \ \ell\notin p_k(S)\}.
\end{aligned}
\]

The associated cost is

\[
\boxed{
R(S)
=
\sum_{w\in A(S)}c_w
+
\sum_{(w,a)\in E(S)}d_{w,a}
+
\sum_{(k,\ell)\in D(S)}r_{k,\ell}.}
\]

### Lemma 1 — fixed-witness necessity

If a repaired contract retains `S` as a compatible transition-closed witness and
satisfies every unwaived coverage obligation, then its operation set must contain
all operations in `A(S)`, `E(S)`, and `D(S)`.

#### Proof

- Every `w in S minus W0` is statically incompatible in the original contract, so
  retaining it requires admission.
- Every originally legal edge from `w in S` to a successor outside `S` violates
  closure unless that transition is disabled.
- If a required component label does not occur anywhere in `p_k(S)`, the witness
  cannot satisfy the obligation, so that obligation must be waived.

The three requirements are disjoint operation types. Every repair with witness `S`
therefore costs at least `R(S)`. QED.

### Lemma 2 — fixed-witness sufficiency

Admitting exactly `A(S)`, disabling exactly `E(S)`, and waiving exactly `D(S)` makes
`S` a nonempty compatible transition-closed subset satisfying every remaining
coverage obligation.

#### Proof

After admitting `A(S)`, every world in `S` is compatible. Every originally legal
edge from `S` to its complement is disabled, while all remaining legal edges from
`S` stay in `S`. Any unwaived required label is not in `D(S)` and is represented by
at least one world in `S`. Thus `S` is a valid witness. The repaired J3 maximal
kernel contains every valid closed subset, hence contains `S` and is admissible.
QED.

### Fixed-witness exactness

The two lemmas give

\[
\boxed{
\text{minimum repair cost conditional on retaining }S = R(S).}
\]

This equality concerns a **fixed** retained subset. It does not select the optimal
`S` or imply that global selection is computationally easy.

## 4. Theorem — exact global objective characterization

### Statement

The minimum cost of any admissible repair in the declared language is

\[
\boxed{
R^*
=
\min_{\varnothing\neq S\subseteq W}R(S).}
\]

Every minimizing subset supplies an optimal retained-world witness through its
forced operation sets. Conversely, every admissible repair has cost at least
`R(K)` for the retained J3 kernel `K` that it produces.

### Proof

For every nonempty `S`, Lemma 2 constructs an admissible repair of cost exactly
`R(S)`, giving the upper bound by minimizing over all `S`.

Now take any admissible repaired contract and let `K` be its nonempty maximal J3
kernel. `K` is compatible and transition closed under the repaired legal rows and
represents every unwaived obligation. Lemma 1 applied to `K` shows that the repair
cost is at least `R(K)`, which is at least the displayed minimum. The mathematical
upper and lower bounds coincide. QED.

This is an exact characterization of the optimum value. It is not an efficient
algorithm for finding the minimizing subset.

## 5. Complexity theorem — J4-REPAIR is NP-complete

Consider the decision problem:

> Given one J4 instance and budget `B`, does a nonempty `S` with `R(S) <= B` exist?

It is in NP because one can verify a proposed subset and its cost in polynomial
time.

For NP-hardness, reduce weighted set cover. Given nonempty universe `U`, weighted
sets `A_1,...,A_n` with costs `c_j`, and budget `B`:

1. create one world `w_j` per set and mark every world incompatible;
2. declare no actions;
3. create one binary component per element `e`, requiring label `1`, with
   `p_e(w_j)=1` exactly when `e in A_j`;
4. assign admission cost `c_j`; and
5. assign every coverage waiver cost `B+1`.

Then

\[
R(S_J)=
\sum_{j\in J}c_j
+(B+1)\left|U\setminus\bigcup_{j\in J}A_j\right|.
\]

Thus `R(S_J) <= B` iff the chosen sets cover `U` with total cost at most `B`.
The construction is polynomial, so J4-REPAIR is NP-hard and hence NP-complete.

The hardness already holds with no transitions, binary component labels, and only
admission and coverage-waiver costs. The coverage term therefore contains weighted
set cover exactly; it is not merely analogous to it.

Full proof and the matching J7 result are recorded in
`docs/crest_repair_complexity_boundary_2026-08-18.md`.

## 6. Corollaries

### Corollary 1 — zero-cost equivalence with J3 admissibility

If every operation that changes the original contract has strictly positive cost,
then

\[
\boxed{
R^*=0
\iff
\text{the original J3 problem is admissible}.}
\]

### Corollary 2 — optimal repair need not be unique

Distinct scientific weakenings can tie. The executable result returns **all optimal
retained-subset witnesses** and reports whether that witness set is unique. Its
`canonical_plan` is only a deterministic representative.

### Corollary 3 — monotonicity in declared costs

Increasing any operation cost while holding the repair language fixed cannot lower
`R*`, because every subset cost is coordinatewise nondecreasing.

## 7. Cascade witness

Use

\[
W=\{w_0,w_1,w_2,s,b\},
\]

where `b` is statically incompatible and

\[
w_0\to w_1\to w_2\to b,
\qquad
s\to s.
\]

Require the labels carried by `w0` and `s`. The unmodified maximal kernel contains
only `s`, so the `w0` coverage obligation fails.

Declare costs:

- disable `w2 -> b`: 1;
- admit `b`: 2;
- waive the missing `w0` obligation: 5;
- all earlier cascade cuts: 10.

The unique optimum is

\[
S^*=\{w_0,w_1,w_2,s\},
\qquad
R^*=1,
\]

with only `w2 -> b` disabled. If admitting `b` also costs 1, two optimal repairs
tie. If `s -> b` replaces the stable self-loop, cost 1 on disabling that edge
recovers the singleton witness `{s}` from an empty original kernel.

## 8. Executable oracle

Implementation:

- `mrm/crest_common_lift_relaxation.py`

Tests:

- `tests/test_crest_common_lift_relaxation.py`
- `tests/test_crest_common_lift_relaxation_degenerate_ties.py`
- `tests/test_crest_repair_set_cover_reduction.py`

The solver enumerates all `2^|W|-1` nonempty ambient subsets. This exponential
algorithm is an exact finite oracle and benchmark. Because J4-REPAIR is NP-complete,
no general polynomial-time method is implied; unless `P=NP`, none exists for all
instances.

The tests replay fixed-witness necessity/sufficiency, the cascade optima, ties,
empty-kernel recovery, validation, and one explicit weighted-set-cover embedding.
The executable reduction witness is not itself the complexity proof.

## 9. Prior-art and novelty boundary

Minimum-cost model repair, transition deletion, invariant-set restoration, weighted
set cover, and finite subset optimization are established formal-verification and
optimization machinery. CREST-J4 claims no generic algorithmic novelty.

Its program-level role is narrower:

- J3 separates static incompatibility, transition escape, and coverage loss;
- J4 assigns different declared costs to those scientifically different failures;
- the fixed-witness formula is necessary and sufficient; and
- every selected optimum is routed back through a verified J3 kernel.

J4 is also not MLTR repair. MLTR preserves one inherited semantic partition after
structural replacement. J4 weakens the cross-component synchronization contract
required before a joint CREST carrier can exist.

## 10. Boundaries

Not proved here:

- inference of costs from ecological data;
- exhaustiveness of the three repair operations;
- transition redirection or component-label modification;
- uniqueness when costs tie;
- a polynomial-time algorithm or tractable subclass classification;
- stochastic, approximate, infinite, controlled-viability, or risk-limited repair;
- ethical or scientific preference for the mathematically cheapest repair.

## 11. Synthesis placement

J4 is owned by the separate CREST synthesis unit, temporarily hosted in this
repository. It is not part of the MRM mechanism-robustness theorem family. See
`crest_synthesis/README.md` and
`docs/crest_synthesis_migration_manifest_2026-08-18.md`.
