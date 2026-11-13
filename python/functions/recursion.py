
def factorial(n):
    if n == 0 or n == 1:
        print(n)
    else:
        n * factorial(n-1)

result = factorial(4)
print(result)