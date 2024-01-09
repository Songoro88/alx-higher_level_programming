#!/usr/bin/python3

"""Defines a Py. class-to-JSON function."""


def class_to_json(obj):
    """return the dictionary rep of a Simple data structure."""
    return obj.__dict__
