"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import itertools

def isPalindrome(n)->bool:
    n = str(n) # Cast to String to iterate over digits
    return n == n[::-1] # n equals reversed n?

def getLargestPalindrome():
    factors = [i for i in range(999, 99, -1)]
    factors = itertools.combinations(factors, 2)
    palindromes = set()
    for a,b in factors:
        n = a*b
        if isPalindrome(n):
            palindromes.add(n)
    return max(palindromes)

print(getLargestPalindrome())