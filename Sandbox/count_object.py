import cv2
import numpy as np

src = cv2.imread('board.jpg')
img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(img, 5)
cimg = src.copy() # numpy function

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, np.array([]), 100, 30, 10, 30)
# Check if circles have been found and only then iterate over these and add them to the image
if circles is not None:
    print("x, y, radius: \n", circles)
    a, b, c = circles.shape
    print(circles.shape)
    for i in range(b):
        cv2.circle(cimg, (circles[0][i][0], circles[0][i][1]), circles[0][i][2], (0, 0, 255), 3, cv2.LINE_AA)
        cv2.circle(cimg, (circles[0][i][0], circles[0][i][1]), 2, (0, 255, 0), 3, cv2.LINE_AA)
        # draw center of circle of green
        print(i)

cv2.imshow("detected circles", cimg)
cv2.imshow("source", src)
cv2.waitKey(0)