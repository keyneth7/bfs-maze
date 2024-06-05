import cv2
import numpy as np
from Modules import globals


def get_camera():
    cap = cv2.VideoCapture(globals.camera)
    while cap.isOpened():
        ret, video = cap.read()
        if ret:
            if cv2.waitKey(1) & 0xFF == ord(" "):
                cv2.destroyAllWindows()
                return video
                break
            videotext = cv2.putText(
                video,
                "Presiona espacio para capturar.",
                (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
                cv2.LINE_AA,
            )
            cv2.imshow("Capture maze", videotext)


def get_points(event, x, y, flags, param):
    global img, points, pointsSel
    cv2.imshow("Maze", img)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 4, (255, 0, 0), -1)
        points.append([x, y])
        if len(points) >= 4:
            get_perspective()
            pointsSel = True
            cv2.destroyAllWindows()


def get_perspective():
    global imgResize
    width = points[1][0] - points[0][0]
    height = points[2][1] - points[0][1]
    pts1 = np.float32([points[0:4]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgResize = cv2.warpPerspective(img, matrix, (width, height))


def get_image():
    global img, points, pointsSel, imgResize
    pointsSel = False
    points = []
    img = get_camera()
    while not pointsSel:
        img = cv2.resize(img, (600, 400))
        cv2.imshow("Maze", img)
        cv2.setMouseCallback("Maze", get_points)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        else:
            continue
    return imgResize
