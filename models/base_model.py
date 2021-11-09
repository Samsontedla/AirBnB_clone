#!/usr/bin/python3
"""
File: base_model.py

Author: Samson Tedla <samitedla23@gmail.com>, Elnatan Samuel <>

Defines a class BaseModel
"""
import uuid

class BaseModel:
    """
    Class that represents the base for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initilize a new BaseModel

        Args:
            takes variable number of arguments and
            keyword arguments
        """
        self.id = str(uuid.uuid4())
