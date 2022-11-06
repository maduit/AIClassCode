import numpy as np
import matplotlib.pyplot as plt
def drawline(k,b,linestyle):
    x=np.arange(0,6)
    y=k*x+b
    plt.plot(x,y,linestyle)
def main():
    x,y=np.random.uniform(0,5,300),np.random.uniform(0,5,300)
    #y=0.3x+1.7
    rs,bs=[],[]
    for ind in range(len(x)):
        if  y[ind]>0.3*x[ind]+1.7:
            rs.append([x[ind],y[ind]])
        else:
            bs.append([x[ind],y[ind]])
    rs,bs=np.array(rs),np.array(bs)
    plt.plot(rs[:,0],rs[:,1],'r*')
    plt.plot(bs[:,0],bs[:,1],'bs')

    err_count_opt=10000
    for ind in range(10000):
        k,b=np.random.uniform(0,5),np.random.uniform(0,5)
        err_count=0
        for point in rs:
            if point[1]<=k*point[0]+b:
                err_count+=1
        for point in bs:
            if point in bs:
                if point[1]>k*point[0]+b:
                    err_count+=1

        if err_count<err_count_opt:
            err_count_opt=err_count
            k_opt=k
            b_opt=b
    drawline(k_opt,b_opt,'g--')
    plt.show()

main()