#!/usr/bin/python3
"""
City's module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City's class
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        constructor
        """

        super().__init__(*args, **kwargs)
