#!/usr/bin/python3
"""
File: city.py

Author:
    Samson Tedla <samitedla23@gmail.com>
    Elnatan Samuel <krosection999@gmail.com>

Defines a class City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """A class that represents a City inheriting from BaseModel"""
    state_id = ""
    name = ""
