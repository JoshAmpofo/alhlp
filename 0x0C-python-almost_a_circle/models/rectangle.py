#!/usr/bin/python3
"""Define child class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize Rectangle

        Args:
            width (int): width dimension of Rectangle
            height (int): height dimension of Rectangle
            x (int): cartesian coordinate x of Rectangle
            y (int): cartesian coordinate y of Rectangle
            id (int): id of Rectangle
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """set width dimension of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """set height dimension of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """set x coordinate of Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """set y coordinate of Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
