import cv2 as cv
import numpy as np

img = cv.imread("bizarre_shape.png")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
threshold = cv.threshold(img_gray, 100, 255, 0)
M = cv.moments(img_gray)

