# Contract-Relative Ecological State Theory (CREST)

> **Status:** program-level metatheory with five conditional finite synthesis
> theorems. CREST does not merge CCOC, MLTR, MRM, and CED, does not claim that their
> generic quotient/refinement/repair/simulation machinery is new, and does not
> supply a nature-given canonical ontology of ecological states.

## 1. Central principle

CREST begins from one ecological claim:

> **Treating two ecological configurations as the same state is a scientific
> commitment about which differences may be ignored for a declared future,
> inherited meaning, retained mechanism family, and evidence/reporting task.**

A compact program notation is

\[
\mathcal C=(\Gamma,\mathcal H,\Theta,D;T),
\]

where

- \(\Gamma\) is the future-action/composition contract;
- \(\mathcal H\) is the inherited-semantics contract;
- \(\Theta\) is the retained mechanism/response-type family;
- \(D\) is the experiment, observation, detection, failure, and risk contract; and
- \(T\) is the report or decision target.

The slogan

\[
\text{“ecological state identity is contract-relative”}
\]

is shorthand for **scientific state-representation adequacy**, not a claim that
ecological systems lack mind-independent structure.

## 2. Four companion adequacy audits

| Audit | Repository | Question | Characteristic failure | Formal remedy/output |
|---|---|---|---|---|
| future sufficiency | CCOC | Which distinctions can an enlarged legal future expose? | future insufficiency | open-interface lower bound / finer predictive interface |
| semantic coherence | MLTR | Can one inherited source law retain its meaning after structural change? | semantic non-portability | unique coarsest source-relative repair, defect, history context |
| mechanism robustness | MRM | Do retained response mechanisms support one future prediction? | mechanism non-robustness | deterministic, typed, or set-valued report; candidate-safe state |
| evidential licensing | CED | Which target-relevant distinctions does finite imperfect evidence justify reporting? | evidential non-resolvability | compatible-world report, required target-safe resolution, risk-limited design |

Passing one companion audit does not imply passing another. Their state spaces,
initial conditions, quantifier orders, failure certificates, and remedies differ.
Shared words such as `state`, `quotient`, `refinement`, or `uncertainty` do not merge
their theorem ownership.

## 3. Conditional synthesis theorem ladder

The five proved finite synthesis layers concern four different mathematical
objects: a carrier, a repair language, a partition, and maps between carriers. Their
generic order-theoretic and optimization machinery is established prior art; the
CREST result is the ecology-program mapping, the explicit gates, and the typed
failure outputs.

### CREST-J3 — maximal synchronized common carrier

Start with a declared finite ambient synchronization of component states, a static
compatibility relation, lifted partial actions, and component-coverage obligations.
Descending transition-closure pruning yields a unique greatest compatible carrier
\(U^*\).

\[
\boxed{
\text{a nonempty common lift exists}
\iff
U^*\neq\varnothing
}
\]

and

\[
\boxed{
\text{a coverage-complete common lift exists}
\iff
U^*\text{ represents every required component label}.}
\]

Every rejected tuple has a finite action chain ending at a statically incompatible
tuple. Carrier failure is therefore returned as a finite no-go certificate rather
than hidden inside a later partition algorithm.

Proof and implementation:

- `docs/crest_maximal_common_lift_theorem_2026-08-17.md`
- `mrm/crest_common_lift.py`
- `tests/test_crest_common_lift.py`

### CREST-J4 — exact minimum relaxation of a failed carrier contract

When J3 is empty or coverage-incomplete, declare nonnegative costs for three repair
operations:

1. admitting one statically incompatible tuple;
2. disabling one originally legal transition; and
3. waiving one component-coverage obligation.

For every nonempty retained subset \(S\subseteq W\), define

\[
\begin{aligned}
A(S)&=S\setminus W_0,\\
E(S)&=\{(w,a):w\in S,\ \tau_a(w)\downarrow,
                  \ \tau_a(w)\notin S\},\\
D(S)&=\{(k,\ell):\ell\in R_k,
                  \ \ell\notin p_k(S)\}.
\end{aligned}
\]

The required fixed-witness cost is

\[
R(S)=
\sum_{w\in A(S)}c_w
+
\sum_{(w,a)\in E(S)}d_{w,a}
+
\sum_{(k,\ell)\in D(S)}r_{k,\ell},
\]

and the exact global optimum is

\[
\boxed{
R^*=\min_{\varnothing\neq S\subseteq W}R(S).}
\]

Necessity and sufficiency coincide because every retained incompatible tuple must be
admitted, every retained edge escaping \(S\) must be disabled, and every required
label absent from \(S\) must be waived; performing exactly those operations makes
\(S\) a valid witness.

With strictly positive contract-changing costs,

\[
\boxed{
R^*=0
\iff
\text{the original J3 problem is already admissible}.}
\]

Optimal repair need not be unique. The solver returns all optimal retained-subset
witnesses and reports ties. Cost values are declared scientific or normative inputs;
the theorem does not infer or endorse them.

Proof and implementation:

- `docs/crest_minimum_common_lift_relaxation_theorem_2026-08-17.md`
- `mrm/crest_common_lift_relaxation.py`
- `tests/test_crest_common_lift_relaxation.py`
- `tests/test_crest_common_lift_relaxation_degenerate_ties.py`

### CREST-J1 — unique coarsest joint state on a fixed carrier

On a declared finite common carrier \(U\), let

\[
C_\Gamma,C_\mathcal H,C_\Theta,C_{D,T}:\Pi(U)\to\Pi(U)
\]

be monotone, inflationary, idempotent audit closures, and let \(B\) be the baseline
partition. Their join closure has one least common fixed point:

\[
\boxed{
J=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B).}
\]

Hence \(J\) is the unique coarsest/least-information partition satisfying all four
representational obligations, up to block renaming. Pairwise audit commutation is
not required; fair cyclic refinement converges to the same \(J\).

The full joint state is deterministically reportable from reliability-qualified
evidence \(E_D\) exactly when

\[
\boxed{J\preceq E_D,}
\]

meaning that every evidence class lies inside one \(J\)-block. If this fails, the
sharp state report is the set of \(J\)-blocks compatible with the evidence class. A
requested target may still be deterministic even when the full state is not.

Proof and implementation:

- `docs/crest_joint_state_theorem_2026-08-17.md`
- `mrm/crest_joint_state.py`
- `tests/test_crest_joint_state.py`

### CREST-J2 — faithful-lift invariance

Let \(\pi:U\twoheadrightarrow V\) be a finite surjective contract projection that
preserves baseline/evidence/target partitions, audit-static distinctions, action
legality, and projected successors. Then every audit closure commutes with
pullback:

\[
C_i^U(\pi^*P)=\pi^*C_i^V(P),
\]

and therefore

\[
\boxed{J_U=\pi^*J_V,\qquad U/J_U\cong V/J_V.}
\]

Full-state and target-only evidence licensing are also preserved. Latent detail
invisible to every declared contract cannot change the scientific joint state.

Proof and implementation:

- `docs/crest_lift_invariance_theorem_2026-08-17.md`
- `mrm/crest_lift_invariance.py`
- `tests/test_crest_lift_invariance.py`

### CREST-J5 — one-sided lift refinement bounds

J2 requires exact faithfulness. J5 covers two controlled departures while keeping
evidence and target partitions as exact pullbacks and requiring shared action
legality and successors to commute.

A projection is **source-stronger** when the source baseline and audit-static
partitions refine the target pullbacks and the source retains every target action,
possibly adding actions. Then

\[
\boxed{
\pi^*J_V\preceq J_U,
\qquad
|U/J_U|\ge |V/J_V|.
}
\]

A projection is **source-weaker** when the source baseline and audit-static
partitions are coarser and its action sets are subsets of the target action sets.
Then

\[
\boxed{
J_U\preceq\pi^*J_V,
\qquad
|U/J_U|\le |V/J_V|.
}
\]

If both conditions hold, the inequalities collapse to J2 equality. Target-only
reportability remains invariant because evidence and target equality are exact
pullbacks. Full-state licensing is one-sided:

- source-stronger: source licensing implies target licensing;
- source-weaker: target licensing implies source licensing.

Both converses can fail. Thus adding preserved scientific obligations can only make
the required state finer, while forgetting obligations can only make it coarser.

Proof and implementation:

- `docs/crest_lax_lift_bounds_theorem_2026-08-18.md`
- `mrm/crest_lax_lift.py`
- `tests/test_crest_lax_lift.py`

## 4. The proved CREST workflow

```text
declared ambient component synchronization
    -> J3: maximal compatible transition-closed carrier U* or finite no-go
    -> if no-go: J4 exact minimum repair in a declared operation/cost language
    -> repaired J3 carrier
    -> declare four audit closures and reliability-qualified evidence
    -> J1: unique coarsest required joint state J
    -> J1: deterministic full state, target-only report, or set-valued ambiguity
    -> compare alternate lifts/contracts:
         J2 exact faithful invariance
         J5 one-sided refinement bounds when obligations differ
```

The arrows are theorem dependencies, not a universal order for field research.
Evidence, mechanisms, targets, or repair priorities may be specified first in an
application.

## 5. What “one state” now means

The strongest safe statement is:

\[
\boxed{
\begin{aligned}
&\text{one declared finite ambient synchronization}
\xrightarrow{\mathrm{J3}}
\text{one maximal coherent carrier or finite no-go},\\
&\text{J3 no-go plus a declared repair language/cost schedule}
\xrightarrow{\mathrm{J4}}
\text{an exact minimum value and all optimal witnesses},\\
&\text{one admissible repaired contract}
\xrightarrow{\mathrm{J1}}
\text{one unique coarsest four-audit required state }J,\\
&\text{fully licensed state}
\Longleftrightarrow
J\preceq E_D,\\
&\text{faithfully redundant lift}
\xrightarrow{\mathrm{J2}}
\text{the same quotient state up to isomorphism},\\
&\text{one-sided obligation change}
\xrightarrow{\mathrm{J5}}
\text{a certified refinement or coarsening bound.}
\end{aligned}}
\]

This does **not** prove:

- a unique state across different future grammars, inherited laws, mechanism
  families, evidence contracts, targets, or ambient alignments;
- a unique repair across different operation languages, costs, or tied optima;
- that every nonfaithful lift comparison satisfies a J5 direction;
- that every arbitrary collection of four companion models has a nonempty
  coverage-complete synchronization;
- that the four audits are philosophically exhaustive;
- that their costs, defects, memory bounds, and risks add; or
- that current ecological observations identify the required state.

## 6. Ecological reading

For a state labelled **pollination maintained**:

1. J3 asks whether future, inherited, mechanism, and evidence descriptions can be
   synchronized into any transition-consistent set of joint ecological worlds.
2. If synchronization fails, J4 separates three concessions: admit a previously
   forbidden joint world, remove a declared future transition, or stop requiring one
   component state to be represented. Their costs must be declared rather than
   hidden.
3. CCOC asks whether future colonization, reconnection, or intervention exposes a
   distinction hidden by the current label.
4. MLTR asks whether the inherited meaning survives pollinator turnover or needs a
   source-relative split.
5. MRM asks whether retained response mechanisms agree on restoration or
   disturbance outcomes.
6. CED asks whether field evidence has earned the distinction needed by the report.
7. J1 computes the least joint distinction satisfying the declared obligations.
8. J2 guarantees that scientifically invisible latent duplication does not change
   the resulting state.
9. J5 distinguishes a genuinely stronger ecological contract from a genuinely
   weaker one: adding future probes or mechanism distinctions can only refine the
   state, while deleting obligations can only coarsen it.

The result is contract-relative without being arbitrary: scientists declare what
the representation and any repair must preserve, while declared dynamics and
evidence can objectively refute a merge, synchronization, or claimed comparison.

## 7. Repository ownership remains separate

- **CCOC:** independently optimized closed-vs-open interface complexity.
- **MLTR:** one inherited source law, target transport, least semantic repair,
  defect, and history.
- **MRM:** retained mechanism disagreement, candidate-safe state, and honest
  deterministic/typed/set-valued prediction.
- **CED:** finite evidence, target reportability, observation failure, calibration,
  and risk-limited design.
- **CREST synthesis in MRM:** conditional carrier construction, typed minimum
  carrier-contract relaxation, joint fixed point, evidence gate, faithful-lift
  invariance, and one-sided lift bounds.

The synthesis theorems consume companion contracts; they do not transfer ownership
of the companion headline theorems to MRM. J4 is not MLTR inherited-semantic repair,
and J5 is not a generic novelty claim for simulation or abstraction precision.

## 8. Prior-art firewall

CREST does not claim novelty for:

- partition refinement, bisimulation, causal/predictive state abstraction;
- closure operators, lattice fixed points, or fair iteration;
- invariant/safety kernels or viability-style pruning;
- minimum-cost model repair, transition deletion, or exhaustive subset search;
- quotient naturality, simulation, abstraction soundness, or one-sided precision
  bounds;
- adequacy-for-purpose, perspectival representation, partial observability, or
  ecological model transferability.

The candidate contribution is the theorem-grounded ecology-specific diagnostic
architecture and the explicit sequence of carrier, typed repair, partition,
evidence, and lift-comparison conditions.

## 9. Current proof control

- [Companion proof recovery](crest_proof_recovery_2026-08-17.md) — detailed CCOC,
  MLTR, MRM, and CED proof audit before synthesis.
- [Synthesis proof ledger](crest_synthesis_proof_ledger_2026-08-17.md) — canonical
  J1/J2/J3/J4/J5 proof status and boundaries.
- [Cross-repository validation](crest_final_validation_2026-08-17.md) — ownership
  and quantifier firewalls.

## 10. Next proof questions

The main unresolved mathematical directions are now:

1. controlled/existential rather than universal common-lift viability;
2. weakest simulation conditions and comparisons when shared action semantics do
   not commute exactly;
3. quantitative bounds from approximate lift faithfulness;
4. richer repair languages and comparison of their optimal values;
5. stochastic, approximate, infinite, and risk-limited variants; and
6. empirical inference and validation of synchronization, costs, and contract
   objects.

A new theorem must change one of these coupled questions. Renaming another fixed
partition refinement, generic repair problem, or simulation inequality is not a
CREST synthesis contribution.
