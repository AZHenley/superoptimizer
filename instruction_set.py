from dataclasses import dataclass


@dataclass
class Instruction:
    opcode: str
    args: tuple[int, ...]

    def __str__(self):
        args = ", ".join(str(arg) for arg in self.args)
        return f"{self.opcode} {args}"


@dataclass
class Program:
    instructions: tuple[Instruction, ...]
    """
    The instructions that make up this program
    """

    mem_size: int
    """
    The amount of memory needed to run this program
    """

    def __str__(self):
        return "\n".join(str(instr) for instr in self.instructions) + "\n"


OPS = {
    "LOAD": ("const",),
    "SWAP": ("mem", "mem"),
    "XOR": ("mem", "mem"),
    "INC": ("mem",)
}
