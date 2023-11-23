#!/usr/bin/python3
"""Module to perform matrix"""


def matrix_divided(matrix, div):
    """Divide each element in the matrix by the given number.

    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int or float): The number to divide each element in the matrix by.

    Returns:
        list: A new matrix with each element rounded to 2 decimal places after division.

    Raises:
        TypeError: If div is not a number or if matrix is not a valid matrix.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
