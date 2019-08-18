import pyautogui as p
import operator
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from Text_Recognition.find_given_letters import get_letters
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)
p.PAUSE = 1
p.FAILSAFE = True

btn_daily_puzzle = p.locateOnScreen('Assets/daily_puzzle_button.png')
block_empty = p.locateOnScreen("Assets/squareT.png")
home_button = "Assets/home_button.png"
img_path = "board.png"

x, y = tuple(map(operator.add, p.locateOnScreen(home_button)[:2], (0, 100)))
board = p.screenshot(region=(x, y, 447, 670))
# board.show()
board.save("board.png")


# display(board)


def display(img):
    plt.imshow(img)
    plt.show()


def enterDailyPuzzle():
    p.click(p.center((p.locateOnScreen('Assets/daily_puzzle_button.png'))))


# def calibrate():
#
#     return x, y


dict_letter_locations = {
    "first": "{},{},{},{}".format(1166, 563, 55, 50),
    "second": "{},{},{},{}".format(1240, 606, 55, 50),
    "third": "{},{},{},{}".format(1240, 694, 55, 50),
    "fourth": "{},{},{},{}".format(1166, 737, 55, 50),
    "fifth": "{},{},{},{}".format(1087, 693, 55, 50),
    "sixth": "{},{},{},{}".format(1087, 605, 55, 50)
}

dict_letter_center_locations = dict(
    [
        (1, (x + 215, y + 445)),
        (2, (x + 290, y + 490)),
        (3, (x + 290, y + 580)),
        (4, (x + 215, y + 625)),
        (5, (x + 140, y + 580)),
        (6, (x + 140, y + 490))
    ]
)

dict_letter_color_locations = dict(
    [
        (1, (x + 215 - 30, y + 445)),
        (2, (x + 290 - 30, y + 490)),
        (3, (x + 290 - 30, y + 580)),
        (4, (x + 215 - 30, y + 625)),
        (5, (x + 140 - 30, y + 580)),
        (6, (x + 140 - 30, y + 490))
    ]
)


# board: (990, 146) first letter: 215, 445

def detectLetterColor():
    # first, second, third, fourth, fifth, sixth =
    a, b = tuple(map(operator.sub, dict_letter_center_locations.get(1), (x, y)))
    a, b = int(a) - 20, int(b)
    p.mouseDown(dict_letter_center_locations.get(1), duration=2.0)
    board_current = p.screenshot(region=(x, y, 447, 670))
    color_letter = board_current.getpixel((a, b))
    print(color_letter)
    p.mouseUp()
    return color_letter


detectLetterColor()
# calibrate()

# def findGivenLetters():
#     x, y = tuple(map(operator.add, calibrate(), (80, 400)))
#     blacks = list(p.locateAllOnScreen("Assets/letter_black.png"))
#     for black in blacks:
#         # print(black[0])
#         if x < black[0] < x + 250 and y < black[1] < y + 250:
#             print(black)


img_given_letters = mpimg.imread(img_path)[412:660, 94:342]


def snap_ocr(x1, y1, x2, y2):
    pass


def ocr(path):
    get_letters(path)

# ocr(img_path)
