#!/usr/bin/python3
""" first class """
import json


class Base:
    """ base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to json """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to json """
        adict = []
        if not list_objs:
            list_objs = []
        for x in list_objs:
            adict.append(x.to_dictionary())

        with open('{}.json'.format(cls.__name__), 'w', encoding='utf-8') as r:
            r.write(cls.to_json_string(adict))

    @staticmethod
    def from_json_string(json_string):
        """ from json """
        if json_string is None:
            return []
        return json.loads(json_string)
