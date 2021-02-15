#!/usr/bin/python3
"""
State unittest
"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    State unittest
    """

    def test_class(self):
        """
        test if the object is a type of State
        """

        obj = State()
        bm = BaseModel()
        self.assertEqual(type(obj), State)
        self.assertTrue(issubclass(State, BaseModel))

    def test_attr(self):
        """
        test attributes
        """

        obj = State()
        self.assertEqual(type(obj.name), str)
