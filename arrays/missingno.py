# Assume that values are consecutive integers in [1.. n].

import numpy as np # only for data generation

def getdata(maxn, startfrom):
    data = np.random.permutation(range(maxn))
    if startfrom==1:
        data = data+1
    gt   = data[-1] # save ground truth
    data = data[:-1]
    data = data.tolist()
    return data,gt

def method1(data):

    # Use data values as position for a second array.
    maxn  = len(data)+1
    plist = [0]*maxn
    for x in data:
        plist[x] = 1

    for i,p in enumerate(plist):
        if p==0:
            break
    return i

def method2(data):
    # Calculate expected total assuming no missing number.
    maxn  = len(data)+1
    total = maxn * (maxn+1) / 2

    # Remove data one by one.
    for x in data:
        total = total-x

    # Remaining value = missing number.
    x = total

    return x

def method3(data):

    # XOR of data
    xor1 = data[0]

    for x in data[1:]:
        xor1 = xor1 ^ x

    maxn = len(data)+1
    xor2 = 1
    for x in range(2, maxn+1):
        xor2 = xor2 ^ x

    result = xor1^xor2
    return result



n = 5
data,gt = getdata(n, startfrom=0)
print("For data starting from 0: ")
print("Init: " + ''.join(str(data)))

i1 = method1(data)
print("Ground truth: %d." % gt)
print("Solution: %d."  % i1)
print("\r\n")


data,gt = getdata(n, startfrom=1)
print("For data starting from 1: ")
print("Init: " + ''.join(str(data)))

i2 = method2(data)
i3 = method3(data)
print("Ground truth: %d." % gt)
print("Solution: %d, %d."  % (i2,i3))
