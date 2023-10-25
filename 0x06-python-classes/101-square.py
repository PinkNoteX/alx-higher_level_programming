#!/usr/bin/python3
"""Define a Square."""


class Square:
    """Define a Square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes attribute size"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Setter for square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Initializes attribute size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """setter for square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Initializes attribute position"""
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[1]) is not int or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) is not int or value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print"""
        print(self.__str__())

    def __str__(self):
        """Print representation of squares"""
        if self.size == 0:
            return
        else:
            str = '\n' * self.__position[1]
        for x in range(self.__size):
            str += ' ' * self.position[0]
            str += '#' * self.__size + '\n'
        return str[:-1]
