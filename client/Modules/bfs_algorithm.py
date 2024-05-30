from collections import deque

# Algoritmo Breadth-first search
## Realiza una búsqueda en anchura para encontrar el camino más corto
## maze: Matriz nxm con valores de 0b0000 a 0b1111.
##       Ubicación de las paredes:
##       - Norte (0b0001) | Sur (0b0010)
##       - Este (0b0100)  | Oeste (0b1000)
## start: Índice de la posición inicial del robot.
## end: Índice de la posición de salida del laberinto


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


# Mapeo de movimientos para el robot
## Obtención de instrucciones que debe seguir el robot.
## delta: [0: Left, 1: Right, 2: Down, 3: Up]


def robot_move(path):
    if path:
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        current = 3

        for i in range(len(path) - 1):
            move = tuple(a - b for a, b in zip(path[i], path[i + 1]))
            delta = directions.index(move)
            current = robot_turn(delta, current)
    else:
        print("No se encontró una ruta válida.")


# Funciones para el movimiento del robot
## MOVE_CONTINUE(): Avanza una posición en la dirección actual
## TURN_LEFT(): Gira 90 grados hacia la izquierda y avanza una posición
## TURN_RIGHT(): Gira 90 grados hacia la derecha y avanza una posición
## MOVE_TURN(): Gira 180 grados o dos veces hacia la derecha y avanza una posición


def robot_turn(delta, current):
    right = [(0, 3), (1, 2), (2, 0), (3, 1)]
    left = [(0, 2), (1, 3), (2, 1), (3, 0)]

    if current == delta:
        print("MOVE_CONTINUE")

    elif (current, delta) in left:
        print("TURN_LEFT")
        current = delta

    elif (current, delta) in right:
        print("TURN_RIGHT")
        current = delta

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
    start = (4, 2)
    end = (0, 4)

    path = find_path(maze, start, end)
    print_path(path, start, end)
    robot_move(path)


if __name__ == "__main__":
    main()
