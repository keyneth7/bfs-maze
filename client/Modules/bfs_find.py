from collections import deque
from get_start import get_start


def bfs_algorithm(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([start])
    parent = {}

    while queue:
        current = queue.popleft()
        if current == end:
            path = []
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        row, col = current
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]  # Left, Right, Down, Up

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and not visited[new_row][new_col]
            ):
                if (maze[row][col] & (8 >> (directions.index((dr, dc))))) == 0:
                    queue.append((new_row, new_col))
                    visited[new_row][new_col] = True
                    parent[(new_row, new_col)] = current
    return None


def find(maze, end):
    start = get_start()
    return bfs_algorithm(maze, start, end)
