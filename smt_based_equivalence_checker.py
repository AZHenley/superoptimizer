import z3
from smt_program_simulator import simulate


class SmtBasedEquivalenceChecker:
    def __init__(self, program1, bit_width, input_size):
        self.solver = z3.Solver()
        self.bit_width = bit_width
        self.input_size = input_size
        self.mem_size = program1.mem_size
        self.state1 = simulate(program1, self.mem_size, bit_width, input_size)

    def is_equivalent_to(self, program2):
        state2 = simulate(program2, self.mem_size, self.bit_width, self.input_size)
        programs_are_different = z3.Or(*(value1 != value2 for value1, value2 in zip(self.state1, state2)))
        return self.solver.check(programs_are_different) == z3.unsat
