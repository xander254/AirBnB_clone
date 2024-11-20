#!/usr/bin/python3
"""
Base class Module.
"""
import json
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Define the BaseModel class with common attributes and methods
    """
    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance"""
        from models import storage
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            # Loop through key-value pairs
            for key, value in kwargs.items():
                # Ignore class key
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Return string representation of the instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Update updated_at timestamp to current time"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of dict instance"""
        # Copy __dict__ and add __class__
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        # Convert datetime attributes to ISO format
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
