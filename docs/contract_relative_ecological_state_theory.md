# Contract-Relative Ecological State Theory (CREST)

> **Status:** program-level metatheory with six conditional finite synthesis
> theorems. CREST does not merge CCOC, MLTR, MRM, and CED, does not claim novelty
> for generic quotient/refinement/repair/viability machinery, and does not supply a
> nature-given ontology of ecological states.

## 1. Central principle

> **Treating two ecological configurations as the same state is a scientific
> commitment about which differences may be ignored for a declared future,
> inherited meaning, retained mechanism family, evidence contract, and target.**

Write the program-level contract schematically as

\[
\mathcal C=(\Gamma,\mathcal H,\Theta,D;T).
\]

The phrase “state identity is contract-relative” concerns the adequacy of a
scientific state representation. It does not deny mind-independent ecological
structure.

## 2. Four companion audits

| Audit | Repository | Question | Failure | Output/remedy |
|---|---|---|---|---|
| future sufficiency | CCOC | Which distinctions can an enlarged legal future expose? | future insufficiency | interface lower bound or finer predictive state |
| semantic coherence | MLTR | Can one inherited law retain its meaning after structural change? | semantic non-portability | least source-relative repair, defect, history |
| mechanism robustness | MRM | Do retained response mechanisms support one prediction? | mechanism non-robustness | deterministic, typed, or set-valued report |
| evidential licensing | CED | Which distinctions does finite imperfect evidence justify reporting? | evidential non-resolvability | compatible-world report, required resolution, design |

The audits differ in carrier, starting partition, quantifier order, certificate, and
remedy. Passing one does not silently satisfy another.

## 3. Synthesis requires a common carrier

The four companion contracts do not automatically share one world set. CREST first
asks whether their declared component descriptions can be synchronized into a
finite carrier. It provides two carrier semantics.

### J3 — universal carrier

Given finite candidate joint worlds \(W\), static compatibility \(W_0\), and partial
deterministic transitions \(\tau_a\), define

\[
F(S)=\{w\in S\cap W_0:
\tau_a(w)\downarrow\Rightarrow\tau_a(w)\in S
\text{ for every declared action }a\}.
\]

Descending iteration from \(W_0\) reaches the unique greatest universally
transition-closed carrier \(U^*\).

\[
\text{nonempty common lift exists}\iff U^*\neq\varnothing.
\]

A coverage-complete lift exists iff \(U^*\) represents every required component
label. Eliminated worlds have finite action-chain certificates.

J3 is appropriate when the representation must survive every declared legal action.

### J6 — controlled carrier

Partition the actions into uncontrollable \(A_u\) and controllable \(A_c\). Define

\[
\begin{aligned}
G(S)=\{w\in S\cap W_0:\;&
\forall a\in A_u,
\tau_a(w)\downarrow\Rightarrow\tau_a(w)\in S,\\
&\exists a\in A_c,
\tau_a(w)\downarrow\text{ and }\tau_a(w)\in S\}.
\end{aligned}
\]

Descending iteration reaches the unique greatest robustly controlled-invariant
carrier \(K^*\).

\[
\text{nonempty controlled common lift exists}\iff K^*\neq\varnothing.
\]

A coverage-complete controlled lift exists iff \(K^*\) represents all required
labels. Every nonempty \(K^*\) admits a deterministic memoryless safe selector.
Every eliminated world has a finite typed AND/OR certificate:

- static incompatibility;
- an uncontrollable escape; or
- failure of every legal control choice.

J6 is appropriate when unavoidable exterior moves must all be survived but the
system or manager may choose one safe action. If doing nothing is allowed, it must
be declared explicitly as a safe action or self-loop.

Under the control-nonblocking condition, the J3 carrier computed over
\(A_u\cup A_c\) is contained in the corresponding J6 carrier. The inclusion can be
strict. This is not a dominance claim: J3 and J6 certify different scientific
contracts.

## 4. Repairing a failed carrier contract

### J4 — exact minimum declared relaxation

If the selected J3-style carrier gate is empty or coverage-incomplete, J4 uses an
explicit repair language:

1. admit one incompatible candidate world;
2. disable one originally legal transition; or
3. waive one coverage obligation.

For every nonempty retained subset \(S\subseteq W\), let

\[
\begin{aligned}
A(S)&=S\setminus W_0,\\
E(S)&=\{(w,a):w\in S,\tau_a(w)\downarrow,
\tau_a(w)\notin S\},\\
D(S)&=\{(k,\ell):\ell\in R_k,\ell\notin p_k(S)\}.
\end{aligned}
\]

The forced repair cost is

\[
R(S)=
\sum_{w\in A(S)}c_w+
\sum_{(w,a)\in E(S)}d_{w,a}+
\sum_{(k,\ell)\in D(S)}r_{k,\ell},
\]

and

\[
\boxed{R^*=\min_{\varnothing\neq S\subseteq W}R(S).}
\]

Every operation in the formula is necessary for that witness, and those operations
are sufficient. Costs are declared scientific or normative inputs. Tied optima are
reported rather than collapsed into a fictitious unique repair.

The current J4 theorem is attached to the universal J3 operation language. A
cost-aware controlled-J6 repair language would be a distinct extension and is not
silently assumed here.

## 5. One joint state on an admissible carrier

### J1 — unique coarsest four-audit state

On a declared finite common carrier \(U\), let

\[
C_\Gamma,C_\mathcal H,C_\Theta,C_{D,T}:\Pi(U)\to\Pi(U)
\]

be monotone, inflationary, idempotent audit closures, and let \(B\) be the baseline
partition. Their join closure gives

\[
\boxed{
J=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B).
}
\]

`J` is the unique coarsest partition satisfying all four representational
obligations. Pairwise audit commutation is unnecessary; fair finite iteration
converges to the same fixed point. One pass through four separately computed minima
can be insufficient.

Let \(E_D\) be the reliability-qualified evidence partition. Then

\[
\boxed{
\text{full deterministic joint-state report exists}
\iff J\preceq E_D.
}
\]

When this fails, the sharp state report is the set of `J` blocks intersecting the
evidence class. A target can still be deterministic when it is constant on each
evidence class, even if the full state is unresolved.

## 6. Comparing alternative common lifts and contracts

### J2 — faithful-lift equality

Let \(\pi:U\twoheadrightarrow V\) preserve baseline, evidence, target, audit labels,
action legality, and projected successors exactly. Then

\[
C_i^U(\pi^*P)=\pi^*C_i^V(P)
\]

for every audit, and

\[
\boxed{J_U=\pi^*J_V,\qquad U/J_U\cong V/J_V.}
\]

Scientifically invisible latent duplication cannot change the state or its
evidential licensing.

### J5 — one-sided lift bounds

When evidence and target remain exact pullbacks and shared action semantics commute,
J5 allows the audit obligations to differ.

If the source baseline/static distinctions are finer and it retains every target
action, possibly adding actions, then

\[
\boxed{\pi^*J_V\preceq J_U.}
\]

If the source baseline/static distinctions are coarser and its actions are subsets
of the target actions, then

\[
\boxed{J_U\preceq\pi^*J_V.}
\]

Added preserved obligations can only refine the required state; forgotten
obligations can only coarsen it. Satisfying both directions recovers J2 equality.
Target-only licensing is invariant under the exact evidence/target pullback. Full
state licensing is one-sided in the expected direction.

## 7. The proved dependency map

```text
declared ambient synchronization
  -> choose carrier semantics:
       J3: survive every legal action
       J6: survive every uncontrollable action + choose one safe control
  -> maximal carrier or finite typed no-go
  -> if using the declared J3 repair language and repair is needed:
       J4 exact least-cost weakening
  -> admissible carrier
  -> J1 unique coarsest four-audit state + evidence gate
  -> compare alternate lifts/contracts:
       J2 faithful equality
       J5 one-sided refinement bounds
```

These arrows are theorem dependencies, not a universal order for field research.

## 8. Ecological reading

For a state called **pollination maintained**:

- CCOC asks whether future colonization, reconnection, or intervention exposes a
  hidden distinction.
- MLTR asks whether the inherited meaning survives pollinator turnover.
- MRM asks whether retained mechanisms agree about restoration responses.
- CED asks whether field evidence has earned the needed distinction.
- J3 asks whether one synchronized description survives every declared action.
- J6 asks whether one synchronized description can survive unavoidable exterior
  moves under at least one declared management policy.
- J1 constructs the least joint distinction required by the four audits.
- J2/J5 determine whether another lift represents the same, a stronger, or a weaker
  scientific contract.

Contract-relativity is therefore constrained rather than arbitrary: scientists
declare the obligations and action roles, while the dynamics and evidence can
refute the merge, carrier, policy, or report.

## 9. Prior-art and ownership firewall

CREST does not claim novelty for:

- partition refinement, closure operators, and lattice fixed points;
- invariant, viability, and safety kernels;
- controllable-predecessor iteration and memoryless finite safety strategies;
- minimum-cost model repair and finite subset optimization;
- quotient naturality, simulation, or abstraction precision;
- adequacy-for-purpose, partial observability, and ecological transferability.

The program contribution is the theorem-grounded ecology-specific contract map and
its typed carrier, repair, partition, evidence, and comparison gates.

Repository ownership remains:

- CCOC — open-future interface obstruction;
- MLTR — inherited-law transport and semantic repair;
- MRM — mechanism-robust prediction;
- CED — evidential reportability and observation design;
- CREST synthesis in MRM — conditional cross-contract coupling.

## 10. What is not proved

- a nature-given unique synchronization or action-role assignment;
- that every companion model admits a coverage-complete J3 or J6 carrier;
- that J6 policies optimize ecological value;
- an exact J4 repair theorem for the controlled-action language;
- comparison for every arbitrary nonfaithful lift map;
- stochastic, partial-observation, delayed-control, approximate, or infinite forms;
- that the four axes are philosophically exhaustive; or
- empirical validity of the declared contracts.

## 11. Proof control and next questions

- [Synthesis proof ledger](crest_synthesis_proof_ledger_2026-08-17.md)
- [Companion proof recovery](crest_proof_recovery_2026-08-17.md)
- [Cross-repository validation](crest_final_validation_2026-08-17.md)

The next high-value questions are now narrower:

1. minimum repair of a failed controlled-J6 contract;
2. partial-observation and policy-memory requirements;
3. stochastic/adversarial disturbance kernels and risk-limited safety;
4. weakest simulation and approximate lift bounds; and
5. empirical inference of synchronizations, action roles, and evidence contracts.

A new theorem must change a coupled premise or failure boundary. Renaming another
refinement, viability, or repair result is not a CREST contribution.
