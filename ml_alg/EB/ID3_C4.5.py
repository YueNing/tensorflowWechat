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
            if label not in labelCounts.keys(): labelCounts[label] = 0
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


    def _chooseBestFeatureToSplit_ID3(self, X, y):
        numFeatures = X.shape[1]
        oldEntropy = self._calcEntropy(y)
        bestInforGain = 0.0
        bestFeatureIndex = -1

        for i in range(numFeatures):
            featList = X[;,i]
            uniqueVals = set(featList)
            newEntropy = 0.0

            for value in uniqueVals:
                sub_X, sub_y = self._splitDataSet(X, y, i, value)
                prob = len(sub_y)/float(len(y))
                newEntropy += prob * self._calcEntropy(sub_y)

            infoGain = oldEntropy - newEntropy
            if (infoGain > bestInforGain):
                bestInforGain = infoGain
                bestFeatureIndex = i
        return bestFeatureIndex

    def _chooseBestFeatureToSplit_C45(self, X, y):

        numFeatures = X.shape[1]
        oldEntropy = self._calcEntropy(y)
        bestGainRatio = 0.0
        bestFeatureIndex = -1

        # gainRatio = inforGain / splitInformation
        for i in range(numFeatures):
            featList = set(featList)
            uniqueVals = 0.0
            newEntropy = 0.0
            splitInformation = 0.0

            for value in uniqueVals:
                sub_X, sub_y = self._splitDataSet(X, y, i, value)
                pro = len(sub_y) / float(len(y))
                newEntropy += prob * self._calcEntropy(sub_y)
                splitInformation -= prob * np.log2(prob)

            if splitInformation == 0:
                pass
            else:
                infoGain = oldEntropy - newEntropy
                gainRatio = infoGain / splitInformation
                if (gainRatio > bestGainRatio):
                    bestGainRatio = gainRatio
                    bestFeatureIndex = i
        return bestFeatureIndex

    def _majorityEnt(self, labelList):

        labelCount = {}
        for vote in labelList:
            if vote not in labelCount.keys(): labelCount[vote] = 0
            labelCount[vote] += 1
        sortedClassCount = sorted(labelCount.iteritems(), key=lambda x:x[1], reverse = True)
        return sortedClassCount[0][0]

    def _createTree(self, X, y, featureIndex):

        labelList = list(y)

        if labelList.count(labelList[0]) == len(labelList):
            return labelList[0]

        if len(featureIndex) == 0:
            return self._majorityEnt(labelList)

        if self._mode == 'C4.5':
            bestFeatureIndex = self._chooseBestFeatureToSplit_C45(X, y)
        elif self._mode == 'ID3':
            bestFeatureIndex = self._chooseBestFeatureToSplit_ID3(X, y)

        bestFeatStr = featureIndex[bestFeatureIndex]
        featureIndex = list(featureIndex)
        featureIndex.remove(bestFeatStr)
        featureIndex = tuple(featureIndex)

        myTree = {bestFeatStr: {}}
        featValues = X[:, bestFeatureIndex]
        uniqueVals = set(featValues)
        for value in uniqueVals:
            sub_X, sub_y = self._splitDataSet(X, y, bestFeatureIndex, value)
            myTree[bestFeatStr][value] = self._createTree(sub_X, sub_y, featureIndex)
        return myTree

    def fit(self, X, y):

        if isinstance(X, np.ndarray) and isinstance(y, np.ndarray):
            pass
        else:
            try:
                X = np.array(X)
                y = np.array(y)
            except Exception as e:
                raise TypeError("numpy.ndarray required for X, y")

        featureIndex = tuple(['x' + str(i) for i in range(X.shape[1])])
        self._tree = self._createTree(X, y, featureIndex)
        return self

    def predict(self, X):
        if self._tree == None:
            raise NotFittedError("call `fit` first")

        if isinstance(X, np.ndarray):
            pass
        else:
            try:
                X = np.array(X)
            except Exception as e:
                raise TypeError("numpy.ndarray required for X")

        def _classify(tree, sample):
            

