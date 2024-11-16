#!/usr/bin/python3
"""
A class State that inherits from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    a class State that inherits from BaseModel
    """

    name = ""
    def __init__(self, *args, **kwargs):
        """ Innit new user method """
        super().__init__(*args, **kwargs)
