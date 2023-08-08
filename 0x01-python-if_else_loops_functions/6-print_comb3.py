#!/usr/bin/python3
for nmr in range(0, 90):
    if nmr % 10 > nmr / 10:
        if nmr != 89:
            print("{:02d}, ".format(nmr), end='')
        else:
            print("{:02d}".format(nmr))
