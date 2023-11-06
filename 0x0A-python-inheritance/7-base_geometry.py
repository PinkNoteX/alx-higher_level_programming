#!/usr/bin/python3
""" not so empty class BaseGeometry """


class BaseGeometry:
    """ BaseGeometry class """
    def __init__(self):
        """ init """
        pass

    def area(self):
        """ area """
        raise Exception('area() is not implemented')
    def integer_validator(self, name, value):
        """ validate int """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
