# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import Counter


def solution(A):
    """Finds element without pair in A and returns the value

    :param A: Array (int)
    :returns: value with odd number of occurence
    :rtype: Integer

    """
    # write your code in Python 3.6
    cnt = Counter(A)
    leftover = 0
    for elem, count in cnt.items():
        if count % 2 != 0:
            leftover = elem

    return leftover
