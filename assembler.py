import re
from instruction_set import *


INSTRUCTION_REGEX = re.compile(r'(\w+)\s+([-\d]+(?:\s*,\s*[-\d]+)*)')


def parse(assembly):
    """
    Turns a string into a program
    """
    lines = assembly.split('\n')
    instructions = []
    mem_size = 1
    for line in lines:
        line = line.strip()
        if line == '':
            continue
        match = INSTRUCTION_REGEX.fullmatch(line)
        if match:
            op, args_str = match.groups()
            args = tuple(int(arg) for arg in args_str.split(","))
            operand_types = OPS[op]
            if len(args) != len(operand_types):
                raise ValueError(f'Wrong number of operands: {line}')
            for arg, arg_type in zip(args, operand_types):
                if arg_type == 'mem':
                    if arg < 0:
                        raise ValueError(f'Negative memory address: {line}')
                    mem_size = max(arg + 1, mem_size)
            instructions.append(Instruction(op, args))
        else:
            raise ValueError(f'Invalid syntax: {line}')
    return Program(tuple(instructions), mem_size)
