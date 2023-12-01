#!/usr/bin/python3
""" Script that shows the last 10 commits of a repository in GitHub """
import requests
import sys

if __name__ == "__main__":
    try:
        repo = sys.argv[1]
        owner = sys.argv[2]

        url = f'https://api.github.com/repos/{owner}/{repo}/commits'
        req = requests.get(url)
        req.raise_for_status()

        json_o = req.json()

        for i in range(min(10, len(json_o))):
            sha = json_o[i].get('sha')
            author_name = json_o[i].get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
