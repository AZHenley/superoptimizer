from superoptimizer import optimal_from_state, run


def count_instructions(assembly):
    if assembly == "\n":
        return 0
    else:
        return assembly.count("\n")


def assert_optimal_length(length, state, max_length, max_val):
    """
    Asserts that, given the arguments `state`, `max_length` and `max_val`, the
    superoptimizer finds a program of length `length` and that this program produces
    the state `state` when run.

    This method does not assert a specific output program, so that tests don't
    fail due to changes in the optimizer that make it output different instructions
    as long as the result is still correct and optimal.
    """
    optimal = optimal_from_state(state, max_length, max_val)
    assert count_instructions(optimal) == length
    assert run(optimal, len(state)) == state


def test_four_threes():
    # Optimal program is a load and three xors
    assert_optimal_length(4, [3, 3, 3, 3], 4, 5)


def test_0_2_1():
    # Optimal program is load, swap and inc
    assert_optimal_length(3, [0, 2, 1], 3, 5)
    assert_optimal_length(3, [0, 2, 1, 0], 4, 5)


def test_zeros():
    # Optimal program is empty
    # Test currently fails because the empty program isn't included in the search space
    assert_optimal_length(0, [0], 1, 3)
    assert_optimal_length(0, [0, 0], 1, 3)


def test_increasing_sequence():
    # Optimal program is inc for first memory slot and then xor+inc for every one after that
    assert_optimal_length(1, [1], 2, 3)
    assert_optimal_length(3, [1, 2], 4, 3)
    assert_optimal_length(5, [1, 2, 3], 5, 3)
