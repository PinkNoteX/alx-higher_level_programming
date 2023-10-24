#!/usr/bin/python3
"""class defines square"""


class Square:
    """class defines square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes attribute size"""
        self.__size = size
        self.position = position

    def area(self):
        """Calculate area"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Setter for square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Initializes attribute size """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
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
        """prints square with the character #"""
        if self.__size == 0:
            print("")
            return
        else:
            for m in range(self.position[1]):
                print()
            for n in range(0, self.size):
                for o in range(self.position[0]):
                    print(" ", end="")
                for p in range(self.size):
                    print("#", end="")
                print("")
