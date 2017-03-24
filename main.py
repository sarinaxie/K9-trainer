from create_data import create_data
from plot_data import plot_data
from integerize_labels import integerize_labels
from split import split
from euclidean_distance import euclidean_distance
from knn import knn
from weighted_knn import weighted_knn
from calculate_error_rate import calculate_error_rate

def compare_errors(k_vals, input_data_file):
    ## read in the input data
    initial_data = create_data(input_data_file)

    ## create plots of the data (this should save the images within the current
    ## directory)
    plot_data(initial_data)

    ## integerize the data labels
    integerized_data, label_dict = integerize_labels(initial_data)

    ## split the data into train and test
    train, test = split(integerized_data)

    ## compute the errors
    errors = {}
    for k in k_vals:
        predicted_labels = knn(train, test, k)
        error_rate = calculate_error_rate(predicted_labels, test)
        errors[k] = error_rate

    ## BONUS: weighting
    for k in k_vals:
        weighted_predicted_labels = weighted_knn(train, test, k)
        weighted_error_rate = calculate_error_rate(weighted_predicted_labels,
              test)
        print("Weighted error value for k = %d was %f" % (k,
           weighted_error_rate))

    return errors

if __name__ == "__main__":
    k_vals = [1, 3, 5, 10, 15]
    # TODO: specify the filename
    #input_data_file =
    errors = compare_errors(k_vals, "iris")
    for k in errors:
        print("Error value for k = %d was %f" % (k, errors[k]))
