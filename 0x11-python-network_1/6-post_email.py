#!/usr/bin/python3
"""
POST request to the passed URL with the email as a parameter
"""
import requests
from sys import argv


if __name__ == '__main__':
    url = sys.argv[1]
    value = {"email" : sys.argv[2]}
    r =  requests.post("url", data = value)
    print(r.text)
