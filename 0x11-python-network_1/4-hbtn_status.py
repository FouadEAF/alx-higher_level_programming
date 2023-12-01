#!/usr/bin/python3
""" Script that fetche an URL with requests package """
import requests


if __name__ == "__main__":
    req = requests.get('https://intranet.hbtn.io/status')
    txt = req.text

    print(f'Body response:\n\t- type: {type(txt)}\n\t- content: {txt}')
