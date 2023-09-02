#!/usr/bin/python3
""" This module is contient a function that divide the numbers of a matrix
"""


def matrix_divided(matrix, div):
    """ Function that divide the numbers of a matrix

    Args:
        matrix: list of a lists of integers/floats
        div: number which divides the matrix

    Returns:
        A new matrix with the result of the division

    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size
        ZeroDivisionError: If div is zero
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msgType = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msgType)

    len_ele = 0
    msgSize = "Each row of the matrix must have the same size"

    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(msgType)

        if len_ele != 0 and len(elems) != len_ele:
            raise TypeError(msgSize)

        for num in elems:
            if not type(num) in (int, float):
                raise TypeError(msgType)

        len_ele = len(elems)

    mx = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (mx)
