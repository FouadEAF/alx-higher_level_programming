#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    listKeys = list(a_dictionary.keys())
    for v in listKeys:
        if value == a_dictionary.get(v):
            del a_dictionary[v]
    return (a_dictionary)
