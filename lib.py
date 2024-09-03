# 2.1
def sum_up_to(n: int) -> int:
    if n == 0:
        return 0
    else:
        return sum_up_to(n - 1) + n

# 2.2
def sum_even(n: int) -> int:
    if n == 0:
        return 0
    else:
        if n % 2 == 0:
            # Is even
            return sum_even(n - 1) + n
        else:
            # Is odd so skip
            return sum_even(n - 1)

# 2.3 Write a function sum_between(m: int, n: int) -> int that returns the sum of the numbers between m and n.
def sum_between(m: int, n: int) -> int:
    if n == m:
        return m
    else:
        return sum_between(m, n-1) + n

# 2.4 Write a function factorial(n: int) -> int that returns the factorial of n.
def factorial(n: int) ->int:
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n

# 2.5 Write a function double_factorial(n: int) -> int that returns n!!
def double_factorial(n: int) -> int:
    if n <= 1:
        return 1

    return double_factorial(n - 2) * n


# 2.6 Write a function logarithm(n: int) -> int that returns the integer base-2 logarithm of n.
def logarithm(n: int) -> int:
    if n <= 0:
        raise ValueError("Input must be a positive integer")

    result = 0
    while n > 1:
        n //= 2
        result += 1

    return result
