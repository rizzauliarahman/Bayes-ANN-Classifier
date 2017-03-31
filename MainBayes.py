import numpy as np
import Performance as perf
import Score as sc
import LoadVisualize as load

def main() :
    trainSet = []
    trainLabel = []

    trainSet, trainLabel = load.loadDataset('Compound.csv')

    print repr(len(trainSet[78]))
    print trainLabel[78]

main()