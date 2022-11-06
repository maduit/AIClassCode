import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
# 一元一次函数图像
# x = np.arange(-10, 10, 0.1)#生成等差数组
# y = 2 * x
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title("一元一次函数")
# plt.plot(x, y)
# plt.show()
#正弦函数
# x = np.arange(-3 * np.pi, 3 * np.pi, 0.1)
# y = 2*x+x*np.sin(x)*np.cos(x)
# y1=2+np.sin(x)*np.cos(x)+x*np.cos(x)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title("正弦函数")
# plt.plot(x, y)
# plt.plot(x, y1)
# plt.show()
x=np.linspace(0,10,50)
y = 2*x+x*np.sin(x)*np.cos(x)
y1=2+np.sin(x)*np.cos(x)+x*np.cos(x)
plt.plot(x, y)
plt.plot(x, y1)
plt.show()