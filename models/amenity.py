#!/usr/bin/python3
"""
Amenity's module
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity's class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        constructor
        """
        super().__init__(*args, **kwargs)
