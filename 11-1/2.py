import numpy as np

def sphere(x,y):
    z=x**2+y**2
    return z
def holder_table(x,y):
    z=-np.abs(np.sin(x)*np.cos(y)*np.exp(np.abs(1-np.sqrt(x**2+y**2)/np.pi)))
    return z
fit_fun=holder_table

x_opt,y_opt=10,10
z_opt=fit_fun(x_opt,y_opt)
print(x_opt,y_opt,z_opt)

for ite in range(1000000):
    x=np.random.uniform(-10,10)
    y=np.random.uniform(-10,10)
    z=fit_fun(x,y)
    if z<z_opt:
        x_opt,y_opt,z_opt=x,y,z
        print(x_opt,y_opt,z_opt)
