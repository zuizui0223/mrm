# CREST synthesis migration manifest — 2026-08-18

> **Decision:** the J/O synthesis program is a fifth logical unit and should move to
> a dedicated `zuizui0223/crest` repository. MRM is the temporary physical host, not
> the scientific owner.

## 1. External prerequisite

Create an empty public repository:

```text
zuizui0223/crest
```

The currently available GitHub connector can modify existing repositories but
cannot create a new one. This is the only external operation required before the
physical transfer can proceed.

## 2. Files owned by the CREST synthesis unit

### Theorem implementation

Move the seven current cross-contract modules from their compatibility paths:

```text
mrm/crest_common_lift.py
mrm/crest_common_lift_relaxation.py
mrm/crest_controlled_lift.py
mrm/crest_controlled_lift_relaxation.py
mrm/crest_joint_state.py
mrm/crest_lift_invariance.py
mrm/crest_lax_lift.py
```

Target package layout:

```text
crest/
  carrier.py
  carrier_repair.py
  controlled_carrier.py
  controlled_repair.py
  joint_state.py
  lift_invariance.py
  lift_bounds.py
```

Keep temporary `mrm.crest_*` import shims only if a demonstrated downstream consumer
requires them. They must be marked compatibility-only and must not expose CREST as
part of the MRM publication API.

### Tests

Move every `tests/test_crest_*.py` file, including:

- J1–J7 theorem tests;
- tied-repair and degenerate-order regressions;
- the weighted-set-cover complexity reductions; and
- O1 repair/evidence obstruction tests.

### Analytic proofs and control documents

Move:

- `docs/contract_relative_ecological_state_theory.md`;
- `docs/crest_joint_state_theorem_2026-08-17.md`;
- `docs/crest_lift_invariance_theorem_2026-08-17.md`;
- `docs/crest_maximal_common_lift_theorem_2026-08-17.md`;
- `docs/crest_minimum_common_lift_relaxation_theorem_2026-08-17.md`;
- `docs/crest_lax_lift_bounds_theorem_2026-08-18.md`;
- `docs/crest_controlled_common_lift_theorem_2026-08-18.md`;
- `docs/crest_minimum_controlled_lift_relaxation_theorem_2026-08-18.md`;
- `docs/crest_repair_complexity_boundary_2026-08-18.md`;
- `docs/crest_repair_evidence_noncommutation_2026-08-18.md`;
- `docs/crest_next_proof_novelty_gate_2026-08-18.md`;
- `docs/crest_synthesis_proof_ledger_2026-08-17.md`;
- `docs/crest_final_validation_2026-08-17.md`;
- `docs/crest_philosophy_claim_ledger_2026-08-17.md`; and
- the present migration manifest and unit charter.

### Philosophy manuscript and submission controls

Move the CREST philosophy manuscript, handoff, audit, verifier, and generated
submission-control artifact. These are CREST outputs rather than MRM companion-paper
outputs.

## 3. Files that remain in MRM

MRM retains only mechanism-robust macro-law assets:

- candidate-independent, typed, and set-valued laws;
- candidate-safe quotient;
- mechanism-ambiguity frontier;
- active/cost-aware discrimination;
- MRM-specific proofs, replay, tests, and manuscript planning; and
- observation adapters explicitly labelled as conditional interfaces to CED.

MRM should link to CREST as a companion program, not host its theorem inventory in
the publication-core section.

## 4. Migration sequence

1. Create `zuizui0223/crest`.
2. Copy the owned files at the current audited main SHA.
3. Establish an independent package, CI matrix, proof ledger, and README.
4. Run all J/O tests and submission controls in the new repository.
5. Replace MRM files with compatibility shims or links only where needed.
6. Run MRM core tests to prove the mechanism package is independent.
7. Merge the removal PR only after both repositories are green.
8. Record source SHAs and file checksums in both repositories.

No theorem development should occur during migration.

## 5. Current freeze

Until the dedicated repository exists:

- J1–J7 and O1 are frozen except for proof/complexity correction;
- no J8 or new O-family may be opened;
- new cross-contract ideas are recorded in an issue, not implemented under `mrm/`;
- MRM development remains limited to its mechanism-robustness axis.

## 6. Success criterion

The split is complete when:

```text
MRM main imports and tests no CREST theorem implementation
AND
CREST main independently reproduces J1–J7, O1, proof ledgers, and manuscript checks.
```

Git history remains the provenance source; files are not deleted until the dedicated
unit has a verified copy.
