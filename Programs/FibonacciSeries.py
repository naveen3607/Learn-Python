# Fibonacci Series
n = int(input("Enter the total number of values in the series,n = "))


def fibonacci(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(f"The sum of the two preceding numbers is", fibonacci(n))
