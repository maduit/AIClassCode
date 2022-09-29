import matplotlib
import matplotlib.pyplot as plt
#绘制散点图
fig = plt.figure()
ax = fig.add_subplot(111)#分割为1行1列第1块
ax.scatter(datingDataMat[:,1], datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
plt.show()