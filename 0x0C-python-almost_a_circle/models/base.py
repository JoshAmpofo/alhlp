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
