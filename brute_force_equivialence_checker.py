from cpu import CPU


def generate_inputs(input_size, max_val):
    """
    Generates all possible tuples of the given size with values ranging from 0 (inclusive)
    to `max_val` (exclusive).
    """
    if input_size == 0:
        yield ()
    else:
        for x in range(max_val):
            for rest in generate_inputs(input_size - 1, max_val):
                yield x, *rest


def are_equivalent(program1, program2, bit_width, input_size):
    mem_size = max(program1.mem_size, program2.mem_size)
    cpu = CPU(mem_size, bit_width)
    for input in generate_inputs(input_size, 2 ** bit_width):
        if cpu.execute(program1, input) != cpu.execute(program2, input):
            return False
    return True
