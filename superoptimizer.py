from itertools import product
from cpu import CPU

class Superoptimizer:
    def __init__(self):
        self.program_cache = {}

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

    def search(self, max_length, max_mem, max_val, target_state):
        cpu = CPU(max_mem)
        for program in self.generate_programs(cpu, max_length, max_mem, max_val):
            state = cpu.execute(program)
            if state == target_state:
                state = tuple(state) 
                if state not in self.program_cache or len(program) < len(self.program_cache[state]):
                    self.program_cache[state] = program
        return self.program_cache.get(tuple(target_state), None)



