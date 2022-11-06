from re import A
import cv2
import numpy as np

def visual(bg,bird,x,y):
    h1,w1=bg.shape[0],bg.shape[1]
    h2,w2=bird.shape[0],bird.shape[1]
    bg[x-int(h2/2):x+int(h2/2),y-int(w2/2):y+int(w2/2)]=bird
    return bg

bg=np.zeros((600,600,3),dtype=np.uint8)+255
bird=cv2.resize(cv2.imread('E:\\AICode\\10-27\\bird.png'),(40,40))
grass=cv2.imread('E:\\AICode\\10-27\\grass.png')
x,y=20,300
v=5
a=1
while True:
    v+=a
    x+=v
    # x+=5

    if x>=570 or x<20:
        break
    outing=visual(bg.copy(),bird.copy(),x,y)
    cv2.imshow('bird3',outing)
    key=cv2.waitKey(30)
    if key==ord(' '):
        v=-20
    # cv2.waitKey(10)
cv2.destroyAllWindows()
# bg=np.zeros((800,800,3),dtype=np.uint8)
# bird=cv2.imread('bird.png')

#     # cv2.imshow('bird',bg)
#     # cv2.waitKey()
# cv2.destroyAllWindows()