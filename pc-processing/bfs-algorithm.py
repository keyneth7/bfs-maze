from collections import deque

# Algoritmo Breadth-first search
## maze: Matriz nxm con valores de 0b0000 a 0b1111.

## start: Indice de la posición inical del robot.
## end: Indice de la posición de salida del laberinto.
## path[]: Lista de tuplas de los indices del recorrido.

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


def print_path(path, start, end):
    if path:
        print(f"Inicio: {start}")
        print(f"Fin: {end}")
        print("Ruta encontrada:")
        for point in path:
            print(point)
    else:
        print("No se encontró una ruta válida.")


def movement_map(path):
    current = 3
    print("Movimientos")
    for i in range(len(path) - 1):
        delta = tuple(a - b for a, b in zip(path[i], path[i + 1]))
        current = robot_turn(get_direction(delta), current)


def get_direction(delta):
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    return directions.index(delta)


def print_direction(delta):
    directions = {(0, 1): "Left", (0, -1): "Right", (-1, 0): "Down", (1, 0): "Up"}

    if delta in directions:
        print(directions[delta])
    else:
        print("Movimiento no reconocido:", delta)


def robot_turn(delta, current):
    directions = [0, 1, 2, 3]  # Left, Right, Down, Up
    right = [(0, 3), (1, 2), (2, 0), (3, 1)]
    left = [(0, 2), (1, 3), (2, 1), (3, 0)]

    if current == directions[delta]:
        print("MOVE_CONTINUE")

    elif (current, directions[delta]) in left:
        print("TURN_LEFT")
        current = directions[delta]

    elif (current, directions[delta]) in right:
        print("TURN_RIGHT")
        current = directions[delta]

    else:
        print("MOVE_TURN")

    return current


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
    print_path(path, start, end)
    movement_map(path)


if __name__ == "__main__":
    main()
