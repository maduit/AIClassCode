import numpy as np
import matplotlib.pyplot as plt
def drawline(k,b,linestyle):
    x=np.arange(0,6)
    y=k*x+b
    plt.plot(x,y,linestyle)

def J(k,b,sample):
    return sample[1]-(k*sample[0]+b)
def main():
    rs=np.array([[0,2.5],[1,2.5],[2,2.8],[3,3.5],[4,3.5],[5,3.4]])
    bs=np.array([[0,0.5],[1,1.5],[2,1.8],[3,2],[4,2.5],[5,2.5]])
    plt.plot(rs[:,0],rs[:,1],'r*')
    plt.plot(bs[:,0],bs[:,1],'bs')


    k,b=1,0
    dk=db=0.001
    dJdk=(J(k+dk,b,rs[-1])-J(k,b,rs[-1]))/dk
    dJdb=(J(k,b+db,rs[-1])-J(k,b,rs[-1]))/db
    print(dJdk,dJdb)
    # drawline(k,b,'g--')
    # plt.show()

main()