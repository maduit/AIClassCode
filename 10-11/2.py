import numpy as np
from matplotlib import pyplot as plt
x=np.array([i*0.1 for i in range(101)])
y = 2*x+x*np.sin(x)*np.cos(x)
plt.plot(x, y)
plt.show()