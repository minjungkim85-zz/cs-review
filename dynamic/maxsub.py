# Find the subarray whose sum is the largest possible
# ("maximum contiguous sum") using Kadane's algorithm

import numpy as np
import sys


n = 5
# data = (n+1) * (np.random.rand(n)-.5) // 1
# data = data.astype('int').tolist()

data = [-4, 3, 2, -1]

print("Init: " + ''.join(str(data)))

maxglobal = None
maxlocal  = None
maxlocalarr = []

for i in range(4):
    curr = data[i]
    if i==0:
        maxlocal = curr
    else:
        maxlocal = max(curr,curr+maxlocal)

    print("%d: maxlocal: %d" % (i,maxlocal))
    maxglobal = max(maxglobal,maxlocal)

print("Max contiguous sum: %d" % maxglobal)
