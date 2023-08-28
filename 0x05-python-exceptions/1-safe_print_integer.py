#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{}".format(value))
    except ValueError:
        return (False)
    else:
        return (True)
