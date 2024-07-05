#!/usr/bin/python3
"""
Python script
- fetches https://alx-intranet.hbtn.io/status
- You must use the package url
"""
from urllib import request

if __name__ == "__main__":
    req = request.Request('https://alx-intranet.hbtn.io/status')
    with request.urlopen(req) as response:
        html = response.read()
    print("- Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
    print("\t- utf8 content:", html.decode(encoding='utf-8'))
