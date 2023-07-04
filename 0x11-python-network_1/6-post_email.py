#!/usr/bin/python3
""" script sends POST request with email and display response
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {
            "email": email
            }
    res = requests.post(url, data)
    print(res.text)
