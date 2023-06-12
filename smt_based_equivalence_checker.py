import z3
from smt_program_simulator import simulate


def are_equivalent(program1, program2, bit_width, input_size):
    solver = z3.Solver()
    mem_size = max(program1.mem_size, program2.mem_size)
    state1 = simulate(program1, mem_size, bit_width, input_size)
    state2 = simulate(program2, mem_size, bit_width, input_size)
    programs_are_different = z3.Or(*(value1 != value2 for value1, value2 in zip(state1, state2)))
    print(programs_are_different)
    return solver.check(programs_are_different) == z3.unsat
