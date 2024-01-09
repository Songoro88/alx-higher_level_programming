#!/usr/bin/python3

"""defines a File-appending function."""


def append_write(filename="", text=""):
    """appends a string to the end of a UTF8 text file.
    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        the num of char appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
