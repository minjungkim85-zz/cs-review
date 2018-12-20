# Given 3 numbers {1, 3, 5}, we need to tell
# the total number of ways we can form a number 'N'
# using the sum of the given three numbers.
# (allowing repetitions and different arrangements).
# https://www.geeksforgeeks.org/solve-dynamic-programming-problem/
#
# At any given point in time, I can only
# add the values from the data (1, 3, or 5).
#
# How many ways to get to state(8)?
# state(8): state(7) + 1
# state(8): state(5) + 3
# state(8): state(3) + 5
#
# |state(8)| = |state(7)| + |state(5)| + |state(3)|
#
# How many ways to get to state(7)?
# state(7): state(6) + 1
# state(7): state(4) + 3
# state(7): state(2) + 5
#
# |state(7)| = |state(6)| + |state(4)| + |state(2)|
#
# etc.

data = [1,3,5]
goal = 6

def getcardinality(data,goal):
    d = {}
    def cardn(n):
        # base case
        if n < 0:
            return 0
        elif n == 0:
            return 1

        # general
        if n in d:
            return d.get(n)
        else:
            c = cardn(n-data[0])+cardn(n-data[1])+cardn(n-data[2])
            d[n] = c
            return c

    d[goal] = cardn(goal)
    return d[goal]

print(getcardinality(data,goal))
