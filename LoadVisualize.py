import numpy as np
import os
from io import StringIO

def loadDataset(filename) :
    path = '.\Dataset'

    attr = np.genfromtxt(os.path.join(path, filename), usecols=(0, 1), delimiter=',')
    label = np.genfromtxt(os.path.join(path, filename), usecols=(-1), delimiter=',')

    return attr, label

# def visualizeScatter()