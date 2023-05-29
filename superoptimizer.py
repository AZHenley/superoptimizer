from itertools import product
from cpu import CPU
import assembler

# Helper function that finds the optimal code given the assembly code.
def optimal_from_code(assembly, max_length, max_mem, max_val, debug=False):
    cpu = CPU(max_mem)
    program = assembler.parse(assembly)
    state = cpu.execute(program)
    print(f"***Source***{assembly}")
    optimal_from_state(state, max_length, max_val, debug)

# Helper function that finds the optimal code given the goal state.
def optimal_from_state(state, max_length, max_val, debug=False):
    max_mem = len(state)
    print(f"***State***\n{state}\n") 
    opt = Superoptimizer()
    shortest_program = opt.search(max_length, max_mem, max_val, state, debug) 
    disassembly = assembler.output(shortest_program)
    print(f"***Optimal***\n{disassembly}\n{'='*20}\n")

class Superoptimizer:
    def __init__(self):
        self.program_cache = {}

    # Generates all possible programs.
    def generate_programs(self, cpu, max_length, max_mem, max_val):
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
    def search(self, max_length, max_mem, max_val, target_state, debug=False):
        count = 0
        cpu = CPU(max_mem)
        for program in self.generate_programs(cpu, max_length, max_mem, max_val):
            state = cpu.execute(program)
            if state == target_state:
                state = tuple(state) 
                if state not in self.program_cache or len(program) < len(self.program_cache[state]):
                    self.program_cache[state] = program
            
            # Debugging.
            if debug:
                count += 1
                if count % 1000000 == 0: print(f"Programs searched: {count:,}")
                if count % 10000000 == 0: 
                    solution = self.program_cache.get(tuple(target_state), None)
                    print(f"Best solution: {solution}")

        return self.program_cache.get(tuple(target_state), None)
