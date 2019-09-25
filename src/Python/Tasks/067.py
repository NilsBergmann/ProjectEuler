"""
Project Euler Problem 67
========================

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

                                    3
                                   7 4
                                  2 4 6
                                 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not
possible to try every route to solve this problem, as there are 2^99
altogether! If you could check one trillion (10^12) routes every second it
would take over twenty billion years to check them all. There is an
efficient algorithm to solve it. ;o)
"""

import os
path = os.getcwd() + "..\\..\\..\\Data\\067.txt"
with open(path) as file:
    data = [[int(i) for i in line.split()] for line in file]

sums = list()
for i in range(len(data)):
    sums.append([0]*(i+1))

for row, line in enumerate(data):
    for column, value in enumerate(line):
        leftOption = 0 if column == 0 else sums[row-1][column-1]
        rightOption = 0 if column >= len(sums[row-1]) else sums[row-1][column]
        sums[row][column] = value + max(leftOption, rightOption)

print(max(sums[-1]))
