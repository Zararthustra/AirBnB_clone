#!/usr/bin/python3
"""
This module is about JSON/dict file storage
"""
import json


class FileStorage:
    """
    FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """
        constructor
        """

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        __objects.append("{}.{}: {}".format(obj.__class__.__name__, obj.id, obj))

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(__file_path, mode="w") as f:
            json.dumps(__objects)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists)
        otherwise, do nothing. If the file doesnt exist, no exception should be raised)
        """
