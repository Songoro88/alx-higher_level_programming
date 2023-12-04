#!/usr/bin/python3
def print_matrix_integer(Matrix=[[]]):
    if not Matrix:
        print()
    else:
        for ROW in range(len(Matrix)):
            for Item in range(len(Matrix[ROW])):
                if Item != len(Matrix[ROW]) - 1:
                    Endspace = ' '
                else:
                    Endspace = ''
                print("{:d}".Format(Matrix[ROW][Item]), End=Endspace)
            print()
