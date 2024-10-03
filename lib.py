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
        return sum_between(m, n - 1) + n


# 2.4 Write a function factorial(n: int) -> int that returns the factorial of n.
def factorial(n: int) -> int:
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


# 2.7 GCD
def gcd(m: int, n: int) -> int:
    """
    Returns greates common divisor
    >>> gcd(2,4)
    2
    """
    if m == n:
        return m

    if m < n:
        return gcd(m, n - m)
    else:
        return gcd(m - n, n)


# 2.10
def print_multiples() -> None:
    """
    Prints multiples of 7 up to but not including 500
    """
    print_multiples_general(7, 500)


def print_multiples_general(k: int = 7, n: int = 500) -> None:
    """
    Prints multiples of k up to but not including n
    """

    def _print_multiples(c: int) -> None:
        if c * k < n:
            print(c * k)
            return _print_multiples(c + 1)

    return _print_multiples(1)


# 2.11
def count_divisors(n: int) -> int:
    """
    Counts the number of divisors of n
    """

    def _count_divisors(c: int) -> int:
        if c == 1:
            return 1
        elif n % c == 0:
            return _count_divisors(c - 1) + 1
        else:
            return _count_divisors(c - 1)

    return _count_divisors(n)


# 3.2
def count(x: any, v: list) -> int:
    """
    Count the number of occurences of X in list V
    """
    if v == []:
        return 0

    test = v.pop()

    if test == x:
        return count(x, v) + 1
    else:
        return count(x, v)


# 3.4
def subset(v: list, w: list) -> bool:
    """
    Yapper yapper docstring
    """
    if v == []:
        return True

    test = v.pop()
    if count(test, w.copy()) == 0:
        return False
    else:
        return subset(v, w)
