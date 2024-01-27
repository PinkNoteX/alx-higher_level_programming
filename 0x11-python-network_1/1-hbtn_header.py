#!/usr/bin/python3
# display the value of the x-request-id var in header of the response

from urllib import request
import sys

with request.urlopen(sys.argv[1]) as res:
    print(res.getheader('X-Request-Id'))
