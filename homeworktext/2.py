from numpy import *
import matplotlib.pyplot as plt

f = open('E:\\AICode\\homeworktext\\customdata.txt')
customdata = f.readlines()

customdata = [s.split('\n')[0] for s in customdata]

customdata = [customdata[i].split('\t') for i in range(1,len(customdata))]

Samples = [[float(c[0]), float(c[1]), int(c[2])] for c in customdata]

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
            age=(s[0]-self.min_age)/(self.max_age-self.min_age)
            salary=(s[1]-self.min_salary)/(self.max_salary-self.min_salary)        
            self.samples.append([age,salary,s[2]])

        self.draw_color=['b','r','g']
        self.draw_mark=['d','s','o']

    def cal_dis(self,p):
        diss=[]
        for s in self.samples:
            diss.append(cal_dis_twopoints(s[:2],p,self.dis_mode))

        diss_sorted=sorted(diss)
        k_pos=[]
        for i in range(self.k):
            point_pos=diss.index(diss_sorted[i])
            k_pos.append(point_pos)
        return k_pos
    '''
    对最近的k个点的类别进行统计,以此来预测新点
    '''
    def classify(self,k_pos):
        classes=[self.samples[pos][2] for pos in k_pos]
        num1=sum(classes)
        num0=len(k_pos)-num1

        class_pred=0
        if num1>num0:
            class_pred=1
        return class_pred

    def draw(self,p,k_pos,class_pred):
        plt.figure(1)
        for s in self.samples_org:
            plt.plot(s[0],s[1],self.draw_color[s[2]]+self.draw_mark[s[2]])
        plt.plot(p[0],p[1],self.draw_color[2]+self.draw_mark[2])

        plt.figure(2)
        plt.plot(p[0],p[1],self.draw_color[class_pred]+self.draw_mark[class_pred])
        for pos in k_pos:
            s=self.samples_org[pos]
            plt.plot(s[0],s[1],self.draw_color[s[2]]+self.draw_mark[s[2]])
            plt.plot([s[0],p[0]],[s[1],p[1]],self.draw_color[s[2]]+'--')

    def run(self,p):
        #对p进行归一化
        age=(p[0]-self.min_age)/(self.max_age-self.min_age)
        salary=(p[1]-self.min_salary)/(self.max_salary-self.min_salary)
        p_input=[age,salary]
        k_pos=self.cal_dis(p_input)
        print(k_pos)
        class_pred=self.classify(k_pos)
        self.draw(p,k_pos,class_pred)
# Samples=[['张三',31,300000],['李四',55,10000000],['王五',22,120000000]]
knn=KNN(9,'o',samples=Samples)
knn.run([31,300000])
knn.run([55,10000000])
knn.run([22,120000000])