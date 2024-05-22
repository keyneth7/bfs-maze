from collections import deque


def find_path(maze, start, end):
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


def route(path, start):
    print("Movimientos")
    for i in range(len(path) - 1):
        delta = tuple(a - b for a, b in zip(path[i], path[i + 1]))
        print_direction(delta)


def print_direction(delta):
    directions = {(0, 1): "Left", (0, -1): "Right", (-1, 0): "Down", (1, 0): "Up"}

    if delta in directions:
        print(directions[delta])
    else:
        print("Movimiento no reconocido:", delta)


def print_path(path, start, end):
    if path:
        print(f"Inicio: {start}")
        print(f"Fin: {end}")
        print("Ruta encontrada:")
        for point in path:
            print(point)
    else:
        print("No se encontró una ruta válida.")


maze = [
    [0b1001, 0b0001, 0b0011, 0b0111, 0b1100, 0b1001, 0b0011, 0b0101],
    [0b1100, 0b1100, 0b1001, 0b0001, 0b0110, 0b1000, 0b0111, 0b1100],
    [0b1100, 0b1010, 0b0100, 0b1010, 0b0011, 0b0100, 0b1011, 0b0100],
    [0b1000, 0b0111, 0b1000, 0b0011, 0b0101, 0b1000, 0b0101, 0b1100],
    [0b1100, 0b1011, 0b0100, 0b1001, 0b0010, 0b0110, 0b1100, 0b1100],
    [0b1010, 0b0111, 0b1110, 0b1110, 0b1011, 0b0011, 0b0010, 0b0110],
]


def main():
    start = (5, 4)
    end = (0, 4)

    path = find_path(maze, start, end)
    route(path, start)


if __name__ == "__main__":
    main()
