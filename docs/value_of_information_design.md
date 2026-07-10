# Value-of-information design

## Finite setup

MRM's probabilistic observation layer gives posterior response-type ambiguity after
an action and observation. The design question is the forward version: before
choosing an action, how much posterior ambiguity is expected to remain?

For a prior \(\pi\) over retained response types, action \(a\), current known
macrostate \(q\), and declared observation likelihood \(L(x\mid q')\), the
predictive probability of observing \(x\) is

\[
P_a(x)=\sum_r \pi(r)L(x\mid G_a^r(q)).
\]

For every observed \(x\) with positive predictive probability, the posterior
\(\pi_{a,x}'\) is the Bayesian update from Result XI.

## Result XII — Expected ambiguity reduction

Let \(H(\pi)\) be posterior entropy in bits. The one-step expected posterior
entropy of action \(a\) is

\[
\mathbb{E}[H\mid a]=\sum_x P_a(x)H(\pi_{a,x}'),
\]

and the expected information gain is

\[
\mathrm{EIG}(a)=H(\pi)-\mathbb{E}[H\mid a].
\]

If actions have declared costs \(c(a)\), MRM can also report a simple net score

\[
\mathrm{Net}(a)=\mathrm{EIG}(a)-c(a)/\lambda,
\]

where \(\lambda>0\) is the declared cost-per-bit exchange rate. In dimensionless
finite witnesses, \(\lambda=1\) is used.

For a declared confidence threshold \(\tau\), the same one-step calculation reports

\[
P(\max_r\pi_{a,X}'(r)\ge \tau),
\]

which is the probability that action \(a\) will license a threshold-resolved
response-type report after one observation.

## Cost-versus-information witness

With four response types and a uniform prior, one action `perfect` reveals the
response type exactly, giving two expected bits of information. A second action
`half_split` reveals only one binary split, giving one expected bit. A third action
`uninformative` gives zero bits.

If all costs are zero, `perfect` is best by expected information gain. If `perfect`
has cost 3, `half_split` has cost 0.25, and one cost unit is worth one bit, then:

- `perfect`: \(2-3=-1\) net bits;
- `half_split`: \(1-0.25=0.75\) net bits;
- `uninformative`: \(0-0=0\) net bits.

The action with maximum raw information and the action with maximum net value are
therefore different.

## MRM interpretation

This layer does not yet optimize a full sequential experiment. It is a one-step
design diagnostic: given declared candidates, priors, likelihoods, and costs, it
scores the next possible actions by expected ambiguity reduction, net information
value, and probability of crossing a declared confidence threshold. If no threshold
is likely to be crossed, MRM should keep posterior ambiguity explicit instead of
pretending that the next action will automatically resolve the mechanism.

## Verification boundary

`rank_actions_by_value_of_information` computes one-step scores for every declared
action. Tests verify exact-probe ranking, cost-induced reversal between raw EIG and
net gain, noisy-observation loss of information, threshold-resolution probability,
and invalid action-cost or threshold rejection.

This extension does not solve multi-step dynamic programming, infer priors,
likelihoods, costs, or losses from data, choose experiments under hard budgets,
model stochastic mechanism transitions, or optimize expected utility beyond the
reported finite one-step scores.
