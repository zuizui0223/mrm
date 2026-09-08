# MRM publication center after the CREST joint-debt split

## Decision

MRM remains a standalone paper, but its center should **not** be moved from Theorem 8 to generic dynamic programming or cost minimization alone.

The reason is structural. CREST now owns an integration-only quantity,

\[
\Delta=D_{\mathrm{joint}}-\sum_iD_i,
\]

so MRM no longer needs to avoid publication merely because CREST contains state- or monitoring-burden results. At the same time, the current MRM headline—exactly \(m\) binary probes are necessary and sufficient to identify \(2^m\) canonical response signatures—sits close to CREST's supporting sequential response-capacity law. The correct separation is therefore by **question**, not by deleting the intervention frontier.

## MRM's independent question

MRM should ask:

> **When several retained mechanisms are compatible with the same visible ecological state, what can be predicted safely without identifying the mechanism, and what is the least active intervention burden required if mechanism resolution is actually demanded?**

This gives one coherent manuscript arc:

1. **Mechanism-safe prediction before identification.** If compatible mechanisms disagree on a requested future response, one deterministic report is not licensed. The minimal candidate-safe quotient preserves only mechanism distinctions that change the declared future response; otherwise typed or set-valued reporting is sufficient.
2. **Canonical identification frontier.** In the transparent \(m\)-bit family, exactly \(m\) binary probes are necessary and sufficient in the worst case to collapse \(2^m\) response signatures to one. This remains the sharp canonical lower/upper bound, but it is no longer sold as an isolated information-count headline.
3. **General adaptive discrimination.** For a finite declared response family outside the canonical construction, dynamic programming returns the shortest exact adaptive intervention tree when one exists.
4. **Cost-aware resolution.** With strictly positive declared action costs,
   \[
   V(q,S)=\min_a\left[c(a)+\max_xV(x,S_{a,q,x})\right]
   \]
   returns the exact minimum worst-case intervention cost, or no resolving plan. The important ecological distinction is that minimum intervention count and minimum experimental burden can disagree.

The scientific object is therefore **resolution choice under mechanism ambiguity**: one need not identify a latent mechanism merely because several mechanisms remain possible, but if a target requires identification, MRM characterizes the exact active burden of obtaining it.

## Why DP + cost alone is not the headline

Finite minimax dynamic programming over

\[
Q\times\{S:\varnothing\ne S\subseteq R\}
\]

with positive action costs is established algorithmic substrate. The cost layer is valuable because it makes MRM operational, not because the Bellman recursion is itself a new general theorem. The manuscript should therefore make the novelty firewall explicit:

- no generic novelty claim for finite dynamic programming;
- no generic novelty claim for decision-tree leaf counting or binary information bounds;
- no generic novelty claim for active diagnosis or experimental design;
- MRM's contribution is the coupling of candidate-safe ecological state/reporting with an exact finite intervention frontier for the declared mechanism-response family.

The existing cost-versus-length witness remains useful because it proves a concrete conceptual separation:

\[
\text{fewest interventions}
\neq
\text{least intervention cost}
\]

in general. It should appear after the mechanism-safe reporting problem has made clear *why* one is intervening to identify a mechanism at all.

## Boundary with CREST

The separation from CREST is now clean.

### CREST

CREST asks how much state resolution is required when multiple scientific responsibilities are imposed jointly on one common lift. Its flagship quantity is non-additive joint debt \(\Delta\). Its sequential \(H\log_2r\) law is supporting structural accounting for response capacity.

### MRM

MRM starts after a mechanism family \(R\) has been retained. It asks whether unresolved members of \(R\) can be safely merged for the requested response, and if not, how an adaptive intervention policy can resolve them exactly. Its object is not joint cross-audit debt but **active collapse of a compatible mechanism set**.

Thus the same phrase “bits/probes” has different ownership:

- CREST: how much state resolution a contract requires;
- MRM: how much active experimentation is required to identify a response type when identification is necessary.

This is a substantive distinction. CREST can require a finer state without prescribing a mechanism-identification experiment. MRM can choose not to identify a mechanism at all when the candidate-safe quotient already licenses the target.

## Recommended manuscript peak

Do not replace Theorem 8 with Result IX. Instead replace the current “Theorem 8 is the manuscript headline” wording with a two-part peak:

\[
\boxed{
\text{safe prediction without full mechanism identification}
\quad\longleftrightarrow\quad
\text{minimum active resolution when identification is required}
}
\]

Theorem 8 supplies the sharp canonical frontier inside the right-hand side. Result IX supplies the cost-aware general finite extension. The central ecological claim is the **choice between retaining ambiguity and paying to resolve it**, not the Bellman recursion itself.

## Submission consequence

MRM should remain separate from CREST. Its next manuscript revision should therefore:

- demote the isolated \(m\)-probe identity from title-level novelty;
- open with mechanism-safe / typed / set-valued prediction;
- present Theorem 8 as the canonical exact frontier showing what full resolution costs when demanded;
- immediately generalize to shortest and minimum-cost adaptive policies;
- retain posterior, noisy-observation, and one-step VOI material as downstream adapters;
- explicitly state that CREST owns cross-responsibility state-debt accounting and that MRM owns mechanism-resolution design.

This preserves the strongest MRM mathematics while removing the direct rhetorical collision with CREST's supporting response-depth result.
