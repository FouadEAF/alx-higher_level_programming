#!/usr/bin/python3
""" This module containt Function that returns True/False
"""


def is_same_class(obj, a_class):
    """ Function that returns True/False if object is a type of a_class

    Args:
        obj: object
        a_class: class type

    Returns:
        True if type of obj is a_class
        False, otherwise
    """
    return type(obj) is a_class
