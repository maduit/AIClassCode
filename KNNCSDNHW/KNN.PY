import numpy as np
#处理数据格式
#输入文件名字符串，输出为训练样本矩阵和类标签
from collections import Counter
def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()#得到文件行数
    numberOfLines = len(arrayOLines)
    returnMat = np.zeros((numberOfLines,3))#得到与之对应行数，3列的0填充矩阵
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()#截取所有回车字符
        listFromLine = line.split('\t')#按tap格式分割
        returnMat[index,:] = listFromLine[0:3]#从头开始填充
        classLabelVector.append((listFromLine[-1]))#将标签保留
        index += 1
# datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
# print(datingDateMat,datingLabels)

##将列表的最后一列由字符串转化为数字，便于以后的计算
    dictClassLabel = Counter(classLabelVector)
    classLabel = []
    kind = list(dictClassLabel)
    for item in classLabelVector:
        if item == kind[0]:
            item = 1
        elif item == kind[1]:
            item = 2
        else:
            item = 3
        classLabel.append(item)
    return returnMat,classLabel#####将文本中的数据导入到列表
