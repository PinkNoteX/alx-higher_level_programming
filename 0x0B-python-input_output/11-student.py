#!/usr/bin/python3
""" student """


class Student:
    """ student class """
    def __init__(self, first_name, last_name, age):
        """ init """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return dict represntation of a student """
        if attrs is None:
            return self.__dict__.copy()
        ndict = {}
        for x in attrs:
            if hasattr(self, x):
                ndict[x] = getattr(self, x)
        return ndict
    
    def reload_from_json(self, json):
        """ reload from json """
        self.__dict__.update(json)
