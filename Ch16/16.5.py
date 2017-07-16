#!/bin/python

import sys
from math import log

def main(argv):
    n = int(argv[1])
    for i in range(n+1):
        print('%d: %d' % (i, count_factorial_zeros_iterative(i)))


def count_factorial_zeros(n):
    """Succinctly returns number of trailing zeros in n!"""
    if n < 0:
        return -1
    elif n == 0:
        return 0
    return sum(int(n/5**i) for i in range(1, int(log(n)/log(5) + 1)))


def count_factorial_zeros_iterative(n):
    """Returns number of trailing zeros in n! by iterating through factors"""
    if n < 0:
        return -1
    zeros = 0

    # To count the number of times n! is divisible by 2 and 5
    twos_count = 0 
    fives_count = 0

    # Iteratively count for each factor in n!
    for i in range(2, n+1):
        while (i % 2) == 0:
            twos_count += 1
            i //= 2
        while (i % 5) == 0:
            fives_count += 1
            i //= 5

        # Count the number of times 2 and 5 divides i, add to zeros
        while fives_count and twos_count:  # counts > 0
            zeros += 1
            fives_count -= 1
            twos_count -= 1

    return zeros
            
if __name__ == '__main__':
    main(sys.argv)
