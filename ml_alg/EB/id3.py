import numpy as np

class DecisionTree(object):

    def __init__(self, mode='C4.5'):
        self._tree = None

        if mode == 'C4.5' or mode == 'ID3':
            self._mode = mode
        else:
            raise Exception('mode must be C4.5 or ID3')

    def _calcuEntropy(self, y):
        num = y.shape[0]

        labelCounts = {}
        for label in y:
            if label not in labelCounts.keys():
                labelCounts[label] = 0
                labelCounts[label] += 1

        entropy = 0.0
        for key in labelCounts:
            prob = float(labelCounts[key]) / num
            entropy -= prob * np.log2(prob)
        return entropy

    def _splitDataSet(self, X, y, index, value):
        ret = []
        featVec = X[:, index]
        X = X[:, [i for i in range(X.shape[1]) if i != index]]
        for i in range(len(featVec)):
            if featVec[i] == value:
                ret.append(i)

        return X[ret,:], y[ret]


    def _chooseBestFeatureToSplit_ID3F(self, X, y):
        numFeatures = X.shape[1]
        oldEntropy = self._calcEntropy(y)
        bestInforGain = 0.0
        bestFeatureIndex = -1

        for i in range(numFeatures):
            featList = X[;,i]
            uniqueVals = set(featList)


