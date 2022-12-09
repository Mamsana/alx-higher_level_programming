#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    if my_list:
        for value in my_list:
            new_list.append(True)
        else:
            new_list.append(False)
    return(new_list)
