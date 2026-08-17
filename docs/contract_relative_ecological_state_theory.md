# Contract-Relative Ecological State Theory (CREST)

> **Status:** program-level metatheory with four conditional finite synthesis
> theorems. CREST does not merge CCOC, MLTR, MRM, and CED, does not claim that their
> generic quotient/refinement/repair machinery is new, and does not supply a
> nature-given canonical ontology of ecological states.

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

The older slogan

\[
\text{“ecological state identity is contract-relative”}
\]

should be read as shorthand for **scientific state-representation adequacy**, not
as a claim that ecological systems lack mind-independent structure.

## 2. Four companion adequacy audits

| Audit | Repository | Question | Characteristic failure | Formal remedy/output |
|---|---|---|---|---|
| future sufficiency | CCOC | Which distinctions can an enlarged legal future expose? | future insufficiency | open-interface lower bound / finer predictive interface |
| semantic coherence | MLTR | Can one inherited source law retain its meaning after structural change? | semantic non-portability | unique coarsest source-relative repair, defect, history context |
| mechanism robustness | MRM | Do retained response mechanisms support one future prediction? | mechanism non-robustness | deterministic, typed, or set-valued report; candidate-safe state |
| evidential licensing | CED | Which target-relevant distinctions does finite imperfect evidence justify reporting? | evidential non-resolvability | compatible-world report, required target-safe resolution, risk-limited design |

Passing one companion audit does not imply passing another. Their state spaces,
initial conditions, quantifier orders, failure certificates, and remedies differ.
The shared use of words such as `state`, `quotient`, or `refinement` does not merge
their theorem ownership.

## 3. Conditional synthesis theorem ladder

CREST now has four proved finite synthesis layers. Their generic order-theoretic and
optimization machinery is established prior art; the program result is the explicit
ecology mapping, its gates, and its typed failure outputs.

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
tuple. Thus carrier failure is returned as a finite no-go certificate rather than
hidden inside a later partition algorithm.

Proof and implementation:

- `docs/crest_maximal_common_lift_theorem_2026-08-17.md`
- `mrm/crest_common_lift.py`
- `tests/test_crest_common_lift.py`

### CREST-J4 — exact minimum relaxation of a failed carrier contract

When J3 is empty or coverage-incomplete, declare nonnegative costs for exactly three
repair operations:

1. admitting one statically incompatible tuple;
2. disabling one originally legal transition; and
3. waiving one component-coverage obligation.

For every nonempty retained subset \(S\subseteq W\), the required operations are
forced. Write

\[
\begin{aligned}
A(S)&=S\setminus W_0,\\
E(S)&=\{(w,a):w\in S,\ \tau_a(w)\downarrow,
                  \ \tau_a(w)\notin S\},\\
D(S)&=\{(k,\ell):\ell\in R_k,
                  \ \ell\notin p_k(S)\}.
\end{aligned}
\]

Then the exact fixed-witness cost is

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

The lower bound is necessary because every retained incompatible tuple must be
admitted, every retained edge escaping \(S\) must be disabled, and every required
label absent from \(S\) must be waived. Performing exactly those operations is
sufficient, so the bounds coincide.

With strictly positive contract-changing costs,

\[
\boxed{
R^*=0
\iff
\text{the original J3 problem is already admissible}.}
\]

Optimal repair need not be unique. The solver returns all optimal retained-subset
witnesses and a deterministic representative while explicitly reporting ties. Cost
values are declared scientific or normative inputs; the theorem does not infer or
endorse them.

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

Full-state and target-only evidence licensing are also preserved. Thus adding
latent detail that no declared contract can see does not change the scientific
joint state. Adding an audit-visible distinction can break the projection and make
the joint state finer.

Proof and implementation:

- `docs/crest_lift_invariance_theorem_2026-08-17.md`
- `mrm/crest_lift_invariance.py`
- `tests/test_crest_lift_invariance.py`

## 4. The proved CREST workflow

```text
declared ambient component synchronization
    -> J3: maximal compatible transition-closed carrier U* or finite no-go
    -> if no-go: J4 exact minimum repair in the declared operation/cost language
    -> repaired J3 carrier
    -> declare four audit closures and reliability-qualified evidence
    -> J1: unique coarsest required joint state J
    -> J1: deterministic full state, target-only report, or set-valued ambiguity
    -> J2: invariance under faithfully redundant refinements of the common lift
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
\\
&\xrightarrow{\mathrm{J3}}
\text{one maximal coherent carrier or finite no-go},
\\
&\text{J3 no-go plus a declared repair language/cost schedule}
\\
&\xrightarrow{\mathrm{J4}}
\text{an exact minimum repair value and all optimal witnesses},
\\
&\text{one admissible repaired contract}
\\
&\xrightarrow{\mathrm{J1}}
\text{one unique coarsest four-audit required state }J,
\\
&\text{fully licensed state}
\Longleftrightarrow
J\preceq E_D,
\\
&\text{faithfully redundant lift}
\Longrightarrow
\text{the same quotient state up to isomorphism.}
\end{aligned}}
\]

This does **not** prove:

- a unique state across different future grammars, inherited laws, mechanism
  families, evidence contracts, targets, or ambient alignments;
- a unique repair across different operation languages, costs, or tied optima;
- that every arbitrary collection of four companion models has a nonempty
  coverage-complete synchronization;
- that the four audits are philosophically exhaustive;
- that their costs, defects, memory bounds, and risks add; or
- that current ecological observations identify the required state.

## 6. Ecological reading

For a state labelled **pollination maintained**:

1. J3 asks whether the future, inherited, mechanism, and evidence descriptions can
   be synchronized into any transition-consistent set of joint ecological worlds.
2. If that synchronization fails, J4 distinguishes three possible concessions:
   admit a previously forbidden joint world, remove a declared future transition,
   or stop requiring one component state to be represented. Their costs must be
   declared rather than hidden.
3. CCOC asks whether future colonization, reconnection, or intervention exposes a
   distinction hidden by the current label.
4. MLTR asks whether the inherited meaning survives pollinator turnover or needs a
   source-relative split.
5. MRM asks whether retained response mechanisms agree on restoration or
   disturbance outcomes.
6. CED asks whether field evidence has earned the distinction needed by the report.
7. J1 computes the least joint distinction satisfying the declared obligations.
8. J2 guarantees that duplicating scientifically invisible latent descriptions does
   not change the resulting state.

The result is contract-relative without being arbitrary: the scientist declares
what the representation and any repair must preserve, while the declared dynamics
and evidence can objectively refute a proposed merge or synchronization.

## 7. Repository ownership remains separate

- **CCOC:** independently optimized closed-vs-open interface complexity.
- **MLTR:** one inherited source law, target transport, least semantic repair,
  defect, and history.
- **MRM:** retained mechanism disagreement, candidate-safe state, and honest
  deterministic/typed/set-valued prediction.
- **CED:** finite evidence, target reportability, observation failure, calibration,
  and risk-limited design.
- **CREST synthesis in MRM:** conditional carrier construction, typed minimum
  carrier-contract relaxation, joint fixed point, evidence gate, and faithful-lift
  invariance.

The synthesis theorems consume companion contracts; they do not transfer ownership
of the companion headline theorems to MRM. J4 must not be redescribed as MLTR's
inherited-semantic repair.

## 8. Prior-art firewall

CREST does not claim novelty for:

- partition refinement, bisimulation, causal/predictive state abstraction;
- closure operators, lattice fixed points, or fair iteration;
- invariant/safety kernels or viability-style pruning;
- minimum-cost model repair, transition deletion, or exhaustive subset search;
- quotient naturality under structure-preserving maps;
- adequacy-for-purpose, perspectival representation, partial observability, or
  ecological model transferability.

The candidate contribution is the theorem-grounded ecology-specific diagnostic
architecture and the explicit sequence of carrier, typed repair, partition,
evidence, and lift conditions.

## 9. Current proof control

- [Companion proof recovery](crest_proof_recovery_2026-08-17.md) — detailed CCOC,
  MLTR, MRM, and CED proof audit before synthesis.
- [Synthesis proof ledger](crest_synthesis_proof_ledger_2026-08-17.md) — canonical
  J1/J2/J3/J4 proof status and boundaries.
- [Cross-repository validation](crest_final_validation_2026-08-17.md) — ownership
  and quantifier firewalls.

## 10. Next proof questions

The main unresolved mathematical directions are now:

1. richer repair languages, including transition redirection or component-label
   revision, and relations among their optima;
2. lax/one-sided lift maps yielding refinement inequalities rather than exact J2
   invariance;
3. existential/control-selective common-lift viability;
4. stochastic, approximate, infinite, and risk-limited variants; and
5. empirical inference and validation of synchronization, costs, and contract
   objects.

A new theorem must change one of these coupled questions. Renaming another fixed
partition refinement or generic repair problem is not a CREST synthesis
contribution.
