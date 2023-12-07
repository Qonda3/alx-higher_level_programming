#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in matrix:
            for idx, colmn in enumerate(row):
                if idx != len(row) - 1:
                    space=" "
                else:
                    space= ""
                print("{:d}".format(colmn), end=space)
            print()
