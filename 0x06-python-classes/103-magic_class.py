#!/usr/bin/python3
"""define magic class"""
import math


class MagicClass:
    """define magic class"""
    def __init__(self, radius=0):
        """init magic class"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self._MagicClass__radius = radius

    def area(self):
        """area"""
        return (math.py * self._MagicClass__radius ** 2)

    def circumference(self):
        """circumference"""
        return (2 * math.pi * self._MagicClass__radius)

    if __name__ == "__main__":
        import dis
        dis.dis(MagicClass)
