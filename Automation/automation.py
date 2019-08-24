import pyautogui as p
import operator
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from Text_Recognition.find_given_letters import *
from Automation.find_difference import *
from Word_Finding.find_word import *
import numpy as np
import sys

# region Configuration
np.set_printoptions(threshold=sys.maxsize)
p.PAUSE = 1
p.FAILSAFE = True
# endregion
# region Initialization
home_button = "Assets/home_button.png"
img_path = "Assets/board.png"
board_prev_path = "Assets/board_prev.png"
board, board_prev = [None] * 2
x, y, x_l, y_l = [0] * 4
dict_letter_center_locations, dict_letter_color_locations = ({} for i in range(2))


# endregion

def set_gameboard():
    global board, x, y, x_l, y_l
    x, y = tuple(map(operator.add, p.locateOnScreen(home_button)[:2], (0, 100)))
    x_l, y_l = x + 94, y + 412
    board_prev = board
    board = p.screenshot(region=(x, y, 447, 670))
    # board.show()
    board.save(img_path)
    if board_prev is not None:
        board_prev.save(board_prev_path)


def locate_letters():
    global dict_letter_center_locations, dict_letter_color_locations

    dict_letter_center_locations = dict(
        [
            (1, (x_l + 120, y_l + 35)),
            (2, (x_l + 50, y_l + 70)),
            (3, (x_l + 194, y_l + 70)),
            (4, (x_l + 40, y_l + 145)),
            (5, (x_l + 210, y_l + 140)),
            (6, (x_l + 85, y_l + 205)),
            (7, (x_l + 165, y_l + 200))
        ]
    )

    dict_letter_color_locations = dict(
        [
            (1, (x_l + 120 - 30, y_l + 35)),
            (2, (x_l + 50 - 30, y_l + 70)),
            (3, (x_l + 194 - 30, y_l + 70)),
            (4, (x_l + 40 - 30, y_l + 145)),
            (5, (x_l + 210 - 30, y_l + 140)),
            (6, (x_l + 85 - 30, y_l + 205)),
            (7, (x_l + 165 - 30, y_l + 200))
        ]
    )


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


def play(order, length):
    for i in range(1, length + 1):
        try:
            x, y = get_value_by_key(dict_letter_center_locations, order[i - 1][0])[0]
        except:
            x, y = get_value_by_key(dict_letter_center_locations, order[i - 1])[0]
        p.moveTo(x, y)
        p.mouseDown()
        # compare(board_prev_path, img_path)
    p.mouseUp()


# region Dictionary Operations
def get_keys_by_value(dictOfElements, valueToFind):
    listOfKeys = []
    for item in dictOfElements.items():
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return listOfKeys


def get_value_by_key(dict, key):
    values = []
    for item in dict.items():
        if item[0] == key:
            values.append(item[1])
    return values


# endregion

def pick_letters(words, dict):
    order = []
    for word in words:
        for i in range(len(word)):
            order.append(get_keys_by_value(dict, word[i]))
    print(order)
    return order


def remove_duplicates_from_order(order):
    locs = []
    for item in order:
        if len(item) > 1:
            indices = [i for i, x in enumerate(order) if x == item]
            if not locs.__contains__(indices):
                locs.append(indices)
    for num in locs:
        order[num[0]] = order[num[0]][0]
        order[num[1]] = order[num[1]][1]
    return order


def main():
    possible_words = []
    set_gameboard()
    locate_letters()
    given_letters = get_letters(img_path, "given_letters")
    possible_words.append(complete_word(['_' * len(x) for x in given_letters], given_letters))
    print("possible_words: ", possible_words[0])
    order = pick_letters(possible_words[0], get_single_letters_locations(len(given_letters)))
    order = remove_duplicates_from_order(order)
    play(order, len(given_letters))


main()
