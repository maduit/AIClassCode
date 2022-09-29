import numpy as np
def distance(diss):
    k=3
    diss_sorted=sorted(diss)

    # for i in range(k):
        # d=diss_sorted[i]
        # index_d=diss.index(d)
        # print('元素{}在diss中的位置是{}'.format(d,index_d))
    s=np.argsort(diss)
    for i in range(k):
        print('元素{}在diss中的位置是{}'.format(diss[s[i]],s[i]))
if __name__=='__main__':
    a=[0,2,3,1,4,7,1]
    distance(a)