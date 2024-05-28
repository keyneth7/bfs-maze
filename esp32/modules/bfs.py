from collections import deque


def search(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque((), 100)
    queue.append(start)
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


def print_path(path, start, end):
    if path:
        print(f"Inicio: {start}")
        print(f"Fin: {end}")
        print("Ruta encontrada:")
        for point in path:
            print(point)
    else:
        print("No se encontró una ruta válida.")


def delta(path):
    DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    move = []

    if path:
        for i in range(len(path) - 1):
            direction = tuple(a - b for a, b in zip(path[i], path[i + 1]))
            delta = DIRECTIONS.index(direction)
            move.append(delta)

    return move


def find(maze, start, end):
    print(f"START: {start} | END:{end}")
    path = search(maze, start, end)
    print_path(path, start, end)
    return delta(path)
