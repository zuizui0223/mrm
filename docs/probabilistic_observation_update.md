# Probabilistic observation update

## Finite setup

Let a declared finite response-type family induce deterministic macro transitions
\(G_a^r:Q\to Q\). A probabilistic observation model declares likelihoods

\[
L(x\mid q)=P(\text{observed }x\mid \text{true successor }q),
\]

with one normalized likelihood row for every true macrostate. A prior distribution
\(\pi(r)\) over retained response types is also declared. These are explicit inputs;
MRM does not infer them from data in this layer.

## Result XI — Posterior response-type update

Given current known macrostate \(q\), action \(a\), observed successor \(x\), and
prior \(\pi\) over response types \(S\), the posterior is

\[
\pi'(r)=
\frac{\pi(r)L(x\mid G_a^r(q))}
{\sum_{s\in S}\pi(s)L(x\mid G_a^s(q))}.
\]

If the denominator is zero, the observation has zero probability under the retained
family and declared likelihood model, so the update returns a contradiction rather
than a posterior.

The posterior supports several MRM-safe summaries:

- maximum-a-posteriori response type or ties;
- posterior entropy in bits;
- a minimal descending-probability credible set for a declared mass;
- a confidence-threshold check for whether a mechanism-resolved report is licensed;
- set-valued successor continuation over response types with positive posterior
  mass when no threshold has been met.

Exact observation is recovered by identity likelihoods. The bounded-support robust
update is recovered at the support level by retaining response types with positive
likelihood, but the probabilistic layer additionally ranks and quantifies them.

## Why this matters for MRM

A noisy observation can strongly favor one response type without justifying a
mechanism-resolved deterministic report. For example, with a uniform prior and
observed state 1, likelihoods can yield a MAP response type with posterior about
0.52. That may pass a 0.50 threshold but fail a 0.90 threshold. MRM therefore keeps
posterior ambiguity explicit instead of silently converting the MAP candidate into a
certain macro-law.

## Verification boundary

`ProbabilisticObservationModel` validates finite normalized likelihood rows.
`posterior_observation_update` implements the one-step Bayesian update above.
Tests verify exact-observation recovery, noisy posterior ambiguity, prior-sensitive
posteriors, zero-evidence contradiction, credible-set construction, threshold
validation, and positive-posterior set-valued continuation.

This extension still assumes deterministic candidate transitions and a known current
true macrostate before the update. It does not infer priors or likelihoods from data,
propagate hidden current-state uncertainty, optimize expected utility or risk, choose
experiments by value of information, or handle stochastic mechanism transitions.
