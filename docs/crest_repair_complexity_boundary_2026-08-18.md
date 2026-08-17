# CREST repair complexity boundary — J4/J7 selection is NP-complete

> **Status:** complexity corollary and claim-boundary document, not CREST-J8. It
> strengthens the computational honesty of J4 and J7. The fixed-witness formulas
> remain exact, but selecting the best retained witness is NP-hard in general.

## 1. Why this boundary is needed

J4 and J7 prove necessary-and-sufficient operation sets after one retained subset
`S` has been fixed. For J4,

\[
R(S)=
\sum_{w\in A(S)}c_w+
\sum_{(w,a)\in E(S)}d_{w,a}+
\sum_{(k,\ell)\in D(S)}r_{k,\ell},
\]

and for J7 the analogous controlled cost is

\[
R_c(S)=
\sum_{w\in A(S)}c_w+
\sum_{(w,a)\in U(S)}d_{w,a}+
\sum_{w\in C(S)}g_w+
\sum_{(k,\ell)\in D(S)}r_{k,\ell}.
\]

The lower and upper bounds coincide **conditional on that fixed `S`**. The global
problems still require choosing `S`:

\[
R^*=\min_{\varnothing\neq S\subseteq W}R(S),
\qquad
R_c^*=\min_{S\in\mathcal F}R_c(S).
\]

The current executable solvers enumerate all `2^|W|-1` nonempty subsets. Exactness
therefore means exact objective characterization and exhaustive finite computation;
it does not imply tractability.

## 2. Decision problems

### J4-REPAIR

**Input:** one finite J4 repair contract, nonnegative integer operation costs, and an
integer budget `B`.

**Question:** is there a nonempty retained subset `S` with `R(S) <= B`?

### J7-REPAIR

**Input:** one finite J7 controlled-repair contract, nonnegative integer operation
costs, and an integer budget `B`.

**Question:** is there a repair-feasible nonempty retained subset `S` with
`R_c(S) <= B`?

Both problems belong to NP: a retained subset is a polynomial-size certificate, and
compatibility, escaping transitions, control feasibility, represented labels, and
total cost can all be checked in polynomial time.

## 3. Theorem — J4-REPAIR is NP-complete

### Reduction from weighted set cover

Take a weighted set-cover instance with:

- a nonempty universe `U = {e_1,...,e_m}`;
- sets `A_1,...,A_n subseteq U`;
- positive integer set costs `c_1,...,c_n`; and
- budget `B`.

Construct a J4 instance as follows.

1. Create one ambient world `w_j` for each set `A_j`.
2. Mark every world statically incompatible, so retaining `w_j` costs exactly
   `c_j` through the world-admission operation.
3. Declare no actions. Hence there are no transition-disable costs and
   `E(S)=emptyset` for every retained subset.
4. For every universe element `e_i`, create one binary component `k_i` whose
   required label is `1`, with

   \[
   p_i(w_j)=1\iff e_i\in A_j.
   \]

5. Give waiver of each required label the cost `B+1`.

For the subset of worlds corresponding to a chosen set family `J`, the repair cost
is

\[
R(S_J)=
\sum_{j\in J}c_j
+(B+1)\left|U\setminus\bigcup_{j\in J}A_j\right|.
\]

Therefore `R(S_J) <= B` exactly when the selected sets cover every element and have
total set cost at most `B`. The construction is polynomial in the set-cover input.
Weighted set cover reduces to J4-REPAIR, so J4-REPAIR is NP-hard. Together with NP
membership, J4-REPAIR is NP-complete.

This hardness already holds in the severe special case with:

- no transitions at all;
- binary component labels;
- all worlds initially incompatible; and
- only world-admission and coverage-waiver costs active.

Thus the coverage term is not merely suggestive of set cover; it contains weighted
set cover exactly.

## 4. Theorem — J7-REPAIR is NP-complete

Use the same weighted set-cover construction, but give every world one controllable
self-loop action `stay`, declare no uncontrollable actions, and make no fallback
control available.

Every nonempty retained subset is then control-feasible: each retained world can
choose its own `stay` self-loop. There are no uncontrollable exits and no fallback
costs, so

\[
R_c(S_J)=
\sum_{j\in J}c_j
+(B+1)\left|U\setminus\bigcup_{j\in J}A_j\right|.
\]

The same budget equivalence proves weighted set cover reduces to J7-REPAIR. Hence
J7-REPAIR is NP-complete.

The hardness therefore does not arise from safety-game complexity, uncontrollable
transitions, or fallback installation. Coverage selection alone suffices.

## 5. Consequences for theorem wording

The safe wording is:

> J4/J7 give an exact finite objective characterization. For a fixed retained
> subset, the necessary-and-sufficient operation set is forced. The supplied oracle
> obtains a global optimum by exhaustive subset enumeration. The general decision
> problem is NP-complete, so no polynomial-time algorithm is implied.

Avoid wording that can be read as an efficient exact algorithm. In particular:

- “the lower and upper bounds coincide” refers to the mathematical optimum and, at
  the lemma level, to fixed-`S` cost;
- “exact global optimum” means the returned value is not heuristic;
- it does **not** mean that finding the minimizing `S` is computationally easy.

Unless `P=NP`, no polynomial-time algorithm solves every J4/J7 instance. Restricted
subclasses may still be tractable, but no such classification is proved here.

## 6. Executable witness

`tests/test_crest_repair_set_cover_reduction.py` instantiates a three-element
weighted set-cover problem in both J4 and J7. The exact oracles return the same
minimum set-cover cost and select the corresponding retained worlds. This test is a
replay of the reduction, not the proof of NP-completeness.

## 7. Prior-art and novelty boundary

Set cover NP-completeness and weighted coverage optimization are established
combinatorial-optimization substrate. CREST claims no novelty for this complexity
result. Its purpose is negative and regulatory: it prevents an exact finite
characterization from being misread as a tractability result and aligns J4/J7 with
CED's explicit treatment of set-cover-style design machinery as generic and
potentially intractable.
