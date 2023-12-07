#!/usr/bin/python3
def no_c(my_string):
    stringNew = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            stringNew = stringNew + char
    return (stringNew)
