import LoadVisualize as load
import numpy as np
import math

def countDistribution(num, attr, label) :
    num_class = num
    classes = np.arange(1, 7)
    prior, likelihood = [], []
    xmean, ymean = [], []
    xstd, ystd = [], []

    x, y = np.array(load.column(attr, 0)), np.array(load.column(attr, 1))
    print label[0]

    for i in range(num_class) :
        prior.append(float(len(attr[label == i+1])) / float(len(attr)))
        xclass = x[label == i+1]
        yclass = y[label == i+1]
        xmean.append(np.mean(xclass))
        ymean.append(np.mean(yclass))
        xstd.append(np.std(xclass))
        ystd.append(np.std(yclass))

    for i in range(len(attr)) :
        temp = []
        for lbl in classes :
            tmp1 = 0.0
            tmp2 = 0.0
            tmp1 += (1 / (xstd[lbl-1] * np.sqrt(2*math.pi))) * np.exp((-((np.square(x[i] - xmean[lbl-1])) / (2 * np.square(xstd[lbl-1])))))
            tmp2 += (1 / (ystd[lbl-1] * np.sqrt(2*math.pi))) * np.exp((-((np.square(y[i] - ymean[lbl-1])) / (2 * np.square(ystd[lbl-1])))))

            temp.append([tmp1, tmp2])

        likelihood.append(temp)

    return prior, likelihood

def getPrediction(prior, likelihood, num_data, num_classes) :
    classes = np.arange(1, 7)
    posterior = []
    pred_label = []

    for i in range(num_data) :
        temp = []
        for lbl in classes :
            likelihood[i][lbl-1] = np.array(likelihood[i][lbl-1])
            likelihood[i][lbl-1] = likelihood[i][lbl-1].clip(min = 0.001)
            post1 = np.log(likelihood[i][lbl-1][0]) + np.log(prior[lbl-1])
            post2 = np.log(likelihood[i][lbl-1][1]) + np.log(prior[lbl-1])

            temp.append(post1 + post2)

        posterior.append(temp)
        pred_label.append(temp.index(np.max(temp)))

    print pred_label[:30]

    return pred_label



