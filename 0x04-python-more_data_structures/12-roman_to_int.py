#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    diclist = list(dic)
    store = 0
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0
    for r in roman_string:
        for x in diclist:
            if x == r:
                store = store + dic.get(x)
    return store
