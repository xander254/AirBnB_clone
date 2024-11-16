#!/usr/bin/python3
"""
A class City that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    a class City that inherits from BaseModel
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Innit new user method """
        super().__init__(*args, **kwargs)
