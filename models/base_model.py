#!/usr/bin/python3
"""
Base class Module.
"""
import json
import uuid
from datetime import datetime

class BaseModel:
    """
    Deffine the BaseModel class with common attributes and methods
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Return string representation of the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at timestamp to current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
         # Copy __dict__ and add __class__
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        # Convert datetime attributes to ISO format
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
