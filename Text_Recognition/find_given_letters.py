import cv2
import numpy as np
import pytesseract
from PIL import Image

# http://blog.tramvm.com/2017/05/recognize-text-from-image-with-python.html
# Path of working folder on Disk


def image_processing(path):
    image = cv2.imread(path)[412:660, 94:342]
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((3, 3), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.erode(image, kernel, iterations=3)
    image = cv2.filter2D(image, -1, kernel)
    ret, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)
    cv2.imwrite("thresh.png", thresh)
    return thresh

def get_letters(path):
    image = image_processing(path)
    result = pytesseract.image_to_string(image,
                                         config="-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                                                " --psm 6")
    result = result.replace(' ', '')
    result = result.replace("\n", '')
    print("Given Letters Are: ", result)
    # cv2.imshow("board", thresh1)
    # cv2.waitKey(0)
    return result


# get_letters("../Automation/board.png")

# result2 = pytesseract.image_to_string(Image.open("test.png"),
#                                      config="-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#                                             " --psm 6")
# result2 = result2.replace(' ', '')
# result2 = result2.replace("\n", '')
# print(result2)