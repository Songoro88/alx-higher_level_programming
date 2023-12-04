#!/usr/bin/python3
ELEMENT_at = __import__('1-element_at').ELEMENT_at

MY_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".Format(idx, ELEMENT_at(MY_List, idx)))
