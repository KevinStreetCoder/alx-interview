#!/usr/bin/python3
"""
0. Minimum Operations
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n 'H' characters.

    :param n: Number of 'H' characters to achieve
    :type n: int
    :return: Minimum number of operations
    :rtype: int
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
s