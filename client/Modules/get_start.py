import cv2
import numpy as np
from Modules.get_image import get_image
from Modules import globals


def image_processing(img, rows, cols):
    img_draw = draw_grid(img, rows, cols)
    img_gray = cv2.cvtColor(img_draw, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY)
    img = cv2.GaussianBlur(img, (3, 3), 0)
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
    return tuple([int(p) for p in position])


def get_start():
    try:
        get_image()
        rows = len(globals.maze)
        cols = len(globals.maze[0])
        img = cv2.imread(globals.imgresize)

        matrix = image_processing(img, rows, cols)
        globals.start = find_robot(matrix, rows, cols)
        matrixres = cv2.resize(matrix, (300, 200))
        cv2.imwrite(globals.imgmatrix, matrixres)
    
    except Exception as e:
        print(f"Error en get_start: {e}")
        exit()
        return None
