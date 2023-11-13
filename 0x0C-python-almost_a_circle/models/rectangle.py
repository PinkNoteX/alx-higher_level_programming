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