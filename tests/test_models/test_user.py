#!/usr/bin/python3
"""
User unittest
"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    User unittest
    """

    def test_class(self):
        """
        test if the object is a type of User
        """

        obj = User()
        bm = BaseModel()
        self.assertEqual(type(obj), User)
        self.assertTrue(issubclass(User, BaseModel))

    def test_attr(self):
        """
        test attributes
        """

        obj = User()
        self.assertEqual(type(obj.email), str)
        self.assertEqual(type(obj.password), str)
        self.assertEqual(type(obj.first_name), str)
        self.assertEqual(type(obj.last_name), str)
