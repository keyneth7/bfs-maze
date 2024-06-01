import cv2
import numpy as np
import globals
from get_image import get_image


def image_processing(img, rows, cols):
    img_draw = draw_grid(img, rows, cols)
    img_gray = cv2.cvtColor(img_draw, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    return img


def draw_grid(img, rows, cols):
    h, w, _ = img.shape
    dy, dx = h / rows, w / cols
    color = (255, 0, 0)
    thickness = 2

    for x in np.linspace(start=dx, stop=w - dx, num=cols - 1):
        x = int(round(x))
        cv2.line(img, (x, 0), (x, h), color=color, thickness=thickness)

    for y in np.linspace(start=dy, stop=h - dy, num=rows - 1):
        y = int(round(y))
        cv2.line(img, (0, y), (w, y), color=color, thickness=thickness)

    return img


def find_robot(matrix, rows, cols):
    img_resized = cv2.resize(matrix, (cols, rows), interpolation=cv2.INTER_AREA)
    img_array = np.array(img_resized)
    min_val = np.min(img_array)
    position = np.argwhere(img_array == min_val)[0]
    return tuple(position)


def get_start(rows, cols):
    get_image()
    img = cv2.imread(globals.resize)

    matrix = image_processing(img, rows, cols)
    coordinates = find_robot(matrix, rows, cols)

    print("START:", coordinates)
    cv2.imshow("Matrix", matrix)
    cv2.imwrite(globals.matrix, matrix)
    cv2.waitKey(0)
    return coordinates
