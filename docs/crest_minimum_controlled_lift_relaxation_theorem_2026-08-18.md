# CREST-J7 — exact minimum repair of a failed controlled carrier contract

> **Status:** conditional finite synthesis theorem with analytic proof and exhaustive
> executable witnesses. Weighted safety-game/model repair and finite subset
> optimization are established substrate. CREST-J7 does not claim a new generic
> repair algorithm. It identifies the exact repair problem induced by the J6
> controlled-carrier gate within one scientifically typed operation language.

## 1. Question

CREST-J6 returns the greatest finite carrier that:

- contains only statically compatible synchronized worlds;
- survives every legal uncontrollable transition; and
- admits at least one legal safe controllable transition at each retained world.

J6 can fail because the kernel is empty or because it omits a required component
label. J7 asks:

> Given explicit costs and explicitly available fallback controls, what is the least
> expensive weakening that makes some nonempty coverage-complete controlled carrier
> possible?

The theorem does not infer the costs, invent ecological controls, or decide which
coverage requirement should be negotiable. Those are contract inputs.

## 2. Declared repair language

Let the original J6 problem have finite worlds \(W\), compatible subset \(W_0\),
uncontrollable actions \(A_u\), controllable actions \(A_c\), partial deterministic
transitions \(\tau_a\), component projections \(p_k\), and required labels
\(R_k\).

J7 permits four operation types.

### A. Admit one incompatible world

For \(w\notin W_0\), declare it compatible at cost \(c_w\).

### B. Disable one uncontrollable transition

For one originally legal \((w,a)\), \(a\in A_u\), make the action illegal at that
world at cost \(d_{w,a}\). Controllable transitions are not disabled merely because
they are unsafe: the controller may avoid them.

### C. Install one declared local fallback control

For each world \(w\), the contract may provide one optional fallback successor

\[
f(w)\in W
\]

and installation cost \(g_w\). Installing it makes a new globally named fallback
action legal at \(w\) with successor \(f(w)\). If no fallback is declared at \(w\),
this operation is unavailable.

The fallback is needed only when none of the original controllable actions has a
successor in the retained witness.

### D. Waive one coverage obligation

For \(\ell\in R_k\), waive \((k,\ell)\) at cost \(r_{k,\ell}\).

All executable costs are finite nonnegative integers. Positive-cost corollaries
assume every contract-changing operation has strictly positive cost.

## 3. Feasible retained witnesses and forced operations

Fix a nonempty subset \(S\subseteq W\). Define

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

Call \(S\) **repair-feasible** when every \(w\in C(S)\) has a declared fallback and

\[
f(w)\in S.
\]

If this condition fails, no operation in the declared language can give that world
a safe control while retaining exactly \(S\).

For a repair-feasible \(S\), define

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

### Statement

Any repaired contract in the declared language that retains \(S\) as a compatible,
robustly controlled-invariant, coverage-complete witness must perform every
operation in \(A(S)\), \(U(S)\), \(C(S)\), and \(D(S)\). Hence its cost is at least
\(R_c(S)\).

### Proof

- Every retained world outside \(W_0\) must be admitted.
- Every retained world's uncontrollable edge exiting \(S\) must be disabled;
  otherwise robust invariance fails.
- At every \(w\in C(S)\), no original control stays in \(S\). The only operation in
  the repair language that can create a safe control is installation of the
  declared fallback at \(w\). If no such fallback enters \(S\), the subset is not
  repair-feasible.
- Every required component label absent from \(p_k(S)\) must be waived.

The four operation types are disjoint, so every repair with witness \(S\) costs at
least the displayed sum. ∎

## 5. Lemma 2 — fixed-witness sufficiency

### Statement

For a repair-feasible \(S\), performing exactly the operations in \(A(S)\),
\(U(S)\), \(C(S)\), and \(D(S)\) makes \(S\) a nonempty compatible robustly
controlled-invariant subset satisfying every remaining coverage obligation.

### Proof

Admitting \(A(S)\) makes every retained world compatible. Disabling \(U(S)\) removes
all uncontrollable exits, while uncontrollable successors not disabled already lie
in \(S\). At a world outside \(C(S)\), an original safe control already remains in
\(S\). At a world in \(C(S)\), the installed fallback has successor \(f(w)\in S\).
Thus every retained world has a safe control. Every unwaived coverage label occurs
in \(S\) by definition of \(D(S)\).

Therefore \(S\) is a valid controlled witness. By J6 greatestness, the repaired
maximal controlled kernel contains \(S\), is nonempty, and satisfies every remaining
coverage obligation. ∎

The two lemmas give the exact conditional cost:

\[
\boxed{
\text{minimum repair cost conditional on retaining }S=R_c(S).
}
\]

## 6. Theorem — exact global optimum or language-level no-go

Let

\[
\mathcal F=\{S\subseteq W:S\neq\varnothing
\text{ and }S\text{ is repair-feasible}\}.
\]

### Statement

If \(\mathcal F\neq\varnothing\), the exact minimum controlled-carrier repair cost is

\[
\boxed{
R_c^*=\min_{S\in\mathcal F}R_c(S).
}
\]

Every minimizing subset yields an optimal repaired contract by its forced operation
sets. Conversely, every admissible repair has cost at least \(R_c(K)\), where \(K\)
is its repaired J6 maximal kernel.

If \(\mathcal F=\varnothing\), no repair exists in the declared language.

### Proof

For each \(S\in\mathcal F\), Lemma 2 constructs an admissible repair of cost exactly
\(R_c(S)\), giving the upper bound.

Take any admissible repaired contract and let \(K\) be its nonempty maximal J6
kernel. Because \(K\) is controlled invariant and coverage complete after the
repair, Lemma 1 shows that the repair contains all operations forced by \(K\) and
therefore costs at least \(R_c(K)\). The repaired kernel has a safe control at each
world, supplied either originally or by an installed declared fallback, so
\(K\in\mathcal F\). Thus every admissible repair costs at least the displayed
minimum. The bounds coincide.

If \(\mathcal F\) is empty, every nonempty subset contains at least one world with
neither an original safe control nor an available fallback entering the subset.
No allowed operation can cure that control failure, so no admissible repair exists
in the language. ∎

## 7. Corollaries

### Zero-cost equivalence

If every contract-changing operation has strictly positive cost, then

\[
\boxed{
R_c^*=0
\iff
\text{the original J6 problem is already admissible}.}
\]

An admissible original kernel gives a zero-operation witness. Conversely, a
zero-cost plan uses no positive-cost operation, so its retained subset was already
compatible, uncontrollable-safe, control-nonblocking, and coverage complete.

### Nonuniqueness

Optimal repair need not be unique. Introducing a fallback control can tie with
blocking an uncontrollable escape that makes an existing control safe. The
executable result returns every optimal retained-subset witness and marks whether
the optimum is unique. Its canonical plan is only a deterministic representative.

### Cost monotonicity

Increasing one declared operation cost while keeping the repair language fixed
cannot reduce \(R_c^*\), because each feasible subset cost is coordinatewise
nondecreasing. A cost increase can change which subset is optimal.

## 8. Five-world witness

Use the J6 worlds

\[
W=\{\mathsf{safe},\mathsf{choice},\mathsf{hazard},
\mathsf{trapped},\mathsf{bad}\},
\]

where `bad` is incompatible. `weather` is uncontrollable, and `protect` and
`exploit` are controllable:

- `hazard --weather--> bad`;
- `trapped --weather--> trapped`;
- `trapped --protect--> hazard`;
- `trapped --exploit--> bad`.

Require the labels carried by `safe`, `choice`, and `trapped`. The original J6
kernel contains only `safe` and `choice`, so the `trap` label is missing.

Declare:

- install `trapped --fallback--> safe`: cost 1;
- disable `hazard --weather--> bad`: cost 2;
- admit `bad`: cost 3;
- waive `trap`: cost 5;
- earlier/unrelated cuts or waivers: high cost.

The unique optimum is

\[
S^*=\{\mathsf{safe},\mathsf{choice},\mathsf{trapped}\},
\qquad
R_c^*=1,
\]

with one local fallback installed. J6 rerun returns the same three-world carrier and
a policy using the fallback at `trapped`.

If the fallback and hazard-edge cut both cost 2, two optimal repairs tie:

1. retain `safe`, `choice`, `trapped` and install the fallback; or
2. retain `safe`, `choice`, `hazard`, `trapped`, disable the weather escape, and use
   the existing `protect` transition.

Admitting `bad` and retaining all worlds is feasible but costs 3. Waiving the trap
coverage costs 5.

## 9. Executable verification

Files:

- `mrm/crest_controlled_lift_relaxation.py`
- `tests/test_crest_controlled_lift_relaxation.py`

The tests verify:

1. the unique fallback optimum and repaired J6 kernel;
2. two tied optimal repairs;
3. zero cost iff the original positive-cost problem is already admissible;
4. monotonicity under a declared cost increase;
5. exact forced operations for selected subsets;
6. a repair language with no feasible subset;
7. a valid but nonoptimal incompatible-world admission; and
8. cost/fallback validation.

The solver enumerates all \(2^{|W|}-1\) nonempty subsets. It is an exact finite
oracle, not a polynomial-time claim.

## 10. Prior-art classification

Generic minimum-cost safety-game repair, controller synthesis, edge modification,
and finite weighted model repair are established formal-methods/optimization
substrate. CREST-J7 does not claim those methods as new.

Its narrower program contribution is:

> the exact repair calculus attached to J6's three structural failure types—static
> incompatibility, uncontrollable escape, and absence of a safe control—plus
> component-coverage failure, while preserving the distinction between disabling an
> unavoidable transition and installing an available management fallback.

J7 is also not MLTR repair. MLTR minimally refines one inherited semantic law after
replacement; J7 weakens a synchronized controlled-carrier contract before the J1
joint state is constructed.

## 11. Boundaries

CREST-J7 does not prove:

- that the fallback controls exist empirically or are ecologically acceptable;
- that the four-operation language is exhaustive;
- transition redirection beyond the declared fallback successor;
- reclassification of an action from uncontrollable to controllable;
- cost inference, reward optimality, or policy performance beyond safety;
- stochastic, partial-observation, delayed-control, infinite, or risk-limited
  repair; or
- polynomial scalability.

The safe theorem-level statement is:

\[
\boxed{
\text{within the declared finite controlled-repair language, J7 returns the exact}
\text{minimum admissible weakening and every tied witness—or a finite-language}
\text{no-repair result when no retained subset can be made control viable.}
}
