#!/usr/bin/python3

"""defines a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.
    Args:
        filename (str): the name of the file to write.
        text (str): the text to write to the file.
    Returns:
        the num of char written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
