from numpy import *
from os import listdir

def loadData(direction):
    trainfileList = listdir(direction)
    m = len(trainfileList)
    dataArray = zeros((m, 1024))
    labelArray = zeros((, 1))
    for i in range(m):
        returnArray = zeros((1, 1024))
        filename = trainfileList[i]
        fr = open('%s/%s'%(direction, filename))
        for j in range(32):
            lineStr = fr.readline()
            for k in range(32):
                returnArray[0, 32*j+k] = int(lineStr[k])
        dataArray[i, :] = returnArray

        filename0 = filename.split('.')[0]
        label = filename0.split('_')[0]
        labelArray[i] = int(label)
    return dataArray, labelArray

def sigmoid(inX):
    return 1.0 / (1 + exp(-inx))

def gradAscent(dataArray, labelArray, alpha, maxCycles):
    dataMat = mat(dataArray)
    labelMat = mat(labelArray)
    m, n = shape(dataMat)
    weigh = ones((n, 1))
    for i in range(maxCycles):
        h = sigmoid(dataMat*weigh)
        error = labelMat - h
        weigh = weigh + alpha * dataMat.transpose()*error
    return weigh

