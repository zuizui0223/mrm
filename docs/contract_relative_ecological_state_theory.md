# Contract-Relative Ecological State Theory (CREST)

> **Status:** program-level metatheory with seven conditional finite synthesis
> theorems and one supporting obstruction. CREST does not merge CCOC, MLTR, MRM,
> and CED, does not claim novelty for generic quotient/refinement/repair/viability
> machinery, and does not supply a nature-given ontology of ecological states.

## 1. Central principle

> **Treating two ecological configurations as the same state is a scientific
> commitment about which differences may be ignored for a declared future,
> inherited meaning, retained mechanism family, evidence contract, and target.**

Write the program contract schematically as

\[
\mathcal C=(\Gamma,\mathcal H,\Theta,D;T).
\]

“State identity is contract-relative” concerns scientific representation adequacy.
It does not deny mind-independent ecological structure.

## 2. Four companion audits

| Audit | Repository | Question | Failure | Formal output |
|---|---|---|---|---|
| future sufficiency | CCOC | Which distinctions can an enlarged legal future expose? | future insufficiency | interface lower bound / finer predictive state |
| semantic coherence | MLTR | Can one inherited law retain its meaning after change? | semantic non-portability | least source-relative repair, defect, history |
| mechanism robustness | MRM | Do retained response mechanisms support one prediction? | mechanism non-robustness | deterministic, typed, or set-valued report |
| evidential licensing | CED | Which distinctions does finite imperfect evidence justify reporting? | evidential non-resolvability | compatible-world report, required resolution, design |

The audits differ in carriers, starting partitions, quantifier orders, certificates,
and remedies. Passing one does not satisfy another automatically.

### Synthesis ownership

Results whose quantified statement essentially couples at least two companion
contracts belong to a fifth logical unit: the **CREST synthesis unit**. The J/O
series is therefore not an MRM theorem family. MRM is only its current physical
host. The ownership charter is `crest_synthesis/README.md`, and physical extraction
to `zuizui0223/crest` is specified in
`docs/crest_synthesis_migration_manifest_2026-08-18.md`.

## 3. Carrier semantics

The companion contracts do not automatically share one world set. CREST first asks
whether their component descriptions can be synchronized into a finite carrier.

### J3 — universal common carrier

For finite ambient worlds `W`, static compatibility `W0`, and partial deterministic
actions `tau_a`, define

\[
F(S)=\{w\in S\cap W_0:
\tau_a(w)\downarrow\Rightarrow\tau_a(w)\in S
\text{ for every action }a\}.
\]

Descending iteration from `W0` yields the unique greatest universally
transition-closed carrier `U*`.

\[
\text{nonempty common lift exists}\iff U^*\neq\varnothing.
\]

A coverage-complete lift exists iff `U*` represents every required component label.
Eliminated worlds have finite action-chain certificates. J3 is appropriate when the
representation must survive **every** declared legal action.

### J6 — controlled common carrier

Partition actions into uncontrollable `A_u` and controllable `A_c`. Define

\[
\begin{aligned}
G(S)=\{w\in S\cap W_0:\;&
\forall a\in A_u,
\tau_a(w)\downarrow\Rightarrow\tau_a(w)\in S,\\
&\exists a\in A_c,
\tau_a(w)\downarrow\text{ and }\tau_a(w)\in S\}.
\end{aligned}
\]

Descending iteration yields the unique greatest robustly controlled-invariant
carrier `K*`.

\[
\text{nonempty controlled lift exists}\iff K^*\neq\varnothing.
\]

Coverage is complete iff `K*` represents all required labels. Every nonempty `K*`
admits a deterministic memoryless safe selector. Eliminated worlds receive finite
AND/OR certificates for static incompatibility, uncontrollable escape, or failure
of every legal control choice.

J6 is appropriate when unavoidable exterior moves must all be survived but one safe
control may be selected. A no-op or wait option must be declared explicitly. Under
control nonblocking, the corresponding J3 carrier is contained in J6's carrier;
strict inclusion is possible.

## 4. Typed carrier repair

### J4 — universal J3 repair characterization

J4 permits admitting an incompatible world, disabling one legal transition, and
waiving one coverage obligation. For every nonempty retained `S subseteq W`, define

\[
\begin{aligned}
A(S)&=S\setminus W_0,\\
E(S)&=\{(w,a):w\in S,\tau_a(w)\downarrow,
\tau_a(w)\notin S\},\\
D(S)&=\{(k,\ell):\ell\in R_k,\ell\notin p_k(S)\}.
\end{aligned}
\]

Then

\[
R(S)=\sum_{w\in A(S)}c_w+
\sum_{(w,a)\in E(S)}d_{w,a}+
\sum_{(k,\ell)\in D(S)}r_{k,\ell},
\]

and

\[
\boxed{R^*=\min_{\varnothing\neq S\subseteq W}R(S).}
\]

For a **fixed** `S`, the operations and cost are necessary and sufficient. Finding
the best `S` is a separate global selection problem.

### J7 — controlled J6 repair characterization

J7 permits admitting an incompatible world, disabling one uncontrollable
transition, installing one declared local fallback control, and waiving one
coverage obligation.

For nonempty `S subseteq W`, define `A(S)` and `D(S)` as above, and

\[
U(S)=\{(w,a):w\in S,\ a\in A_u,
\tau_a(w)\downarrow,\ \tau_a(w)\notin S\}.
\]

Let

\[
C(S)=\{w\in S:\nexists a\in A_c
\text{ with }\tau_a(w)\downarrow\text{ and }\tau_a(w)\in S\}.
\]

The subset is repair-feasible only when every `w in C(S)` has a declared fallback
successor `f(w) in S`. For feasible `S`,

\[
\boxed{
R_c(S)=
\sum_{w\in A(S)}c_w+
\sum_{(w,a)\in U(S)}d_{w,a}+
\sum_{w\in C(S)}g_w+
\sum_{(k,\ell)\in D(S)}r_{k,\ell}.
}
\]

If `F` is the family of repair-feasible nonempty subsets, then

\[
\boxed{R_c^*=\min_{S\in\mathcal F}R_c(S)}
\]

when `F` is nonempty; otherwise no repair exists in the declared language. Again,
necessity and sufficiency are fixed-witness statements before global selection.

### Computational boundary

The J4-REPAIR and J7-REPAIR decision problems are NP-complete by direct reductions
from weighted set cover. The reduction already works:

- for J4 with no transitions; and
- for J7 with no uncontrollable actions and one controllable self-loop per world.

Thus the coverage-selection term alone suffices for hardness. The executable
solvers enumerate all `2^|W|-1` nonempty subsets. They are exact exponential oracles,
not tractability results. See
`docs/crest_repair_complexity_boundary_2026-08-18.md`.

J4 and J7 are not interchangeable, and neither is MLTR semantic repair. J4/J7 weaken
a cross-component carrier contract before J1 constructs a state; MLTR repairs one
inherited macro-law after structural replacement.

## 5. Joint state on an admissible carrier

### J1 — unique coarsest four-audit state

On finite carrier `U`, let

\[
C_\Gamma,C_\mathcal H,C_\Theta,C_{D,T}:\Pi(U)\to\Pi(U)
\]

be monotone, inflationary, idempotent closures, with baseline `B`. Their join gives

\[
\boxed{J=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B).}
\]

`J` is the unique coarsest partition satisfying all four obligations. Fair finite
iteration reaches it without pairwise commutation; a single pass through separately
computed minima can fail.

For reliability-qualified evidence partition `E_D`,

\[
\boxed{
\text{full deterministic state report exists}\iff J\preceq E_D.
}
\]

Otherwise the sharp state report is the set of `J` blocks compatible with the
evidence class. A target may still be deterministic without full-state resolution.

The least-common-fixed-point machinery is classical closure/refinement substrate.
J1's CREST role is the explicit joint four-contract construction and evidence gate;
it must not be sold as a new generic partition theorem.

## 6. Comparing lifts and contracts

### J2 — faithful-lift equality

If surjection `pi:U -> V` preserves baseline, evidence, target, audit labels, action
legality, and successors exactly, then

\[
C_i^U(\pi^*P)=\pi^*C_i^V(P)
\]

and

\[
\boxed{J_U=\pi^*J_V,\qquad U/J_U\cong V/J_V.}
\]

Scientifically invisible latent duplication cannot change the state or licensing.

### J5 — one-sided lift bounds

With exact evidence/target pullback and exact shared-action semantics:

\[
\text{finer source obligations}\Rightarrow\pi^*J_V\preceq J_U,
\]

\[
\text{coarser source obligations}\Rightarrow J_U\preceq\pi^*J_V.
\]

Both directions recover J2 equality. Target-only licensing is invariant;
full-state licensing is one-sided in the corresponding direction.

## 7. Supporting obstruction O1

O1 gives a finite J7×J1/CED witness with

\[
\boxed{R_{\mathrm{struct}}^*=1<R_{\mathrm{licensed}}^*=2.}
\]

The cheapest controlled-carrier repair can leave the full joint state unresolved by
the evidence, while a more expensive repair is fully licensed. The target can still
be reportable under the cheaper repair. O1 therefore shows that carrier feasibility,
state adequacy, and evidential licensing are distinct optimization targets. It is a
supporting obstruction, not J8.

## 8. Proved dependency map

```text
declared ambient synchronization
  -> choose action contract:
       J3: survive every legal action
       J6: survive all uncontrollable moves + choose one safe control
  -> maximal carrier or finite typed no-go
  -> choose matching repair language if needed:
       J4: universal-contract repair characterization
       J7: controlled-contract repair characterization
  -> admissible carrier
  -> J1 unique coarsest four-audit state + evidence gate
  -> compare alternate lifts/contracts:
       J2 faithful equality
       J5 one-sided bounds
  -> O1 warns that cheapest structural and licensed repairs can differ
```

These arrows are theorem dependencies, not a mandatory field-work order.

## 9. Ecological reading

For a state called **pollination maintained**:

- CCOC tests future colonization, reconnection, and intervention exposure;
- MLTR tests inherited meaning after pollinator turnover;
- MRM tests retained mechanisms' restoration predictions;
- CED tests whether field evidence earned the distinction;
- J3 asks whether every declared action preserves a synchronized carrier;
- J6 asks whether unavoidable exterior moves can be survived under one policy;
- J4/J7 price declared concessions when the relevant carrier fails;
- J1 constructs the least joint state; and
- J2/J5 compare alternative latent descriptions and contract strengths.

Contract-relativity is constrained rather than arbitrary: scientists declare the
obligations, action roles, fallbacks, and costs, while dynamics and evidence can
refute a merge, carrier, policy, repair, or report.

## 10. Prior-art and ownership firewall

CREST does not claim novelty for:

- partition refinement, closure operators, or lattice fixed points;
- invariant, viability, and safety kernels;
- controllable-predecessor iteration or memoryless finite safety strategies;
- minimum-cost model/safety-game repair, weighted set cover, or subset optimization;
- quotient naturality, simulation, or abstraction precision;
- adequacy-for-purpose, partial observability, or ecological transferability.

Its candidate contribution is the theorem-grounded ecology-specific contract map and
its typed carrier, repair, partition, evidence, and comparison gates.

Ownership remains:

- CCOC — open-future interface obstruction;
- MLTR — inherited-law transport and semantic repair;
- MRM — mechanism-robust prediction;
- CED — evidential reportability and design; and
- CREST synthesis unit — conditional cross-contract coupling.

## 11. What is not proved

- a nature-given synchronization, action-role assignment, fallback, or cost scale;
- that every companion model admits a coverage-complete J3/J6 carrier;
- policy optimality beyond safety;
- exhaustiveness of the J4/J7 repair languages;
- a polynomial algorithm or tractable subclass classification for J4/J7;
- arbitrary transition redirection or action-role reclassification;
- comparison for every nonfaithful lift;
- stochastic, partial-observation, delayed-control, approximate, or infinite forms;
- philosophical exhaustiveness of the four axes; or
- empirical validity of the declared contracts.

## 12. Routing and stop rule

Single-axis work returns to its companion repository. Essential multi-axis work may
enter the CREST synthesis unit only if it establishes a new coupled
noncommutation, impossibility, necessary-and-sufficient boundary, or minimality
statement. Generic algorithmic extension is insufficient.

The J/O series is frozen before physical extraction. No J8 or new O-family may be
implemented under `mrm/`. Current work is limited to proof correction, complexity
and prior-art audit, regression testing, manuscript consolidation, and migration.

Proof controls:

- [Synthesis proof ledger](crest_synthesis_proof_ledger_2026-08-17.md)
- [Companion proof recovery](crest_proof_recovery_2026-08-17.md)
- [Cross-repository validation](crest_final_validation_2026-08-17.md)
- [Next-proof novelty gate](crest_next_proof_novelty_gate_2026-08-18.md)
- [Unit charter](../crest_synthesis/README.md)
