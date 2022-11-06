import numpy as np
from matplotlib import pyplot as plt

def f(x):
    return np.sin(x)
dx=0.001
x=np.linspace(0,10,int(10.0/dx)+1)

gx=np.cumsum(f(x)*dx)
print(gx)
plt.plot(x,gx,'r:')
plt.plot(x,-np.cos(x),'bo')
plt.show()
# print(f(x)*dx)
# np.bum(f(x)*dx)