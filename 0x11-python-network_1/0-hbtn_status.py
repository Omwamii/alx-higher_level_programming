#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status
"""


if "__name__" == "__main__":
    from urllib.request import urlopen

    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as response:
        body = response.read()
        utf8_content = body.decode('utf-8')
        print('Body response:')
        print(f'\t- type: {type(body)}')
        print(f'\t- content: {body}')
        print(f'\t- utf8 content: {utf8_content}')
