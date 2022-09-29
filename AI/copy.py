
def caldis(a,b,mode):
    if len(a)==len(b):
        if mode=='o':
            s_o=0
            # for i in range(len(a)):
            #     s_o+=(a[i]-b[i])**2
            s_o=sum([(a[i]-b[i])**2 for i in range(len(a))])
            return s_o**0.5
        if mode=='m':
            s_m=0
            # for i in range(len(a)):
            #     s_m+=abs(a[i]-b[i])
            s_m=sum([abs(a[i]-b[i]) for i in range(len(a))])
            return s_m
    else:
        return -1
# a=[1,2,3,5,9]
# b=[5,6,7,9,1]
# d_o=caldis(a,b,'o')
# print(d_o)
# d_m=caldis(a,b,'m')
# print(d_m)

def caldis_smaple_newpoint(samples,newpoint,mode):
    # diss=[]
    # for i in range(len(samples)):
    #     s=samples[i]
    #     diss.append(caldis(s,newpoint,'o'))
    diss=[caldis(samples[i],newpoint,mode) for i in range(len(samples))]
    return diss

def sort_m(diss,k):
    if k>=len(diss):
        return -1
    else:
       diss_sorted=sorted(diss)
       for i in range(k):
           d=diss_sorted[i]
           pos_d=diss.index(d)
           print('元素{}在diss中的位置{}'.format(d,pos_d))
    #    inds=[diss.index(diss_sorted[i]) for i in range(k)]
    #    return inds


samples=[[2,1],[0,1],[0.3,0.7],[0.8,1.2],[0.77,0.963],[1.5,-0.23],[3.3,1.7]]
newpoint=[0,0]
# print(caldis_smaple_newpoint(samples,newpoint,'o'))
# print(caldis_smaple_newpoint(samples,newpoint,'m'))
diss=caldis_smaple_newpoint(samples,newpoint,'o')
print(sort_m(diss,3))
