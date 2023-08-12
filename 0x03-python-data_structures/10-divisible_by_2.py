#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    check_divisible = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            check_divisible.append(True)
        else:
            check_divisible.append(False)
    return (check_divisible)
