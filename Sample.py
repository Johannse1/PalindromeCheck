def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)


def factorial_iterative(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact


# print(factorial_recursive(6))
print(factorial_iterative())
