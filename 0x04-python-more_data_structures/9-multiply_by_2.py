#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDic = a_dictionary.copy()
    listKey = list(newDic.keys())
    for i in listKey:
        newDic[i] *= 2
    return (newDic)
