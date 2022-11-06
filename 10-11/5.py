import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 3*x**3 + 2*x**2.5 + np.exp(4*x)

def df(x):
    return 9*x**2 + 5*x**1.5 + 4*np.exp(4*x)

x=np.linspace(0,10,101)
fx=f(x)
fx1=f(x+0.001)
dfx=df(x)
dfx1=f(fx1-fx)/0.001
plt.plot(x,fx)
plt.plot(x,dfx1,'r:')
plt.plot(x,dfx,'b.')
plt.legend(['fx,dfx1,fdx'])
plt.show()