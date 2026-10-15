from functools import cache
from math import sqrt


def fibonacci(n: int) -> list[int]:
    """Returns a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


@cache
def hof(a: int) -> int:
    """Computes the Hofstadter value for a given input."""
    if a <= 2:
        return 1
    return hof(a - hof(a - 1)) + hof(a - hof(a - 2))


def sqr(operand: int | float) -> int | float:
    """Calculates the square of the specified parameter, even if it is a float."""
    return operand * operand


def pi(depth: int) -> float:
    """Calculates the value of pi using the method of inscribed and circumscribed polygons."""
    if depth < 4:
        raise ValueError("depth must be at least 4")

    n = 4
    while n <= depth:
        lower = 0.0
        for i in range(1, n):
            lower += sqrt(1 - sqr(i / n)) / n
        upper = lower + 1 / n
        n *= 2
    return (lower + upper) * 2
