"""
Name: Sarina Xie
UNI: sx2166

This function creates 6 unique scatterplots from the irisdata it is given.
"""
import numpy as np
import matplotlib.pyplot as plt

#for testing
from create_data import create_data

def plot_data(data):
    """Function that makes a scatterplot from data"""
    
    #organize data by label
    #thanks Eelco Hoogendoom for suggesting numpy.in1d
    #http://stackoverflow.com/questions/1962980
    iset = data[np.in1d(data[:,4], ["Iris-setosa"])]
    iversi = data[np.in1d(data[:,4], ["Iris-versicolor"])]
    ivirg = data[np.in1d(data[:,4], ["Iris-virginica"])]
    
    #data
    xset = iset[:,0]
    yset = iset[:,1]
    xversi = iversi[:,0]
    yversi = iversi[:,1]
    xvirg = ivirg[:,0]
    yvirg = ivirg[:,1]
    #plotting
    plt.figure()
    plt.plot(xset,yset,"xr",label = "Iris setosa")
    plt.plot(xversi,yversi,"xy",label = "Iris versicolor")
    plt.plot(xvirg,yvirg,"xb",label = "Iris virginica")
    #margins, labels, legend
    plt.margins(0.05)
    plt.title("Sepal length vs Sepal width")
    plt.xlabel("Sepal length")
    plt.ylabel("Sepal width")
    plt.legend()
    
    xset = iset[:,0]
    yset = iset[:,2]
    xversi = iversi[:,0]
    yversi = iversi[:,2]
    xvirg = ivirg[:,0]
    yvirg = ivirg[:,2]
    plt.figure()
    plt.plot(xset,yset,"xr",label = "Iris setosa")
    plt.plot(xversi,yversi,"xy",label = "Iris versicolor")
    plt.plot(xvirg,yvirg,"xb",label = "Iris virginica")
    plt.margins(0.05)
    plt.title("Sepal length vs Petal length")
    plt.xlabel("Sepal length")
    plt.ylabel("Petal length")
    plt.legend()
    
    xset = iset[:,0]
    yset = iset[:,3]
    xversi = iversi[:,0]
    yversi = iversi[:,3]
    xvirg = ivirg[:,0]
    yvirg = ivirg[:,3]
    plt.figure()
    plt.plot(xset,yset,"xr",label = "Iris setosa")
    plt.plot(xversi,yversi,"xy",label = "Iris versicolor")
    plt.plot(xvirg,yvirg,"xb",label = "Iris virginica")
    plt.margins(0.05)
    plt.title("Sepal length vs Petal width")
    plt.xlabel("Sepal length")
    plt.ylabel("Petal width")
    plt.legend()

    xset = iset[:,1]
    yset = iset[:,2]
    xversi = iversi[:,1]
    yversi = iversi[:,2]
    xvirg = ivirg[:,1]
    yvirg = ivirg[:,2]
    plt.figure()
    plt.plot(xset,yset,"xr",label = "Iris setosa")
    plt.plot(xversi,yversi,"xy",label = "Iris versicolor")
    plt.plot(xvirg,yvirg,"xb",label = "Iris virginica")
    plt.margins(0.05)
    plt.title("Sepal width vs Petal length")
    plt.xlabel("Sepal width")
    plt.ylabel("Petal length")
    plt.legend()
    
    xset = iset[:,1]
    yset = iset[:,3]
    xversi = iversi[:,1]
    yversi = iversi[:,3]
    xvirg = ivirg[:,1]
    yvirg = ivirg[:,3]
    plt.figure()
    plt.plot(xset,yset,"xr",label = "Iris setosa")
    plt.plot(xversi,yversi,"xy",label = "Iris versicolor")
    plt.plot(xvirg,yvirg,"xb",label = "Iris virginica")
    plt.margins(0.05)
    plt.title("Sepal width vs Petal width")
    plt.xlabel("Sepal width")
    plt.ylabel("Petal width")
    plt.legend()
    
    xset = iset[:,2]
    yset = iset[:,3]
    xversi = iversi[:,2]
    yversi = iversi[:,3]
    xvirg = ivirg[:,2]
    yvirg = ivirg[:,3]
    plt.figure()
    plt.plot(xset,yset,"xr",label = "Iris setosa")
    plt.plot(xversi,yversi,"xy",label = "Iris versicolor")
    plt.plot(xvirg,yvirg,"xb",label = "Iris virginica")
    plt.margins(0.05)
    plt.title("Petal length vs Petal width")
    plt.xlabel("Petal length")
    plt.ylabel("Petal width")
    plt.legend()
    
    return None

if __name__ == '__main__':
    irisdata = create_data("iris")
    plot_data(irisdata)
    