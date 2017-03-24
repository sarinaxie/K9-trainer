"""
Name: Sarina Xie
UNI: sx2166

This file contains a function that calculates the error rate for the test set.
error rate = number of errors/number of predictions
"""
#for testing
from create_data import create_data
from integerize_labels import integerize_labels
from split import split
from knn import knn

def calculate_error_rate(predicted_labels, test_data):
    """Function that calculates the error rate for the test set"""
    test = test_data[:,len(test_data.T)-1]
    errors = 0
    for i in range(0, len(test)):
        
        if (predicted_labels[i] != test[i]):
            errors += 1
            
    error_rate = errors/len(test_data)
    
    return error_rate

if __name__ == '__main__':
    irisdata = create_data("iris")
    irisdata = integerize_labels(irisdata)
    train, test = split(irisdata[0])
    
    predictions = knn(train, test, 10)
    #print(predictions)
    rate = calculate_error_rate(predictions, test)
    print("error rate", rate)