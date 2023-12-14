#!/usr/bin/python3
def multiply_by_2(my_dictionary):
    New_Dir = my_dictionary.copy()
    list_keys = list(new_dir.keys())

    for i in list_keys:
        New_Dir[i] *= 2

    return (New_Dir)
