#!/usr/bin/python3
"""Define class Base"""


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