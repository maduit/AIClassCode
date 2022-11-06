import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def draw_pic(X, Y, Z,z_max, title, z_min=0): 
    fig=plt.figure() 
    ax=Axes3D(fig)
    ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.cm.hot)#ax.contourt(xYZzdir=zoffset=-2cmap=pit.cm.hot ax.set zlim(zminzmax) ax.set_title(title)
    ax.set_zlim(z_min,z_max)
    ax.set_title(title)
    plt.show()

def get_X_AND_Y(X_min,X_max,Y_min,Y_max):
    X=np.arange(X_min,X_max,0.1)
    Y=np.arange(Y_min,X_max,0.1)
    X,Y=np.meshgrid(X,Y)
    return X,Y

def sphere(X_min=-3,X_max=3,Y_min=-3,Y_max=3):
    X,Y=get_X_AND_Y(X_min,X_max,Y_min,Y_max)
    Z=X**2+Y**2
    return X,Y,Z,20,'sphere function'
def hoder_table(X_min=-10,X_max=10,Y_min=-10,Y_max=10):
    X,Y=get_X_AND_Y(X_min,X_max,Y_min,Y_max)
    Z=np.abs(np.sin(X)*np.cos(Y)*np.exp(np.abs(1-np.sqrt(X**2+Y**2)/np.pi)))
    return X,Y,Z,0,'table function'

def main():
    Z_min=None
    X,Y,Z,Z_max,title=sphere()
    draw_pic(X,Y,Z,Z_max,title,Z_min)

main()
# #plt.savefig(".ImyProject/Algorithm/pic/%spng%title)#保存图片 plt.show
# def get XAND_Y(XminXmax,Y_minY_max) X=np.arange(X_min,X_max,0.1) Y=np.arange(Y_minY_max.1) X,Y=np.meshgrid(XY) retum x Y
# #rastrigin测试两数
# def Rastrigin(X_min=-5.52,X_max=5.12Y_min=-5.12Ymax=5.12) A=10
# X,Y=get X AND_Y(X_min,X_max,Y_min,Y_max)
# Z=2*A+X**2-A*np.cos(2*nppi*X)+Y**2-A*np.cos(2*nppi*Y) retum x Yz100,"Rastrigin function
# #Ackley测试函数
# defAckley(X_min=-5Xmax=5Y_min=-5Ymax=5) XY=get XAND Y(X minX maxYminYmax Z=-20*np.exp(-0.2*p.sqrt(0.5*(X**2+Y**2))) - \
# np.exp(0.5*(np.cos(2*np.pi*X)+np.cos(2*nppi*Y)))+np.e+20 retun xY15"Ackley function
# #Sphere测试两数
# def Sphere(X min=-3Xmax=3Ymin=-3Ymax=3): X,Y=get_X_AND_Y(X_min,X_max,Y_min,Y_max) Z=x**2+Y**2
# return x Y z 20, "Sphere function"