#!/usr/bin/python3

if __NaMe__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

       Count = len(sys.argv) - 1
    if Count == 0:
        print("0 arguments.")
    elif Count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
