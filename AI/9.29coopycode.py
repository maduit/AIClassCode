from array import array
import matplotlib.pyplot as plt
import random
import numpy as np

#距离度量
def caldis(a,b,mode):
    if len(a)!=len(b)+1:
        return -1
    else: 
        #欧氏距离（二维）：   
        if mode=='o':
            s_o=sum((a[i]-b[i])**2 for i in range(len(a)-1))
            return [s_o**0.5,a[-1]]
        #曼哈顿距离（二维）：
        elif mode=='m':
            s_m=sum([abs(a[i]-b[i]) for i in range(len(a)-1)])
            return [s_m,a[-1]]

def caldis_sample_newpoint(samples,newpoint,mode):
    diss=[caldis(samples[i],newpoint,mode) for i in range(len(samples))]
    return diss

def sort_m(diss,k):
    if k>=len(diss):
        return -1
    else:
       diss_sorted=sorted(diss)
       inds=[diss.index(diss_sorted[i]) for i in range(k)]
       return inds
#生成样本
np.random.seed(10)
array_size =100  #100个
array_x,array_y=np.random.uniform(0,5,array_size),np.random.uniform(0,5,array_size)
new_point=[np.random.uniform(0,5,1),np.random.uniform(0,5,1)]
Samples=[]
#Samples里新增加样本点，每个点的结构是[x,y,flag],
#flag=0,if x<y; flag=1,otherwise.

# for i in range(len(array_x)):
#     if(array_x[i]>array_y[i]):
#         Samples.append([array_x[i],array_y[i],0])
#     else:
#         Samples.append([array_x[i],array_y[i],1])

Samples=[[array_x[i],array_y[i],0 if array_x[i]>array_y[i] else 1] for i in range(len(array_x))]
diss=caldis_sample_newpoint(Samples,new_point,'o')
dis_inds=sort_m(diss,9)

for ind in dis_inds:
    s=Samples[ind]
    if s[2]==0:
        plt.plot(s[0],s[1],'bd')
    else:
        plt.plot(s[0],s[1],'rs')
plt.plot(new_point[0],new_point[1],'go')

classes=[Samples[ind][2] for ind in dis_inds]
print(classes)
#统计classes中0和1的数量，如果0多，则new_point类别为0；否则为1
new_point.append(1 if classes.count(0)>classes.count(1) else 0)
print(new_point)
plt.axis([0,5,0,5])
