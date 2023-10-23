#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    alist = []
    m = 0
    for r in range(list_length):
        try:
            m = my_list_1[r] / my_list_2[r]
        except IndexError:
            print("out of range")
        except ValueError:
            print("wrong type")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            alist.append(m or 0)
    return (alist)
