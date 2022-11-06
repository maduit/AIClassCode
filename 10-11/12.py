import numpy as np
import matplotlib.pyplot as plt

x=np.random.uniform(0,5,300)
y=np.random.uniform(0,5,300)

rs,bs=[],[]
for ind in range(len(x)):
    if y[ind]>0.3*x[ind]+1.7:
        rs.append([x[ind],y[ind]])
    else:
        bs.append([x[ind],y[ind]])
        
rs,bs=np.array(rs),np.array(bs)
plt.plot(rs[:,0],rs[:,1],'r*')
plt.plot(bs[:,0],bs[:,1],'bs')



num_err_opt,k_opt,b_opt=10000,0,0
for ite in range(10000):
    k,b=np.random.uniform(-10,10,1),np.random.uniform(-10,10,1)
    if num_err_opt<100:
        k=np.random.uniform(k_opt-1,k_opt+1,1)
        b=np.random.uniform(b_opt-1,b_opt+1,1)
    if num_err_opt<10:
        k=np.random.uniform(k_opt-0.1,k_opt+0.1,1)
        b=np.random.uniform(b_opt-0.1,b_opt+0.1,1)
    rs_err,bs_err=[],[]
    
    for ind in range(len(rs)):
        if rs[ind,1] < k*rs[ind,0]+b:
            rs_err.append([rs[ind,0],rs[ind,1]])
    for ind in range(len(bs)):
        if bs[ind,1] > k*bs[ind,0]+b:
            bs_err.append([bs[ind,0],bs[ind,1]])
            
    num_err=len(rs_err)+len(bs_err)
    if num_err<num_err_opt:
        num_err_opt=num_err
        k_opt,b_opt=k,b
    if (ite+1)%1000==0:
        print(k_opt,b_opt,num_err_opt)
        
x=np.arange(0,6)
y=k_opt*x+b_opt
plt.plot(x,y)
plt.show()





