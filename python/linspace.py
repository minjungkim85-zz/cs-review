# Generate n numbers in [x1, x2]
x0 = 0.5
x1 = 1.
n = 3

x = map(float,range(n+1))[:-1]
x = map(lambda x: (x1-x0)*x/(n-1) + x0, x)
print(x)
