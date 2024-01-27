#!/usr/bin/python3
""" requests """
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        v = sys.argv[1]
    else:
        v = ""
    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': v})
    try:
        if r.json():
            print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
