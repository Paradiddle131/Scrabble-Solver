import cv2
import numpy as np
import pytesseract
from PIL import Image
import matplotlib.pyplot as plt


# http://blog.tramvm.com/2017/05/recognize-text-from-image-with-python.html
# Path of working folder on Disk


def image_processing(path, get_from):
    if get_from is "given_letters":
        image = cv2.imread(path)[412:660, 94:342]
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        kernel = np.ones((3, 3), np.uint8)
        image = cv2.dilate(image, kernel, iterations=1)
        image = cv2.erode(image, kernel, iterations=2)
        image = cv2.filter2D(image, -1, kernel)
        ret, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)
        # plt.imshow(thresh)
        # plt.show()
        cv2.imwrite("../Automation/Assets/thresh.png", thresh)
        cv2.imwrite("../Automation/Assets/thresh1.png", thresh[5:5+60, 90:90+60])
        cv2.imwrite("../Automation/Assets/thresh2.png", thresh[47:47+60, 21:21+60])
        cv2.imwrite("../Automation/Assets/thresh3.png", thresh[47:47+60, 165:165+60])
        cv2.imwrite("../Automation/Assets/thresh4.png", thresh[120:120+60, 15:15+60])
        cv2.imwrite("../Automation/Assets/thresh5.png", thresh[117:117+60, 180:180+60])
        cv2.imwrite("../Automation/Assets/thresh6.png", thresh[180:180+60, 60:60+60])
        cv2.imwrite("../Automation/Assets/thresh7.png", thresh[180:180+60, 140:140+60])
        return thresh
    elif get_from is "revealed_letters":
        image = cv2.imread(path)[:380, :]
        cv2.imshow("image", image)
        cv2.waitKey(0)


def get_letters(path, get_from):
    image = image_processing(path, get_from)
    result = pytesseract.image_to_string(image,
                                         config="-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                                                " --psm 6")
    result = result.replace(' ', '')
    result = result.replace("\n", '')
    result = result.lower()
    print("Given Letters Are: ", result)
    return result


def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return listOfKeys


def get_single_letters_locations(length):
    dict_loc = {}
    letters = []
    for i in range(1, length+1):
        img_letter = cv2.imread("../Automation/Assets/thresh{}.png".format(i))
        letter = pytesseract.image_to_string(img_letter,
                                             config="-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                                                    " --psm 6")
        letters.append(letter.lower())
    for i, x in enumerate(letters, 1):
        dict_loc.update([(i, x)])
    print(dict_loc)
    return dict_loc


# get_single_letters_locations()
# image_processing("../Automation/Assets/board.png", "given_letters")
# get_letters("../Automation/Assets/board.png", "given_letters")
