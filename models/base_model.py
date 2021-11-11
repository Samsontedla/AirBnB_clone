#!/usr/bin/python3
"""
File: base_model.py

Authors:
        Samson Tedla <samitedla23@gmail.com>
        Elnatan Samuel <krosection999@gmail.com>

Defines a class called BaseModel
"""
import uuid
from datetime import datetime

class BaseModel:
    """Class that represents the BaseModel for the HBnB project"""

    def __init__(self, *args, **kwargs):
        """
        Initilize a new BaseModel

        Args:
            args: variable number of arguments(unused)
            kwargs: keyword/value pairs of attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    self.__dict__[key] = value
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.today()
    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        self.__dict__["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.__dict__["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__
    def __str__(self):
        """Method that prints formatted output"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
