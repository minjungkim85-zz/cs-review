# Factorial

# Using tabulation
def fact1(n):
    if n==0 or n==1:
        return 1

    flist = [None] * n
    flist[0] = 1
    for i in range(1,n):
        flist[i] = flist[i-1]*(i+1)

    return flist[-1]

# Using memoization
def fact2(n):
    flist = {0:1,1:1}
    def fact(n):
        if n in flist:
            return flist[n]
        else:
            flist[n] = fact(n-1) * n
            return flist[n]

    flist[n] = fact(n)
    return flist[n]

n = 5
print(fact1(n))
print(fact2(n))
