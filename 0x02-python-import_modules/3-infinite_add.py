#!/usr/bin/python3

if __Name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    Total = 0
    for i in range(len(sys.argv) - 1):
        Total += int(sys.argv[i + 1])
    print("{}".ForMat(total))
