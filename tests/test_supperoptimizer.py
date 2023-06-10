from superoptimizer import optimize


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
    optimal = """
LOAD 3
XOR 1, 0
XOR 2, 0
XOR 3, 0
    """.strip() + "\n"
    assert optimize(assembly, MAX_LENGTH, 4, 3, 0) == optimal


def test_three_threes():
    assembly = """
LOAD 3
SWAP 0, 1
LOAD 3
SWAP 0, 2
LOAD 3
    """
    optimal = """
LOAD 3
XOR 1, 0
XOR 2, 0
    """.strip() + "\n"
    assert optimize(assembly, MAX_LENGTH, 3, 3, 0) == optimal
    assert optimize(assembly, 3, 3, 3, 0) == optimal
    assert optimize(assembly, 2, 3, 3, 0) == None
    assert optimize(assembly, 3, 3, 2, 0) == None

    # Changing the input size to 1 doesn't change anything as the first input will be overridden by the load
    assert optimize(assembly, MAX_LENGTH, 3, 3, 1) == optimal

    # For input size 2, we'll need to clear the second input using swap and another load
    optimal = """
LOAD 3
SWAP 0, 1
LOAD 3
XOR 2, 0
    """.strip() + "\n"
    assert optimize(assembly, MAX_LENGTH, 3, 3, 2) == optimal


def test_0_2_1():
    assembly = """
LOAD 2
SWAP 0, 1
LOAD 1
SWAP 0, 2
    """
    optimal = """
LOAD 2
SWAP 0, 1
INC 2
    """.strip() + "\n"
    # Optimal program is load, swap and inc
    assert optimize(assembly, MAX_LENGTH, 3, 2, 0) == optimal
    assert optimize(assembly, MAX_LENGTH, 4, 2, 0) == optimal


def test_no_op():
    assembly = """
SWAP 0,0
    """
    # Program results in the memory being unchanged, so optimal program is empty
    assert optimize(assembly, MAX_LENGTH, 1, 3, 0) == "\n"
    assert optimize(assembly, MAX_LENGTH, 2, 3, 0) == "\n"
    assert optimize(assembly, MAX_LENGTH, 2, 2, 1) == "\n"
    assert optimize(assembly, MAX_LENGTH, 2, 2, 2) == "\n"


def test_increasing_sequence():
    assembly = """
INC 0
INC 1
INC 1
    """
    optimal = """
LOAD 2
SWAP 0, 1
LOAD 1
    """.strip() + "\n"
    assert optimize(assembly, MAX_LENGTH, 2, 3, 0) == optimal

    assembly = """
INC 0
INC 1
INC 1
INC 2
INC 2
INC 2
    """
    optimal = """
LOAD 2
SWAP 0, 1
LOAD 3
SWAP 0, 2
LOAD 1
    """.strip() + "\n"
    assert optimize(assembly, MAX_LENGTH, 3, 3, 0) == optimal


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
    optimal = """
INC 0
XOR 1, 0
INC 1
XOR 2, 1
INC 2
    """.strip() + "\n"
    assert optimize(assembly, MAX_LENGTH, 3, 2, 1) == optimal
