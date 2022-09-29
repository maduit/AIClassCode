#两行四列
# import numpy as np
# x=np.array([[1,2,3,5],[4,5,6,10]])
# print(x.shape)

#数组行数
# import numpy as np
# x=np.array([[1,2,3,5],[4,5,6,10]])
# print(x.shape[0])

#数组列数
# import numpy as np
# x=np.array([[1,2,3,5],[4,5,6,10]])
# print(x.shape[1])

#数组列数
# import numpy as np
# x=np.array([[1,2,3,5],[4,5,6,10]])
# print(x.shape[-1])

# 对于图像来说：

# image.shape[0]——图片高

# image.shape[1]——图片长

# image.shape[2]——图片通道数

# 而对于矩阵来说：

# shape[0]：表示矩阵的行数

# shape[1]：表示矩阵的列数

# import numpy as np

# A=[1,3,5]
# print(np.tile(A,(5,3))) 

# print(2**8)

# import numpy as np
# a=[1,5,3,8,9,4,6]
# s=np.argsort(a)
# for i in range(3):
#     print(s[i])
# ls=['aa','b','c','ddd','aa']

# cou={} #创建一个空字典
# for i in ls:
#     cou[i]=cou.get(i,0)+1     #之后称其为get的赋值语句，目的是新建字典键值对
    
#     '''
#     赋值语句代码等价于
#     cou[i]=0
#     cou[i}=cou[i]+1
#     '''
# print(cou)
# import numpy as np
# np.random.seed(10)

# L1 = np.random.randn(3, 3)
# L2 = np.random.randn(3, 3)
# print(L1)
# print(L2)
# s= 'www.dod.com.cn'
# 默认分隔符
# print(s.split())
#  . 分割
# print(s.split("."))
#  分割一次   2次
# print(s.split('.',1))
# print(s.split('.',2))
# # 取出被 . 分割的下标为1的字符串
# print(s.split('.',2)[1])
# # 分割最多次实际与不加参数一样（默认分割富一样）
# print(s.split('.',-1))
# #分割三次并将分割的字符串保存到三个文件内
# s1,s2,s3=s.split('.',2)
# print(s1)
# print(s2)
# print(s3)
# 去掉换行符  \n  \t
# c = '''hello
#     world'''
# print(c)
# print(c.split('\n'))
# print(c.split('\t'))

# 分离文件名和路径
#os.path.split()：按照路径将文件名和路径分割开
# import os
# print(os.path.split('/dodo/soft/python/'))
# print(os.path.split('/dodo/soft/python'))

#超级实例列举
# a= 'hello boy<[www.dodo.com.cn]>byebye'
# 已[分割
# print(a.split('['))
# 以【分割后取值下标为1的值，然后再次已】分割取下标为0的值
# print(a.split('[')[1].split(']')[0])
# 以【分割后取值下标为1的值，然后再次以】分割取下标为0的值在次以。分割
# print(a.split('[')[1].split(']')[0].split('.'))

import matplotlib.pyplot as plt
# plt.plot([0,1,2,3],[4,5,6,7],'o')

        # self.draw_color=['b','r','g']
        # self.draw_mark=['d','s','o']
# s=[1,2,3,2,3]
# print(s[:2])
'''
在python的画图plt.figure函数中,
如果使用plt.figure(1)表示定位（创建）第一个画板
,如果没有参数默认创建一个新的画板
'''
plt.figure(1)
