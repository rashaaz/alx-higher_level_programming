#!/usr/bin/python3
"""This module provides a function for matrix multi using NumPy."""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy's matmul function.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The result of the matrix multiplication.

    Raises:
        ValueError: If the matrices cannot be multiplied.
        TypeError: If the matrices are not valid
        (not lists of lists, contain non-numeric elements,
                   rows of different sizes).
    """
    return numpy.matmul(m_a, m_b)
