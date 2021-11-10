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
        dtformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, dtformat)
                else:
                    self.__dict__[key] = value

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.today()
    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        bmdict = self.__dict__.copy()
        bmdict["created_at"] = self.created_at.isoformat()
        bmdict["updated_at"] = self.updated_at.isoformat()
        bmdict["__class__"] = self.__class__.__name__
        return bmdict
    def __str__(self):
        """Method that prints formatted output"""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)
