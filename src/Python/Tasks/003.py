"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
def maxFactor(n:int)->list:
    factors = []
    factor = 2
    while factor ** 2 <= n:
        while n % factor == 0:
            n /= factor
            factors.append(factor)
        factor += 1
    # print(factors, n)
    if n > 1:
        return int(n)
    return int(max(factors))

print(maxFactor(600851475143))