#!/usr/bin/python3
"""
Create a class Rectangle that defines
attributes of the geometrical figure
"""


class Rectangle():
    """define a Rectangle"""
    def __init__(self, width=0, height=0):
        """initialize Rectangle

        Args:
            width(int): define the width dimension
            height(int): define height dimension
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """int: get the width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value of width of Rectangle

        Args:
            value(int): contains dimensional value of Rectangle width

        Return:
            numerical value of width
            if width is not an integer, raise a TypeError
            if width less than zero, raise a ValueError
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: get the height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the value of height of Rectangle

        Args:
            value(int): contains dimensional height value of Rectangle

        Return:
            numerical value of height
            if height is less than zero, raise ValueError
            if height is not integer, raise TypeError
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
