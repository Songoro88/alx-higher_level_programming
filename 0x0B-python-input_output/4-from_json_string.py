#!/usr/bin/python3

"""defines a string-to-JSON Function."""
import json


def to_json_string(my_obj):
    """return the JSON rep of a string object."""
    return json.dumps(my_obj)
