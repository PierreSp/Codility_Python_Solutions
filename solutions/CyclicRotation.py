# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, K):
    """Shifts each value in A K times

    :param A: Input array (int)
    :param K: Number of shifts
    :returns: new shiftes array [Int]
    :rtype: Array (int)

    """
    # write your code in Python 3.6
    result = [0] * len(A)  # prefill new array to avoid tmp memory solutions
    for index in range(len(A)):
        # calculate new position (current index + shift) and restart at 0 for values larger len(A)
        shift = (index + K) % len(A)
        result[shift] = A[index]

    return result
