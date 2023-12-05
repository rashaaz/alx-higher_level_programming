#!/usr/bin/python3
"""Function to generate Pascal's triangle up to a given number"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list of lists of int: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    tri = [[1]]
    while len(tri) != n:
        trian = tri[-1]
        tp = [1]
        for j in range(len(trian) - 1):
            tp.append(trian[j] + trian[j + 1])
        tp.append(1)
        tri.append(tp)
    return tri
