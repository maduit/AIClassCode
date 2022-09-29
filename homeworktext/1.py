import matplotlib.pyplot as plt

f = open('E:\\AICode\\homeworktext\\customdata.txt')

customdata = f.readlines()

customdata = [s.split('\n')[0] for s in customdata]
a=[]
b=[]

# for s in customdata:
#    customdata.append(s.split('\n')[0])
# print(a)

customdata = [customdata[i].split('\t') for i in range(1,len(customdata))]
# for i in range(1,len(customdata)):
#     a.append(customdata[i].split('\t'))
# print(a)
#     print(customdata[i].split('\t'))
# print(customdata)
Samples = [[float(c[0]), float(c[1]), int(c[2])] for c in customdata]
# for c in customdata:
#     a.append(float(c[0]))
#     a.append(float(c[1]))
#     a.append(int(c[2]))
#     b.append(a)
#     a=[]
# print(b)
for s in Samples:

    if s[2]==0:

        plt.plot(s[0],s[1],'rs')

    else:

        plt.plot(s[0], s[1], 'bd')

plt.show()

'''
计算两个向量a,b之间的距离
'''
def cal_dis_twopoints(a,b,mode):
    if len(a)!=len(b):return -1
    if mode=='o':
        res=[(a[i]-b[i])**2 for i in range(len(a))]
        return sum(res)**0.5
    if mode=='m':
        res=[abs(a[i]-b[i]) for i in range(len(a))]
        return sum(res)


'''
定义KNN类的初始化函数
'''
class KNN():
    def __init__(self,k,dis_mode,samples):
        self.k=k
        self.dis_mode=dis_mode
        self.samples_org=samples
        #将原始数据归一化至[0,1]区间内，以统一量纲
        self.min_age=min([s[0] for s in self.samples_org])
        self.max_age=max([s[0] for s in self.samples_org])
        self.min_salary=min([s[1] for s in self.samples_org])
        self.max_salary=max([s[1] for s in self.samples_org])
        self.samples=[]
        for s in self.samples_org:
            age=(s[0]-self.min_age)/(self.max_age-self.min_age4)
            salary=(s[1]-self.min_salary)/(self.max_salary-self.min_salary)        
            self.samples.append([age,salary,s[2]])

        self.draw_color=['b','r','g']
        self.draw_mark=['d','s','o']
    