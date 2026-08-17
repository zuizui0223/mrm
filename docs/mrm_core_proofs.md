# MRM core proofs — recovered proof spine

> **Status:** proof recovery for existing MRM results. This document adds no new theorem and changes no executable behavior. It converts the already implemented finite results into one explicit analytic proof spine and separates theorem proofs from finite replay.

## 1. Setup

Let `Q` be a finite nonempty observable macrostate set, `A` a finite nonempty action set, and `C` a finite nonempty retained candidate-mechanism family. Candidate `theta` induces deterministic maps

\[
G_a^\theta:Q\to Q\qquad(a\in A).
\]

Two candidates are in the same **response type** when their complete transition tables agree. Let `R` denote the finite response-type set, and write

\[
G_a^r:Q\to Q
\]

for the common transition map of response type `r`.

MRM asks what may be reported when `r` is not known.

---

## 2. Universal deterministic law criterion

### Theorem 1

A candidate-independent deterministic macro law

\[
H_a:Q\to Q\qquad(a\in A)
\]

satisfying

\[
H_a(q)=G_a^r(q)
\quad\text{for every }q,a,r
\]

exists if and only if `|R|=1`.

### Proof

If such `H_a` exists, then for every pair `r,r'`, action `a`, and state `q`,

\[
G_a^r(q)=H_a(q)=G_a^{r'}(q).
\]

Thus all response types have identical complete transition tables, so there is only one response type.

Conversely, if `|R|=1`, choose its representative `r_0` and define

\[
H_a(q)=G_a^{r_0}(q).
\]

Every retained candidate has the same response table by definition of response type, so this `H` is candidate independent. \(\square\)

This is the formal justification for `CandidateLawFamily.universal` and `universal_transition` in `mrm/laws.py`.

---

## 3. Typed and set-valued honest reports

### Proposition 2

When `|R|>1`, the typed state space `Q x R` carries a deterministic transition law

\[
T_a(q,r)=(G_a^r(q),r).
\]

If response type is omitted, the exact candidate-forgetting one-step report is

\[
F_a(q)=\{G_a^r(q):r\in R\}.
\]

A singleton deterministic report on `Q` is uniformly correct over the retained family exactly when `F_a(q)` is a singleton for every `(q,a)`.

### Proof

The typed law is deterministic because both coordinates of `T_a(q,r)` are uniquely specified. If the type is unknown, the possible observed successors are exactly those attained by at least one retained response type, which is the set `F_a(q)`.

A candidate-independent deterministic successor `H_a(q)` is uniformly correct exactly when every retained response type gives that same successor, i.e. exactly when `|F_a(q)|=1` for every `(q,a)`. \(\square\)

Thus the set-valued report is not an approximation: it is the exact candidate-forgetting successor relation under the declared finite family.

---

## 4. Candidate-safe product lower bound

Call the family **uniformly response-separated** when for every two distinct response types `r != r'` and every observable state `q`, there exists a declared action `a` such that

\[
G_a^r(q)\ne G_a^{r'}(q).
\]

An exact typed interface is required to preserve the currently observed macrostate.

### Theorem 3

Under uniform response separation, every exact deterministic candidate-safe interface has at least

\[
|Q||R|
\]

states. Hence

\[
K_{\mathrm{typed}}\ge \log_2|Q|+\log_2|R|.
\]

The full typed product attains the bound.

### Proof

Consider two distinct typed states `(q,r)` and `(q',r')`.

If `q != q'`, an observation-preserving interface cannot merge them because their current observable macrostates differ.

If `q=q'` but `r!=r'`, uniform response separation supplies an action `a` with

\[
G_a^r(q)\ne G_a^{r'}(q).
\]

After one action their observed successors differ. Any exact deterministic interface that merged the two source states would have to assign one quotient successor to that class, contradicting observation preservation after the action. Therefore no two distinct elements of `Q x R` may be merged.

The quotient is thus discrete on `Q x R`, giving the cardinality and bit lower bounds. The typed product itself is deterministic and observation preserving, so equality is attainable. \(\square\)

This is the analytic statement replayed by `candidate_safe_memory_bits` in `mrm/laws.py`.

---

## 5. Joint exterior-mechanism lower bound

This is a conditional bridge to CCOC rather than a separate arithmetic rule.

Let a jointly realizable comparison family be

\[
I\times E_1\times\cdots\times E_q\times R.
\]

Assume the declared future grammar contains operational separators that can decode the inside coordinate, each exterior coordinate, and the response type, uniformly over all remaining coordinates.

### Proposition 4

Every exact joint interface has at least

\[
|I|\left(\prod_j|E_j|\right)|R|
\]

states and therefore

\[
K_{\mathrm{joint}}\ge
\log_2|I|+\sum_j\log_2|E_j|+\log_2|R|.
\]

### Proof

Take two distinct joint states. They differ in at least one coordinate. By the joint operational-separation premise, the declared decoder/probe for that coordinate yields different future observable traces. Hence the two states cannot share one exact interface label. All joint product states are pairwise distinguishable, so the exact quotient is discrete on the declared comparison family. \(\square\)

The module `mrm/joint.py` replays the resulting cardinality identity. It does **not** prove that separately established exterior and mechanism bounds add without the joint premise.

---

## 6. Minimal candidate-safe quotient

The full typed product can be larger than necessary when response type is locally irrelevant.

Let

\[
X=Q\times R,
\qquad
T_a(q,r)=(G_a^r(q),r),
\qquad
o(q,r)=q.
\]

Let `P_0` partition `X` by the observable state `q`. Recursively define `P_{n+1}` by equality of the signatures

\[
\sigma_{n+1}(x)=
\left(o(x),([T_a(x)]_{P_n})_{a\in A}\right).
\]

This is the refinement implemented in `mrm/quotient.py`: the signature contains the current observable state and the vector of successor `P_n`-blocks. It does **not** explicitly carry the old `P_n` block identifier as an extra component.

### Theorem 5

The stabilized partition `P_*` is the unique coarsest observation-preserving deterministic quotient of the typed product. Equivalently, it has the fewest states among exact candidate-safe deterministic interfaces that retain the current macrostate.

### Proof

First we show that the recursively generated sequence is monotone even though the previous block label is not written explicitly in the next signature.

`P_1` refines `P_0` because equality of `\sigma_1` implies equality of the first component `o(x)`.

Assume inductively that `P_n` refines `P_{n-1}`. Suppose `x` and `y` lie in the same `P_{n+1}` block. Then they have the same current observation and, for every action `a`, the successors `T_a(x)` and `T_a(y)` lie in the same `P_n` block. Since `P_n` refines `P_{n-1}`, those successors also lie in the same `P_{n-1}` block. Hence `x` and `y` have equal `\sigma_n` signatures and therefore lie in the same `P_n` block. Thus

\[
P_{n+1}\preceq P_n
\]

for every `n`. Because `X` is finite, only finitely many strict refinements are possible, so the sequence stabilizes at some `P_*`.

At a fixed point, states in one block have the same observable state and, for every action, successors in one common fixed-point block. Therefore observation and every declared successor factor through the quotient; `P_*` is candidate-safe and deterministic.

For coarseness, let `Qhat` be any observation-preserving deterministic quotient. We prove by induction that `Qhat` refines every `P_n`. The base case holds because `Qhat` preserves the current observable state and therefore refines `P_0`. Assume `Qhat` refines `P_n`. If two typed states share a `Qhat`-class, determinism of `Qhat` sends them under every action to one common successor `Qhat`-class; by the induction hypothesis those successor states also share their `P_n`-blocks. The two source states also have the same current observation. Hence their `\sigma_{n+1}` signatures are equal, so they lie in the same `P_{n+1}` block. Therefore `Qhat` refines `P_{n+1}`.

At stabilization every observation-preserving deterministic candidate-safe quotient refines `P_*`, proving that `P_*` is coarsest. Two coarsest partitions refine one another and therefore coincide. \(\square\)

This proof now matches the actual signature recurrence in `minimal_candidate_safe_quotient`; it does not rely on a nonexistent explicit old-block component. It is the MRM specialization of the neutral finite refinement argument in `docs/neutral_latent_world_quotient.md`. The common partition-refinement machinery is classical substrate; the MRM specialization fixes the latent worlds to observable-state × response-type pairs.

### Corollary 5.1 — future-trajectory characterization

Two typed states lie in the same `P_*` block if and only if they have the same observed trajectory for every finite declared action word.

### Proof

If they share a fixed-point block, action stability preserves block equality after each symbol, and observation preservation gives identical observed trajectories by induction on word length.

Conversely, suppose two typed states have identical observed trajectories for every finite action word. They begin in the same `P_0` block. Inductively, if they remain together in `P_n`, then for every action their successor pair has identical observed trajectories for every finite continuation word. By the same induction hypothesis, applied to those successor pairs, the successors lie in the same `P_n` block. Hence the two source states have equal `\sigma_{n+1}` signatures and remain together in `P_{n+1}`. They are never separated and therefore share a `P_*` block. \(\square\)

---

## 7. Exact shortest active discrimination

For a current observed state `q` and a nonempty compatible response-type set `S`, define a **configuration** `(q,S)`. Action `a` partitions `S` by the next observed state:

\[
S_{a,q,x}=\{r\in S:G_a^r(q)=x\}.
\]

Singleton sets are terminal.

### Lemma 6.1 — simple optimal plan

If any finite exact discrimination plan exists from `(q,S)`, there is an optimal worst-case-depth plan that never revisits the same configuration on one root-to-leaf branch.

### Proof

Suppose a branch revisits the same configuration `(q,S)`. From that point onward the scientific information state is identical: the same current observable state and same compatible response-type set remain. Replace the earlier occurrence by the continuation used after the later occurrence. This removes at least one action and preserves every later possible branch and terminal identification. Repeating removes all repeated configurations. \(\square\)

Because there are only

\[
|Q|(2^{|R|}-1)
\]

configurations, a shortest successful plan has finite depth strictly below this number.

### Theorem 6 — shortest-plan dynamic program

The iteration implemented by `shortest_active_discrimination_plan` returns a plan with minimum worst-case number of actions, or `None` exactly when no finite declared policy identifies the requested response types.

### Proof

Let `D_k` be the set of configurations from which exact identification is possible in at most `k` further actions. `D_0` consists exactly of singleton configurations.

Inductively, a nonterminal configuration `(q,S)` lies in `D_{k+1}` exactly when there exists an action `a` such that every nonempty outcome configuration `(x,S_{a,q,x})` lies in `D_k`. This is precisely the update performed by the algorithm: it adds a configuration when all child configurations already have plans and assigns one plus the maximum child depth.

By induction over `k`, after the `k`th expansion the stored plans are exactly the configurations solvable within `k` actions, with the minimum worst-case depth among such plans. Lemma 6.1 bounds the depth of any optimal finite plan by the finite number of configurations minus one, so the finite iteration reaches every solvable configuration. If the target is absent at the fixed point, no finite exact plan exists. \(\square\)

---

## 8. Canonical mechanism-ambiguity frontier

For `m>=1`, let

\[
R_m=\{0,1\}^m,\qquad Q=\{0,1\},
\]

and for `r=(r_1,...,r_m)` define

\[
G^r_{\mathrm{probe}_i}(q)=r_i.
\]

### Theorem 7 — exact memory frontier

The minimal candidate-safe quotient has exactly

\[
2^{m+1}
\]

states and `m+1` bits. Relative to a fixed-candidate two-state law, unresolved mechanism ambiguity costs exactly `m` additional bits.

### Proof

Any two distinct response signatures differ in some coordinate `i`. From either observed state, `probe_i` produces different next observations for the two signatures. Uniform response separation therefore holds, and Theorem 3 makes the full typed product minimal. Its cardinality is

\[
|Q||R_m|=2\cdot2^m=2^{m+1}.
\]

Taking logarithms gives `m+1` bits, versus one bit for the fixed two-state observable law. \(\square\)

### Theorem 8 — exact intervention frontier

Exactly `m` binary probes are necessary and sufficient in the worst case to identify one of the `2^m` response signatures.

### Proof

Sufficiency: apply each probe once. The observed outcomes are the `m` signature bits and identify `r` exactly.

Necessity: each intervention has at most two observable outcomes in this family, so a depth-`d` adaptive tree has at most `2^d` leaves. Exact identification of `2^m` response types needs at least `2^m` distinct terminal leaves. Thus `2^d>=2^m`, hence `d>=m`. \(\square\)

After `k` distinct probes, the unobserved `m-k` bits remain free, leaving exactly `2^{m-k}` compatible signatures.

---

## 9. Minimum-cost active discrimination

Let every action have finite strictly positive cost `c(a)>0`.

### Theorem 9

Among all finite exact discrimination policies, the Bellman recurrence

\[
V(q,\{r\})=0,
\]

\[
V(q,S)=\min_a\left[c(a)+\max_{x:S_{a,q,x}\ne\varnothing}V(x,S_{a,q,x})\right]
\]

returns the minimum worst-case total action cost whenever exact identification is possible; otherwise the value is undefined and the implementation returns no plan.

### Proof

Strictly positive costs imply that an optimal finite policy can be chosen with no repeated configuration on a branch: if the same `(q,S)` recurs, removing the intervening cycle preserves the information state and strictly lowers total cost. Therefore an optimum, when it exists, lies among finitely many simple configuration trees.

For a nonterminal configuration, every exact policy chooses some first action `a`; after observed outcome `x`, it must continue with an exact policy for `(x,S_{a,q,x})`. Its worst-case cost is therefore at least

\[
c(a)+\max_x V(x,S_{a,q,x}).
\]

Choosing the best first action gives the Bellman lower bound. Conversely, combining an action attaining the minimum with optimal child policies constructs a policy achieving the recurrence. Finite dynamic programming over the finite configuration set therefore returns the exact optimum. \(\square\)

With unit action costs, this recurrence reduces to the shortest worst-case-depth objective of Theorem 6.

---

## 10. Observation and VOI adapters: proof status

These executable modules are retained as adapters around the mechanism-report problem, not as separate MRM headline theorems.

### Robust support update

For a declared compatible true-successor set `N(x)`, the update

\[
S'=\{r\in S:G_a^r(q)\in N(x)\}
\]

is exactly the subset of retained response types not contradicted by the observed support. This follows directly from the definition of compatibility. A singleton identifies a type under the declared support; an empty set contradicts the family/support contract.

### Probabilistic posterior update

The formula in `mrm/probabilistic.py` is Bayes' rule on the declared finite response-type family. The proof burden is therefore algebraic normalization and support validation, which the tests replay; no new probabilistic theorem is claimed.

### One-step VOI

The EIG formula in `mrm/voi.py` is the standard entropy identity

\[
\mathrm{EIG}(a)=H(\pi)-\sum_x P_a(x)H(\pi'_{a,x}).
\]

MRM uses it as a declared one-step design diagnostic. No claim of novelty is made for Bayesian experimental design, entropy reduction, or cost-adjusted VOI.

---

## 11. Proof/replay boundary

The analytic proofs above quantify over every finite family satisfying their stated premises. The Python modules and tests serve different roles:

- `mrm/laws.py` checks finite response-type and reporting constructions;
- `mrm/quotient.py` constructs the fixed point and discrimination policy;
- `mrm/frontier.py` replays the canonical `m`-indexed witnesses for finite supplied widths;
- `mrm/costs.py` replays positive-cost dynamic programming;
- `mrm/joint.py` checks the joint-product cardinality identity under the declared joint-separation premise;
- the test suite and `scripts/verify_mrm_core.py` guard implementation/theorem agreement.

A passing finite replay is not the proof of an all-family or all-`m` theorem. The proofs are the arguments above; the replay verifies the implementation on declared finite instances.