#!/usr/bin/python3
""" This module is contient a function that print a square.
"""


def print_square(size):
    """ Function that print a square with the character #.

    Args:
        size: size of the square printed.

    Returns:
        No return.

    Raises:
        TypeError: If size is not an integer number.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
