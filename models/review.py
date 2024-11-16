#!/usr/bin/python3
"""
A class Review that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    a class review that inherits from BaseModel
    """

    place_id = ""
    user_id ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Innit new user method """
        super().__init__(*args, **kwargs)
