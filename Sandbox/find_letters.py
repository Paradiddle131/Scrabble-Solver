import cv2
import numpy as np
import pytesseract
from PIL import Image


# http://blog.tramvm.com/2017/05/recognize-text-from-image-with-python.html

a = 1.1
b = 255
def get_string(scale):
    global a
    global b
    img = cv2.imread("detected_1.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (int(img.shape[1] * 1.5), int(img.shape[0] * 1.5)))
    kernel = np.ones((2, 2), np.uint8)
    # img = cv2.dilate(img, kernel, iterations=1)
    # img = cv2.erode(img, kernel, iterations=1)
    # img = cv2.filter2D(img, -1, kernel)
    # cv2.imwrite("removed_noise.png", img)
    ret, thresh1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
    opening = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel, iterations=2)
    thresh1 = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    cv2.imwrite("thresh.png", thresh1)
    result = pytesseract.image_to_string(Image.open("thresh.png"),
                                         config="-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPRSTUVYZ"
                                                " --psm 12"
                                         "--textord_min_linesize: 2.5"
                                         "textord_heavy_nr: 20"
                                         "speckle_large_max_size: 950")
    result = result.replace(' ', '')
    result = result.replace("\n", '')
    # print(len(result))
    # while result.__contains__("KESISRERA") == False:
    #     a += .1
    #     print("a: ", a, " - ", result)
    #     get_string(a)
    cv2.imshow("img", thresh1)
    cv2.waitKey(0)
    return result


print(get_string(a) + "\n")
