from __future__ import annotations

from mrm.crest_joint_state import (
    AuditRefinement,
    JointCRESTContract,
    apply_audits_once,
    partition_refines,
    solve_joint_crest_state,
)


def _partitions(size: int):
    if size <= 0:
        yield ()
        return

    def visit(prefix: list[int], maximum: int):
        if len(prefix) == size:
            yield tuple(prefix)
            return
        for value in range(maximum + 2):
            prefix.append(value)
            yield from visit(prefix, max(maximum, value))
            prefix.pop()

    yield from visit([0], 0)


def _cascade_contract(*, coarse_evidence: bool = False) -> JointCRESTContract:
    worlds = ("z", "a", "b", "c", "d", "r", "s")
    z, a, b, c, d, r, s = range(len(worlds))
    base = ("terminal", "live", "live", "live", "live", "live", "live")
    static = ("same",) * len(worlds)

    def transition(
        predecessor: tuple[int, int] | None,
    ) -> tuple[tuple[int, ...], ...]:
        successors = [r] * len(worlds)
        successors[z] = z
        successors[r] = r
        successors[s] = r
        if predecessor is not None:
            source, target = predecessor
            successors[source] = target
        return tuple((successor,) for successor in successors)

    audits = (
        AuditRefinement(
            "future", static, ("open",), transition((a, z))
        ),
        AuditRefinement(
            "semantic", static, ("carry",), transition((b, a))
        ),
        AuditRefinement(
            "mechanism", static, ("probe",), transition((c, b))
        ),
        AuditRefinement(
            "target", static, ("report",), transition((d, c))
        ),
    )
    evidence = (
        ("z", "a", "b", "c", "rest", "rest", "rest")
        if coarse_evidence
        else ("z", "a", "b", "c", "d", "tail", "tail")
    )
    targets = (
        "stop",
        "continue",
        "continue",
        "continue",
        "stop",
        "stop",
        "stop",
    )
    return JointCRESTContract(worlds, base, evidence, targets, audits)


def test_noncommuting_audits_have_one_order_independent_joint_state() -> None:
    contract = _cascade_contract()
    forward = solve_joint_crest_state(
        contract,
        audit_order=("future", "semantic", "mechanism", "target"),
    )
    reverse = solve_joint_crest_state(
        contract,
        audit_order=("target", "mechanism", "semantic", "future"),
    )

    assert forward.class_labels == reverse.class_labels
    assert forward.blocks == (
        ("z",),
        ("a",),
        ("b",),
        ("c",),
        ("d",),
        ("r", "s"),
    )
    assert forward.strict_passes == 1
    assert reverse.strict_passes == 4

    one_reverse_pass = apply_audits_once(
        contract,
        audit_order=("target", "mechanism", "semantic", "future"),
    )
    assert one_reverse_pass != reverse.class_labels

    base = tuple(
        0 if label == "terminal" else 1 for label in contract.base_labels
    )
    admissible = []
    for candidate in _partitions(len(contract.worlds)):
        if not partition_refines(candidate, base):
            continue
        if all(audit.is_fixed(candidate) for audit in contract.audits):
            admissible.append(candidate)

    assert len(admissible) == 2
    assert forward.class_labels in admissible
    assert all(
        partition_refines(candidate, forward.class_labels)
        for candidate in admissible
    )


def test_evidence_gate_separates_full_state_from_target_report() -> None:
    licensed = solve_joint_crest_state(_cascade_contract())
    assert licensed.full_state_licensed
    assert licensed.target_report_licensed
    assert all(len(values) == 1 for values in licensed.sharp_state_report)

    unresolved = solve_joint_crest_state(
        _cascade_contract(coarse_evidence=True)
    )
    assert not unresolved.full_state_licensed
    assert unresolved.target_report_licensed
    assert unresolved.sharp_state_report[-1] == (4, 5)
    assert unresolved.sharp_target_report[-1] == ("stop",)


def test_partial_action_rows_are_preserved() -> None:
    audit = AuditRefinement(
        "future",
        ("same", "same"),
        ("a",),
        ((None,), (0,)),
    )
    assert audit.close((0, 0)) == (0, 1)
