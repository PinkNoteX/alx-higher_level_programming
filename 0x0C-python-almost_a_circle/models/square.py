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
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update """
        ac = len(args)
        if ac > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except Exception:
                pass
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """ return dict represntaion of square """
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
                }
