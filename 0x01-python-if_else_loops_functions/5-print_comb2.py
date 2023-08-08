#!/usr/bin/python3
for nmr in range(0, 100):
    if nmr != 99:
        print("{:02d}, ".format(nmr), end='')
    else:
        print("{:02d}".format(nmr))
