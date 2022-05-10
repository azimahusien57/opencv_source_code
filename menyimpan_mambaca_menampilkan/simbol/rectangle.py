# -*- coding: utf-8 -*-
"""
Created on Mon May 10 22:55:12 2021

@author: Lestari
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
#cara2 dalam video campture yg terdetek kotak
cap = cv2.VideoCapture(0)
#cara 1
#membuat gambar hitam
#img=cv2.imread('1.jpg')

#membuat kotak
#img= cv2.rectangle(img,(5,10),(100,50),(0,255,0),0)
#tampilkan gambar
#cv2.imshow('kotak',img)

#cv2. waitKey(0)
#cv2.destroyAllWindows()

#untuk menampilkan matplotlib
#plt.imshow(img)
#plt.show()


while(True):
    rer,frame=cap.read()
    frame=cv2.rectangle(frame,(50,10),(100,50),(0,255,0),3)
    cv2.imshow('kotak',frame)
    if cv2.waitKey(1)==ord('q'):
        break
    cap.release()
    cv2.destroyAllWindows()
