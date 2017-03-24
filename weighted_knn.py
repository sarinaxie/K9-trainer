"""
Name: Sarina Xie
UNI: sx2166

This file contains a function that predicts the label of a row in data by
looking at its k nearest neighbors. It returns a vertical matrix composed
of all of these labels.
"""
import numpy as np
from find_k_nearest_neighbors import find_k_nearest_neighbors
from weighted_majority_vote import weighted_majority_vote

def weighted_knn(train_data, test_data, k):
    """Function that predicts the label of each row in test_data by by looking
    at its k nearest neighbors in train_data"""
    predicted_labels = []
    for row in test_data:
        neighbors = find_k_nearest_neighbors(row, train_data, k)
        predicted_labels.append(weighted_majority_vote(neighbors))
        
    predicted_labels = np.matrix(predicted_labels)
    predicted_labels = predicted_labels.T
    
    weighted_predicted_labels = predicted_labels
    return weighted_predicted_labels