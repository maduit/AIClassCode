import numpy as np
import matplotlib.pyplot as plt

def f(x,x_low,x_up,x_low_new,x_up_new):
    return x_low_new+(x_up_new-x_low_new)*(x-x_low)/(x_up-x_low)

x_low =-5
x_up=5
x=np.arange(x_low,x_up,0.01)
x_norm = f(x,x_low,x_up,3,5)
plt.plot(x,x_norm)
plt.show()