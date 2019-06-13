# Binary gap
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import re


def solution(N):
    ''' Binary gap solver
    This function returns the length of the longest sequence of the integer representation of N
    which consists of 0's and is surrounded by 1's. If it does not exist, it returns 0.
    '''
    if not isinstance(N, int):
        raise ("N is not a valid integer")

    result = 0
    sets = None
    binary_representation = bin(N)

    # Duplicate 1 as re cannot work with overlaps and we do not cause problems
    binary_representation = str(binary_representation).replace("1", "11")

    # find all sets of numbers surrounded by 1's
    sets = re.findall(r"1(0+?)1", binary_representation)
    sets = [len(x) for x in sets]
    if len(sets) > 0:
        result = max(sets)
    else:
        # No surrounded array found
        result = 0

    return result
