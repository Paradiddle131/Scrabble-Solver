import math
import sys
import cv2
import imutils
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def writeArrayTxt(array, filename):
    f = open("{}.txt".format(filename), "w+")
    for i in range(len(array)):
        for j in range(len(array[i])):
            f.write(str(array[i][j]) + " ")
        f.write("\n")
    f.close()


def showArrayImage(array, filename):
    img = Image.fromarray(array)
    img.save('{}.png'.format(filename))


np.set_printoptions(threshold=sys.maxsize)
image = cv2.imread("game_ss3.png")[96:476]
boundaries = [
    ([255, 255, 255], [255, 255, 255]),
    # ([82, 56, 255], [189, 180, 255])
]
output = []
for i, (lower, upper) in enumerate(boundaries):
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)
    # region Write & Show
    # cv2.imwrite('Write/detected_{}.png'.format(i), np.hstack([image, output])[:, 466:])
    # cv2.imshow("images", np.hstack([image, output])[:, 466:])
    # cv2.waitKey(0)
    # endregion

image = np.hstack([image, output])[:, 466:]
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 120, 250)

cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
mask = np.ones(image.shape[:2], dtype="uint8") * 255

white = 255
black = 0
# im = Image.open('Write/detected_0.png')

longestH, longestV, CountConsecutive = [0] * 3
board = np.zeros((38, 46)).astype(int)


# def findIntervals(y, x):
#     ty, tx = y, x
#     if gray[y][x] == 255:

# def searchBoxes():
#     global ny, nx
#     count, countW, countB, horizontal, vertical, L, countL, countH, currentB = [0] * 9
#     countWH, countWV = [1] * 2
#     for y in range(len(gray)):
#         for x in range(len(gray[0])):
#             try:
#                 tx, ty = x, y
#                 if gray[y][x] == 255:
#                     while gray[y][x + 1] != 0:
#                         x += 1
#                         countWH += 1  # 33
#                     cx = int(math.ceil(countWH / 2))  # x + 16
#                     nx = x - cx
#                     while gray[y + 1][nx] != 0:
#                         y += 1
#                         countWV += 1  # 33
#                     cy = int(math.ceil(countWV / 2))
#                     ny = y - cy
#                     # region Count Blocks
#                     L, currentB = [0] * 2
#                     # region Draw Grid Circle
#                     if gray[ny][nx] == 0:
#                         cv2.circle(img=gray, center=(nx, ny), radius=1, color=(255, 0, 0), thickness=3)
#                     elif gray[ny][nx] == 255:
#                         cv2.circle(img=gray, center=(nx, ny), radius=1, color=(0, 0, 0), thickness=3)
#                     # endregion
#                     for a in range(-16, 16):
#                         p = gray[ny][nx + a]
#                         if -3 < a < 3 and p == 0:
#                             currentB += 1
#                         L += int(p / 255)
#                         if p == 0:
#                             countB += 1
#                     if L > 14:
#                         countW += 1
#                         board[round(ny / 10)][round(nx / 10)] = 1
#                     # if 1 < L < 22 and not (
#                     #         gray[ny][nx + 14] == 255 and gray[ny][nx - 18] == 255):
#                     #     countL += 1
#                     #     board[round(ny / 10)][round(nx / 10)] = 2
#                     # if gray[ny][nx + 13] == 255 and gray[ny][nx - 15] == 255 and gray[ny][nx] == 0:
#                     if 2 < L < 6 and gray[ny][nx] == 0 and (currentB == 5):
#                         countH += 1
#                         board[round(ny / 10)][round(nx / 10)] = 3
#                     # endregion
#                     # region Count Consecutive Blocks
#
#                     # endregion
#                 if tx != x:
#                     y = ty
#             except:
#                 pass
#
#         y += 33
#     # region Print
#     print("Boxes: ", countW)
#     # print("Letters:", countL)
#     print("Hearts:", countH)
#     # endregion

def countConsecutiveBoxes():
    count, countW, countB, horizontal, vertical, L, countL, countH, currentB = [0] * 9
    for y in range(15, len(gray), 35):
        for x in range(0, len(gray[0]), 35):
            try:
                if gray[y][x] == 255:
                    L, currentB = [0] * 2
                    for a in range(-16, 16):
                        p = gray[y][x + a]
                        if -3 < a < 3 and p == 0:
                            currentB += 1
                        L += int(p / 255)
                        if p == 0:
                            countB += 1
                    if L > 14:
                        countW += 1
                    if 2 < L < 6 and gray[y][x] == 0 and (currentB == 5):
                        countH += 1
            except:
                pass
    print("Boxes: ", countW)
    print("Hearts:", countH)


def calibrate(offset=True):
    cx, cy, nx, ny = [0] * 4
    countWH, countWV = [0] * 2
    try:
        for y in range(0, len(gray)):
            for x in range(0, len(gray)):
                tx, ty = x, y
                if gray[y][x] == 255:
                    while gray[y][x + 1] != 0:
                        x += 1
                    while gray[y][x - 1] != 0:
                        x -= 1
                        countWH += 1  # 33
                    cx = int(math.ceil(countWH / 2))  # x + 16
                    nx = x + cx
                    while gray[y + 1][nx] != 0:
                        y += 1
                    while gray[y - 1][nx] != 0:
                        y -= 1
                        countWV += 1  # 33
                    cy = int(math.ceil(countWV / 2))
                    ny = y + cy
                    if offset:
                        return ny - ty, nx - tx  # (-3, 1)
                    else:
                        return cy * 2, cx * 2
    except:
        pass


# countConsecutiveBoxes()
# print(calibrate())
# searchBoxes()
# writeArrayTxt(board, "board_with_offset")
# showArrayImage(board, "board_with_offset")
# cv2.imwrite('Write/detected_g2.png', gray)
# cv2.imshow("gray", gray)
# cv2.waitKey(0)
# game_ss    W:27 L:9 H:1
# game_ss2   W:31 L:0 H:1
# game_ss2_2 W:25 L:6 H:1


def searchBoxes():
    yo, xo = calibrate()
    count, countW, countB, horizontal, vertical, L, countL, countH, currentB = [0] * 9
    for y in range(yo, len(gray), 33):  # y = 380  13 offset
        for x in range(xo, len(gray[0]), 33):  # y = 400 5 offset
            try:
                # region Count Blocks
                L, currentB = [0] * 2
                # # region Draw Grid Circle
                # if gray[y][x] == 0:
                #     cv2.circle(img=gray, center=(x, y), radius=1, color=(255, 0, 0), thickness=3)
                # elif gray[y][x] == 255:
                #     cv2.circle(img=gray, center=(x, y), radius=1, color=(0, 0, 0), thickness=3)
                # # endregion
                for a in range(-16, 16):
                    p = gray[y][x + a]
                    if -3 < a < 3 and p == 0:
                        currentB += 1
                    L += int(p / 255)
                    if p == 0:
                        countB += 1
                if L > 14:
                    countW += 1
                    board[round(y / 10)][round(x / 10)] = 1
                # if 1 < L < 22 and not (
                #         gray[y][x + 14] == 255 and gray[y][x - 18] == 255):
                #     countL += 1
                #     board[round(y / 10)][round(x / 10)] = 2
                # if gray[y][x + 13] == 255 and gray[y][x - 15] == 255 and gray[y][x] == 0:
                if 2 < L < 6 and gray[y][x] == 0 and (currentB == 5):
                    countH += 1
                    board[round(y / 10)][round(x / 10)] = 3
                # endregion
                # region Count Consecutive Blocks

                # endregion
            except:
                pass
    # region Print
    print("Boxes: ", countW)
    # print("Letters:", countL)
    print("Hearts:", countH)
    # endregion

# searchBoxes()
# writeArrayTxt(gray, "gray")
# cv2.imwrite('Write/detected_g2.png', gray)

# def calibrate():
#     cx, cy, nx, ny = [0] * 4
#     countWH, countWV = [1] * 2
#     try:
#         for y in range(0, len(gray), 35):
#             for x in range(0, len(gray), 35):
#                 tx, ty = x, y
#                 if gray[y][x] == 255:
#                     while gray[y][x + 1] != 0:
#                         x += 1
#                     while gray[y][x - 1] != 0:
#                         x -= 1
#                         countWH += 1  # 33
#                     cx = int(math.ceil(countWH / 2))  # x + 16
#                     nx = x + cx
#                     while gray[y + 1][nx] != 0:
#                         y += 1
#                     while gray[y - 1][nx] != 0:
#                         y -= 1
#                         countWV += 1  # 33
#                     cy = int(math.ceil(countWV / 2))
#                     ny = y + cy
#                     return ny - ty, nx - tx  # (-3, 1)
#     except:
#         pass


def countWhites():
    global longestH, longestV
    countH = 0
    unique, counts = np.unique(gray[0], return_counts=True)
    dictCount = dict(zip(unique, counts))
    print(dictCount)
    print(dictCount.get(255))
    h, w = calibrate(offset=False)
    for i in range(0, len(gray), h):
        found = False
        for j in range(len(gray[i])):
            try:

            except:
                pass


countWhites()

# def countWhites():
#     global longestH, longestV
#     countH = 0
#     unique, counts = np.unique(gray[0], return_counts=True)
#     dictCount = dict(zip(unique, counts))
#     print(dictCount)
#     print(dictCount.get(255))
#     h, w = calibrate(offset=False)
#     for i in range(0, len(gray), h):
#         found = False
#         for j in range(len(gray[i])):
#             try:
#                 if gray[i][j] == 255:
#                     if gray[i][j + 1] != 0:
#                         pass
#                     elif gray[i][j + 1] == 0 and gray[i][j + 5] == 0:
#                         if longestH == 0:
#                             longestH = 1
#                     elif gray[i][j + 1] == 0 and gray[i][j + 5] == 255:
#                         countH += 1
#                         while gray[i][j + 1] == 0 and gray[i][j + 5] == 255:
#                             while True:
#                                 j += 5
#                                 while gray[i][j + 1] != 0:
#                                     j += 1
#                                 if gray[i][j + 1] == 0:
#                                     countH += 1
#                                     break
#             except:
#                 pass
#         if longestH < countH:
#             longestH = countH
#             countH = 0