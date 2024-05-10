#!/usr/bin/python3

"""
Module: minoperations

This module provides a function to calculate the fewest number of
operations needed
to result in exactly n H characters in a file.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in
    exactly n H characters in the file.

    Args:
        n (int): The desired number of characters.

    Returns:
        int: The fewest number of operations needed, or 0 if impossible.
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
