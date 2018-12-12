import numpy as np

def getdata(n):
    data = n*np.random.rand(n)
    data = data.astype('int')

    unique,counts = np.unique(data,return_counts=True)
    ints = np.arange(n)
    dups = unique[counts > 1]

    return data,dups

n = 50
data,gt = getdata(n)

counts = [0]*n
dups = []

for x in data:
    if counts[d] == 1:
        dups.append(d)
    counts[d] += 1

dups.sort()

print("Ground truth:")
print(gt)

print("Solution: ")
print(dups)
