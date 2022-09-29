from numpy import *
import operator
#创建数据集
def createrDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels
ture = 1
#inX:输入向量; dataSet:训练样本集; labels:标签向量 k=最近邻居个数; 其中标签元素数目和矩阵dataSet的行数相同。
def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0] #行数
    #计算欧式距离
    diffMat = tile(inX,(dataSetSize,1))-dataSet #扩展dataSet行，分别相减，形成（x1-x2）矩阵
    sqDiffMat = diffMat**2
    print(sqDiffMat)
    #array内部行列求和，axis=1表示按列求和，即把每一行的元素加起来
    sqDistances = sqDiffMat.sum(axis=1)
    print(sqDistances)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()#从小到大排序，获得索引值(下标）
    print(sortedDistIndicies)
    #选择距离最小的k个点
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        print(voteIlabel)
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
        print(classCount[voteIlabel])
    #排序
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=ture)
    print(sortedClassCount)
    return sortedClassCount[0][0]