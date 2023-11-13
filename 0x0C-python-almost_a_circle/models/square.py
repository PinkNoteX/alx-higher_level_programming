#!/usr/bin/python3
""" square that inherits rectangle """
from models.rectangle import Rectangle


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

    @property
    def size(self):
        """ get size """
        return self.width

    @size.setter
    def size(self, value):
        """ size settter """
        self.height = value
        self.width = value
