# Robust observation update

## Finite setup

Let a declared finite response-type family induce deterministic macro transitions
\(G_a^r:Q\to Q\). Exact MRM discrimination assumes that the observed successor
macrostate equals the true successor. This extension keeps the same deterministic
candidate family, but allows bounded observation error through a declared
set-valued observation support

\[
N(x)\subseteq Q,
\]

where \(N(x)\) is the nonempty set of true successor states compatible with the
observed macrostate \(x\). This is not a probability model; it is only a support
constraint.

## Result X — Conservative response-type update

Given current known macrostate \(q\), action \(a\), observed successor \(x\), and
prior response-type set \(S\), retain exactly

\[
S' = \{r\in S : G_a^r(q)\in N(x)\}.
\]

Response types outside \(S'\) are impossible under the declared observation-error
support. Response types inside \(S'\) remain possible and must not be discarded.
Thus:

- \(|S'|=1\) supports a mechanism-resolved typed report;
- \(|S'|>1\) requires retaining ambiguity or reporting the set-valued successor
  over \(S'\);
- \(|S'|=0\) is a contradiction between the observation, the retained candidates,
  and the declared error model.

The exact-observation case is recovered by \(N(x)=\{x\}\).

## Why this matters for MRM

Bounded observation error can turn an apparently identifying intervention into a
non-identifying one. If a direct probe predicts successors 0, 1, 2, and 3 for four
response types, an exact observation of 2 identifies type 2. But if the observed
state 2 is compatible with true states 1, 2, and 3, the honest update leaves three
response types. MRM should then keep a candidate-safe or set-valued report rather
than pretending that the noisy observation identified the mechanism.

## Verification boundary

`RobustObservationModel` validates nonempty observation neighborhoods over the
same finite macrostate space as the candidate family. `robust_observation_update`
implements the conservative support update above. Tests verify exact-observation
recovery, bounded-error retention, prior-subset updates, contradiction detection,
set-valued successor continuation, and invalid neighborhood rejection.

This extension still assumes deterministic candidate transitions and a known
current true macrostate before the one-step update. It does not yet propagate
uncertainty over the current state, estimate observation-error probabilities,
compute posterior probabilities, optimize risk, or handle stochastic mechanism
transitions.
