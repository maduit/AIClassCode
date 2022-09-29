from array import array
import matplotlib.pyplot as plt

# samples=[[1,2,],[2,3],[3,4]]

# for s in samples:
#     plt.plot(s[0],s[1],'yo')
# plt.show()

# samples1=[[1,2,3,4,5],[6,7,8,9,10]]
# plt.plot(samples1[0],samples1[1],'gs:')

# samples2=[[1,2,3,4,5],[-6,-7,-8,-9,-10]]
# plt.plot(samples2[0],samples2[1],'bd:')
# plt.show()

#要求：
#随机生成100个点，x坐标在[0,5]之间，y坐标在[0,5]之间,
#当点位于y=x直线上及其上方时，该点画成红色
#当点位于y=x直线下方时，该点画成蓝色

import random
import numpy as np


#生成样本
np.random.seed(10)
array_size =100
array_x=np.random.uniform(0,5,array_size)
array_y=np.random.uniform(0,5,array_size)
new_point=[np.random.uniform(0,5,1),np.random.uniform(0,5,1)]
print(new_point)
# Samples=[]
#samples里新增加样本点，每个点的结构是[x,y,flag],
#flag=0,if x<y; flag=1,otherwise.
for i in range(len(array_x)):
    if(array_x[i]>array_y[i]):
        plt.plot(array_x[i],array_y[i],'rs')
        # Samples.append(array_x[i],array_y[i],0)
    else:
        # Samples.append(array_x[i],array_y[i],1)
        plt.plot(array_x[i],array_y[i],'bo')
# S=np.array(Samples)
# print(S.shape)
# plt.plot(S[:,0],S[:,1],'d')
plt.show()