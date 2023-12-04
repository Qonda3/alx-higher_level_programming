#!/usr/bin/python3
def uppercase(str):
    res = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            res = res + chr(ord(char) - ord('a') + ord('A'))
        else:
            res = res + char
    print(res)
    print()
