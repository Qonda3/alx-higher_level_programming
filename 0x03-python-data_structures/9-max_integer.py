#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return (None)

    if not my_list:
        return (None)

    value = my_list[0]
    for n in my_list:
        if n > value:
            value = n

    return (value)
