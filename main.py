from superoptimizer import *


def print_optimal_from_code(assembly, max_length, max_mem, max_val, debug=False):
    print(f"***Source***{assembly}")
    state = run(assembly, max_mem)
    print("***State***")
    print(state)
    print()
    print("***Optimal***")
    print(optimize(assembly, max_length, max_mem, max_val, debug))
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
    assembly = """
LOAD 2
SWAP 0, 1
LOAD 1
SWAP 0, 2
    """
    print_optimal_from_code(assembly, 3, 3, 5)


main()
