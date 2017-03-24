"""
Name: Sarina Xie
UNI: sx2166

This file contains a function that takes a numpy matrix and creates an
identical numpy matrix except that all the labels are converted into unique
integers corresponding to those labels. It then returns a tuple made of the 
new matrix and a dictionary of label_string, label_int pairs.
"""
#for testing
from create_data import create_data

def integerize_labels(data):
    """Function that takes a numpy matrix and creates an identical numpy array
    except with integerized labels and a dictionary of the label-int pairs"""
    
    #create dictionary
    label_dict = {}    
    labelnum = len(data.T)-1
    count = 0;
    for rownum in range(0, len(data)):
        label = data[rownum,labelnum]
        if label not in label_dict:
            label_dict[label] = count
            count += 1
            
    integerized_data = data
    
    #integerize labels
    #thanks mdml
    #http://stackoverflow.com/questions/19666626
    for label in label_dict:
        integerized_data[integerized_data == label] = label_dict[label]

    return (integerized_data, label_dict)

if __name__ == '__main__':
    irisdata = create_data("iris")
    data, labeldict = integerize_labels(irisdata)
    print(data)
    print(labeldict)