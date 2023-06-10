from itertools import product
from cpu import CPU
import assembler
import brute_force_equivialence_checker


def run(assembly, max_mem, input=()):
    """
    Helper function that runs a piece of assembly code.
    """
    cpu = CPU(max_mem)
    program = assembler.parse(assembly)
    return cpu.execute(program, input)


def optimize(assembly, max_length, max_mem, max_val, input_size=0, debug=False):
    """
    Helper function that finds the optimal code given the assembly code.
    """
    program = assembler.parse(assembly)
    opt = Superoptimizer(brute_force_equivialence_checker.are_equivalent)
    shortest = opt.search(max_length, max_mem, max_val, program, input_size, debug)
    return assembler.output(shortest)


class Superoptimizer:
    def __init__(self, are_equivalent):
        self.are_equivalent = are_equivalent

    # Generates all possible programs.
    def generate_programs(self, cpu, max_length, max_mem, max_val):
        yield []
        for length in range(1, max_length + 1):
            for prog in product(cpu.ops.values(), repeat=length):
                arg_sets = []
                for op in prog:
                    if op == cpu.load:
                        arg_sets.append([tuple([val]) for val in range(max_val + 1)])
                    elif op == cpu.swap or op == cpu.xor:
                        arg_sets.append(product(range(max_mem), repeat=2))
                    elif op == cpu.inc:
                        arg_sets.append([tuple([val]) for val in range(max_mem)])
                for arg_set in product(*arg_sets):
                    program = [(op, *args) for op, args in zip(prog, arg_set)]
                    yield program

    # Tests all of the generated programs and returns the shortest.
    def search(self, max_length, max_mem, max_val, program, input_size=0, debug=False):
        count = 0
        cpu = CPU(max_mem)
        for optimal in self.generate_programs(cpu, max_length, max_mem, max_val):
            if self.are_equivalent(optimal, program, max_mem, max_val, input_size):
                return optimal

            # Debugging.
            if debug:
                count += 1
                if count % 1000000 == 0:
                    print(f"Programs searched: {count:,}")

        return None
