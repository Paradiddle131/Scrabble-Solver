import cv2
import numpy as np

img_rgb = cv2.imread('game_screen.PNG')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('square.png', 0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.6
loc = np.where(res >= threshold)

template2 = cv2.imread('game_screen_heart.png', 0)
w2, h2 = template2.shape[::-1]
res2 = cv2.matchTemplate(img_gray, template2, cv2.TM_CCOEFF_NORMED)
loc2 = np.where(res2 >= threshold)

for pt in zip(*loc[::-1]):
    if pt[1] < 437:
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
for pt in zip(*loc2[::-1]):
    if pt[1] < 437:
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imwrite("result.png", img_rgb)
cv2.imshow('Detected', img_rgb)
cv2.waitKey(0)