#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not roman_string or not isinstance(roman_string, str)):
        return 0

    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_num.keys())
    num = 0
    last_rom = 0
    list_num = [0]

    for ch in roman_string:
        for r in list_keys:
            if r == ch:
                if rom_num.get(ch) <= last_rom:
                    num += to_subtract(list_num)
                    list_num = [rom_num.get(ch)]
                else:
                    list_num.append(rom_num.get(ch))
                last_rom = rom_num.get(ch)
    num += to_subtract(list_num)
    return (num)

def to_subtract(list_num):
    subtract = 0
    maxList = max(list_num)
    for n in list_num:
        if maxList > n:
            subtract += n
    return (maxList - subtract)
