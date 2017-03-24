"""
Name: Sarina Xie
UNI: sx2166

This file contains a function that returns an integer that represents the
majority label of neighbors.
"""
import numpy as np

#for testing
from create_data import create_data
from integerize_labels import integerize_labels
from split import split
from find_k_nearest_neighbors import find_k_nearest_neighbors

def weighted_majority_vote(neighbors):
    """Function that returns an integer that represents the majority label of
    neighbors"""

    #get number of labels
    labels = set()
    labelnum = len(neighbors.T)-1
    for rownum in range(0, len(neighbors)):
        label = neighbors[rownum,labelnum]
        if label not in labels:
            labels.add(label)
            
    """
    how I would implement weighted majority vote:
    -separate neighbors into flower classes
    -for each class, add up all the distances from the test point to its
    neighbors
    -divide each sum by how many samples were in the class
    -the smallest sum is the closest one
    """
    
    majority_label = -1
    largest = -1
    for label in labels:
        #separate out a class
        tempclass = neighbors[np.in1d(neighbors[:,labelnum], label)]
        if (len(tempclass) > largest):
            largest = len(tempclass)
            majority_label = label
    
            
    weighted_majority_label = majority_label
    return weighted_majority_label

if __name__ == '__main__':
    irisdata = create_data("iris")
    irisdata = integerize_labels(irisdata)
    train, test = split(irisdata[0])
    a = test[30]
    print("row", a)
    neighbors = find_k_nearest_neighbors(a, train, 10)
    print("neighbors", neighbors)
    prediction = weighted_majority_vote(neighbors)
    print("prediction", prediction)