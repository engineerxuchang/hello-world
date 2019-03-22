#!/usr/bin/python3

import sys

# iterative method
def fib_iteratively(n):
    result, next_item = 0, 1
    i = 1
    while i <= n:
        result, next_item = next_item, result + next_item
        i += 1

    return result

def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("The input is not a number.")

    if n < 0:
        raise ValueError("The input value must be inter!")

    result = []

    for i in range(n):
        result.append(fib_iteratively(i))

    return result


f = fibonacci(10)
print(f)