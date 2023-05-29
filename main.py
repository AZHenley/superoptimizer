from superoptimizer import *
from cpu import *
import assembler

# Helper function that finds the optimal code given assembly code.
def optimal_from_code(assembly, max_length, max_mem, max_val):
    cpu = CPU(max_mem)
    program = assembler.parse(assembly)
    state = cpu.execute(program)
    print(f"***Source***{assembly}")
    optimal_from_state(state, max_length, max_val)

# Helper function that finds the optimal code given the goal state.
def optimal_from_state(state, max_length, max_val):
    max_mem = len(state)
    print(f"***State***\n{state}\n") 
    opt = Superoptimizer()
    shortest_program = opt.search(max_length, max_mem, max_val, state) 
    disassembly = assembler.output(shortest_program)
    print(f"***Optimal***\n{disassembly}\n===\n")

# Test 1
assembly = """
LOAD 3
SWAP 0, 1
LOAD 3
SWAP 0, 2
LOAD 3
SWAP 0, 3
LOAD 3
"""
optimal_from_code(assembly, 4, 4, 5)

# Test 2
state = [0, 2, 1]
optimal_from_state(state, 3, 5)