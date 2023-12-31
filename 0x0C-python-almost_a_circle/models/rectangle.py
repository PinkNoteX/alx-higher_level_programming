#!/usr/bin/python3
""" rectangle inherting from base """
from models.base import Base


class Rectangle(Base):
    """ class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ init """
        super().__init__(id)
        self.width = width
        self.height = height
        self.y = y
        self.x = x

    @property
    def width(self):
        """ get width """
        return self.__width

    @property
    def height(self):
        """ get height """
        return self.__height

    @property
    def x(self):
        """ get x """
        return self.__x

    @property
    def y(self):
        """ get y """
        return self.__y

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ get area """
        return self.height * self.width

    def display(self):
        """ display rectangle """
        for y in range(self.y):
            print()
        for col in range(self.height):
            for x in range(self.x):
                print(' ', end='')
            for row in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """ str """
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ args """
        ac = len(args)
        if ac > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except Exception:
                pass
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
            if 'width' in kwargs:
                self.width = kwargs['width']

    def to_dictionary(self):
        """ return dict represntation of Rectangle """
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
            }
