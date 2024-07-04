#!/usr/bin/python3
"""
Prime Game Module
=================

This module contains the implementation of the Prime Game where Maria and Ben
take turns picking prime numbers and removing them and their multiples from a
set of consecutive integers.

Functions:
----------
- isWinner(x, nums): Determines the winner of the game after x rounds.

Example Usage:
--------------
isWinner = __import__('0-prime_game').isWinner
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
"""


def isWinner(x, nums):
    """
    Determine the winner of each game round and the overall winner.

    Parameters:
    -----------
    x : int
        The number of rounds to be played.
    nums : list of int
        An array where each element is the upper limit of the set of
        consecutive integers for each round.

    Returns:
    --------
    str or None:
        The name of the player that won the most rounds ('Maria' or 'Ben').
        Returns None if there is no overall winner.
    """
    if not nums or x < 1:
        return None

    # Find the maximum number in nums to determine the sieve size
    max_num = max(nums)

    # Sieve of Eratosthenes to find all primes up to max_num
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    p = 2
    while (p * p <= max_num):
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1

    # Count wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = sum(is_prime[1:n + 1])
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


# Ensure the script is executable
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
