# superoptimizer

A toy superoptimizer for a made-up assembly language. See the blog post: [My first superoptimizer](https://austinhenley.com/blog/superoptimizer.html).

It works by generating every possible permutation of code instructions and operands, then tests each generated program for equivalence to the original program. I broke the project up into these steps:

- Design a simple assembly language.
- Write an emulator that executes an assembly program and returns the final state.
- Write a function that tests the equivalence of two programs based on their before/after state.
- Write an assembler that can translate to and from human-readable assembly and the internal assembly representation.
- Write an optimizer that generates every program of length _1_ to _n_ instructions with every possible operand from _0_ to _k_ with _x_ memory cells.

To focus on the superoptimizer and not making a comprehensive, realistic assembly language, I limited it to a boring set of instructions:

- **LOAD _val_** which loads the immediate value into memory location 0.
- **SWAP _mem_, _mem_** which swaps the values of the two memory locations.
- **XOR _mem_, _mem_** which performs a bitwise XOR operation on the values of the memory locations and stores the result in the first's location.
- **INC _mem_** which increments the value at the memory location.

There are many possible improvements:

- **Start state.** Right now it assumes the start state is always the same, which means there is no concept of program input.
- **Program equivalence.** A set of inputs and outputs should be specified such that two programs can actually be tested for equivalence.
- **Pruning.** Many nonsensical programs are generated, which significantly slows it down.
- **More instructions.** There need to be more instructions, especially a conditional instruction, to give the superoptimizer more opportunities to make improvements.

The blog [post](https://austinhenley.com/blog/superoptimizer.html) expands on all of these details.


