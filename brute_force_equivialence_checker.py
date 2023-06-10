from cpu import CPU


def generate_inputs(input_size, max_val):
    if input_size == 0:
        yield ()
    else:
        for x in range(max_val + 1):
            for rest in generate_inputs(input_size - 1, max_val):
                yield (x, *rest)


def are_equivalent(program1, program2, max_mem, max_val, input_size):
    cpu = CPU(max_mem)
    for input in generate_inputs(input_size, max_val):
        if cpu.execute(program1, input) != cpu.execute(program2, input):
            return False
    return True
