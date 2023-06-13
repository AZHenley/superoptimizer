import pytest

from assembler import parse
from instruction_set import *


def test_empty_program():
    assert parse('') == Program((), 1)


def test_that_all_instructions_and_mem_size():
    assembly = """
        LOAD 42
        XOR 2, 3
        SWAP 42, 23
        INC 13
    """
    instructions = (
        Instruction('LOAD', (42,)),
        Instruction('XOR', (2, 3)),
        Instruction('SWAP', (42, 23)),
        Instruction('INC', (13,))
    )
    assert parse(assembly) == Program(instructions, 43)


def test_syntax_errors():
    with pytest.raises(ValueError):
        parse("LOAD !&%*")

    with pytest.raises(ValueError):
        parse("LOAD")

    with pytest.raises(ValueError):
        parse("LOAD 23, 42")

    with pytest.raises(ValueError):
        parse("XOR 23")

    with pytest.raises(ValueError):
        parse("XOR 23, -42")

    with pytest.raises(ValueError):
        parse("INC 1, 2")

    with pytest.raises(ValueError):
        parse("SWAP 23")

    with pytest.raises(ValueError):
        parse("SWAP 23, -42")
