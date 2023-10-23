#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except Exception as Error:
        sys.stderr.write("Exception: {}\n".format(Error))
        return (False)
    else:
        return (True)
