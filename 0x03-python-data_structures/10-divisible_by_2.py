#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res_list = []
    for n in my_list:
        res_list.append(n % 2 == 0)
    return (res_list)
