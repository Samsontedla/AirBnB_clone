#!/usr/bin/python3
"""
File: amenity.py

Author:
    Samson Tedla <samitedla23@gmail.com>
    Elnatan Samuel <krosection999@gmail.com>

Defines a class Amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class that represents a Amenity inheriting from BaseModel"""
    name = ""
