import numpy as np

def sphere(x,y):
    z=x**2+y**2
    return z
def holder_table(x,y):
    z=-np.abs(np.sin(x)*np.cos(y)*np.exp(np.abs(1-np.sqrt(x**2+y**2)/np.pi)))
    return z
fit_fun=holder_table
n=20
p_lopt=np.random.uniform(-10,10,(n,2))
p=p_lopt
z_lopt=fit_fun(p_lopt[:,0],p_lopt[:,1])
z_gopt=np.min(z_lopt[np.argmin(z_lopt)])
p_gopt=p_lopt[np.argmin(z_lopt)]
print(p_lopt,z_lopt,z_lopt)


for ite in range(1000):
    v=np.random.uniform(-0.01,0.01,(n,2))
    v+=0.5*np.random.uniform(-1,1)*(p_lopt-p)
    v+=0.3*np.random.uniform(-1,1)*(p_gopt-p)
    p+=v

    p=np.clip(p,-10)