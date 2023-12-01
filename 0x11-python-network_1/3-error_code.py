#!/usr/bin/python3
""" Script that take in a URL, send a request and display
    the value of the X-Request-Id variable found in the header
"""
from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except error.HTTPError as err:
        print(f'Error code: {err.code}')
