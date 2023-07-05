#!/usr/bin/python3
""" list 10 commits from most recent to oldest of repo
"""
import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    res = requests.get(url)
    data = res.json()
    count = 1
    for item in data:
        if count > 10:
            break
        print(f"{item['sha']}: {item['commit']['author'].get('name')}")
        count += 1
