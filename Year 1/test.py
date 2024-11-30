def factorial(n):
    if n == 0: #BASE CASE
        return 1
    return n * factorial(n-1)

print(factorial(10))