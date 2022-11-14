#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# img1 = cv.imread('/images/hummingbird_from_pixabay.png')

# img = cv.imread('images/hummingbird_from_pixabay.png')
# img2 = cv.imread('C:/users/flori/Documents/DBV_Programming/ex2/code02/images/hummingbird_from_pixabay.png')

test_img = np.ndarray([4,1,3],np.uint8)
test_img[0][0]=[255,0,0]
test_img[1][0]=[0,255,0]
test_img[2][0]=[0,0,255]
test_img[3][0]=[255,255,255]

gray = cv.cvtColor(test_img,cv.COLOR_RGB2GRAY)

z = 0