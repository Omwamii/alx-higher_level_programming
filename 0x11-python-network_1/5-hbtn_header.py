#!/usr/bin/python3
""" script takes URL, sends request and displays value of
X-Request-Id in response header
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    info = response.headers.get('X-Request-Id')
    if info:
        print(info)
