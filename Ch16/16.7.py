#!/bin/python

import sys

def main(argv):
    a = int(argv[1])
    b = int(argv[2])
    if greater(a, b) == a:
        print('a=%d > b=%d' % (a, b))
    else:
        print('a=%d < b=%d' % (a, b))


def greater(a, b):
"""Returns the greater of two ints without if-else comparisons"""
    k = b - a
    shiftcount = max(sys.getsizeof(a), sys.getsizeof(b)) - 1
    k = logical_rshift(k, shiftcount)
    return (k * a) ^ b ^ (k * b)

def logical_rshift(a, n):
    return (a >> n) if a >= 0 else ((a + (1 << sys.getsizeof(a))) >> n)
            
if __name__ == '__main__':
    main(sys.argv)
