#!/usr/bin/python3
"""
File: state.py

Author:
    Samson Tedla <samitedla23@gmail.com>
    Elnatan Samuel <krosection999@gmail.com>

Defines a class State
"""
from models.base_model import BaseModel


class State(BaseModel):
    """A class that represents a State inheriting from BaseModel"""
    name = ""
