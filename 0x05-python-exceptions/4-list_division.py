#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    alist = []
    m = 0
    for r in range(list_length):
        m = 0
        try:
            m = my_list_1[r] / my_list_2[r]
        except IndexError:
            print("out of range")
            m = 0
        except ValueError:
            print("wrong type")
            m = 0
        except TypeError:
            print("wrong type")
            m = 0
        except ZeroDivisionError:
            print("division by 0")
            m = 0
        finally:
            alist.append(m)
    return (alist)
