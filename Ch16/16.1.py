#!/bin/python
import sys

def main(argv):
    a, b = int(argv[1]), int(argv[2])
    print('Before swap: a=%d, b=%d' % (a, b))
    a, b = swap(a, b)
    print('After swap: a=%d, b=%d' % (a, b))

def swap(a, b):
    b = b-a
    a = a+b
    b = a-b
    return a, b

if __name__ == '__main__':
    main(sys.argv)
