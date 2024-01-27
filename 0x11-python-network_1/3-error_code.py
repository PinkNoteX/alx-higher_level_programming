#!/usr/bin/python3
# send req and display body of response

from urllib import request, parse, error
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as res:
            page = res.read().decode('utf-8')
            print(page)
    except error.URLError as x:
        print("Error code: {}".format(x.code))
