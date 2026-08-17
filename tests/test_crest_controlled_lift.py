from __future__ import annotations

import pytest

from mrm.crest_common_lift import (
    ComponentCoverage,
    SynchronizedLiftProblem,
    maximal_common_lift,
)
from mrm.crest_controlled_lift import (
    ControlledSynchronizedLiftProblem,
    maximal_controlled_common_lift,
)


def _controlled_problem(
    *, required_labels=("safe", "choice")
) -> ControlledSynchronizedLiftProblem:
    worlds = ("safe", "choice", "hazard", "trapped", "bad")
    components = (
        ComponentCoverage(
            "role",
            ("safe", "choice", "hazard", "trap", "bad"),
            tuple(required_labels),
        ),
    )
    return ControlledSynchronizedLiftProblem(
        worlds=worlds,
        compatible=(True, True, True, True, False),
        uncontrollable_actions=("weather",),
        controllable_actions=("protect", "exploit"),
        uncontrollable_successors=((0,), (1,), (4,), (3,), (4,)),
        controllable_successors=(
            (0, 0),
            (0, 4),
            (2, 2),
            (2, 4),
            (4, 4),
        ),
        components=components,
    )


def _universal_problem() -> SynchronizedLiftProblem:
    controlled = _controlled_problem()
    successors = tuple(
        tuple(uncontrollable_row) + tuple(controllable_row)
        for uncontrollable_row, controllable_row in zip(
            controlled.uncontrollable_successors,
            controlled.controllable_successors,
        )
    )
    return SynchronizedLiftProblem(
        worlds=controlled.worlds,
        compatible=controlled.compatible,
        actions=("weather", "protect", "exploit"),
        successors=successors,
        components=controlled.components,
    )


def test_controlled_kernel_retains_choice_and_returns_memoryless_policy() -> None:
    result = maximal_controlled_common_lift(_controlled_problem())

    assert result.worlds == ("safe", "choice")
    assert result.exists
    assert result.coverage_complete
    assert result.admissible
    assert result.policy == (
        ("safe", "protect", "safe"),
        ("choice", "protect", "safe"),
    )

    retained = set(result.viable_indices)
    for world, action, successor in result.policy:
        world_index = result.problem.worlds.index(world)
        action_index = result.problem.controllable_actions.index(action)
        successor_index = result.problem.worlds.index(successor)
        assert result.problem.controllable_successors[world_index][action_index] == successor_index
        assert successor_index in retained
        assert all(
            item is None or item in retained
            for item in result.problem.uncontrollable_successors[world_index]
        )


def test_controlled_kernel_is_greatest_and_strictly_larger_than_universal_kernel() -> None:
    problem = _controlled_problem()
    controlled = maximal_controlled_common_lift(problem)

    for mask in range(1 << len(problem.worlds)):
        subset = tuple(
            index for index in range(len(problem.worlds)) if mask & (1 << index)
        )
        if problem.is_controlled_invariant_subset(subset):
            assert set(subset).issubset(controlled.viable_indices)

    universal = maximal_common_lift(_universal_problem())
    assert universal.worlds == ("safe",)
    assert set(universal.viable_indices).issubset(controlled.viable_indices)
    assert controlled.worlds != universal.worlds


def test_elimination_certificates_distinguish_environment_and_control_failure() -> None:
    result = maximal_controlled_common_lift(_controlled_problem())

    hazard = result.elimination_certificate("hazard")
    assert hazard.kind == "uncontrollable_escape"
    assert hazard.round == 1
    assert hazard.action == "weather"
    assert hazard.depth == 1
    assert hazard.children[0][1].world == "bad"
    assert hazard.children[0][1].kind == "static"
    assert hazard.children[0][1].round == 0

    trapped = result.elimination_certificate("trapped")
    assert trapped.kind == "no_safe_control"
    assert trapped.round == 2
    assert trapped.depth == 2
    assert tuple(action for action, _ in trapped.children) == (
        "protect",
        "exploit",
    )
    assert tuple(child.world for _, child in trapped.children) == (
        "hazard",
        "bad",
    )
    assert trapped.children[0][1].round == 1
    assert trapped.children[1][1].round == 0

    with pytest.raises(ValueError, match="viable worlds have no elimination certificate"):
        result.elimination_certificate("safe")


def test_missing_coverage_returns_controlled_no_go_certificate() -> None:
    result = maximal_controlled_common_lift(
        _controlled_problem(required_labels=("safe", "choice", "trap"))
    )

    assert result.worlds == ("safe", "choice")
    assert result.missing_coverage == (("role", ("trap",)),)
    assert not result.coverage_complete
    assert not result.admissible

    certificates = result.coverage_elimination_certificates("role", "trap")
    assert len(certificates) == 1
    assert certificates[0].world == "trapped"
    assert certificates[0].kind == "no_safe_control"


def test_no_legal_control_is_a_finite_leaf_no_go() -> None:
    problem = ControlledSynchronizedLiftProblem(
        worlds=("idleless",),
        compatible=(True,),
        uncontrollable_actions=(),
        controllable_actions=("act",),
        uncontrollable_successors=((),),
        controllable_successors=((None,),),
        components=(
            ComponentCoverage("role", ("idleless",), ()),
        ),
    )
    result = maximal_controlled_common_lift(problem)

    assert not result.exists
    certificate = result.elimination_certificate("idleless")
    assert certificate.kind == "no_safe_control"
    assert certificate.round == 1
    assert certificate.children == ()
    assert certificate.depth == 0


def test_problem_rejects_ambiguous_action_roles_and_bad_shapes() -> None:
    with pytest.raises(ValueError, match="must be disjoint"):
        ControlledSynchronizedLiftProblem(
            worlds=("x",),
            compatible=(True,),
            uncontrollable_actions=("a",),
            controllable_actions=("a",),
            uncontrollable_successors=((0,),),
            controllable_successors=((0,),),
            components=(ComponentCoverage("role", ("x",), ("x",)),),
        )

    with pytest.raises(ValueError, match="must align with worlds and actions"):
        ControlledSynchronizedLiftProblem(
            worlds=("x",),
            compatible=(True,),
            uncontrollable_actions=(),
            controllable_actions=("stay",),
            uncontrollable_successors=((),),
            controllable_successors=((),),
            components=(ComponentCoverage("role", ("x",), ("x",)),),
        )
