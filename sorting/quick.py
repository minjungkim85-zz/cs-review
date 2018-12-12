import numpy as np
x = np.random.permutation(range(20))

def sort(x):
    print(x)
    if len(x) <= 1:
        # Base case: list of one item is already "sorted"
        return x
    elif len(x) == 2:
        if x[0] > x[1]:
            x = [x[1],x[0]]
        return x
    else:
        left  = []
        right = []
        pivot = x[-1]

        for xi in x[:-1]:
            if xi < pivot: left.append(xi)
            else:          right.append(xi)

        left  = sort(left)
        right = sort(right)

        x = left + [pivot] + right

        return x

print(sort(x))
