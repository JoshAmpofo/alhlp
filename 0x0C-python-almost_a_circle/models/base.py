#!/usr/bin/python3
"""Define class Base"""

import json


class Base:
    """creates a Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize base class

        Args:
            id (int): id of object instances created
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list dictionaries

        Args:
            list_dictionaries (list): list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of instances that inherit from Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as jf:
            if list_objs is None:
                jf.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jf.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of JSON str repr of json_string

        Args:
            json_string (str): string representation of a list of dicts
        """

        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)
