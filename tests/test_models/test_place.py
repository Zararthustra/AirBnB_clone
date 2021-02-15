#!/usr/bin/python3
"""
Place unittest
"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Place unittest
    """

    def test_class(self):
        """
        test if the object is a type of Place
        """

        obj = Place()
        bm = BaseModel()
        self.assertEqual(type(obj), Place)
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attr(self):
        """
        test attributes
        """

        obj = Place()
        self.assertEqual(type(obj.city_id), str)
        self.assertEqual(type(obj.user_id), str)
        self.assertEqual(type(obj.name), str)
        self.assertEqual(type(obj.description), str)
        self.assertEqual(type(obj.number_rooms), int)
        self.assertEqual(type(obj.number_bathrooms), int)
        self.assertEqual(type(obj.max_guest), int)
        self.assertEqual(type(obj.price_by_night), int)
        self.assertEqual(type(obj.latitude), float)
        self.assertEqual(type(obj.longitude), float)
        self.assertEqual(type(obj.amenity_ids), list)
