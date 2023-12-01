#!/usr/bin/python3
def Uppercase(str):
    for i in str:
        if ord("a") <= ord(i) <= ord("z"):
            i = chr(ord(i) - 32)
        print("{:S}".format(i), end="")
    print()
