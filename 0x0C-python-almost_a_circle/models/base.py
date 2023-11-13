#!/usr/bin/python3
""" first class """
import json
import csv
import os.path


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

    @classmethod
    def create(cls, **dictionary):
        """ create instance """
        if cls.__name__ == 'Rectangle':
            new = cls(1, 1)
            new.update(**dictionary)
            return new
        elif cls.__name__ == 'Square':
            new = cls(1)
            new.update(**dictionary)
            return new
        else:
            return None

    @classmethod
    def load_from_file(cls):
        """ load from file """
        alist = []
        try:
            with open('{}.json'.format(cls.__name__), 'r',
                      encoding='utf-8') as x:
                objlist = cls.from_json_string(x.read())
        except IOError:
            return []
        for dictionary in objlist:
            alist.append(cls.create(**dictionary))
        return alist

    @classmethod
    def load_from_file_csv(cls):
        """ load from csv """
        if os.path.exists("{}.csv".format(cls.__name__)) is False:
            return []

        with open("{}.csv".format(cls.__name__), 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            alist = list(reader)

        if cls.__name__ == "Rectangle":
            akeys = ['id', 'width', 'height', 'x', 'y']
        else:
            akeys = ['id', 'size', 'x', 'y']
        retlist = []
        for x in alist:
            dic_csv = {}
            for r in enumerate(x):
                dic_csv[akeys[r[0]]] = int(r[1])
            retlist.append(dic_csv)
        inlist = []
        for m in range(len(retlist)):
            inlist.append(cls.create(**alist[m]))
        return inlist

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save to csv """
        altd = []
        if cls.__name__ == "Rectangle":
            akeys = ['id', 'width', 'height', 'x', 'y']
            adic = [0, 0, 0, 0, 0]
        else:
            adic = [0, 0, 0, 0]
            akeys = ['id', 'size', 'x', 'y']
        if not list_objs:
            pass
        else:
            for m in list_objs:
                for x in range(len(akeys)):
                    adic[x] = m.to_dictionary()[akeys[x]]
                altd.append(adic[:])
        with open('{}'.format(cls.__name__), 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(altd)
