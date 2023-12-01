#!/usr/bin/python3
""" Script that send a POST request to the URL
    and to an URL with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    data = {'q': ""}

    try:
        data['q'] = sys.argv[1]
    except IndexError:
        pass

    req = requests.post('http://0.0.0.0:5000/search_user', data)

    try:
        json_o = req.json()
        if not json_o:
            print("No result")
        else:
            print(f"[{json_o.get('id')}] {json_o.get('name')}")
    except ValueError:
        print("Not a valid JSON")
