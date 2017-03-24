"""
Name: Sarina Xie
UNI: sx2166

This file contains a function that reads in a data file and returns an
m x (n+1) numpy matrix. The first n columns correspond to the n features of
the data set and the last column corresponds to the label of the row.
"""
import numpy as np

def create_data(input_data_file):
    """Function that makes a data file into an m x (n+1) numpy matrix"""
    
    infile = open(input_data_file + ".data")
    dlist = infile.readlines()
    otherlist = []
    for row in dlist:
        #make each row into list
        row = [x.strip('\n') for x in row.split(',')]
        #turn numbers into floats
        for i in range(0, len(row)-1):
            row[i] = float(row[i])
        #for some reason you can't just change dlist
        otherlist.append(row)
    data = np.matrix(otherlist, dtype=object)
    return data

if __name__ == '__main__':
    string = "1, 2, 3"
    string = [x.strip(' ') for x in string.split(',')]
    print(string)
    for i in range(0, len(string)-1):
        string[i] = float(string[i])
    print(string)
    for thing in string:
        print(type(thing))
    a = np.matrix([[1, 2], [3, 4]])
    print(a)
    matrix = create_data("iris")
    print(matrix)
    print(matrix[0,1])
    print(len(matrix.T))
