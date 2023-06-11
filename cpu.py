import assembler


def run(assembly, input=()):
    """
    Helper function that runs a piece of assembly code.
    """
    program = assembler.parse(assembly)
    cpu = CPU(program.mem_size)
    return cpu.execute(program, input)


class CPU:
    def __init__(self, max_mem_cells):
        self.max_mem_cells = max_mem_cells

    def execute(self, program, input=()):
        state = [0] * self.max_mem_cells
        state[0: len(input)] = input
        for instruction in program.instructions:
            match instruction.opcode:
                case 'LOAD':
                    state[0] = instruction.args[0]
                case 'SWAP':
                    mem1, mem2 = instruction.args
                    state[mem1], state[mem2] = state[mem2], state[mem1]
                case 'XOR':
                    mem1, mem2 = instruction.args
                    state[mem1] ^= state[mem2]
                case 'INC':
                    state[instruction.args[0]] += 1
        return state
