import numpy as np
import matplotlib.pyplot as plt

x=np.random.uniform(0,5,100)
y=np.random.uniform(0,5,100)
#y = 0.3x+1.7

rs,bs=[],[]
for ind in range(len(x)):
    if y[ind]>0.3*x[ind]+1.7:
        rs.append([x[ind],y[ind]])
    else:
        bs.append([x[ind],y[ind]])
rs,bs=np.array(rs),np.array(bs)
# plt.plot(rs[:,0],rs[:,1],'r*')
# plt.plot(bs[:,0],bs[:,1],'bs')

k,b=np.random.uniform(-10,10,1),np.random.uniform(-10,10,1)
rs_err=[]
for ind in range(len(rs)):
    if rs[ind,1]<k*rs[ind,0]+b:
        rs_err.append([rs[ind,0],rs[ind,1]])
# rs_err=np.array(rs_err)
# plt.plot(rs_err[:,0],rs_err[:,1],'g*')


bs_err=[]
for ind in range(len(bs)):
    if bs[ind,1]<k*bs[ind,0]+b:
        bs_err.append([bs[ind,0],bs[ind,1]])
# bs_err=np.array(bs_err)
# plt.plot(bs_err[:,0],bs_err[:,1],'ys')


num_err=len(rs_err)+len(bs_err)
print(k,b,num_err)
# x=np.arange(0,6)
# y=k*x+b
# plt.plot(x,y)
# plt.show()