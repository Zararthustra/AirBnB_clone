#!/usr/bin/python3
"""
City unittest
"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    City unittest
    """

    def test_class(self):
        """
        test if the object is a type of City
        """

        obj = City()
        bm = BaseModel()
        self.assertEqual(type(obj), City)
        self.assertTrue(issubclass(City, BaseModel))

    def test_attr(self):
        """
        test attributes
        """

        obj = City()
        self.assertEqual(type(obj.state_id), str)
        self.assertEqual(type(obj.name), str)
