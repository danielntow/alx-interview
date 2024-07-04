# 0x0A-primegame

# Prime Game

This project is a solution to the Prime Game problem.

## Description

Maria and Ben play a game where they take turns choosing a prime number from a set of consecutive integers and removing that number and its multiples from the set. The player that cannot make a move loses the game. The function `isWinner(x, nums)` determines the winner after `x` rounds of the game.

## Usage

To use the function, run the following script:

```bash
#!/usr/bin/python3
isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
