# MRM contribution map for the combined evidence-and-prediction paper

## Combined paper role

MRM supplies the reporting and future-action layer of the proposed combined CED–MRM manuscript. CED asks which latent ecological worlds a finite experiment can separate under observation error. MRM asks whether the ecological report target is constant across the worlds that remain compatible.

The combined paper should not reproduce the full MRM theorem inventory. It should import only the results needed to turn an experiment-induced quotient into an honest ecological prediction.

## Headline MRM contributions retained

### 1. Universal / typed / set-valued report criterion

A candidate-independent deterministic law is justified only when all retained response types agree on every declared future action. Under disagreement, the report must retain response type or remain set-valued.

In the combined notation, this becomes the target-constancy criterion on each experiment-record class.

### 2. Minimal candidate-safe quotient

The coarsest observation-preserving deterministic quotient of observable state × response type retains exactly the distinctions that declared future actions can expose.

In the combined paper, this is the future-action-stable refinement of the experiment-induced quotient. This is the main MRM minimality result and should remain theorem-level.

### 3. Active discrimination

The shortest and minimum-cost adaptive intervention trees refine the remaining response-type class until the report target becomes deterministic, or certify that the declared grammar cannot do so.

In the combined paper, the objective should be stated as target resolution, not necessarily full mechanism identification.

### 4. Mechanism-ambiguity frontier

The canonical binary family shows how unresolved response dimensions increase the size of the exact candidate-safe representation and the number of interventions needed for identification.

This remains the quantitative witness for why unresolved mechanism ambiguity matters, but it should appear after the joint presence × mechanism example rather than as a separate paper opening.

## Results demoted to methods or supplement

- joint exterior-mechanism product lower bound;
- bounded-support observation update;
- Bayesian posterior update;
- credible sets and MAP diagnostics;
- one-step value-of-information scores;
- detailed dynamic-programming implementation;
- all secondary witness tables.

These results remain useful. They are not equal headline contributions in the combined paper.

## Joint witness interpretation

The CED bridge witness uses latent worlds `(presence, response_type)`.

- Passive records leave all worlds together.
- Detection separates absence from presence.
- Detection alone cannot determine the management response among present worlds.
- A response intervention separates present response types.
- Response type remains irrelevant in absent worlds because the report target is identical there.

This recovers the central MRM principle in a target-aware form: the goal is not to retain every mechanism label, but only distinctions that change the report under declared future actions.

## Required MRM-side analysis before submission

1. Express `minimal_candidate_safe_quotient` in the neutral latent-world notation used by the combined paper.
2. Prove that the fixed point is the coarsest refinement preserving current observation and deterministic future target transitions.
3. Recast shortest and minimum-cost discrimination as target-resolution policies rather than full type-identification policies.
4. Build one small cost-aware policy for the joint plant–pollinator example:
   - additional detection effort;
   - response-typing intervention;
   - stop and report set-valued prediction.
5. Compare the policy selected under perfect observation with the policy selected under a CED false-alert or common-mode risk constraint.

## Story discipline

The MRM section should answer one question:

> Given the latent class left by the experiment, what ecological prediction can be reported honestly, and which intervention is worth taking next?

It should not become a separate tutorial on Bayesian model selection or value of information.

## Submission decision

The combined manuscript is supportable if:

- the experiment-induced quotient and minimal candidate-safe quotient use one notation;
- the joint witness requires both presence and mechanism dimensions;
- active discrimination is expressed as refinement of target-compatible classes;
- observation-error results enter as reliability of that refinement; and
- one ecological example supports the entire narrative.

Otherwise MRM should remain a later standalone mechanism-reporting paper.
