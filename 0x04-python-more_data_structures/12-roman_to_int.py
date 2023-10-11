#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    store = 0
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0
    for r in range(len(roman_string)):
        if dic.get(roman_string[r], 0) == 0:
            return 0
        if r != (len(roman_string) - 1) and\
                dic[roman_string[r]] < dic[roman_string[r + 1]]:
            store = store + dic[roman_string[r]] * -1
        else:
            store = store + dic[roman_string[r]]
    return store
