def solution(X, Y, D):
    """Calculates minimum amount of jumps from X to Y with jumps of length D

    :param X: Start position (int)
    :param Y: Target position (int)
    :param D: Jump length (int)
    :returns: Min number of jumps
    :rtype: Integer

    """
    # write your code in Python 3.6
    distance = Y - X
    modulo = divmod(distance, D)
    if modulo[1] == 0:
        jumps = modulo[0]
    else:
        # If there is a remainder add one jump
        jumps = modulo[0] + 1

    return jumps
