# -*- coding: utf-8 -*-
"""
Created on Mon May 10 22:42:00 2021

@author: Lestari
"""

#membuat garis

import cv2
import numpy as np
from matplotlib import pyplot as plt

# buat koodinat
img= np.zeros((512,512,3),np.uint8)
#fungsi garis
img = cv2.line(img,(0,0),(511,511),(255,0,0),3)
#menanmpilkan gambar
#plt.imshow(img)
#plt.show()
cv2.imshow('line',img)
cv2.waitKey(0)
cv2.destroyAllWindows()