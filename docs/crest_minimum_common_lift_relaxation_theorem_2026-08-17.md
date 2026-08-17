# CREST-J4 — exact minimum relaxation of a failed common-lift contract

> **Status:** conditional finite synthesis theorem with analytic proof and an
> exhaustive executable oracle. Generic weighted model repair, edge deletion, and
> finite subset optimization are established substrate. CREST-J4 does not claim a
> new general model-repair algorithm; it identifies the exact repair problem created
> by the J3 common-carrier gate and keeps its three scientific failure types
> separate.

## 1. Question

CREST-J3 returns a unique maximal compatible transition-closed carrier `U*` for one
declared ambient synchronization. Two no-go outcomes are possible:

1. `U*` is empty; or
2. `U*` is nonempty but fails one or more component-coverage obligations.

CREST-J4 asks:

> Within an explicitly declared repair language and cost contract, what is the
> least expensive weakening that makes some nonempty coverage-complete common lift
> possible?

The theorem does not decide which ecological commitments should be cheap to relax.
Those costs are inputs. It determines the exact optimum after they are declared.

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

Disable one originally legal transition `(w,a)` at cost `d_{w,a}`.
The action becomes illegal only at that retained world. The transition is not
redirected.

### C. Coverage relaxation

Waive one obligation `(k,l)` with `l in R_k` at cost `r_{k,l}`.

All costs are finite nonnegative integers in the executable theorem oracle.
Positive-cost corollaries require every contract-changing operation to have
strictly positive cost.

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

### Lemma 1 — necessity for a fixed witness

If a repaired contract retains `S` as a compatible transition-closed witness and
satisfies every unwaived coverage obligation, then its operation set must contain
all operations in `A(S)`, `E(S)`, and `D(S)`.

#### Proof

- Every `w in S minus W0` is statically incompatible in the original contract. If
  it is retained, it must be admitted.
- For every originally legal edge from `w in S` to a successor outside `S`, closure
  of `S` fails unless that transition is disabled.
- If a required component label does not occur anywhere in `p_k(S)`, then `S`
  cannot satisfy that obligation; the obligation must be waived.

These three requirements concern disjoint operation types, so every repair with
witness `S` costs at least `R(S)`. QED.

### Lemma 2 — sufficiency for a fixed witness

Admitting exactly `A(S)`, disabling exactly `E(S)`, and waiving exactly `D(S)` makes
`S` a nonempty compatible transition-closed subset satisfying every remaining
coverage obligation.

#### Proof

After admitting `A(S)`, every world in `S` is compatible. Every originally legal
edge from `S` to its complement has been disabled, while all remaining legal edges
from `S` stay in `S`; hence `S` is transition closed. Any unwaived required label is
not in `D(S)` and therefore is represented by at least one world in `S`. Thus `S`
is a valid witness. The repaired J3 maximal kernel contains every valid closed
subset, so it contains `S`, is nonempty, and satisfies all remaining coverage
obligations. QED.

### Fixed-witness exactness

Lemmas 1–2 give

\[
\boxed{
\text{minimum repair cost conditional on retaining }S = R(S).}
\]

This is stronger than merely producing one feasible patch: for a fixed retained
subset, the three operation sets are forced.

## 4. Theorem — exact global minimum

### Statement

The minimum cost of any admissible repair in the declared language is

\[
\boxed{
R^*
=
\min_{\varnothing\neq S\subseteq W}R(S).}
\]

Every minimizing subset supplies an optimal retained-world witness through its
forced operation sets `A(S)`, `E(S)`, and `D(S)`. Conversely, every admissible
repair has cost at least `R(S)` for the retained J3 kernel `S` that it produces.

### Proof

For every nonempty `S`, Lemma 2 constructs an admissible repair of cost exactly
`R(S)`. Therefore the global optimum is at most the displayed minimum.

Now take any admissible repaired contract and let `K` be its nonempty maximal J3
kernel. `K` is compatible and transition closed under the repaired legal rows and
represents every unwaived obligation. Lemma 1 applied to `K` shows that the repair
cost is at least `R(K)`, which is at least the minimum over all nonempty subsets.
The upper and lower bounds coincide. QED.

## 5. Corollaries

### Corollary 1 — zero-cost equivalence with J3 admissibility

If every operation that changes the original contract has strictly positive cost,
then

\[
\boxed{
R^*=0
\iff
\text{the original J3 problem is admissible}.}
\]

If the original problem is admissible, its maximal kernel is a witness requiring no
operations. Conversely, a zero-cost forced plan contains no positive-cost operation,
so its witness was already statically compatible, transition closed, and
coverage-complete in the original contract.

### Corollary 2 — optimal repair need not be unique

Distinct scientific weakenings can tie. For example, admitting one previously
incompatible successor can cost the same as disabling the edge leading to it.
Accordingly the executable result returns **all optimal retained-subset witnesses**
and reports whether that witness set is unique. Its `canonical_plan` is only a
deterministic representative, not a theorem that nature chooses that repair.

### Corollary 3 — monotonicity in declared costs

Increasing any operation cost while holding the repair language fixed cannot lower
`R*`, because every subset cost is coordinatewise nondecreasing.

## 6. Cascade witness

Use the J3 ambient worlds

\[
W=\{w_0,w_1,w_2,s,b\},
\]

where `b` is statically incompatible and

\[
w_0\to w_1\to w_2\to b,
\qquad
s\to s.
\]

Require the component labels carried by `w0` and `s`. The unmodified maximal kernel
contains only `s`, so the `w0` coverage obligation fails.

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

with only `w2 -> b` disabled. If admitting `b` is also assigned cost 1, two optimal
repairs tie: cut the edge or retain all five worlds and admit `b`.

If `s -> b` replaces the stable self-loop, the original J3 kernel is empty. With
cost 1 on disabling `s -> b`, the exact optimizer recovers the singleton witness
`{s}`.

## 7. Executable theorem oracle

Implementation:

- `mrm/crest_common_lift_relaxation.py`

Tests:

- `tests/test_crest_common_lift_relaxation.py`

The solver enumerates all `2^|W|-1` nonempty ambient subsets. This exponential
algorithm is intentional: it is an exact finite theorem oracle and benchmark, not a
claim of polynomial-time scalability.

The tests verify:

1. the unique one-edge optimum in the cascade;
2. necessity and sufficiency of the forced operation set for every nonempty subset;
3. the positive-cost zero iff J3-admissible corollary;
4. tied optimal repairs;
5. recovery from an empty kernel; and
6. cost-contract validation.

## 8. Prior-art and novelty boundary

Minimum-cost model repair, transition deletion, invariant-set restoration, and
weighted finite repair are established in formal verification and optimization.
Relevant neighboring work includes probabilistic model repair, abstract model
repair, and optimal repair for omega-regular properties.

CREST-J4 therefore does **not** claim generic novelty for weighted repair or subset
enumeration. Its program-level contribution is narrower:

- J3 separates static incompatibility, transition escape, and coverage loss;
- J4 assigns distinct declared costs to those scientifically different failures;
- the theorem proves an exact repair formula and routes every optimal plan back to a
  verified J3 kernel.

This is also not MLTR repair. MLTR preserves one inherited semantic partition after
structural replacement. CREST-J4 weakens the cross-component synchronization
contract required before a joint CREST carrier can exist.

## 9. Boundaries

Not proved here:

- that the cost values can be inferred from ecological data;
- that enabling worlds, disabling transitions, and waiving coverage are the only
  legitimate repair operations;
- transition redirection, component-label modification, or contract addition;
- one unique optimum when costs tie;
- a polynomial-time algorithm;
- stochastic, approximate, infinite, controlled-viability, or risk-limited repair;
- that a mathematically cheapest repair is ethically or scientifically preferable.

## 10. Updated synthesis chain

```text
declared ambient synchronization
  -> J3 maximal common carrier or finite no-go
  -> if no-go: J4 exact least-cost declared contract relaxation
  -> repaired J3 carrier
  -> J1 unique coarsest four-audit state + evidence gate
  -> J2 invariance under faithfully redundant lifts
```

CREST-J4 turns the J3 no-go certificate into a finite, auditable repair decision
without hiding which scientific commitment was weakened.
