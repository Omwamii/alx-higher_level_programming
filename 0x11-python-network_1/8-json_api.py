#!/usr/bin/python3
""" takes in a letter and sends POST request to
http://0.0.0.0:5000/search_user with the letter as param
"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) < 2:
        param = ""
    else:
        param = sys.argv[1]
    data = {"q": param}
    res = requests.post(url, data=data)
    try:
        res = res.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if res:
            print(f"[{res['id']}] {res['name']}")
        else:
            print("No result")
