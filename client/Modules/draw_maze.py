from Modules.bfs_path import bfs_path
from Modules.get_start import get_start
from Modules import globals
import cv2


def draw_maze():
    img = get_start()
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    pathlist = bfs_path(globals.maze, globals.start, globals.end)
    rows = len(globals.maze)
    cols = len(globals.maze[0])

    h, w, _ = img.shape
    dy, dx = h / rows, w / cols
    path_color = (255, 0, 0)
    thickness = 2

    for i in range(len(pathlist) - 1):
        start_point = (
            int(pathlist[i][1] * dx + dx / 2),
            int(pathlist[i][0] * dy + dy / 2),
        )
        end_point = (
            int(pathlist[i + 1][1] * dx + dx / 2),
            int(pathlist[i + 1][0] * dy + dy / 2),
        )
        cv2.line(img, start_point, end_point, path_color, thickness)

    return img
