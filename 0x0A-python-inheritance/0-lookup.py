#!/usr/bin/python3

"""defines the Object Attribute Lookup Function."""


def lookup(obj):
    """return list of the object's available attributes."""
    return (dir(obj))
