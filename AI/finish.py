def caldis(a,b,mode):
    if len(a)==len(b):
        if mode=='o':
            s_o=0
            s_o=sum([(a[i]-b[i])**2 for i in range(len(a))])
            return s_o**0.5
        if mode=='m':
            s_m=0
            s_m=sum([abs(a[i]-b[i]) for i in range(len(a))])
            return s_m
    else:
        return -1
def caldis_smaple_newpoint(samples,newpoint,mode):
    diss=[caldis(samples[i],newpoint,mode) for i in range(len(samples))]
    return diss

def sort_m(diss,k):
    if k>=len(diss):
        return -1
    else:
       diss_sorted=sorted(diss)
       inds=[diss.index(diss_sorted[i]) for i in range(k)]
       return inds


samples=[[2,1],[0,1],[0.3,0.7],[0.8,1.2],[0.77,0.963],[1.5,-0.23],[3.3,1.7]]
newpoint=[0,0]
diss=caldis_smaple_newpoint(samples,newpoint,'o')
print(sort_m(diss,3))
