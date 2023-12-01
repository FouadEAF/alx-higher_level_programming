#!/usr/bin/python3
""" Script that send a request to the URL and display the value
    of a variable in the response header
"""
import requests
import sys


if __name__ == "__main__":
    try:
        req = requests.get(sys.argv[1])
        print(req.headers['X-Request-Id'])
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
