#!/usr/bin/python3
"""
A class User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    a class User that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Innit new user method """
        super().__init__(*args, **kwargs)
