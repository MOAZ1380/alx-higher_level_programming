#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays 
the body of the response (decoded in utf-8).
You have to manage urllib.error.HTTPError exceptions and print:
Error code: followed by the HTTP status code
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    req_uest = urllib.request.Request(url)
    try:
        with request.urlopen(req_uest) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as s:
        print("Error code: ", s.code)
