#!/usr/bin/python3
""" github """
import requests
from sys import argv

try:
    req = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(req.json().get('id'))
except Exception:
    print("None")
