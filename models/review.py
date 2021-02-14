#!/usr/bin/python3
"""
Review's module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review's class
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self):
        """
        constructor
        """
        super().__init__()
