#!/usr/bin/python3
""" not so empty rectangle"""


class Rectangle:
    """ define rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ width and height intialize"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.width == 0 or self.height == 0:
            return astr
        for x in range(self.height):
            astr += str(self.print_symbol) * self.width + '\n'
        return astr[:-1]

    def __repr__(self):
        """repr"""
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """del"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compare rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2
