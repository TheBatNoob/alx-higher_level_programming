#!/usr/bin/python3
"""
Module 0-lookup.py
Function that returns the list of available attributes and methods
"""


def lookup(obj):
    """ Function that returns the list of available attributes
        and methods of an object
    Args:
        obj: instance of the class
    Returns:
        List of attributes
    """

    return dir(obj)
