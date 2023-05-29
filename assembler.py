import re
from cpu import CPU

def parse(assembly):
    lines = assembly.split('\n')
    program = []
    cpu = CPU(1)
    for line in lines:
        match = re.match(r'(\w+)\s+([-\d]+)(?:,\s*([-\d]+)(?:,\s*([-\d]+))?)?', line)
        if match:
            op_str, *args_str = match.groups()
            op = cpu.ops[op_str]
            args = [int(arg) for arg in args_str if arg is not None]
            program.append((op, *args))
    return program

def output(program):
    if len(program) == 0: return "\n"
    cpu = CPU(1)
    assembly = ""
    for instruction in program:
        op = instruction[0]
        args = instruction[1:]
        if op.__name__ == cpu.load.__name__:
            assembly += f"LOAD {args[0]}\n"
        elif op.__name__ == cpu.swap.__name__:
            assembly += f"SWAP {args[0]}, {args[1]}\n"
        elif op.__name__ == cpu.xor.__name__:
            assembly += f"XOR {args[0]}, {args[1]}\n"
        elif op.__name__ == cpu.inc.__name__:
            assembly += f"INC {args[0]}\n"
    return assembly