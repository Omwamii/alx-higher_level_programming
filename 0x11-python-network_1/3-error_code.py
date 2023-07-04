#!/usr/bin/python3
""" takes URL , sends request and displays reponse body
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            utf8_content = response.read().decode('utf-8')
            print(utf8_content)
    except urllib.error.URLError as e:
        print(f"Error code: {e.code}")
