#!/usr/bin/python3
""" Function that find a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    mid = int(length / 2)
    l_int = list_of_integers

    if mid - 1 < 0 and mid + 1 >= length:
        return l_int[mid]
    elif mid - 1 < 0:
        return l_int[mid] if l_int[mid] > l_int[mid + 1] else l_int[mid + 1]
    elif mid + 1 >= length:
        return l_int[mid] if l_int[mid] > l_int[mid - 1] else l_int[mid - 1]

    if l_int[mid - 1] < l_int[mid] > l_int[mid + 1]:
        return l_int[mid]

    if l_int[mid + 1] > l_int[mid - 1]:
        return find_peak(l_int[mid:])

    return find_peak(l_int[:mid])
