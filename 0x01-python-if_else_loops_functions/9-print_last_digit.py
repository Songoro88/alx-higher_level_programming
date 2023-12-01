#!/usr/bin/python3
def Print_last_Digit(num):
    if num < 0:
        last_num = (-num % 10)
    elif number >= 0:
        last_num = number % 10
    print("{:d}".format(last_num), end="")
    return last_num
