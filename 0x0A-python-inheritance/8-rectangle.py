#!/usr/bin/python3
""" not so empty classes"""


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


class Rectangle(BaseGeometry):
    """creates rectangle class"""

    def __init__(self, width, height):
        """ init """
        if not super().integer_validator("height", height):
            self.__height = height
        if not super().integer_validator("width", width):
            self.__width = width
