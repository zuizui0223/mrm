# Contract-Relative Ecological State Theory (CREST)

> **Status:** program-level metatheory with seven conditional finite synthesis
> theorems. CREST does not merge CCOC, MLTR, MRM, and CED, does not claim novelty
> for generic quotient/refinement/repair/viability machinery, and does not supply a
> nature-given ontology of ecological states.

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

## 3. Carrier semantics

The companion contracts do not automatically share one world set. CREST first asks
whether their component descriptions can be synchronized into a finite carrier.

### J3 — universal common carrier

For finite ambient worlds \(W\), static compatibility \(W_0\), and partial
deterministic actions \(\tau_a\), define

\[
F(S)=\{w\in S\cap W_0:
\tau_a(w)\downarrow\Rightarrow\tau_a(w)\in S
\text{ for every action }a\}.
\]

Descending iteration from \(W_0\) yields the unique greatest universally
transition-closed carrier \(U^*\).

\[
\text{nonempty common lift exists}\iff U^*\neq\varnothing.
\]

A coverage-complete lift exists iff \(U^*\) represents every required component
label. Eliminated worlds have finite action-chain certificates. J3 is appropriate
when the representation must survive **every** declared legal action.

### J6 — controlled common carrier

Partition actions into uncontrollable \(A_u\) and controllable \(A_c\). Define

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
carrier \(K^*\).

\[
\text{nonempty controlled lift exists}\iff K^*\neq\varnothing.
\]

Coverage is complete iff \(K^*\) represents all required labels. Every nonempty
\(K^*\) admits a deterministic memoryless safe selector. Eliminated worlds receive
finite AND/OR certificates for:

- static incompatibility;
- uncontrollable escape; or
- failure of every legal control choice.

J6 is appropriate when unavoidable exterior moves must all be survived but one safe
control may be selected. A no-op or wait option must be declared explicitly.

Under control nonblocking, the corresponding J3 universal carrier is contained in
J6's carrier; strict inclusion is possible. J3 and J6 certify different action
quantifications rather than competing notions of correctness.

## 4. Typed carrier repair

### J4 — repair of the universal J3 contract

J4 permits:

1. admitting an incompatible world;
2. disabling one legal transition; and
3. waiving one coverage obligation.

For every nonempty retained \(S\subseteq W\), let

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

The operations are necessary and sufficient for that retained witness. Costs are
inputs, and tied optima remain explicit.

### J7 — repair of the controlled J6 contract

J7 preserves the distinction between unavoidable transitions and selectable
controls. Its repair language permits:

1. admitting an incompatible world;
2. disabling one **uncontrollable** transition;
3. installing one declared local fallback control; and
4. waiving one coverage obligation.

For nonempty \(S\subseteq W\), define \(A(S)\) and \(D(S)\) as above, and

\[
U(S)=\{(w,a):w\in S,\ a\in A_u,
\tau_a(w)\downarrow,\ \tau_a(w)\notin S\}.
\]

Let

\[
C(S)=\{w\in S:\nexists a\in A_c
\text{ with }\tau_a(w)\downarrow\text{ and }\tau_a(w)\in S\}.
\]

The subset is **repair-feasible** only when each \(w\in C(S)\) has a declared
fallback successor \(f(w)\in S\). For feasible \(S\),

\[
\boxed{
R_c(S)=
\sum_{w\in A(S)}c_w+
\sum_{(w,a)\in U(S)}d_{w,a}+
\sum_{w\in C(S)}g_w+
\sum_{(k,\ell)\in D(S)}r_{k,\ell}.
}
\]

If \(\mathcal F\) is the family of repair-feasible nonempty subsets, then

\[
\boxed{R_c^*=\min_{S\in\mathcal F}R_c(S)}
\]

when \(\mathcal F\neq\varnothing\). If \(\mathcal F=\varnothing\), no repair exists
in the declared language.

For a fixed feasible witness, every term is necessary: incompatible worlds must be
admitted, uncontrollable exits must be blocked, control-deficient worlds need their
declared fallback, and missing labels must be waived. Those operations are also
sufficient, so the bounds coincide. With strictly positive change costs,
\(R_c^*=0\) iff the original J6 contract is admissible. Tied optima remain explicit.

J4 and J7 are not interchangeable, and neither is MLTR semantic repair. J4/J7 weaken
a cross-component carrier contract before J1 constructs a state; MLTR repairs one
inherited macro-law after structural replacement.

## 5. Joint state on an admissible carrier

### J1 — unique coarsest four-audit state

On finite carrier \(U\), let

\[
C_\Gamma,C_\mathcal H,C_\Theta,C_{D,T}:\Pi(U)\to\Pi(U)
\]

be monotone, inflationary, idempotent closures, with baseline \(B\). Their join gives

\[
\boxed{J=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B).}
\]

`J` is the unique coarsest partition satisfying all four obligations. Fair finite
iteration reaches it without pairwise commutation; a single pass through separately
computed minima can fail.

For reliability-qualified evidence partition \(E_D\),

\[
\boxed{
\text{full deterministic state report exists}\iff J\preceq E_D.
}
\]

Otherwise the sharp state report is the set of `J` blocks compatible with the
evidence class. A target may still be deterministic without full-state resolution.

## 6. Comparing lifts and contracts

### J2 — faithful-lift equality

If surjection \(\pi:U\twoheadrightarrow V\) preserves baseline, evidence, target,
audit labels, action legality, and successors exactly, then

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

- finer source obligations plus all target actions imply
  \[
  \boxed{\pi^*J_V\preceq J_U};
  \]
- coarser source obligations plus a subset of target actions imply
  \[
  \boxed{J_U\preceq\pi^*J_V}.
  \]

Both directions recover J2 equality. Target-only licensing is invariant; full-state
licensing is one-sided in the corresponding direction.

## 7. Proved dependency map

```text
declared ambient synchronization
  -> choose action contract:
       J3: survive every legal action
       J6: survive all uncontrollable moves + choose one safe control
  -> maximal carrier or finite typed no-go
  -> choose matching repair language if needed:
       J4: universal-contract repair
       J7: controlled-contract repair
  -> admissible carrier
  -> J1 unique coarsest four-audit state + evidence gate
  -> compare alternate lifts/contracts:
       J2 faithful equality
       J5 one-sided bounds
```

These arrows are theorem dependencies, not a mandatory field-work order.

## 8. Ecological reading

For a state called **pollination maintained**:

- CCOC tests future colonization, reconnection, and intervention exposure;
- MLTR tests inherited meaning after pollinator turnover;
- MRM tests retained mechanisms' restoration predictions;
- CED tests whether field evidence earned the distinction;
- J3 asks whether all declared actions preserve one synchronized carrier;
- J6 asks whether unavoidable exterior moves can be survived under one policy;
- J4/J7 price the least declared concession when the relevant carrier fails;
- J1 constructs the least joint state; and
- J2/J5 compare alternative latent descriptions and contract strengths.

Contract-relativity is constrained rather than arbitrary: scientists declare the
obligations, action roles, fallbacks, and costs, while dynamics and evidence can
refute a merge, carrier, policy, repair, or report.

## 9. Prior-art and ownership firewall

CREST does not claim novelty for:

- partition refinement, closure operators, or lattice fixed points;
- invariant, viability, and safety kernels;
- controllable-predecessor iteration or memoryless finite safety strategies;
- minimum-cost model/safety-game repair or subset optimization;
- quotient naturality, simulation, or abstraction precision;
- adequacy-for-purpose, partial observability, or ecological transferability.

Its candidate contribution is the theorem-grounded ecology-specific contract map and
its typed carrier, repair, partition, evidence, and comparison gates.

Repository ownership remains:

- CCOC — open-future interface obstruction;
- MLTR — inherited-law transport and semantic repair;
- MRM — mechanism-robust prediction;
- CED — evidential reportability and design;
- CREST synthesis in MRM — conditional cross-contract coupling.

## 10. What is not proved

- a nature-given synchronization, action-role assignment, fallback, or cost scale;
- that every companion model admits a coverage-complete J3/J6 carrier;
- policy optimality beyond safety;
- exhaustiveness of the J4/J7 repair languages;
- arbitrary transition redirection or action-role reclassification;
- comparison for every nonfaithful lift;
- stochastic, partial-observation, delayed-control, approximate, or infinite forms;
- philosophical exhaustiveness of the four axes; or
- empirical validity of the declared contracts.

## 11. Proof control and next questions

- [Synthesis proof ledger](crest_synthesis_proof_ledger_2026-08-17.md)
- [Companion proof recovery](crest_proof_recovery_2026-08-17.md)
- [Cross-repository validation](crest_final_validation_2026-08-17.md)

The next high-value questions are:

1. partial-observation and finite-memory control;
2. stochastic/adversarial risk-limited safety and repair;
3. weakest/approximate lift simulations;
4. richer repair-language comparison; and
5. empirical inference of synchronization, action roles, fallbacks, costs, and
   evidence.

A new theorem must change a coupled premise or failure boundary. Renaming another
refinement, viability, or repair result is not a CREST contribution.
