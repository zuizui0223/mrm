# Contract-Relative Ecological State Theory (CREST)

> **Status:** program-level synthesis / working upper concept. This document does not
> introduce a new theorem, does not merge the companion repositories, and does not
> claim novelty for the phrase or for quotient/refinement machinery.

## 1. Central principle

The shared research program can be stated as one ecological principle:

> **An ecological state is not determined by the present visible configuration
> alone. State identity is relative to the future operations that may become
> relevant, the meanings inherited across structural change, the mechanisms still
> retained as possible, and the evidence contract under which distinctions may be
> reported.**

A compact working form is

\[
\boxed{\text{ecological state identity is contract-relative, not intrinsic}.}
\]

CREST therefore treats an ecological state representation as indexed by a declared
contract rather than as an unconditional label attached to a configuration.

Write a program-level contract schematically as

\[
\mathcal C=(\Gamma,\mathcal H,\Theta,D;T),
\]

where

- \(\Gamma\) is the declared future-action / composition grammar;
- \(\mathcal H\) is the inherited-semantics contract, including any accepted
  source law and source--target relation;
- \(\Theta\) is the retained mechanism or response-type family;
- \(D\) is the experiment / observation / detection contract; and
- \(T\) is the ecological report or decision target.

The tuple is a synthesis notation, not a claim that all four repositories already
share one state space or one equivalence relation.

## 2. Four adequacy audits

A proposed ecological state variable is **operationally admissible under
\(\mathcal C\)** only to the extent that four logically distinct questions have
been answered.

### A. Future sufficiency — CCOC

**Question:** What distinctions can become necessary when the legal future is
opened?

CCOC holds the finite system and declared grammar family fixed and asks how the
minimum exact response interface changes when independently available closed
futures are replaced by a jointly open future grammar.

Its characteristic failure is

\[
\boxed{\text{future insufficiency}.}
\]

A state representation can be exact in every supplied closed context yet fail to
be comparably small for the open grammar. The missing information is not created by
observation error or mechanism uncertainty; it is forced by distinctions that
future legal operations can expose.

Program-level ecological reading:

> Current functional equivalence need not imply causal equivalence under future
> colonization, reconnection, dispersal, rewiring, or newly legal intervention.

### B. Semantic coherence — MLTR

**Question:** Which distinctions must be added so that an inherited ecological law
keeps its meaning after structural change?

MLTR fixes one accepted source macro-law, carries its labels through a declared
source--target relation, and tests whether the inherited partition remains exact.
If not, it returns the unique coarsest exact target refinement constrained to
preserve inherited semantics.

Its characteristic failure is

\[
\boxed{\text{semantic non-portability}.}
\]

Program-level ecological reading:

> A guild label, resilience class, occupancy class, or functional state that was
> meaningful before turnover or rewiring is not automatically meaningful after it.

### C. Mechanism robustness — MRM

**Question:** What may be predicted when several retained causal mechanisms agree
on the present state but disagree about future interventions?

MRM fixes a common observed macrostate space and a declared family of candidate
transition mechanisms. Raw candidate labels are collapsed to response types.
A candidate-independent deterministic law is licensed only where all retained
response types agree. Otherwise an honest state representation must retain the
response distinction where it matters, or the report must remain set-valued or
posterior-ambiguous.

Its characteristic failure is

\[
\boxed{\text{mechanism non-robustness}.}
\]

MRM's minimal candidate-safe quotient is therefore the **mechanism-relative state
layer** of CREST: it retains exactly the response-type distinctions that declared
future actions can expose while allowing locally irrelevant mechanism distinctions
to merge.

Program-level ecological reading:

> The same visible community state may not define one predictive state when
> retained mechanisms imply different management or disturbance responses.

### D. Evidential licensing — CED

**Question:** Which distinctions can finite and imperfect evidence justify
reporting?

CED partitions latent worlds by the records produced under a declared experiment
and observation contract. A deterministic report is licensed only when the target
is constant over the remaining compatible class; otherwise the honest output is
ambiguity-retaining, set-valued, or risk-limited.

Its characteristic failure is

\[
\boxed{\text{evidential non-resolvability}.}
\]

Program-level ecological reading:

> An ecologically real or predictively important distinction is not automatically
> a distinction that finite monitoring has resolved.

## 3. Why MRM is a genuine fourth axis

MRM is not reducible to the other three audits.

- It is not CCOC: CCOC varies the admissible future grammar / exterior
  addressability in a declared system, whereas MRM retains alternative transition
  laws on a common observed macrostate space.
- It is not MLTR: MLTR fixes one inherited source law and asks for its least
  semantics-preserving repair after a declared replacement. MRM instead asks what
  can be reported when several candidate response laws remain possible.
- It is not CED: CED asks what an experiment record resolves. MRM asks whether the
  worlds or response types that remain possible agree on future target behavior.

The four questions can interact without becoming the same theorem.

## 4. MRM integration map

The present MRM theorem program fits CREST as follows.

| MRM result | CREST role |
|---|---|
| universal deterministic criterion | mechanism-robustness gate |
| typed / set-valued report | honest fallback when mechanism robustness fails |
| candidate-safe product lower bound | memory cost of uniformly relevant response ambiguity |
| minimal candidate-safe quotient | minimal mechanism-relative state representation |
| mechanism-ambiguity frontier | sharp witness for retained mechanism memory |
| active / cost-aware discrimination | intervention route for resolving target-relevant mechanism ambiguity |
| bounded / probabilistic observation update | adapter from an evidence contract into the remaining response-type set |
| one-step VOI | optional design diagnostic after the mechanism-report target is fixed |
| joint exterior--mechanism lower bound | conditional CCOC--MRM bridge under joint operational separation |

This keeps the MRM publication identity narrow: **honest prediction under unresolved
mechanism ambiguity**. CREST is an upper concept, not a reason to promote every
cross-repository bridge into the MRM main theorem list.

## 5. CED--MRM boundary

MRM already contains bounded-support and probabilistic observation updates. Under
CREST these are interpreted as **adapters**, not as ownership of the full evidence
layer.

CED owns the broader question of finite reportability under intervention design,
imperfect detection, shared failure, calibration, and explicit risk contracts.
MRM may consume a CED-style compatible-world or posterior class and ask a different
question:

> Do the still-compatible response types agree on the requested future target?

Thus a legitimate cross-repository composition is

```text
CED: evidence contract -> compatible latent worlds / risk-limited class
MRM: retained worlds -> target agreement, mechanism-safe state, or set-valued report
```

This composition does not imply that CED and MRM should be one manuscript or that
one quotient subsumes the other.

## 6. CCOC--MRM boundary

Both CCOC and MRM can produce memory lower bounds, but the indexed uncertainty is
different.

- CCOC: exterior / future-composition distinctions become operationally
  addressable under a wider grammar.
- MRM: retained response mechanisms disagree under declared actions.

The existing joint exterior--mechanism result is a bridge only when the full
exterior-by-response-type product is jointly realizable and operationally
separable. The two lower bounds must not be added arithmetically without that joint
premise.

## 7. MLTR--MRM boundary

MLTR fixes one source semantics and one declared transport relation. MRM retains a
family of possible response laws. A future synthesis could admit uncertainty over
replacement relations or replacement mechanisms, but that would be a new joint
problem.

Do not silently reinterpret the current MRM candidate-safe quotient as an MLTR
repair theorem, and do not reinterpret MLTR transport defect as mechanism
ambiguity.

## 8. A four-layer ecological example

Consider a coarse state labelled **pollination maintained**.

1. **CCOC / future contract:** future colonization or a newly connected pollinator
   channel can expose response distinctions hidden by the current community.
2. **MLTR / inherited semantics:** after pollinator turnover, the old functional
   class may need to split into states with and without substitute-response
   capacity.
3. **MRM / retained mechanisms:** even within a repaired visible state, retained
   mechanisms may disagree about whether competitor removal, floral manipulation,
   or habitat restoration will recover pollination. A deterministic prediction is
   licensed only where those response types agree.
4. **CED / evidence contract:** camera, eDNA, visitation, or experimental records
   may still be unable to distinguish the target-relevant worlds because of finite
   sensitivity or shared failure. The report must not claim a mechanism-resolved
   state that the evidence has not licensed.

The same present configuration can therefore support different legitimate state
representations depending on which contracts are declared.

## 9. Program-level adequacy principle

CREST uses the following statement as a **research principle**, not yet as a proved
single theorem:

\[
\boxed{
\text{usable ecological state}
\Rightarrow
\begin{cases}
\text{future-sufficient},\\
\text{semantically coherent},\\
\text{mechanism-robust or ambiguity-explicit},\\
\text{evidentially licensed}.
\end{cases}}
\]

Equivalently:

> **Remember distinctions that can matter, preserve distinctions required by
> inherited meaning, retain mechanism distinctions that change prediction, and
> report only distinctions that the evidence can support.**

Passing one audit does not imply passing the others.

## 10. Why the repositories remain separate

CREST is an upper research architecture. It is **not** a repository-merger rule.
The theorem and provenance units remain separate:

- **CCOC:** open-future exact-interface obstruction and sharpness;
- **MLTR:** source-relative transport, minimal repair, defect, and history;
- **MRM:** mechanism-robust deterministic / typed / set-valued reporting and
  candidate-safe state;
- **CED:** finite evidence, imperfect detection, failure architecture, and
  risk-limited reportability.

Keeping the proofs separate prevents a shared vocabulary such as `quotient`,
`refinement`, `state`, or `uncertainty` from hiding different quantifier orders and
different mathematical objects.

## 11. Future synthesis questions

Only a result that genuinely couples two or more contracts should become a new
synthesis theorem. High-value questions include:

1. **Audit commutation.** Under what conditions does mechanism-robustification
   commute with structural transport or with evidence-induced quotienting?
2. **Joint admissible state.** Given a common latent representation, when is there a
   finite state interface that is simultaneously future-sufficient,
   inheritance-coherent, mechanism-robust, and evidentially resolvable?
3. **Failure localization.** Can one identify the minimum contract that must be
   strengthened when an ecological state fails the full adequacy audit?

Do not create a new theorem merely by intersecting existing partitions or adding
existing complexity bounds. A synthesis result must expose a new noncommutation,
minimality statement, or impossibility that is not already one companion theorem
under renamed variables.

## 12. Development rule

MRM remains responsible for the mechanism-relative layer. New MRM theorem work
should therefore change one of these questions:

- when mechanism ambiguity can be safely forgotten;
- what minimal mechanism-relative state must be retained;
- what honest report replaces unsupported determinism; or
- what intervention can resolve target-relevant mechanism ambiguity.

Questions whose central object is open-composition interface growth, inherited-law
repair, or finite-evidence certification should be routed to CCOC, MLTR, or CED
respectively.
