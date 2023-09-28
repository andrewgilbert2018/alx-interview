#!/usr/bin/python3
"""
a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer
Pascal Triangle Algorithm in python3
"""


def pascal_triangle(n):
    """
    Creates a pascal triangle

    @n: level of the pascal triangle

    Return: list of list
    """
    result = []
    if n <= 0:
        return result

    last = [1]
    for i in range(1, n + 1):
        actual = [1] * i
        actual = [last[index - 1] + last[index] if index > 0 and
                  index < len(actual) - 1 else 1 for index,
                  value in enumerate(actual)]
        last = actual
        result.append(actual)
    return result
