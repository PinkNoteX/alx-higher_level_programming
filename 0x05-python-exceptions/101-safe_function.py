#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        x = fct(*args)
    except Exception as Error:
        sys.stderr.write("Exception: {}\n".format(Error))
        x = None
    return (x)
