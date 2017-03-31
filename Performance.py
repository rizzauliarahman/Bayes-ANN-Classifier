def getPerformance(scoreList, mode) :
    totalTp = 0.0
    totalTn = 0.0
    totalFp = 0.0
    totalFn = 0.0
    finalPrecision = 0.0
    finalRecall = 0.0
    simpleAvg = 0.0

    if mode == 'micro' :
        for score in scoreList :
            totalTp += score.Tp
            totalTn += score.Tn
            totalFp += score.Fp
            totalFn += score.Fn

        finalPrecision = totalTp / (totalTp + totalFp)
        finalRecall = totalTp / (totalTp + totalFn)

        return finalPrecision, finalRecall

    elif mode == 'macro' :
        for i in range(len(scoreList)) :
            finalPrecision = (finalPrecision + scoreList[i].getPrecision()) / (i + 1)
            finalRecall = (finalRecall + scoreList[i].getRecall()) / (i + 1)

        return finalPrecision, finalRecall

    elif mode == 'simple' :
        correctScore = 0.0

        for score in scoreList :
            correctScore += score.Tp

        simpleAvg = correctScore / len(scoreList)

        return simpleAvg

    else :
        return 'Please input the correct mode'