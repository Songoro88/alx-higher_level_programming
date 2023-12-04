#!/usr/bin/python3
def new_in_list(MY_List, idx, ELEMENT):
    if idx < 0:
        return MY_List
    elif idx >= len(MY_List):
        return MY_List
    New_List = list(MY_List)
    New_List[idx] = element
    return New_List
