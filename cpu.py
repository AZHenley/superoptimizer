class CPU:
    def __init__(self, max_mem_cells):
        self.max_mem_cells = max_mem_cells
        self.state = [0] * max_mem_cells
        self.ops = {'LOAD': self.load, 'SWAP': self.swap, 'XOR': self.xor, 'INC': self.inc}

    def execute(self, program):
        state = self.state.copy()
        for instruction in program:
            op = instruction[0]
            args = list(instruction[1:])
            args.insert(0, state)
            state = op(*args)
        return state

    def load(self, state, val):
        state[0] = val
        return state
    
    def swap(self, state, mem1, mem2):
        state[mem1], state[mem2] = state[mem2], state[mem1]
        return state
    
    def xor(self, state, mem1, mem2):
        state[mem1] = state[mem1] ^ state[mem2]
        return state
    
    def inc(self, state, mem):
        state[mem] += 1
        return state