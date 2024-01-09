#!/usr/bin/python3

"""defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """write an object to a text file using JSON rep."""
    with open(filename, "X") as f:
        json.dump(my_obj, f)
