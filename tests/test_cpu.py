from superoptimizer import run


def test_load_and_swap():
    assembly = """
LOAD 3
SWAP 0, 1
LOAD 3
SWAP 0, 2
LOAD 3
SWAP 0, 3
LOAD 3
    """
    assert run(assembly, 4) == [3, 3, 3, 3]
    assert run(assembly, 10) == [3, 3, 3, 3, 0, 0, 0, 0, 0, 0]


def test_load_and_xor():
    assembly = """
LOAD 42
XOR 1, 0
LOAD 23
XOR 1, 0
    """
    assert run(assembly, 2) == [23, 42 ^ 23]


def test_load_and_inc():
    assembly = """
LOAD 41
INC 0
INC 1
INC 1
INC 1
    """
    assert run(assembly, 2) == [42, 3]


def test_input():
    assembly = """
XOR 1, 0
INC 1
    """
    assert run(assembly, 2) == [0, 1]
    assert run(assembly, 2, [2]) == [2, 3]
    assert run(assembly, 2, [1, 2]) == [1, 4]
