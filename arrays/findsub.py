# Find the subarray whose sum matches the desired value
# https://www.geeksforgeeks.org/find-subarray-with-given-sum/
data = [1, 4, 20, 3, 10, 5]
desiredsum = 33 # desired sum

print("Init: " + ''.join(str(data)))
print("Desired sum: %d.\r\n" % desiredsum)

# For each element in array
n = len(data)
result = (None,None)
i = 0
for i in range(n):
    if i == 0:
        currsum = data[i]
    else:
        currsum = currsum + data[i]

    print("%d: sum(%s) = %d" % (i, ''.join(str(data[:i+1])),currsum))


    # if my current sum is greater than desired sum,
    # repeatedly remove elements until either I get the
    # desired sum or drop below the desired sum.
    for j in range(i):
        if currsum > desiredsum:
            currsum = currsum - data[j]

            print("%d: sum(%s) = %d" % (i, ''.join(str(data[j+1:i+1])),currsum))

        if currsum == desiredsum:
            result = (j+1,i)
            break

print("\r\n")
if result[0] is not None:
    subarr = data[result[0]:result[1]]
    print("Solution:\r\ndata[%d:%d]" % (result) + " = " + ''.join(str(subarr)) + " = "  + str(sum(subarr)))
else:
    print("Solution: None.")
