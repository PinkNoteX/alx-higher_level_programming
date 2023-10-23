#!/usr/bin/python3
def safe_print_division(a, b):
    x = 0
    try:
        x = a / b
    except TypeError:
        x = None
    except ZeroDivisionError:
        x = None
    finally:
        print(f"Inside result: {x}")
    return (x)
