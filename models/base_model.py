#!/usr/bin/python3
"""
This module is the Base Model module
"""
import uuid
from datetime import datetime
from models.__init__ import storage

class BaseModel:
    """
    BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """
        constructor
            args:
                args (int): int
                kwargs: assign
        """
        if kwargs:
            self.id = kwargs["id"]
            self.my_number = kwargs["my_number"]
            self.name = kwargs["name"]
            self.created_at = datetime.strptime(kwargs["created_at"], '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(kwargs["updated_at"], '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        str magic method
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        date = datetime.now()
        self.updated_at = date
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        dic = {
                "id": self.id,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat(),
                "name": self.name,
                "my_number": self.my_number,
                "__class__": self.__class__.__name__
                }
        return dic
