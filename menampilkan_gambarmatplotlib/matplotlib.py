# -*- coding: utf-8 -*-
"""
Created on Mon May 10 02:05:49 2021

@author: Lestari
"""

import cv2
#import matplotlib
from matplotlib import pyplot as plt

#membaca gambar
img= cv2.imread('10.jpg')
# menampilkan gambar dengan matplotlib
plt.imshow(img)

#fungsi menyembunhikan sumbu x dan y
plt.xticks([]),plt.yticks([])
plt.show()
