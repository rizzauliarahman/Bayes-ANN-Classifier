import numpy as np
import os
from io import StringIO

def column(matrix, i) :
    return [row[i] for row in matrix]

def loadDataset(filename) :
    path = '.\Dataset'

    attr = np.genfromtxt(os.path.join(path, filename), usecols=(0,1), delimiter=',')
    label = np.genfromtxt(os.path.join(path, filename), usecols=(-1), delimiter=',', dtype=int)

    return attr, label

def visualizeScatter(attr, label) :
    from matplotlib import pyplot as plt

    scatter = plt.figure()

    colors = ['c', 'm', 'y', 'k', 'r', 'g']
    labels = ['1', '2', '3', '4', '5', '6']

    perclass = {}

    for i in range(len(labels)) :
        perclass[i] = attr[label == i+1]

    for i in range(len(perclass)) :
        color = colors[i]
        x, y = column(perclass[i], 0), column(perclass[i], 1)
        plt.scatter(x, y, c=color, label = labels[i])


    plt.show()
