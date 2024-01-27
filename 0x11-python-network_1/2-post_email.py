#!/usr/bin/python3
""" post email """
from urllib import request
from urllib import parse
import sys

if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    data = parse.urlencode(value).encode('ascii')
    handler = request.Request(sys.argv[1], data)
    with request.urlopen(handler) as res:
        page = res.read().decode('utf-8')
        print(page)
