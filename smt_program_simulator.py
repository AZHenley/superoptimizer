import z3


def simulate(program, mem_size, bit_width, input_size):
    """
    Simulate the behavior of the program using an SMT solver.

    The result will be a list containing, for each memory cell, an SMT value representing the
    value that will reside in that memory location after running the program.
    """

    def mem_cell(i):
        if i < input_size:
            return z3.BitVec(f'input{i}', bit_width)
        else:
            return z3.BitVecVal(0, bit_width)

    state = [mem_cell(i) for i in range(mem_size)]
    for instruction in program.instructions:
        match instruction.opcode:
            case 'LOAD':
                state[0] = z3.BitVecVal(instruction.args[0], bit_width)
            case 'SWAP':
                mem1, mem2 = instruction.args
                state[mem1], state[mem2] = state[mem2], state[mem1]
            case 'XOR':
                mem1, mem2 = instruction.args
                state[mem1] ^= state[mem2]
            case 'INC':
                mem = instruction.args[0]
                state[mem] += 1
    return state
