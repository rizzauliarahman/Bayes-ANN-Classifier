class Score :
    Tp = 0
    Tn = 0
    Fp = 0
    Fn = 0

    def __init__(self, params):
        self.Tp = params['Tp']
        self.Tn = params['Tn']
        self.Fp = params['Fp']
        self.Fn = params['Fn']

    def getPrecision(self) :
        return self.Tp / (self.Tp + self.Fp)

    def getRecall(self) :
        return self.Tp / (self.Tp + self.Fn)