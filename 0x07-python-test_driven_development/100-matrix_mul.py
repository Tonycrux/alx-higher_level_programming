#!/usr/bin/python3
"""Task 6 - Matrix Multiplication
This is our function to be tested
"""


def matrix_mul(m_a, m_b):
    """Multiples two matrices
    Args:
        m_a (list): first matrix
        m_b (list): second matrix
    Returns:
        Returns the product matrix
    Raises:
        TypeErrors and ValueErrors
    """
    te1 = " must be a list"
    te2 = " must be a list of lists"
    te3 = " should contain only integers or floats"
    te4a = "each row of "
    te4b = " must should be of the same size"
    ve1 = " can't be empty"
    ve2 = "m_a and m_b can't be multiplied"
    if type(m_a) is not list:
        raise TypeError("m_a" + te1)
    if type(m_b) is not list:
        raise TypeError("m_b" + te1)
    if not any(isinstance(row, list) for row in m_a):
        raise TypeError("m_a" + te2)
    if not any(isinstance(row, list) for row in m_b):
        raise TypeError("m_b" + te2)
    for l in m_a:
        if len(l) == 0:
            raise ValueError("m_a" + ve1)
    for l in m_b:
        if len(l) == 0:
            raise ValueError("m_b" + ve1)
    for row in m_a:
        for e in row:
            if not isinstance(e, (int, float)):
                raise TypeError("m_a" + te3)
    for row in m_b:
        for e in row:
            if not isinstance(e, (int, float)):
                raise TypeError("m_b" + te3)
    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError(te4a + "m_a" + te4b)
    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError(te4a + "m_b" + te4b)
    if len(m_a[0]) != len(m_b):
        raise ValueError(ve2)
    new = []
    for ar in m_a:
        nr = []
        for c in range(len(m_b[0])):
            nr.append(sum(a * b for a, b in zip(ar, list(r[c] for r in m_b))))
        new.append(nr)
    return new
