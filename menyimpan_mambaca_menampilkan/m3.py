# -*- coding: utf-8 -*-
"""
Created on Mon May 10 01:59:38 2021

@author: Lestari
"""

import cv2

#membaca gambar
img=cv2.imread('10.jpg')
#menampilkan gambar
cv2.imshow('person',img)
#menyimpan gambar
cv2.imwrite('save_person.png',img)

#menunda windows terdestroy
cv2.waitKey(0)
#mendestroy windows
cv2.destroyAllWindows()