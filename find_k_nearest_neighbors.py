"""
Name: Sarina Xie
UNI: sx2166

This file contains a function that takes a test point, a set of training data, 
and an int k describing how many neighbors to find and returns a
k x (n+1) matrix that contains the k nearest neighbors of the test point from
the training data.
"""
import numpy as np

#for testing
from create_data import create_data
from integerize_labels import integerize_labels
from split import split
from euclidean_distance import euclidean_distance

def find_k_nearest_neighbors(test_point, train_data, k):
    """Function that finds the k nearest neighbors of a test point"""
    #make list of all euclidean distances
    distances = [euclidean_distance(test_point, x) for x in train_data]
    distances = np.array(distances)
    #get indices of k nearest neighbors
    distances = np.argsort(distances)[:k]
    #initialize k_nearest_neighbors and then fill it up
    k_nearest_neighbors = train_data[distances[0]]
    for i in range(1, len(distances)):
        k_nearest_neighbors = np.append(k_nearest_neighbors, \
        train_data[distances[i]], 0)
    
    return k_nearest_neighbors

if __name__ == '__main__':
    irisdata = create_data("iris")
    irisdata = integerize_labels(irisdata)
    train, test = split(irisdata[0])
    a = test[0]
    print(a)
    knn = find_k_nearest_neighbors(a, train, 4)
    print(knn)