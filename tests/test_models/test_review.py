#!/usr/bin/python3
"""
Review unittest
"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Review unittest
    """

    def test_class(self):
        """
        test if the object is a type of Review
        """

        obj = Review()
        bm = BaseModel()
        self.assertEqual(type(obj), Review)
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attr(self):
        """
        test attributes
        """

        obj = Review()
        self.assertEqual(type(obj.place_id), str)
        self.assertEqual(type(obj.user_id), str)
        self.assertEqual(type(obj.text), str)
