#!/usr/bin/python3
"""
FileStorage unittest
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    """
    FileStorage unittest
    """

    def test_class(self):
        """
        test if the object is a type of FileStorage
        """

        obj = FileStorage()
        self.assertEqual(type(obj), FileStorage)

    def test_attr(self):
        """
        test attributs
        """

        obj = FileStorage()
        self.assertEqual(obj._FileStorage__file_path, "file.json"),
        self.assertEqual(type(obj._FileStorage__objects), dict),

    def test_save(self):
        """
        test if the method save() save the object in JSON file
        """

        obj = BaseModel()
        obj.name = "Tutur"
        obj.my_number = 29
        obj.save()
        self.assertTrue(os.path.exists("file.json"))
