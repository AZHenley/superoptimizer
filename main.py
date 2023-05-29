from superoptimizer import *

def main():
    # Test 1
    assembly = """
LOAD 3
SWAP 0, 1
LOAD 3
SWAP 0, 2
LOAD 3
SWAP 0, 3
LOAD 3
    """
    optimal_from_code(assembly, 4, 4, 5)

    # Test 2
    state = [0, 2, 1]
    optimal_from_state(state, 3, 5)

    ## Test 3 - Careful, I don't think this will finish for days.
    # state = [2, 4, 6, 8, 10, 12]
    # optimal_from_state(state, 10, 15, True)

main()