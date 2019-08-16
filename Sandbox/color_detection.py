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
image = cv2.imread("game_ss2_2.png")[86:486]
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
    # cv2.imwrite('Write/detected_0{}.png'.format(i), np.hstack([image, output])[:, 466:])
    # cv2.imshow("images", np.hstack([image, output])[:, 466:])
    # cv2.waitKey(0)

image = np.hstack([image, output])[:, 466:]
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 120, 250)

cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
mask = np.ones(image.shape[:2], dtype="uint8") * 255

white = 255
black = 0
im = Image.open('Write/detected_0.png')

longestH, longestV, CountConsecutive = [0]*3
board = np.zeros((40, 46)).astype(int)
def searchBoxes():
    count, countW, countB, horizontal, vertical, L, countL, countH = [0] * 8
    for y in range(24, len(gray), 32):  # y = 460
        for x in range(5, len(gray[0]), 32):  # y = 400
            try:
                #region Count Blocks
                L = 0
                # cv2.circle(img=gray, center=(x, y), radius=1, color=(255, 0, 0), thickness=3)
                for a in range(-16, 16):
                    p = gray[y][x + a]
                    L += p
                    if p == 0:
                        countB += 1
                if L > 255 * 14:
                    countW += 1
                    board[round(y / 10)][round(x / 10)] = 1
                if 255 * 1 < L < 255 * 22 and not (gray[y][x + 13] == 255 and gray[y][x - 15] == 255 and gray[y][x] == 0):
                    countL += 1
                    board[round(y / 10)][round(x / 10)] = 2
                if gray[y][x + 13] == 255 and gray[y][x - 15] == 255 and gray[y][x] == 0:
                    countH += 1
                    board[round(y / 10)][round(x / 10)] = 3
                #endregion
                #region Count Consecutive Blocks

                #endregion
            except:
                pass
    #region Print
    print("Boxes: ", countW)
    print("Letters:", countL)
    print("Hearts:", countH)
    #endregion

# def calibrate():
#     try:
#         for y in range(0, len(gray), 32):
#             for x in range(0, len(gray), 32):
#                if gray[y][x] == 255:
#
#     except:
#         pass
searchBoxes()
writeArrayTxt(board, "board_with_offset")
showArrayImage(board, "board_with_offset")
cv2.imwrite('Write/detected_g.png', gray)
# cv2.imshow("gray", gray)
# cv2.waitKey(0)
# game_ss    W:27 L:9 H:1
# game_ss2   W:31 L:0 H:1
# game_ss2_2 W:25 L:6 H:1
