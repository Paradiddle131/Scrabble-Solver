from __future__ import print_function
import cv2 as cv
import numpy as np
import random as rng
import sys

def avg(lst):
    return int(sum(lst) / len(lst))

# def listSquares(cnts, corners):
#     with open("squares_list.txt", "w+") as output:
#         output.write(str(sorted(cnts)))
#         output.write("\n")
#         output.writelines(corners)
list_corners = []
list_squares = []
def listSquares(cnts):
    for i in range(0, len(cnts), 2):
        list_squares.append([cnts[i][0][0], cnts[i][0][1]])
    print("list_squares: ", list_squares)

def isSquare(cnts, count):
    if count % 4 == 0:
        cnts = cnts[0]
        list_cnts, points1, points2 = ([] for i in range(3))
        c1, c2, c3, c4 = [0]*4
        for i in range(len(cnts)):
            list_cnts.append([cnts[i][0][0], cnts[i][0][1]])
        for i in range(len(list_cnts)):  # 8
            points1.append(list_cnts[i][0])
            points2.append(list_cnts[i][1])
        points1.sort()
        points2.sort()
        c1 = avg(points1[:4])
        c2 = avg(points1[4:])
        c3 = avg(points2[:4])
        c4 = avg(points2[4:])
        if abs(c1 - c2) - abs(c3 - c4) < 5:
            list_corners.append([c1, c2, c3, c4])
        # if abs(c1 - c2) - abs(c3 - c4) < 5:
        #     print("Square")
        # else:
        #     print("Not Square")
        count += 1
        return True if abs(c1 - c2) - abs(c3 - c4) < 5 else False

def findLongest(cnts):
    # sort square lists
    for i in cnts:
        i.sort()
    print(cnts)
    # print("list_corners: ", cnts)
    # print("list_corners: ", sorted(cnts))
    # print("list_corners: ", sorted(cnts[1]))

def thresh_callback(threshold):
    f = open("contours.txt", "w+")
    # canny_output = cv.Canny(src_gray, threshold, threshold * 2)[:90]
    canny_output = cv.Canny(src_gray, threshold, threshold * 2)
    contours, hierarchy = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # print("contours: ", contours)
    print(contours[0].tolist())
    print(contours[0][0][0])
    print("len(contours)): ", len(contours))
    print("len(contours[0])): ", len(contours[0]))

    print(type(contours[0][0][0]))
    print(contours[0][0][0].tolist())
    print(type(contours[0][0][0].tolist()))
    point = contours[0][0][0].tolist()
    cnts_list = contours[0].tolist()
    print("shape: ", src.shape)
    for i in contours[0][0]:
        print(i)
        x = i[0]
        y = i[1]
    minn = max(src.shape[:2])
    maxx = min(src.shape[:2])
    print(maxx)
    print(minn)
    # for i in range(len(contours)):  # 16
    #     for j in range(len(contours[i])):  # 8
    #         if

    with open("file.txt", "w+") as output:
        output.write(str(sorted(cnts_list)))

    square_count = 0
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    # shape_count = int(len(contours)/4)
    # square_count = int(len(contours)/4)
    # rectangle_count = int(len(contours)/4)
    # print(drawing.shape)
    # print(len(contours[:7]))
    # print("shape_count: ", shape_count)
    # print("square_count: ", square_count)
    # print("rectangle_count: ", rectangle_count)
    for i in range(len(contours)):
        try:
            if isSquare(contours[i:i+4], i):
                square_count += 1
                color = (250, 250, 100)
                cv.drawContours(drawing, contours, i, color, 2, cv.LINE_8, hierarchy, 0)
        except:
            pass
    print("There are ", square_count, " squares.")
    print("list_corners: ", list_corners)
    print("list_corners: ", sorted(list_corners))
    print("list_corners: ", sorted(list_corners[0]))
    findLongest(list_corners)
    # findLongest(contours)
    cv.imshow('Contours', drawing)
    listSquares(contours[0].tolist())
    print(contours)

# src = cv.imread("single_square.png")
# src = cv.imread("game_screen2.jpg")
src = cv.imread("400x400_rgb.png")
# src = cv.imread("game_ss.png")

src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
src_gray = cv.blur(src_gray, (3,3))

window_name = 'Source'
cv.namedWindow(window_name)
cv.imshow(window_name, src)
max_thresh = 255
thresh = 150 # initial threshold
cv.createTrackbar('Canny Thresh:', window_name, thresh, max_thresh, thresh_callback)
thresh_callback(thresh)

cv.waitKey()