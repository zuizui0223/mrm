# CREST-O1 — carrier-repair cost and evidential licensing need not commute

> **Status:** proved finite synthesis obstruction with an executable witness. This
> is intentionally **not** promoted to a new theorem family. Generic constrained
> finite optimization, diagnosability, observability, and minimum-cost model repair
> are established substrate. The CREST contribution is the explicit separation
> between a J7 carrier repair and the downstream J1/CED licensing gate.

## 1. Question

CREST-J7 returns the exact minimum cost of making a controlled common carrier
admissible inside a declared repair language. CREST-J1 then constructs the unique
coarsest state required on the repaired carrier, and the CED evidence condition asks
whether that state is deterministically reportable.

It is tempting to assume the following workflow is harmless:

```text
choose the cheapest J7 carrier repair
  -> construct the J1 state
  -> check whether evidence licenses it
```

CREST-O1 shows that this workflow can fail even in a five-world deterministic
system. The cheapest structural repair can produce an unlicensed joint state, while
a more expensive structural repair produces the least-cost licensed state.

## 2. Two different optima

Let `R` be the finite family of feasible J7 repair plans. For repair `r`, write

- `c(r)` for its exact J7 carrier-repair cost;
- `J_r` for the downstream J1 joint state on the repaired maximal carrier; and
- `E_r` for the reliability-qualified evidence partition on that carrier.

The ordinary structural optimum is

\[
R_{\mathrm{struct}}^*
=
\min_{r\in\mathcal R}c(r).
\]

The minimum full-state-licensed repair is instead

\[
R_{\mathrm{licensed}}^*
=
\min\{c(r):r\in\mathcal R,\ J_r\preceq E_r\},
\]

when the feasible licensed set is nonempty.

There is no general reason for these minima to agree.

## 3. Strict separation witness

Use the J6/J7 ambient worlds

\[
W=\{\mathsf{safe},\mathsf{choice},\mathsf{hazard},
     \mathsf{trapped},\mathsf{bad}\}.
\]

`bad` is statically incompatible. `hazard` has an uncontrollable transition to
`bad`. `trapped` has its ordinary controls leading to `hazard` or `bad`. Coverage
requires the labels carried by `safe`, `choice`, and `trapped`.

Declare the relevant repair costs:

- install a local fallback at `trapped` leading to `safe`: cost `1`;
- disable the uncontrollable `hazard -> bad` transition: cost `2`;
- admit `bad`: cost `3`;
- waive the `trapped` coverage obligation: cost `5`.

J7 proves that the unique minimum structural repair is the cost-1 fallback plan,
retaining

\[
S_f=\{\mathsf{safe},\mathsf{choice},\mathsf{trapped}\}.
\]

For the downstream J1 contract, declare one future action recording whether that
local fallback is available. The repaired carrier has two J1 classes:

\[
J_f=
\{\{\mathsf{safe},\mathsf{choice}\},
  \{\mathsf{trapped}\}\}.
\]

The evidence partition deliberately places all three worlds in one record class.
Therefore

\[
J_f\not\preceq E_f.
\]

The cost-1 carrier repair is not a fully licensed state repair. The report target is
constant, however, so target-only reporting remains licensed; this preserves the
CED distinction between full-state resolution and target reportability.

Now use the cost-2 repair that disables `hazard -> bad` and retains

\[
S_h=\{\mathsf{safe},\mathsf{choice},\mathsf{hazard},
      \mathsf{trapped}\}.
\]

No fallback is installed. Under the same downstream question, every world has the
same fallback-legality row, so the J1 state is the one-block partition

\[
J_h=\{S_h\}.
\]

The one-class evidence partition resolves this state, hence

\[
J_h\preceq E_h.
\]

The executable exhaustive search over every nonempty retained subset gives

\[
\boxed{
R_{\mathrm{struct}}^*=1
<
R_{\mathrm{licensed}}^*=2.
}
\]

## 4. Consequence

The following implication is false:

\[
\arg\min_{r\in\mathcal R}c(r)
\subseteq
\{r:J_r\preceq E_r\}.
\]

Equivalently, minimum carrier repair and downstream evidential licensing do not
commute in general.

This is not a claim that the cost-2 repair is ecologically preferable in every
sense. It says only that an optimization target restricted to carrier feasibility
cannot guarantee a state that the evidence is entitled to report.

A complete decision procedure must therefore either:

1. constrain the repair search by the downstream licensing condition;
2. accept an ambiguity-explicit full-state report after the cheapest repair; or
3. strengthen the evidence contract separately.

## 5. Why this is an obstruction, not CREST-J8

The finite constrained minimum exists by elementary optimization once the repair
family and downstream contracts are declared. Diagnosability, observability,
sensor selection, safety-game synthesis, and minimum-cost model repair already
provide extensive neighboring theory.

The reusable CREST result here is the strict cross-contract witness:

> a J7-optimal structural repair need not be J1/CED-admissible, even when a more
> expensive licensed repair exists and the requested target is already reportable.

That statement changes the ordering of existing CREST gates but does not yet justify
another general theorem family.

## 6. Executable source

- `tests/test_crest_repair_evidence_noncommutation.py`

The test:

1. independently confirms the J7 structural optimum `1`;
2. constructs the downstream J1 contract for every feasible retained subset;
3. checks full-state and target-only licensing;
4. proves the unique minimum licensed repair has cost `2`; and
5. records the strict state-count reversal: the cheaper repair requires two J1
   states while the costlier licensed repair requires one.
