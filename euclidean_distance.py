"""
Name: Sarina Xie
UNI: sx2166

This file contains a function that calculates the euclidean distance between
two 1 x (n+1) vectors.
"""
import math

#for testing
from create_data import create_data
from integerize_labels import integerize_labels
from split import split

def euclidean_distance(x1,x2):
    """Function that calculates the euclidean distance b/w 2 vectors"""
    sum = 0
    #len(x1.T)-1 is the number of elements excluding the label
    for i in range(0,len(x1.T)-1):
        dif = math.pow(x1[0,i] - x2[0,i], 2)
        sum += dif        
    
    distance = math.sqrt(sum)
    return distance
    
if __name__ == '__main__':
    irisdata = create_data("iris")
    irisdata = integerize_labels(irisdata)
    train, test = split(irisdata[0])
    a = test[0]
    b = test[1]
    
    print("row 0 of test", a)
    print("row 1 of test", b)
    print(euclidean_distance(a,b))