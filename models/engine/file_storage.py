#!/usr/bin/python3
"""
This module is about JSON/dict file storage
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place


class FileStorage:
    """
    FileStorage class filestorage class
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """
        empty constructor method
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
                json_file = json.load(f)
                for key, value in json_file.items():
                    self.new(eval(value["__class__"])(**value))
        except:
            pass
