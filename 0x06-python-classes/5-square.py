#!/usr/bin/python3
"""class defines square"""


class Square:
    """class defines square"""
    def __init__(self, size=0):
        """Initializes attribute size"""
        self.__size = size

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

    def my_print(self):
        """prints square with the character #"""

        if self.__size != 0:
            for r in range(self.__size):
                for m in range(self.__size):
                    print('#', end='')
                print("")
        else:
            print("")
