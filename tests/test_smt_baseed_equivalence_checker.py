import assembler
from smt_based_equivalence_checker import SmtBasedEquivalenceChecker


def are_equivalent(program1, program2, bit_width, input_size):
    return SmtBasedEquivalenceChecker(program1, bit_width, input_size).is_equivalent_to(program2)


def test_add_three():
    three_incs = assembler.parse("""
        INC 0
        INC 0
        INC 0
    """)
    load_three = assembler.parse('LOAD 3')
    one_inc = assembler.parse('INC 0')

    assert are_equivalent(three_incs, load_three, 8, 0)
    assert not are_equivalent(three_incs, one_inc, 8, 0)
    # With a single bit, += 1 and += 3 are equivalent
    assert are_equivalent(three_incs, one_inc, 1, 0)

    # If there's user input, setting to three and increasing by three are no longer equivalent
    assert not are_equivalent(three_incs, load_three, 8, 1)
    # However, += 1 and += 3 are still equivalent for single bits
    assert are_equivalent(three_incs, one_inc, 1, 1)


def test_swap_vs_xor():
    swap_with_xor = assembler.parse("""
        XOR 0, 1
        XOR 1, 0
        XOR 0, 1
    """)
    swap_with_swap = assembler.parse('SWAP 0, 1')
    just_xor = assembler.parse('XOR 0, 1')

    assert are_equivalent(swap_with_xor, swap_with_swap, 8, 2)
    assert not are_equivalent(swap_with_xor, just_xor, 8, 2)
    assert not are_equivalent(swap_with_swap, just_xor, 8, 2)


def test_large_program_with_lots_of_inputs():
    program1 = assembler.parse("""
        INC 0
        XOR 0, 1
        XOR 1, 0
        XOR 0, 1
        INC 1
        SWAP 1, 2
        INC 3
        XOR 3, 2
        INC 4
        INC 5
    """)
    program2 = assembler.parse("""
        SWAP 0, 2
        SWAP 0, 1
        INC 2
        INC 2
        INC 3
        XOR 3, 2
        INC 4
        INC 5
    """)
    assert are_equivalent(program1, program2, 8, 6)
