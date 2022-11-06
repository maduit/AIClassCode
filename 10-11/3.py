import numpy as np
from matplotlib import pyplot as plt
x=np.array([i*0.1 for i in range(101)])
dfx=2+np.sin(x)*np.cos(x)+x*np.cos(x)

dx=0.001

fx= 2*x+x*np.sin(x)*np.cos(x)
fx2=2*(x+dx)+(x+dx)*np.cos((x+dx))*np.sin((x+dx))

dfx2=(fx2-fx)/dx


plt.figure(1)
plt.plot(x,fx)
plt.xlabel('x')
plt.ylabel('f(x)')

plt.figure(2)
plt.plot(x,dfx,'r:')
plt.plot(x,dfx2,'b.')
plt.xlabel('x')
plt.ylabel('df(x)/dx')
plt.legend(['dfx','dfx2'])
plt.show()