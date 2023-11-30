#!/usr/bin/python3
import random
number = random.randint(-8, 8)
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
elif number < 0:
    print(f"{number} is negative")
