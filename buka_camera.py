# -*- coding: utf-8 -*-
"""
Created on Mon May 10 02:18:32 2021

@author: Lestari
"""

#import library open cv
import cv2

# variabel untuk videocamp
cap = cv2.VideoCapture(0)

# fungsi untuk membuat frame pengaturan pada video
while(True): 
    #membaca video
    ret, frame=cap.read()
    #menampilkan video realtime
    cv2.imshow('frame',frame)
    #pengaturan frame
    if cv2.waitKey(1)== ord('q'):
        break
    #didalam release kasi angka
    cap.release()
    cv2.destroyAllWindows()
    

