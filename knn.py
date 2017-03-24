"""
Name: Sarina Xie
UNI: sx2166

This file contains a function that predicts the label of a row in data by
looking at its k nearest neighbors. It returns a vertical matrix composed
of all of these labels.
"""
import numpy as np
from find_k_nearest_neighbors import find_k_nearest_neighbors
from majority_vote import majority_vote

#for testing
from create_data import create_data
from integerize_labels import integerize_labels
from split import split

def knn(train_data, test_data, k):
    """Function that predicts the label of each row in test_data by by looking
    at its k nearest neighbors in train_data"""
    predicted_labels = []
    for row in test_data:
        neighbors = find_k_nearest_neighbors(row, train_data, k)
        predicted_labels.append(majority_vote(neighbors))
        
    predicted_labels = np.matrix(predicted_labels)
    predicted_labels = predicted_labels.T
    
    return predicted_labels

if __name__ == '__main__':
    irisdata = create_data("iris")
    irisdata = integerize_labels(irisdata)
    train, test = split(irisdata[0])
    
    predictions = knn(train, test, 10)
    print(test)
    print(predictions)