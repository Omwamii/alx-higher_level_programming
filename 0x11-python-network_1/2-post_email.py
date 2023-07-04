#!/usr/bin/python3
""" script takes URL and email and sends POST request to URL
with email as param, displays body of response header
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import sys

url = sys.argv[1]
email = sys.argv[2]

data = urlencode({'email': email}).encode('utf-8')
request = Request(url, data=data, method='POST')
with urlopen(request) as response:
    body = response.read().decode('utf-8')
    print(body)
