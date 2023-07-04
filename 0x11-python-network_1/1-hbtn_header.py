#!/usr/bin/python3
""" script that sends request to url and displays
X-Request-Id variable found in response header
"""
from urllib.request import urlopen
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')

    if x_request_id is not None:
        print(x_request_id)
