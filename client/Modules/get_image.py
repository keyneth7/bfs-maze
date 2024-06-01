import cv2
import numpy as np
import globals

points = []
img = cv2.imread(globals.maze)


def get_points(event, x, y, flags, param):
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 4, (255, 0, 0), -1)
        points.append([x, y])
        print(points)
        cv2.imshow("Maze", img)
        if len(points) >= 4:
            get_perspective()


def get_perspective():
    width = points[1][0] - points[0][0]
    height = points[2][1] - points[0][1]
    pts1 = np.float32([points[0:4]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (width, height))
    cv2.imshow("Resize", imgOutput)
    cv2.waitKey(2000)
    cv2.imwrite(globals.resize, imgOutput)


def get_image():
    global img
    img = cv2.resize(img, (600, 400))
    cv2.imshow("Maze", img)
    cv2.setMouseCallback("Maze", get_points)
    cv2.waitKey(8000)
