#!/usr/bin/python3
"""
A class Amenity that inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    an class Amenity that inherits from BaseModel
    """

    name = ""
    def __init__(self, *args, **kwargs):
        """ Innit new user method """
        super().__init__(*args, **kwargs)
