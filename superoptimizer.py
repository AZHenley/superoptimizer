from itertools import product
import assembler
import brute_force_equivialence_checker
from instruction_set import *


def optimize(assembly, max_length, bit_width, input_size=0, *,
             equivalence_checker=brute_force_equivialence_checker.are_equivalent,
             debug=False):
    """
    Helper function that finds the optimal code given the assembly code.
    """
    program = assembler.parse(assembly)
    opt = Superoptimizer(equivalence_checker)
    return opt.search(max_length, bit_width, program, input_size, debug)


class Superoptimizer:
    def __init__(self, are_equivalent):
        self.are_equivalent = are_equivalent

    @staticmethod
    def generate_operands(operand_type, max_mem, bit_width):
        if operand_type == "const":
            return range(2 ** bit_width)
        elif operand_type == "mem":
            return range(max_mem)
        else:
            raise ValueError(f"Illegal operand type: {operand_type}")

    @staticmethod
    def generate_programs(max_length, max_mem, bit_width):
        """
        Generates all possible programs
        """
        yield Program((), 0)
        for length in range(1, max_length + 1):
            instructions = []
            for op, operand_types in OPS.items():
                arg_sets = (Superoptimizer.generate_operands(ot, max_mem, bit_width) for ot in operand_types)
                instructions.extend(assembler.Instruction(op, args) for args in product(*arg_sets))
            for prog in product(instructions, repeat=length):
                yield Program(prog, max_mem)

    # Tests all the generated programs and returns the shortest.
    def search(self, max_length, bit_width, program, input_size=0, debug=False):
        count = 0
        for optimal in self.generate_programs(max_length, program.mem_size, bit_width):
            if self.are_equivalent(optimal, program, bit_width, input_size):
                return optimal

            # Debugging.
            if debug:
                count += 1
                if count % 1000000 == 0:
                    print(f"Programs searched: {count:,}")

        return None
