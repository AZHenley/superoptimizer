import assembler


def run(assembly, bit_width, input=()):
    """
    Helper function that runs a piece of assembly code.
    """
    program = assembler.parse(assembly)
    cpu = CPU(program.mem_size, bit_width)
    return cpu.execute(program, input)


class CPU:
    def __init__(self, max_mem_cells, bit_width):
        self.max_mem_cells = max_mem_cells
        self.limit = 2 ** bit_width

    def execute(self, program, input=()):
        state = [0] * self.max_mem_cells
        state[0: len(input)] = input
        for instruction in program.instructions:
            match instruction.opcode:
                case 'LOAD':
                    state[0] = instruction.args[0] % self.limit
                case 'SWAP':
                    mem1, mem2 = instruction.args
                    state[mem1], state[mem2] = state[mem2], state[mem1]
                case 'XOR':
                    mem1, mem2 = instruction.args
                    state[mem1] ^= state[mem2]
                case 'INC':
                    mem = instruction.args[0]
                    state[mem] = (state[mem] + 1) % self.limit
        return state
