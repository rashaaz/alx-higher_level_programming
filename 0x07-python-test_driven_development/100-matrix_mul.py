#!/usr/bin/python3
"""Module for matrix multiplication."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        list: The result of multiplying m_a by m_b.

    Raises:
        TypeError: If m_a or m_b is not a list, if any element within m_a
                   or m_b is not a list, or if the elements are not integers
                   or floats.
        ValueError: If m_a or m_b is empty, if the rows within m_a or m_b are
                    not of the same size, or if the number of columns in m_a
                    is not equal to the number of rows in m_b.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    m_a_pp = False
    m_b_pp = False
    m_a_ee = False
    m_b_ee = False
    m_a_nn = False
    m_b_nn = False
    for ii in m_a:
        if not isinstance(ii, list):
            raise TypeError("m_a must be a list of lists")
        if len(ii) != len(m_a[0]):
            m_a_ee = True
        for jj in ii:
            if not isinstance(jj, (int, float)):
                m_a_nn = True

    for ii in m_b:
        if not isinstance(ii, list):
            raise TypeError("m_b must be a list of lists")
        if len(ii) != len(m_b[0]):
            m_b_ee = True
        for jj in ii:
            if not isinstance(jj, (int, float)):
                m_b_nn = True

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    if m_a_nn:
        raise TypeError("m_a should contain only integers or floats")

    if m_b_nn:
        raise TypeError("m_b should contain only integers or floats")

    if m_a_ee:
        raise TypeError("each row of m_a must should be of the same size")

    if m_b_ee:
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    es = [[] for g in range(len(m_a))]

    for g in range(len(m_a)):
        for h in range(len(m_b[0])):
            d = 0
            for kk in range(len(m_b)):
                d += m_a[g][kk] * m_b[kk][h]
            es[g].append(d)

    return es


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
