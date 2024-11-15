#!/usr/bin/python3
"""
File storage class module.
"""
import json
import os
#from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        print("return all files")
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj
        print("new obj created")

    def save(self):
        """Serializes __objects to the JSON file (__file_path)."""
        from models.base_model import BaseModel
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)
        print("saved to file")

    def reload(self):
        """Deserializes the JSON file to __objects if the file exists."""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as JsonFile:
                try:
                    obj_dict = json.load(JsonFile)
                    for key, value in obj_dict.items():
                        cls_name, obj.id = key.split(".")
                        cls = eval(cls_name)
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
                    print("read the file")
                except Exception:
                    print("Error loading objects {e}.".format(e))
        else:
            print("The file {} was not found".format(FileStorage.__file_path))
