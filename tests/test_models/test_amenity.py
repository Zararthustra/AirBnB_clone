#!/usr/bin/python3
"""
Amenity unittest
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Amenity unittest
    """

    def test_class(self):
        """
        test if the object is a type of Amenity
        """

        obj = Amenity()
        bm = BaseModel()
        self.assertEqual(type(obj), Amenity)
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attr(self):
        """
        test attributes
        """

        obj = Amenity()
        self.assertEqual(type(obj.name), str)
