#!/usr/bin/python3
#fetch https://alx-intranet.hbtn.io/status

from urllib import request

with request.urlopen("https://alx-intranet.hbtn.io/status") as res:
    page = res.read()
    print('Body response:')
    print('\t- type: {}'.format(type(page)))
    print('\t- content: {}'.format(page))
    print('\t- utf8 content: {}'.format(page.decode('utf-8')))
