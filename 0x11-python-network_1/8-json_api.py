#!/usr/bin/python3
""" requests """
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        val = sys.argv[1]
    else:
        val = ""
    req = requests.post("http://0.0.0.0:5000/search_user", data={'q': val})
    try:
        if req.json():
            print("[{}] {}".format(req.json().get('id'), req.json().get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
