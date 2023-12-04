#!/usr/bin/python3
def element_at(MY_List, idx):
    if idx < 0:
        return None
    elif idx >= len(MY_List):
        return None
    return MY_List[idx]
