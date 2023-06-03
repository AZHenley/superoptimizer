from superoptimizer import *


def print_optimal_from_code(assembly, max_length, max_mem, max_val, debug=False):
    print(f"***Source***{assembly}")
    state = run(assembly, max_mem)
    print_optimal_from_state(state, max_length, max_val, debug)


def print_optimal_from_state(state, max_length, max_val, debug=False):
    print("***State***")
    print(state)
    print()
    print("***Optimal***")
    print(optimal_from_state(state, max_length, max_val, debug))
    print("=" * 20)
    print()


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
    print_optimal_from_code(assembly, 4, 4, 5)

    # Test 2
    state = [0, 2, 1]
    print_optimal_from_state(state, 3, 5)

    ## Test 3 - Careful, I don't think this will finish for days.
    # state = [2, 4, 6, 8, 10, 12]
    # print_optimal_from_state(state, 10, 15, True)


main()
