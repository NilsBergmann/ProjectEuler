"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""
n = 1
__check_list = [11, 13, 14, 16, 17, 18, 19, 20]

def divides(n, r):
    for i in __check_list:
        if n % i != 0:
            return False
    return True

def solve():
    n = 2520
    while True:
        if not divides(n, 20):
            n += 2520
        else:
            return n

print(solve())