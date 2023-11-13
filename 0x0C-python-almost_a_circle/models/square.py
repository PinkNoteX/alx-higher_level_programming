#!/usr/bin/python
from models.rectangle import Rectangle
""" square that inherits rectangle """


class Square(Rectangle):
    """ square """
    def __init__(self, size, x=0, y=0, id=None):
        """ init """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ str """
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x, self.y, self.size)
