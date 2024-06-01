from bfs_find import *
import globals

def img_gui():

    end = (0, 4)
    path = find(globals.maze, end)
    for point in path:
        print(point)


if __name__ == "__main__":
    img_gui()
