import numpy as np
import Performance as perf
import Score as sc
import LoadVisualize as load
import BayesClassifier as bayes

def main() :
    trainSet = []
    trainLabel = []

    trainSet, trainLabel = load.loadDataset('Compound.csv')

    load.visualizeScatter(trainSet, trainLabel)
    prior, likelihood = bayes.countDistribution(6, trainSet, trainLabel)
    trainPred = bayes.getPrediction(prior, likelihood, len(trainSet), num_classes=6)

main()