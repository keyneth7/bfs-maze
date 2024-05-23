from bfs_algorithm import *


def main():
    start = (3, 1)
    end = (0, 4)

    path = find_path(maze, start, end)
    print_path(path, start, end)
    robot_move(path)


if __name__ == "__main__":
    main()
