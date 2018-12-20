# Fibonacci sequence

# Using recursion
def fib1(n):
    if n <= 1:
        return n
    else:
        return fib1(n-1) + fib1(n-2)

# Using dynamic programming: memoization (top-down)
def fib2(n):
    fibdict = {0:0, 1:1} # Base case

    def fib(n):
        if n in fibdict:
            return fibdict[n]
        else:
            fibdict[n] = fib(n-1) + fib(n-2)
            return fibdict[n]

    return fib(n)

# Using dynamic programming: tabulation (bottom-up)
def fib3(n):
    if n==0:
        return 0
    else:
        prev = 0
        curr = 1

        for _ in range(n-1):
            fib  = prev + curr
            prev = curr
            curr = fib

        return fib

n = 6
print(fib1(n))
print(fib2(n))
print(fib3(n))
