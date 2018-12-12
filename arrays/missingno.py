import numpy as np # only for data generation

def getdata(maxn=10):
    data = np.random.permutation(range(maxn))
    gt   = data[-1] # save ground truth
    data = data[:-1]

    return data,gt


n = 100
data,gt = getdata(n)
plist = [0]*n

for x in data:
    plist[d] = 1

for i,p in enumerate(plist):
    if p==0:
        break

print("Ground truth: %d." % gt)
print("Solution: %d."  % i)
