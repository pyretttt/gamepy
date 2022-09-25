"""Guess number game"""

from typing import Callable

import numpy as np
import statistics as st


def guess_number(number: int, bounds: range) -> int:
    """Guess number algorithm

    Args:
        number (int): number to guess. Constrainted by range
        bounds (range): Number to guess bounds

    Returns:
        int: number of tries
    """
    count = 0
    constraints = list(bounds)

    while 1:
        count += 1
        pivot = len(constraints)//2
        median = constraints[pivot]

        if median == number:
            return count
        elif median > number:
            constraints = constraints[:pivot]
        elif median < number:
            constraints = constraints[pivot + 1:]


def execute(fn: Callable[[int, range], int], number_of_tries: int = 10000) -> int:
    """Executes given function, given number of times

    Args:
        fn (Callable[[int, range], int]): function to execute
        number_of_tries (int, optional): Number of tries. Defaults to 10000.

    Returns:
        int: Average output of given function.
    """
    constraints = range(1, 101)
    output = [fn(np.random.randint(constraints.start, constraints.stop), constraints) 
              for _ in 
              range(0, number_of_tries)]
    
    print("Output are: ", output[:10])
    
    return st.mean(output)

if __name__ == '__main__':
    result = execute(guess_number)
    print(f"Average number of guess is: {result}")
