#!/usr/bin/python3
""" This module contain a function that return the nbr of line of a text file
"""


def number_of_lines(filename=""):
    """ Function that read from a file and print its number of lines

    Args:
        filename: filename

    Raises
        Exception: when the file can be opened

    """
    nbr_lines = 0
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            nbr_lines += 1
    return nbr_lines
