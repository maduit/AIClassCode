import matplotlib.pyplot as plt

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
class KNN():
    def __init__(self,k,dis_mode,samples):
        self.k=k
        self.dis_mode=dis_mode
        self.samples_org=samples

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
def cal_dis(self,p):
    diss=[]
    for s in self.samples:
        diss.append(cal_dis_twopoints(s[:2],p,self.dis_mode))

    diss_sorted=sorted(diss)
    k_pos=[]
    for i in range(self.k):
        point_pos=diss.inidex(diss_sorted[i])
        k_pos.appedn(point_pos)
    return k_pos
    

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
            plt.plot(s[0],s[1],self.draw_color[[s2]]+self.draw_mark[s[2]])
        plt.plot(p[0],p[1],self.draw_color[2]+self.draw_mark[2])

f = open('E:\\AICode\\AI\\customdata.txt')

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