import cv2
import numpy as np

def gen(height: int, width: int, num: int):
    #define smallest width to generate the pic
    w=np.power(2,num)*1
    h=w
    step=1
    side=1
    pic=np.zeros((h+2*side,w+2*side,4),np.uint8)
    for j in range(np.power(2,num-1)):
        pic[side:side+h,side+2*j*step:side+2*j*step+step,0:4]=255
        pic[side:side+h,side+2*j*step+step:side+2*j*step+2*step,0:4]=0
    pic=cv2.resize(pic,(2*side+width,2*side+height),interpolation=cv2.INTER_NEAREST)
    return pic