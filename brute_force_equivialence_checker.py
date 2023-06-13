from cpu import CPU


class BruteForceEquivalenceChecker:
    def __init__(self, program1, bit_width, input_size):
        self.program1 = program1
        self.bit_width = bit_width
        self.max_val = 2 ** bit_width
        self.input_size = input_size

    def generate_inputs(self, input_size):
        """
        Generates all possible tuples of the given size with values ranging from 0 (inclusive)
        to `max_val` (exclusive).
        """
        if input_size == 0:
            yield ()
        else:
            for x in range(self.max_val):
                for rest in self.generate_inputs(input_size - 1):
                    yield x, *rest

    def is_equivalent_to(self, program2):
        mem_size = max(self.program1.mem_size, program2.mem_size)
        cpu = CPU(mem_size, self.bit_width)
        for input in self.generate_inputs(self.input_size):
            if cpu.execute(self.program1, input) != cpu.execute(program2, input):
                return False
        return True
