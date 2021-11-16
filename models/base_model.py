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
import models


class BaseModel:
    """A class that represents the BaseModel for the HBnB project"""
    def __init__(self, *args, **kwargs):
        """
        Initilize a new BaseModel

        Args:
            args: variable number of arguments(unused)
            kwargs: keyword/value pairs of arguments/attributes
        """
        #self.id = str(uuid.uuid4())
        #self.created_at = datetime.today()
        #self.updated_at = datetime.today()
        #models.storage.new(self)
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                                        value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)
    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        obdict = self.__dict__.copy()
        obdict["created_at"] = self.created_at.isoformat()
        obdict["updated_at"] = self.updated_at.isoformat()
        obdict["__class__"] = self.__class__.__name__
        return obdict

    def __str__(self):
        """Method that prints formatted output"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
