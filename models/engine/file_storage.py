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
            args:
                obj: object input
        """
        obj_name = obj.__class__.__name__ + "." + obj.id
        self.__objects[obj_name] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        new_dict = {}
        for key in self.__objects:
            new_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, mode="w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file exists)
        otherwise, do nothing)
        """
        try:
            with open(self.__file_path) as f:
                #self.__objects = json.load(f)
        except:
            pass
