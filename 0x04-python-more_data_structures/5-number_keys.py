#!/usr/bin/python3
def number_keys(a_dictionary):
    nmr = 0
    listKey = list(a_dictionary.keys())
    for i in listKey:
        nmr += 1
    return (nmr)
