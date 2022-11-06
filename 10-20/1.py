import numpy as np
import cv2
class map:
    def __init__(self,num_city,num_king):
        self.bg=np.zeros((600,600,3),dtype=np.uint8)
        self.bg[:,:,0]=173
        self.bg[:,:,1]=205
        self.bg[:,:,2]=255

        self.city_img=cv2.resize(cv2.imread('city.png'),(30,30))
        self.kings=[]
        for i in range(num_king):
            tmp=cv2.resize(cv2.imread('hero{}.png'.format(i+1)),(60,60))
            self.kings.append(tmp)
        self.num_city=num_city
        self.num_king=num_king

        self.cx=np.random.randint(30,570,self.num_city)
        self.cy=np.random.randint(30,570,self.num_city)

        self.kx=np.random.randint(30,570,self.num_king)
        self.ky=np.random.randint(30,570,self.num_king)
        self.control_list=-1

    def calcontrol(self):
        self.control_list=[]
        for i in range(self.num_city):
            diss=[]
            for j in range(self.num_king):
                dis=(self.cx[i]-self.kx[j]**2+self.cy[i]-self.ky[j])**2
                diss.append(dis)
            closest_king_ind=np.argmin(np.array(diss))
            self.control_list.append(closest_king_ind)
    def visual(self):
        self.img=self.bg.copy()
        for ind in range(self.num_city):