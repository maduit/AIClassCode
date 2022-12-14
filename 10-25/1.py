import numpy as np
import matplotlib.pyplot as plt

def euclDistance(v1,v2):
    return np.sqrt(sum((v2-v1)**2))

def initCentroids(data,k):
    numSamples,dim=data.shape
    centroids=np.zeros((k,dim))
    for i in range(k):
        index = int(np.random.uniform(0,numSamples))
        centroids[i,:] = data[index,:]
    return centroids

def kmeans(data,k):
    numSamples=data.shape[0]
    clusterData=np.array(np.zeros((numSamples,2)))
    clusterChanged=True
    centrodis=initCentroids(data,k)
    while clusterChanged:
        clusterChanged=False
        for i in range(numSamples):
            minDist=100000.0
            minIndex=0
            for j in range(k):
                distance=euclDistance(centrodis[j,:],data[i,:])
                if distance<minDist:
                    minDist=distance
                    clusterData[i,1]=minDist
                    minIndex=j
            if clusterData[i,0] != minIndex:
                clusterChanged=True
                clusterData[i,0]=minIndex
        for j in range(k):
            cluster_index = np.nonzero(clusterData[:,0] == j)
            pointsInCluster=data[cluster_index]
            centrodis[j,:]=np.mean(pointsInCluster,axis=0)
    return centrodis,clusterData

def showCluster(data,k,centrodis,clusterData):
    numSamples,dim=data.shape
    if dim != 2:
        print('dimension of your data is not 2!')
        return 1
    mark=['oy','ob','og','ok','^r','+r','dr','<r','pr']
    if k>len(mark):
        print('your k is too large!')
        return 1
    for i in range(numSamples):
        markIndex=int(clusterData[i,0])
        plt.plot(data[i,0],data[i,1],mark[markIndex])

    mark = ['*y','*b','*g','*k','^r','+r','sb','db','<b','pb']
    for i in range(k):
        plt.plot(centrodis[i,0],centrodis[i,1],mark[i],markersize=20)
    plt.show()

if __name__ == "__main__":
    k = 5
    data=np.loadtxt(open("E:\\AICode\\10-25\Mall_Customers.csv","rb"),delimiter=",",skiprows=1,usecols=[2,3])
    centroids,clusterData=kmeans(data,k)
    if np.isnan(centroids).any():
        print('Error')
    else:
        print('cluster complete!')
    showCluster(data,k,centroids,clusterData)