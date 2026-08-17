# CREST-J6 — maximal controlled common-lift viability

> **Status:** conditional finite synthesis theorem with analytic proof and exhaustive
> finite witnesses. Greatest controlled-invariant kernels, finite safety games, and
> memoryless safety selectors are established viability/game-theoretic substrate.
> CREST-J6 does not claim a new generic safety-game algorithm. It refines the J3
> common-carrier gate by distinguishing unavoidable exterior transitions from
> selectable ecological or management actions, and by returning typed finite no-go
> certificates when no safe synchronized carrier exists.

## 1. Question left by CREST-J3

CREST-J3 requires every declared legal transition of every retained joint world to
remain inside the common carrier. That is appropriate when every transition is an
unavoidable possibility that the state representation must survive.

Some ecological actions, however, are selectable:

- a manager may choose one restoration intervention rather than all interventions;
- an organism may choose one available behavioral response;
- a sampling or management policy may avoid a known unsafe action;
- an exterior disturbance may remain unavoidable even while management actions are
  selectable.

Treating selectable actions as if all must remain safe can remove worlds that admit
one valid policy. CREST-J6 therefore separates:

- **uncontrollable actions**, every legal successor of which must remain safe; and
- **controllable actions**, at least one legal successor of which must remain safe.

The theorem remains a safety/viability result. It does not optimize rewards or infer
which actions are controllable in an observed ecosystem.

## 2. Finite controlled synchronization contract

Let `W` be a finite ambient set of candidate joint worlds and let

\[
W_0\subseteq W
\]

be the statically compatible worlds. Let

\[
A_u
\quad\text{and}\quad
A_c
\]

be disjoint finite sets of uncontrollable and controllable actions. For each action,
let

\[
\tau_a:W\rightharpoonup W
\]

be a partial deterministic successor map. An undefined successor means that the
action is illegal at that world.

A nonempty subset \(S\subseteq W\) is **robustly controlled invariant** when, for
every \(w\in S\):

1. \(w\in W_0\);
2. every legal uncontrollable successor remains in \(S\):
   \[
   a\in A_u,\ \tau_a(w)\downarrow
   \Longrightarrow
   \tau_a(w)\in S;
   \]
3. at least one legal controllable action remains in \(S\):
   \[
   \exists a\in A_c:\ \tau_a(w)\downarrow
   \text{ and }\tau_a(w)\in S.
   \]

The third condition is deliberately nonblocking. If an application permits doing
nothing, waiting, or terminating safely, that option must be represented explicitly
as a controllable self-loop or terminal action.

As in J3, each component \(k\) has a projection

\[
p_k:W\to L_k
\]

and a set of required labels \(R_k\subseteq L_k\). A controlled common lift is
**coverage complete** when every required label occurs in the retained carrier.

## 3. Controlled predecessor operator

For \(S\subseteq W\), define

\[
\boxed{
\begin{aligned}
G(S)=\{w\in S\cap W_0:\;&
\forall a\in A_u,
\ \tau_a(w)\downarrow\Rightarrow\tau_a(w)\in S,\\
&\exists a\in A_c,
\ \tau_a(w)\downarrow\text{ and }\tau_a(w)\in S\}.
\end{aligned}}
\]

The operator is monotone: if \(S\subseteq T\), every uncontrollable successor that
lies in \(S\) lies in \(T\), and every safe controllable successor in \(S\) is also
safe in \(T\). It is also contracting on its argument because \(G(S)\subseteq S\).

Starting from

\[
S_0=W_0,
\qquad
S_{n+1}=G(S_n),
\]

gives a descending finite sequence.

## 4. Theorem 1 — greatest controlled common carrier

### Statement

The descending sequence stabilizes after at most \(|W_0|\) strict rounds at a
unique greatest robustly controlled-invariant subset

\[
K^*=\bigcap_{n\ge 0}S_n.
\]

Consequently:

\[
\boxed{
\text{a nonempty robustly controlled common lift exists}
\iff
K^*\neq\varnothing,
}
\]

and

\[
\boxed{
\text{a coverage-complete robustly controlled common lift exists}
\iff
K^*\text{ represents every required component label}.}
\]

### Proof

Finiteness makes the descending chain stabilize at some \(S_N\). At stabilization,

\[
S_N=G(S_N),
\]

so every retained world is statically compatible, survives all legal
uncontrollable actions, and has at least one legal controllable successor in
\(S_N\). Hence \(S_N\) is robustly controlled invariant.

Now let \(C\subseteq W\) be any robustly controlled-invariant subset. Since
\(C\subseteq W_0=S_0\), suppose inductively that \(C\subseteq S_n\). Every world of
\(C\) has all legal uncontrollable successors in \(C\subseteq S_n\) and at least one
legal controllable successor in \(C\subseteq S_n\). Therefore

\[
C\subseteq G(S_n)=S_{n+1}.
\]

By induction, \(C\subseteq S_n\) for all \(n\), and hence \(C\subseteq K^*\). Thus
\(K^*\) is the unique greatest robustly controlled-invariant subset.

The nonempty existence criterion follows immediately. For coverage, if a smaller
controlled-invariant lift represents every required label, it lies inside \(K^*\),
so \(K^*\) represents them as well. Conversely, if \(K^*\) represents them, it is
itself a coverage-complete witness. ∎

## 5. Theorem 2 — memoryless safe selector

### Statement

If \(K^*\neq\varnothing\), there exists a deterministic memoryless selector

\[
\mu:K^*\to A_c
\]

such that

\[
\tau_{\mu(w)}(w)\in K^*
\]

for every \(w\in K^*\). Under arbitrary legal uncontrollable transitions and every
application of \(\mu\), trajectories starting in \(K^*\) remain in \(K^*\).

### Proof

Because \(K^*=G(K^*)\), each \(w\in K^*\) has at least one legal controllable
successor in \(K^*\). Choose one such action independently for each finite world.
The uncontrollable condition in the fixed-point definition keeps every legal
uncontrollable successor in \(K^*\), and the selected controllable action also stays
inside. Induction over any finite interleaving proves safety. ∎

The selector need not be unique. The executable implementation returns the first
safe action in the declared action order as a canonical witness, not as a theorem
that this action is ecologically optimal.

## 6. Theorem 3 — finite typed no-go certificates

Simultaneous pruning assigns a removal round to every eliminated world.

- **Static leaf:** \(w\notin W_0\), removed at round zero.
- **Uncontrollable escape:** at round \(r>0\), one legal uncontrollable action leads
  to a world removed at a lower round.
- **No safe control:** at round \(r>0\), every legal controllable successor was
  removed at a lower round; if no controllable action is legal, this is a finite
  leaf.

### Statement

Every world outside \(K^*\) admits a finite rank-decreasing AND/OR certificate:

- an uncontrollable-escape node has one existential witness edge showing that the
  environment can force exit;
- a no-safe-control node branches over all legal controllable actions, showing that
  every available choice reaches an already losing world; and
- leaves are static incompatibility or absence of any legal control.

The certificate depth is at most the number of pruning rounds.

### Proof

A world removed at round \(r>0\) fails one of the two dynamic conditions relative to
\(S_{r-1}\). An uncontrollable witness successor lies outside \(S_{r-1}\), hence was
removed at a strictly lower round. In the control-failure case, every legal control
successor lies outside \(S_{r-1}\), so each child has lower rank; if there are no
legal controls, no child is required. Recursive expansion terminates because the
rank strictly decreases along every edge and reaches round zero or a no-control
leaf. ∎

For a missing coverage label, attaching such a certificate to every compatible
ambient world carrying that label gives a finite coverage no-go explanation.

## 7. Relation to CREST-J3

J3 treats all declared actions universally: every legal action successor must stay
inside the retained carrier. J6 treats only uncontrollable actions universally and
requires one safe controllable action.

If every compatible world has at least one legal controllable action, and J3 is run
on the union \(A_u\cup A_c\) with the same transitions, then every J3-invariant
subset is J6-controlled invariant. Therefore

\[
\boxed{
U^*_{\mathrm{J3}}\subseteq K^*_{\mathrm{J6}}.
}
\]

The inclusion can be strict because J3 rejects a world with one unsafe selectable
action even when another selectable action is safe.

This comparison does not say J6 is universally preferable. It answers a different
scientific contract: J3 certifies safety under **all** declared actions, whereas J6
certifies the existence of a safe control policy against **all uncontrollable**
actions.

## 8. Strict five-world witness

Let

\[
W=\{\mathsf{safe},\mathsf{choice},\mathsf{hazard},
      \mathsf{trapped},\mathsf{bad}\},
\]

with `bad` statically incompatible. Let `weather` be uncontrollable and let
`protect`, `exploit` be controllable.

Uncontrollable transitions are:

\[
\begin{array}{c|ccccc}
 &\mathsf{safe}&\mathsf{choice}&\mathsf{hazard}&\mathsf{trapped}&\mathsf{bad}\\
\hline
\mathsf{weather}
 &\mathsf{safe}&\mathsf{choice}&\mathsf{bad}&\mathsf{trapped}&\mathsf{bad}.
\end{array}
\]

Controllable transitions are:

\[
\begin{array}{c|cc}
 &\mathsf{protect}&\mathsf{exploit}\\
\hline
\mathsf{safe}&\mathsf{safe}&\mathsf{safe}\\
\mathsf{choice}&\mathsf{safe}&\mathsf{bad}\\
\mathsf{hazard}&\mathsf{hazard}&\mathsf{hazard}\\
\mathsf{trapped}&\mathsf{hazard}&\mathsf{bad}\\
\mathsf{bad}&\mathsf{bad}&\mathsf{bad}.
\end{array}
\]

Round zero removes `bad`. Round one removes `hazard` because `weather` reaches
`bad`. Round two removes `trapped` because both selectable actions reach losing
worlds. The controlled kernel is

\[
\boxed{
K^*=\{\mathsf{safe},\mathsf{choice}\},
}
\]

with the memoryless policy `protect` at both worlds.

If J3 instead treats `weather`, `protect`, and `exploit` all universally, it removes
`choice` because `exploit` reaches `bad`, leaving only

\[
U^*_{\mathrm{J3}}=\{\mathsf{safe}\}.
\]

Thus the inclusion is strict. Exhaustive enumeration of all subsets verifies that
every robustly controlled-invariant subset lies inside \(K^*\).

## 9. Executable verification

Files:

- `mrm/crest_controlled_lift.py`
- `tests/test_crest_controlled_lift.py`

The tests verify:

1. the two-world controlled kernel and canonical memoryless policy;
2. greatestness by exhaustive enumeration of all ambient subsets;
3. strict enlargement over the corresponding J3 universal kernel;
4. rank-decreasing uncontrollable and control-failure certificates;
5. coverage no-go certificates;
6. the no-legal-control leaf; and
7. validation of action-role disjointness and transition tables.

## 10. Prior-art classification

The generic mathematics is established:

- viability and discriminating kernels compute maximal subsets from which state
  constraints can be maintained under controls and disturbances;
- finite safety games admit fixed-point characterizations and memoryless winning
  strategies; and
- backward controllable-predecessor iteration is standard verification/control
  substrate.

CREST-J6 does not claim those generic results. Its narrower program contribution is:

> the controlled variant of the CREST cross-component carrier gate, preserving the
> distinction between unavoidable exterior futures and selectable ecological
> actions, together with component-coverage checks and typed finite no-go
> certificates that route failure before J1 joint-state construction.

## 11. Boundaries

CREST-J6 does not prove:

- that an ecological action is correctly classified as controllable or
  uncontrollable;
- optimality for cost, reward, resilience, or information gain;
- stochastic disturbances or probabilistic safety;
- partial observation, delayed control, or policy memory requirements;
- that one safe policy preserves every normative ecological target;
- an infinite or continuous-state viability theorem; or
- empirical validity of the declared synchronization.

The safe theorem-level statement is:

\[
\boxed{
\text{a finite synchronized ecological carrier is controllably viable exactly when}
\text{the J6 greatest kernel is nonempty; coverage and failure remain finitely}
\text{certifiable, and one memoryless safe selector then exists.}
}
