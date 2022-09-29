from array import array
import matplotlib.pyplot as plt
import random
import numpy as np

def caldis(a,b,mode):
    #a,b长度相等
    if len(a)!=len(b)+1:
        return -1
    else:    
        if mode=='o':
            # s_o=0
            s_o=sum((a[i]-b[i])**2 for i in range(len(a)-1))
            return [s_o**0.5,a[-1]]
        elif mode=='m':
            # s_m=0
            s_m=sum([abs(a[i]-b[i]) for i in range(len(a)-1)])
            return [s_m,a[-1]]
    # else:
        # return -1
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

np.random.seed(10)
array_size =100
array_x,array_y=np.random.uniform(0,5,array_size),np.random.uniform(0,5,array_size)
new_point=[np.random.uniform(0,5,1),np.random.uniform(0,5,1)]
Samples=[]
# print(new_point)
for i in range(len(array_x)):
    if(array_x[i]>array_y[i]):
        # plt.plot(array_x[i],array_y[i],'rs')
        Samples.append([array_x[i],array_y[i],0])
    else:
        Samples.append([array_x[i],array_y[i],1])
        # plt.plot(array_x[i],array_y[i],'bo')
# print(Samples)

diss = caldis_sample_newpoint(Samples,new_point,'o')
# print(diss)
dis_inds=sort_m(diss,9)#位置
# print(dis_inds)
for ind in dis_inds:
    s=Samples[ind]
    # print(Samples[ind])
    if s[2]==0:
        plt.plot(s[0],s[1],'bd')
    else:
        plt.plot(s[0],s[1],'rs')
plt.plot(new_point[0],new_point[1],'go')

classes=[Samples[ind][2] for ind in dis_inds]
#print(classes)
#统计classes中0和1的数量，如果0多，则new_point类别为0；否则为1
f=0
for i in classes:
    if i==0:
        f=f-1
    elif i==1:
        f=f+1
if f>0:
    new_point.append(1)
elif f<0:
    new_point.append(0)
print(new_point)

#plt.axis对坐标轴进行设置
plt.axis([0,5,0,5])
