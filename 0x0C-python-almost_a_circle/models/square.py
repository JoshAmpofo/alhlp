#!/usr/bin/python3
"""Define child class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize Square and its associated properties

        Args:
            size (int): size of Square
            x (int): x dimensonal value of Square
            y (int): y dimensional value of Square
            id (int): instance id of Square

        Return:
            raise TypeError if attribute is not an integer
            raise ValueError if attribute is less than or equal to zero
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """informal string representation of objects in Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
