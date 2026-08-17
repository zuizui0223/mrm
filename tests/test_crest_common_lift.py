from __future__ import annotations

from itertools import combinations

from mrm.crest_common_lift import (
    ComponentCoverage,
    SynchronizedLiftProblem,
    maximal_common_lift,
)


def _cascade_problem(
    *,
    require_lost_state: bool = True,
    retain_stable: bool = True,
) -> SynchronizedLiftProblem:
    worlds = ("w0", "w1", "w2", "stable", "bad")
    stable_successor = 3 if retain_stable else 4
    successors = (
        (1,),
        (2,),
        (4,),
        (stable_successor,),
        (4,),
    )
    future_required = ("f0", "stable") if require_lost_state else ("stable",)
    components = (
        ComponentCoverage(
            "future",
            ("f0", "f1", "f2", "stable", "bad"),
            future_required,
        ),
        ComponentCoverage(
            "semantic",
            ("s0", "s1", "s2", "stable", "bad"),
            ("stable",),
        ),
        ComponentCoverage(
            "mechanism",
            ("m0", "m1", "m2", "stable", "bad"),
            ("stable",),
        ),
        ComponentCoverage(
            "evidence",
            ("e0", "e1", "e2", "stable", "bad"),
            ("stable",),
        ),
    )
    return SynchronizedLiftProblem(
        worlds=worlds,
        compatible=(True, True, True, True, False),
        actions=("step",),
        successors=successors,
        components=components,
    )


def _subsets(indices: tuple[int, ...]):
    for size in range(len(indices) + 1):
        yield from combinations(indices, size)


def test_descending_pruning_returns_the_unique_maximal_closed_subset() -> None:
    problem = _cascade_problem()
    result = maximal_common_lift(problem)

    assert result.worlds == ("stable",)
    assert result.exists
    assert not result.coverage_complete
    assert not result.admissible
    assert result.missing_coverage == (("future", ("f0",)),)

    compatible_indices = tuple(
        index for index, compatible in enumerate(problem.compatible) if compatible
    )
    closed_subsets = [
        subset for subset in _subsets(compatible_indices) if problem.is_closed_subset(subset)
    ]
    assert closed_subsets == [(), (3,)]
    assert all(set(subset).issubset(result.viable_indices) for subset in closed_subsets)


def test_elimination_ranks_give_a_finite_obstruction_chain() -> None:
    result = maximal_common_lift(_cascade_problem())

    assert result.elimination_reasons[4].round == 0
    assert result.elimination_reasons[2].round == 1
    assert result.elimination_reasons[1].round == 2
    assert result.elimination_reasons[0].round == 3
    assert result.elimination_chain("w0") == ("w0", "w1", "w2", "bad")
    assert result.elimination_chain("w1") == ("w1", "w2", "bad")
    assert result.elimination_chain("stable") == ("stable",)
    assert result.coverage_elimination_chains("future", "f0") == (
        ("w0", "w1", "w2", "bad"),
    )


def test_coverage_complete_lift_exists_exactly_when_kernel_covers_requirements() -> None:
    incomplete = maximal_common_lift(_cascade_problem(require_lost_state=True))
    complete = maximal_common_lift(_cascade_problem(require_lost_state=False))

    assert not incomplete.coverage_complete
    assert not incomplete.admissible
    assert complete.coverage_complete
    assert complete.admissible
    assert complete.worlds == ("stable",)
    assert complete.coverage_elimination_chains("future", "stable") == ()


def test_empty_kernel_is_a_common_lift_no_go() -> None:
    result = maximal_common_lift(
        _cascade_problem(require_lost_state=False, retain_stable=False)
    )

    assert not result.exists
    assert not result.coverage_complete
    assert not result.admissible
    assert result.worlds == ()
    assert result.elimination_chain("stable") == ("stable", "bad")


def test_illegal_actions_do_not_create_false_obstructions() -> None:
    problem = SynchronizedLiftProblem(
        worlds=("compatible", "outside"),
        compatible=(True, False),
        actions=("optional",),
        successors=((None,), (1,)),
        components=(
            ComponentCoverage(
                "future", ("kept", "outside"), ("kept",)
            ),
        ),
    )
    result = maximal_common_lift(problem)

    assert result.worlds == ("compatible",)
    assert result.admissible
    assert result.restricted_successors == ((None,),)


def test_maximal_kernel_contains_every_declared_closed_common_lift() -> None:
    problem = SynchronizedLiftProblem(
        worlds=("left", "right", "sink", "bad"),
        compatible=(True, True, True, False),
        actions=("a", "b"),
        successors=(
            (2, 1),
            (2, 1),
            (2, 2),
            (3, 3),
        ),
        components=(
            ComponentCoverage(
                "future", ("left", "right", "sink", "bad"), ("sink",)
            ),
        ),
    )
    result = maximal_common_lift(problem)

    assert result.viable_indices == (0, 1, 2)
    assert result.admissible
    compatible = (0, 1, 2)
    for subset in _subsets(compatible):
        if problem.is_closed_subset(subset):
            assert set(subset).issubset(result.viable_indices)
