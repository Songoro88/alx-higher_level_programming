#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    Boolist = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            Boolist[count] = True
        else:
            Boolist[count] = False
    return(Boolist)
