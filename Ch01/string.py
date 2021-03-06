# Chapter 1 of CtCI

def problem1_structures(string):
    """Determine if string has unique chrs using extra data structure"""
    # Runs in O(n) time, with O(n) space
    seenchars = set()
    for char in string:
        if char in seenchars:
            return False
        else:
            seenchars.add(char)
    return True

def problem1_no_structures(string):
    """Determine if string has unique chrs w/o extra data structures"""
    # Runs in O(n^2) time, with O(1) space
    for i, char1 in enumerate(string):
        for char2 in string[i+1:]:
            if char1 == char2:
                return False
    return True


## Test ## --------------------------------------------------------------------
import random

def gen_test_str(n=50):
    """Returns randomly generated string of length n"""
    return ''.join([chr(random.randint(65, 122)) for _ in range(n)])

def problem1_structures_test():
    """Tests problem 1 with data structures allowed"""
    s = gen_test_str(10)
    print("String: %s" % s)
    print("Is Unique: " + str(problem1_structures(s)))

def problem1_no_structures_test():
    """Tests problem 1 with data structures not allowed"""
    s = gen_test_str(10)
    print("String: %s" % s)
    print("Is Unique: " + str(problem1_no_structures(s)))
