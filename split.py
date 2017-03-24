"""
Name: Sarina Xie
UNI: sx2166

This file contains a function that randomly takes 15 instances from each of
the classes in integerized_data and puts them into a numpy matrix named
test_data. The unselected instances are put in the numpy matrix train_data.
The function returns the tuple (train_data, test_data).
"""
import numpy as np

#for testing
from create_data import create_data
from integerize_labels import integerize_labels

def split(integerized_data):
    """Function that takes data in a numpy matrix and makes a test set and
    training set from it"""

    #shuffle to introduce randomness   
    np.random.shuffle(integerized_data)
    
    #create dictionary
    #because label_dict isn't passed to split() for some ungodly reason
    label_dict = {}    
    labelnum = len(integerized_data.T)-1
    count = 0;
    for rownum in range(0, len(integerized_data)):
        label = integerized_data[rownum,labelnum]
        if label not in label_dict:
            label_dict[label] = count
            count += 1
    
    #separate out a class
    tempclass = integerized_data[np.in1d(integerized_data[:,labelnum], 0)]
    #take 15 lines from it and make them into test_data
    test_data = tempclass[:15]
    #take the rest of it and make it into train_data
    train_data = tempclass[15:]
    for i in range(1, len(label_dict)):
        #separate out a class
        tempclass = integerized_data[np.in1d(integerized_data[:,labelnum], i)]
        #take 15 lines from it and append them to test_data
        temp15 = tempclass[:15]
        test_data = np.append(test_data, temp15, 0)
        #take the rest of it and append it to train_data
        temprest = tempclass[15:]
        train_data = np.append(train_data, temprest, 0)

    return (train_data, test_data)

if __name__ == '__main__':
    irisdata = create_data("iris")
    irisdata = integerize_labels(irisdata)
    split(irisdata[0])