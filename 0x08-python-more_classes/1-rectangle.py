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
