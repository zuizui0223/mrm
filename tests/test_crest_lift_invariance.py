from __future__ import annotations

import pytest

from mrm.crest_joint_state import (
    AuditRefinement,
    JointCRESTContract,
    solve_joint_crest_state,
)
from mrm.crest_lift_invariance import (
    FaithfulContractProjection,
    pullback_partition,
    solve_lift_invariant_joint_states,
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


def _trivial_audit(name: str, world_count: int) -> AuditRefinement:
    return AuditRefinement(
        name=name,
        static_labels=("same",) * world_count,
        actions=(),
        successors=tuple(() for _ in range(world_count)),
    )


def _target_contract(*, coarse_evidence: bool = False) -> JointCRESTContract:
    worlds = ("z", "a", "r")
    future = AuditRefinement(
        name="future",
        static_labels=("same", "same", "same"),
        actions=("open",),
        successors=((0,), (0,), (2,)),
    )
    evidence = (
        ("terminal", "live", "live")
        if coarse_evidence
        else ("z", "a", "r")
    )
    targets = (
        ("stop", "continue", "continue")
        if coarse_evidence
        else ("stop", "continue", "stop")
    )
    return JointCRESTContract(
        worlds=worlds,
        base_labels=("terminal", "live", "live"),
        evidence_labels=evidence,
        target_labels=targets,
        audits=(
            future,
            _trivial_audit("semantic", len(worlds)),
            _trivial_audit("mechanism", len(worlds)),
            _trivial_audit("target", len(worlds)),
        ),
    )


def _source_contract(
    *,
    duplicate: str = "r",
    visible_duplicate: bool = False,
    coarse_evidence: bool = False,
) -> tuple[JointCRESTContract, tuple[int, ...]]:
    if duplicate == "r":
        worlds = ("z", "a", "r0", "r1")
        projection = (0, 1, 2, 2)
        future_successors = ((0,), (0,), (2,), (2,))
        base = ("terminal", "live", "live", "live")
        evidence = (
            ("terminal", "live", "live", "live")
            if coarse_evidence
            else ("z", "a", "r", "r")
        )
        targets = (
            ("stop", "continue", "continue", "continue")
            if coarse_evidence
            else ("stop", "continue", "stop", "stop")
        )
        mechanism_static = (
            ("same", "same", "type-0", "type-1")
            if visible_duplicate
            else ("same",) * len(worlds)
        )
    elif duplicate == "a":
        worlds = ("z", "a0", "a1", "r")
        projection = (0, 1, 1, 2)
        future_successors = ((0,), (0,), (0,), (3,))
        base = ("terminal", "live", "live", "live")
        evidence = ("z", "a", "a", "r")
        targets = ("stop", "continue", "continue", "stop")
        mechanism_static = ("same",) * len(worlds)
    else:
        raise ValueError("unknown duplicate")

    future = AuditRefinement(
        name="future",
        static_labels=("same",) * len(worlds),
        actions=("open",),
        successors=future_successors,
    )
    mechanism = AuditRefinement(
        name="mechanism",
        static_labels=mechanism_static,
        actions=(),
        successors=tuple(() for _ in worlds),
    )
    contract = JointCRESTContract(
        worlds=worlds,
        base_labels=base,
        evidence_labels=evidence,
        target_labels=targets,
        audits=(
            future,
            _trivial_audit("semantic", len(worlds)),
            mechanism,
            _trivial_audit("target", len(worlds)),
        ),
    )
    return contract, projection


def test_every_audit_closure_commutes_with_faithful_pullback() -> None:
    target = _target_contract()
    source, world_projection = _source_contract()
    projection = FaithfulContractProjection(
        source=source,
        target=target,
        source_to_target=world_projection,
    )

    target_partitions = tuple(_partitions(len(target.worlds)))
    assert len(target_partitions) == 5
    for audit in target.audits:
        for partition in target_partitions:
            assert projection.audit_closure_commutes(audit.name, partition)


def test_redundant_latent_detail_preserves_the_joint_quotient() -> None:
    target = _target_contract()
    source, world_projection = _source_contract()
    projection = FaithfulContractProjection(
        source=source,
        target=target,
        source_to_target=world_projection,
    )
    result = solve_lift_invariant_joint_states(
        projection,
        audit_order=("target", "mechanism", "semantic", "future"),
    )

    assert result.target_state.blocks == (("z",), ("a",), ("r",))
    assert result.source_state.blocks == (("z",), ("a",), ("r0", "r1"))
    assert result.source_state.class_labels == pullback_partition(
        result.target_state.class_labels, world_projection
    )
    assert result.target_block_by_source_block == (0, 1, 2)
    assert result.quotient_isomorphic
    assert result.full_state_licensing_preserved
    assert result.target_licensing_preserved


def test_two_different_faithful_lifts_share_one_reduced_joint_state() -> None:
    target = _target_contract()
    source_r, projection_r = _source_contract(duplicate="r")
    source_a, projection_a = _source_contract(duplicate="a")

    result_r = solve_lift_invariant_joint_states(
        FaithfulContractProjection(source_r, target, projection_r)
    )
    result_a = solve_lift_invariant_joint_states(
        FaithfulContractProjection(source_a, target, projection_a)
    )

    assert result_r.target_state.class_labels == result_a.target_state.class_labels
    assert result_r.source_state.state_count == result_a.source_state.state_count == 3
    assert result_r.target_block_by_source_block == (0, 1, 2)
    assert result_a.target_block_by_source_block == (0, 1, 2)


def test_full_state_and_target_licensing_are_both_projection_invariant() -> None:
    target = _target_contract(coarse_evidence=True)
    source, world_projection = _source_contract(coarse_evidence=True)
    result = solve_lift_invariant_joint_states(
        FaithfulContractProjection(source, target, world_projection)
    )

    assert not result.target_state.full_state_licensed
    assert not result.source_state.full_state_licensed
    assert result.target_state.target_report_licensed
    assert result.source_state.target_report_licensed
    assert result.full_state_licensing_preserved
    assert result.target_licensing_preserved


def test_audit_visible_duplicate_is_a_sharp_projection_obstruction() -> None:
    target = _target_contract()
    visible_source, world_projection = _source_contract(visible_duplicate=True)

    with pytest.raises(ValueError, match="static labels"):
        FaithfulContractProjection(
            source=visible_source,
            target=target,
            source_to_target=world_projection,
        )

    target_state = solve_joint_crest_state(target)
    source_state = solve_joint_crest_state(visible_source)
    assert target_state.state_count == 3
    assert source_state.state_count == 4
    assert source_state.blocks == (("z",), ("a",), ("r0",), ("r1",))


def test_projection_must_preserve_evidence_and_be_surjective() -> None:
    target = _target_contract()
    source, world_projection = _source_contract()
    altered = JointCRESTContract(
        worlds=source.worlds,
        base_labels=source.base_labels,
        evidence_labels=("z", "a", "r0", "r1"),
        target_labels=source.target_labels,
        audits=source.audits,
    )
    with pytest.raises(ValueError, match="evidence partition"):
        FaithfulContractProjection(altered, target, world_projection)

    with pytest.raises(ValueError, match="surjective"):
        FaithfulContractProjection(source, target, (0, 1, 1, 1))
