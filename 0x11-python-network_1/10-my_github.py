#!/usr/bin/python3
"""script that takes github credentials and uses GitHub API
to display id
"""
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    try:
        response = requests.get(url, auth=(user, password))
        response.raise_for_status()
        print(response.json().get('id'))
    except requests.exceptions.RequestException as e:
        print("None")
