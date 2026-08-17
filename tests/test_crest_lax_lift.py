from __future__ import annotations

import pytest

from mrm.crest_joint_state import AuditRefinement, JointCRESTContract
from mrm.crest_lax_lift import (
    OneSidedContractProjection,
    solve_one_sided_lift_comparison,
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


def _empty_rows(size: int) -> tuple[tuple[int, ...], ...]:
    return tuple(() for _ in range(size))


def _contract(
    worlds,
    base,
    evidence,
    targets,
    *,
    future_actions=(),
    future_successors=None,
    mechanism_static=None,
) -> JointCRESTContract:
    size = len(worlds)
    same = ("same",) * size
    if future_successors is None:
        future_successors = _empty_rows(size)
    if mechanism_static is None:
        mechanism_static = same
    audits = (
        AuditRefinement(
            "future",
            same,
            tuple(future_actions),
            tuple(tuple(row) for row in future_successors),
        ),
        AuditRefinement("semantic", same, (), _empty_rows(size)),
        AuditRefinement("mechanism", tuple(mechanism_static), (), _empty_rows(size)),
        AuditRefinement("target", same, (), _empty_rows(size)),
    )
    return JointCRESTContract(
        tuple(worlds), tuple(base), tuple(evidence), tuple(targets), audits
    )


def _reduced_contract(*, coarse_evidence: bool = False) -> JointCRESTContract:
    evidence = (
        ("terminal", "live", "live")
        if coarse_evidence
        else ("z", "a", "r")
    )
    return _contract(
        ("z", "a", "r"),
        ("terminal", "live", "live"),
        evidence,
        ("stop", "continue", "continue"),
        future_actions=("open",),
        future_successors=((0,), (0,), (2,)),
    )


def _strong_duplicate_contract() -> JointCRESTContract:
    return _contract(
        ("z", "a", "r0", "r1"),
        ("terminal", "live", "live", "live"),
        ("z", "a", "r", "r"),
        ("stop", "continue", "continue", "continue"),
        future_actions=("open",),
        future_successors=((0,), (0,), (2,), (3,)),
        mechanism_static=("same", "same", "m0", "m1"),
    )


def _faithful_duplicate_contract() -> JointCRESTContract:
    return _contract(
        ("z", "a", "r0", "r1"),
        ("terminal", "live", "live", "live"),
        ("z", "a", "r", "r"),
        ("stop", "continue", "continue", "continue"),
        future_actions=("open",),
        future_successors=((0,), (0,), (2,), (3,)),
    )


def _weak_contract() -> JointCRESTContract:
    return _contract(
        ("z", "a", "r"),
        ("terminal", "live", "live"),
        ("terminal", "live", "live"),
        ("stop", "continue", "continue"),
    )


def test_stronger_source_can_only_refine_the_pulled_target_state() -> None:
    projection = OneSidedContractProjection(
        source=_strong_duplicate_contract(),
        target=_reduced_contract(),
        source_to_target=(0, 1, 2, 2),
        direction="source_stronger",
    )

    for audit in projection.target.audits:
        for partition in _partitions(len(projection.target.worlds)):
            assert projection.audit_closure_bound(audit.name, partition)

    comparison = solve_one_sided_lift_comparison(projection)
    assert comparison.source_state.blocks == (
        ("z",),
        ("a",),
        ("r0",),
        ("r1",),
    )
    assert comparison.target_state.blocks == (("z",), ("a",), ("r",))
    assert comparison.strict
    assert comparison.state_count_bound_holds
    assert comparison.source_state.state_count == 4
    assert comparison.target_state.state_count == 3
    assert comparison.source_state.full_state_licensed is False
    assert comparison.target_state.full_state_licensed is True
    assert comparison.full_state_licensing_implication == (
        "source_implies_target",
        True,
    )
    assert comparison.target_licensing_preserved


def test_weaker_source_can_only_coarsen_the_pulled_target_state() -> None:
    projection = OneSidedContractProjection(
        source=_weak_contract(),
        target=_reduced_contract(coarse_evidence=True),
        source_to_target=(0, 1, 2),
        direction="source_weaker",
    )

    for audit in projection.target.audits:
        for partition in _partitions(len(projection.target.worlds)):
            assert projection.audit_closure_bound(audit.name, partition)

    comparison = solve_one_sided_lift_comparison(projection)
    assert comparison.source_state.blocks == (("z",), ("a", "r"))
    assert comparison.target_state.blocks == (("z",), ("a",), ("r",))
    assert comparison.strict
    assert comparison.state_count_bound_holds
    assert comparison.source_state.state_count == 2
    assert comparison.target_state.state_count == 3
    assert comparison.source_state.full_state_licensed is True
    assert comparison.target_state.full_state_licensed is False
    assert comparison.full_state_licensing_implication == (
        "target_implies_source",
        True,
    )
    assert comparison.target_licensing_preserved


def test_faithful_projection_is_the_equality_case_of_both_bounds() -> None:
    source = _faithful_duplicate_contract()
    target = _reduced_contract()
    for direction in ("source_stronger", "source_weaker"):
        projection = OneSidedContractProjection(
            source=source,
            target=target,
            source_to_target=(0, 1, 2, 2),
            direction=direction,
        )
        comparison = solve_one_sided_lift_comparison(projection)
        assert comparison.equality
        assert comparison.source_state.blocks == (
            ("z",),
            ("a",),
            ("r0", "r1"),
        )
        assert comparison.source_state.state_count == comparison.target_state.state_count
        assert comparison.source_state.full_state_licensed
        assert comparison.target_state.full_state_licensed


def test_shared_action_semantics_must_commute() -> None:
    broken = _contract(
        ("z", "a", "r0", "r1"),
        ("terminal", "live", "live", "live"),
        ("z", "a", "r", "r"),
        ("stop", "continue", "continue", "continue"),
        future_actions=("open",),
        future_successors=((0,), (0,), (2,), (1,)),
        mechanism_static=("same", "same", "m0", "m1"),
    )
    with pytest.raises(ValueError, match="successors do not commute"):
        OneSidedContractProjection(
            source=broken,
            target=_reduced_contract(),
            source_to_target=(0, 1, 2, 2),
            direction="source_stronger",
        )


def test_direction_rejects_action_inclusion_reversal() -> None:
    with pytest.raises(ValueError, match="stronger source must retain every target action"):
        OneSidedContractProjection(
            source=_weak_contract(),
            target=_reduced_contract(coarse_evidence=True),
            source_to_target=(0, 1, 2),
            direction="source_stronger",
        )

    extra_action_source = _contract(
        ("z", "a", "r"),
        ("terminal", "live", "live"),
        ("z", "a", "r"),
        ("stop", "continue", "continue"),
        future_actions=("open", "extra"),
        future_successors=((0, 0), (0, 1), (2, 2)),
    )
    with pytest.raises(ValueError, match="weaker source may not add"):
        OneSidedContractProjection(
            source=extra_action_source,
            target=_reduced_contract(),
            source_to_target=(0, 1, 2),
            direction="source_weaker",
        )


def test_evidence_change_is_not_silently_attributed_to_audit_strength() -> None:
    split_evidence_source = _contract(
        ("z", "a", "r0", "r1"),
        ("terminal", "live", "live", "live"),
        ("z", "a", "r0", "r1"),
        ("stop", "continue", "continue", "continue"),
        future_actions=("open",),
        future_successors=((0,), (0,), (2,), (3,)),
        mechanism_static=("same", "same", "m0", "m1"),
    )
    with pytest.raises(ValueError, match="evidence partition must be an exact target pullback"):
        OneSidedContractProjection(
            source=split_evidence_source,
            target=_reduced_contract(),
            source_to_target=(0, 1, 2, 2),
            direction="source_stronger",
        )
