''' Task:
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].

'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    """ Returns the missing number from array A [1...N+1] with len(A) = N
    Should work in O(N)

    :param A: Input array (int)
    :returns: Missing value (int)
    :rtype: Integer

    """
    # write your code in Python 3.6
    if len(A) == 0:
        return 1

    A.sort()
    ind = 1

    while (A[ind - 1] == ind):
        if (ind == len(A)):
            return ind + 1
        ind += 1
    return ind
