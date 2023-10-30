#!/usr/bin/python3
""" not so empty rectangle"""


class Rectangle:
    """ define rectangle"""
    def __init__(self, width=0, height=0):
        """ width and height intialize"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """ get height"""
        return self.__height

    @property
    def width(self):
        """ get width"""
        return self.__width

    @height.setter
    def height(self, value):
        """ height setter"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @width.setter
    def width(self, value):
        """ width setter"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def perimeter(self):
        """ gets perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def area(self):
        return self.width * self.height

    def __str__(self):
        """ string """
        astr = ""
        if self.width == 0 ir self.height == 0:
            return astr
        for x in range(self.height):
            astr += '#' * self.width + '\n'
        return astr[:-1]
