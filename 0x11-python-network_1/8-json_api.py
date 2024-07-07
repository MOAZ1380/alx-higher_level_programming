#!/usr/bin/python3
"""
Module  sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]
    data = {'q' : q}
    r = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        json_data = r.json()
        if bool(json_data) is False:
            print("No result")
        else:
            print("[{}] {}".format(json_data['id'], json_data['name']))
    except:
        print("Not a valid JSON")
