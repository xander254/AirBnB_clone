#!/usr/bin/python3
"""
A class Place that inherits from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    a class Place that inherits from BaseModel
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    max_guest = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = 0.0

    def __init__(self, *args, **kwargs):
        """ Innit new user method """
        super().__init__(*args, **kwargs)
