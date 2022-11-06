import numpy as np
import matplotlib.pyplot as plt
def cross(father,mother):
    tmp=father[:3]
    father[:3]=mother[:3]
    mother[:3]=tmp
    return father,mother

father=[0,0,0,0,0,0,0,0]
mother=[1,1,1,1,1,1,1,1]
def vary(x):
    if np.random.uniform(0,1)>0.8:
        pos=np.random.randint(0,len(x))
        x[pos]=1-x[pos]
    return x
f_new=vary(father)
print(f_new)

n=4

def bin_encode(x,n):
    result=np.round((x*(x**n-1))).astype(np.int)
    