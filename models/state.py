#!/usr/bin/python3
"""
State's module
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State's class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        constructor
        """

        super().__init__(*args, **kwargs)
