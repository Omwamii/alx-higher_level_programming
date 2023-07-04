#!/usr/bin/python3
""" script takes URL and email and sends POST request to URL
with email as param, displays body of response header
"""
from urllib.parse import urlencode
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {
            "email": email
            }
    request = urllib.request.Request(url, urlencode(data).encode('utf-8'))
    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
        print(body)
