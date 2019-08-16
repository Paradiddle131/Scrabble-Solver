from __future__ import print_function
import cv2 as cv
import imutils
import numpy as np
import random as rng
from Sandbox.ShapeDetectorClass.shapedetector import ShapeDetector

rng.seed(12345)

def thresh_callback(threshold):
    canny_output = cv.Canny(src_gray, threshold, threshold * 2)
    contours, hierarchy = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    for i in range(len(contours)):
        if hierarchy[0][0][3] == -1:
            color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
            cv.drawContours(drawing, contours, i, color, 2, cv.LINE_8, hierarchy, 0)
        # mask = cv.inRange(src, lower, upper)
        # output = cv.bitwise_and(image, image, mask=mask)
        # # show the images
        # cv.imshow("images", np.hstack([image, output]))
    # print(contours)
    # sd = ShapeDetector()
    # for c in contours:
    #     M = cv2.moments(c)
    #     cx = int((M["m10"] / M["m00"]) * ratio)
    #     cy = int((M["m01"] / M["m00"]) * ratio)
    #     shape = sd.detect(c)
    #
    #     c = c.astype("float")
    #     c *= ratio
    #     c = c.astype("int")
    #     cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    #     cv2.putText(image, shape, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
    #
    #     cv2.imshow("Image", image)
    #     cv2.waitKey(0)
    cv.imshow('Contours', drawing)


src = cv.imread("game_screen2.jpg")
# src = cv.imread("Sandbox/game_ss.PNG")

src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
src_gray = cv.blur(src_gray, (3,3))
src_gray = src_gray[45:440]

window_name = 'Source'
cv.namedWindow(window_name)
cv.imshow(window_name, src)
max_thresh = 255
thresh = 190 # initial threshold
cv.createTrackbar('Canny Thresh:', window_name, thresh, max_thresh, thresh_callback)
thresh_callback(thresh)



cv.waitKey()
