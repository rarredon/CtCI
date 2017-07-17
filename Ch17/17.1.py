#!/bin/python
import sys


def main(argv):
    a = int(argv[1])
    b = int(argv[2])

    print('a=%d, b=%d ==> a+b=%d' % (a, b, add(a, b)))


def add(a, b):
    """Add two numbers a and b without arithmetic ops"""
    result = 0
    carry_i = 0

    # Iterate over each bit in the int
    for i in range(sys.getsizeof(int)):
        # Get the ith bits in a and b
        a_i = (a & (1 << i)) >> i
        b_i = (b & (1 << i)) >> i

        # ith bit in the result
        result_i = a_i ^ b_i ^ carry_i

        # The carry, used for the next iteration
        carry_i = a_i & b_i | carry_i & (a_i | b_i)
        result |= (result_i << i)
    return result


if __name__ == '__main__':
    main(sys.argv)
