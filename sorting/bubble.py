import numpy as np

data   = np.random.permutation(range(10))
sorted = False
print("Init" + ": "+ np.array2string(data))

while not sorted:
    sorted = True

    for i in range(0,len(data)-1):
        if data[i] > data[i+1]:
            # integer swap
            data[i]   = data[i] + data[i+1]
            data[i+1] = data[i] - data[i+1]
            data[i]   = data[i] - data[i+1]

            sorted = False

        print(str(i+1) + ": "+ np.array2string(data))
