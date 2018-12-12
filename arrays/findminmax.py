import numpy as np

def getdata(n=10):
    data = n*np.random.rand(n)
    data = data.astype('int')
    return data,np.min(data),np.max(data)


data,gtmin,gtmax = getdata()

min = 1000000
max = 0
for x in data:
    if x > max: max = x
    if x < min: min = x

print("Ground truth: %d, %d" % (gtmin,gtmax))
print("Solution: %d, %d" % (min,max))
