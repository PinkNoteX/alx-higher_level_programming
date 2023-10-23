#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    if my_list:
        for r in range(x):
            try:
                print("{}".format(my_list[r]), end='')
                counter = counter + 1
            except IndexError:
                break
    print("")
    return(counter)
