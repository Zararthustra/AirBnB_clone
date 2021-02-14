#!/usr/bin/python3
"""
User's module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User's class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
