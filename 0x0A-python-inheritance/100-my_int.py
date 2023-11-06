#!/usr/bin/python3
""" class that inherites from int """


class MyInt(int):
    """ the class """

    def init(self, value):
        """ init """
        self.value = value

    def __eq__(self, value):
        """ rev eq to not eq """
        return self.value != value

    def __ne__(self, value):
        """ rev not eq to eq """
        return self.value == value
