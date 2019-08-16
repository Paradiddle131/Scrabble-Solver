import  cv2 as cv

def avg(lst):
    return int(sum(lst) / len(lst))

src = cv.imread("200x200_rgb.png")
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
src_gray = cv.blur(src_gray, (3,3))
canny_output = cv.Canny(src_gray, 150, 150 * 2)[:90]
contours, hierarchy = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


doubles = [
[140,  22],
[138,  24],
[138,  70],
[140,  72],
[188,  72],
[190,  70],
[190,  24],
[188,  22],
[188,  22],
[190,  24],
[190,  70],
[188,  72],
[140,  72],
[138,  70],
[138,  24],
[141,  69],
[187,  69],
[187,  25],
[142,  25],
[186,  25],
[187,  26],
[187,  68],
[186,  69],
[142,  69],
[141,  68],
[79,  24],
[79,  70],
[81,  72],
[129,  72],
[131,  70],
[131,  24],
[129,  22],
[129,  22],
[131,  24],
[131,  70],
[129,  72],
[81,  72],
[79,  70],
[79,  24],
[82,  69],
[128,  69],
[128,  25],
[83,  25],
[127,  25],
[128,  26],
[128,  68],
[127,  69],
[83,  69],
[82,  68],
[20, 23],
[20, 71],
[21, 72],
[71, 72],
[72, 71],
[72, 23],
[71, 22],
[70, 22],
[72, 24],
[72, 70],
[70, 72],
[22, 72],
[20, 70],
[20, 24],
[23, 69],
[69, 69],
[69, 25],
[24, 25],
[68, 25],
[69, 26],
[69, 68],
[68, 69],
[24, 69],
[23, 68]
]
doubles_sorted = [
[20, 23],
[20, 24],
[20, 70],
[20, 71],
[21, 72],
[22, 72],
[23, 68],
[23, 69],
[24, 25],
[24, 69],
[68, 25],
[68, 69],
[69, 25],
[69, 26],
[69, 68],
[69, 69],
[70, 22],
[70, 72],
[71, 22],
[71, 72],
[72, 23],
[72, 24],
[72, 70],
[72, 71],
[79, 24],
[79, 24],
[79, 70],
[79, 70],
[81, 72],
[81, 72],
[82, 68],
[82, 69],
[83, 25],
[83, 69],
[127, 25],
[127, 69],
[128, 25],
[128, 26],
[128, 68],
[128, 69],
[129, 22],
[129, 22],
[129, 72],
[129, 72],
[131, 24],
[131, 24],
[131, 70],
[131, 70],
[138, 24],
[138, 24],
[138, 70],
[138, 70],
[140, 22],
[140, 72],
[140, 72],
[141, 68],
[141, 69],
[142, 25],
[142, 69],
[186, 25],
[186, 69],
[187, 25],
[187, 26],
[187, 68],
[187, 69],
[188, 22],
[188, 22],
[188, 72],
[188, 72],
[190, 24],
[190, 24],
[190, 70],
[190, 70]
]
one_square = [138, 24], [138, 70], [140, 22],  [140, 72], [188, 22], [188, 72], [190, 24], [190, 70]

diff_list = []
couple_list = []
for i in doubles_sorted:
    diff = abs(i[0] - i[1])
    diff_list.append(diff)
    couple = i
    couple_list.append(i)

print(one_square)
print(contours[0].tolist())
points1 = []
points2 = []

for i in range(len(one_square)):  # 8
    print(one_square[i][0])
    print(one_square[i][1])
    points1.append(one_square[i][0])
    points2.append(one_square[i][1])
points1.sort()
points2.sort()
corner1 = avg(points1[:4])
corner2 = avg(points1[4:])
corner3 = avg(points2[:4])
corner4 = avg(points2[4:])

print(points1)
print(points2)
print("corner 1: ", corner1)
print("corner 2: ", corner2)
print("corner 3: ", corner3)
print("corner 4: ", corner4)


def isSquareC(c1, c2, c3, c4):
    if abs(c1 - c2) - abs(c3 - c4) < 5:
        print("Square")
    else:
        print("Not Square")
    return True if abs(c1 - c2) - abs(c3 - c4) < 5 else False

def isSquare(cnts):
    cnts = cnts[0]
    list_cnts = []
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
        print("Square")
    else:
        print("Not Square")
    return True if abs(c1 - c2) - abs(c3 - c4) < 5 else False



# isSquareC(corner1, corner2, corner3, corner4)
isSquare(contours)