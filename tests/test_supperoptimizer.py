from superoptimizer import optimize
from assembler import parse, Program


MAX_LENGTH = 1000000


def test_four_threes():
    assembly = """
        LOAD 3
        SWAP 0, 1
        LOAD 3
        SWAP 0, 2
        LOAD 3
        SWAP 0, 3
        LOAD 3
    """
    optimal = parse("""
        LOAD 3
        XOR 1, 0
        XOR 2, 0
        XOR 3, 0
    """)
    assert optimize(assembly, MAX_LENGTH, 3, 0) == optimal


def test_three_threes():
    assembly = """
        LOAD 3
        SWAP 0, 1
        LOAD 3
        SWAP 0, 2
        LOAD 3
    """
    optimal = parse("""
        LOAD 3
        XOR 1, 0
        XOR 2, 0
    """)
    assert optimize(assembly, MAX_LENGTH, 3, 0) == optimal
    # Assert that the program is still found with a tight max_length
    assert optimize(assembly, 3, 3, 0) == optimal
    # Assert that the program is not found with a max_length that's below the optimal length
    assert optimize(assembly, 2, 3, 0) is None
    # Assert that the program is not found when max_val is too low
    assert optimize(assembly, 3, 2, 0) is None

    # Changing the input size to 1 doesn't change anything as the first input will be overridden by the load
    assert optimize(assembly, MAX_LENGTH, 3, 1) == optimal

    # For input size 2, we'll need to clear the second input using swap and another load
    optimal = parse("""
        LOAD 3
        SWAP 0, 1
        LOAD 3
        XOR 2, 0
    """)
    assert optimize(assembly, MAX_LENGTH, 3, 2) == optimal


def test_0_2_1():
    assembly = """
        LOAD 2
        SWAP 0, 1
        LOAD 1
        SWAP 0, 2
    """
    optimal = parse("""
        LOAD 2
        SWAP 0, 1
        INC 2
    """)
    assert optimize(assembly, MAX_LENGTH, 2, 0) == optimal


def test_no_op():
    assembly = """
        SWAP 0,0
    """
    empty_program = Program((), 0)
    # Program results in the memory being unchanged, so optimal program is empty
    assert optimize(assembly, MAX_LENGTH, 3, 0) == empty_program
    assert optimize(assembly, MAX_LENGTH, 2, 1) == empty_program
    assert optimize(assembly, MAX_LENGTH, 2, 2) == empty_program


def test_increasing_sequence():
    assembly = """
        INC 0
        INC 1
        INC 1
    """
    optimal = parse("""
        LOAD 1
        XOR 1, 0
        INC 1
    """)
    assert optimize(assembly, MAX_LENGTH, 3, 0) == optimal

    assembly = """
        INC 0
        INC 1
        INC 1
        INC 2
        INC 2
        INC 2
    """
    optimal = parse("""
        LOAD 1
        XOR 1, 0
        XOR 2, 0
        INC 1
        XOR 2, 1
    """)
    assert optimize(assembly, MAX_LENGTH, 3, 0) == optimal


def test_increasing_from_input():
    # Given the input x, the following program should produce the sequence x+1, x+2, x+3
    assembly = """
        XOR 1, 0
        XOR 2, 0
        INC 0
        INC 1
        INC 1
        INC 2
        INC 2
        INC 2
    """
    optimal = parse("""
        INC 0
        XOR 1, 0
        INC 1
        XOR 2, 1
        INC 2
    """)
    assert optimize(assembly, MAX_LENGTH, 2, 1) == optimal
