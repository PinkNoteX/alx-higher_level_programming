#!/usr/bin/python3
""" class that inherites from int """


class MyInt(int):
    """ the class """

    def __init__(self, value):
        """ init """
        self.value = value

    def __eq__(self, x):
        """ rev eq to not eq """
        return self.value != x

    def __ne__(self, x):
        """ rev not eq to eq """
        return self.value == x
