#!/usr/bin/python3
"""
File: file_storage.py

Authors:
    Samson Tedla <samitedla23@gmail.com>
    Elnatan Samuel <krosection999@gmail.com>

Defines a FileStorage class
"""

import json
from model.base_model import BaseModel

class FileStorage:
    """
    Class that serializes instances to a JSON file 
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        objcn = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objcn, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

    def reload(self):
