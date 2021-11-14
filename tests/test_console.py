#!/usr/bin/python3
"""
A test file to test the console for the hbnb project
"""

import unittest
with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd("help show")
