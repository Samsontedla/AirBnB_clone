#!/usr/bin/python3
"""
File: file_storage.py

Authors:
    Samson Tedla <samitedla23@gmail.com>
    Elnatan Samuel <krosection999@gmail.com>

Defines a FileStorage class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Class that serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obdict = {}
        for key in self.__objects:
            obdict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(obdict, f)

    def reload(self):
        """deserializes JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                json_obj = json.load(f)
                for key, value in json_obj.items():
                    self.__objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:
            return
