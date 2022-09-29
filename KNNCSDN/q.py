import KNN
from numpy import *
dataSet,labels = KNN.createrDataSet()
inX = array([0,0.3])
k = 3
output = KNN.classify0(inX,dataSet,labels,k)
print("测试数据为:",inX,"分类结果为：",output)