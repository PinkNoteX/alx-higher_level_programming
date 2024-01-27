#!/usr/bin/python3
"""display the value of the x-request-id var in header"""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as res:
    print(res.getheader('X-Request-Id'))
