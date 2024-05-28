# bfs-maze-bot
Modelo de un robot autónomo capaz de resolver laberintos utilizando una tarjeta esp32 como unidad de control principal. El robot combina el uso del algoritmo de Búsqueda en Anchura (BFS) con técnicas de visión artificial para mapear y navegar a través del laberinto de manera eficiente.

## 🤖 Arquitectura y caracteristicas
El sistema se divide en dos secciones principales: el cliente y la ESP32 (servidor/robot). La implementación del software está basada en Python y Micropython.

<p align="center">
    <img src="http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/queined/bfs-maze-bot/main/diagram.iuml" width="500">
</p>


El modelo posee una interfaz de usuario que permite a los usuarios interactuar con el robot. Se encarga de enviar comandos y recibir datos del servidor ESP32. La ESP32 actúa como el servidor y el controlador principal del robot. Gestiona la recepción de comandos del cliente, controla los motores y realiza la navegación en el laberinto.

## 🚩 Algoritmo y laberinto

<p align="center">
    <img src="https://i.postimg.cc/mD4TYq8j/maze.png" width="350">
</p>

[BFS (Búsqueda en Anchura)](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/) es un método para explorar grafos que trabaja en niveles, explorando todos los nodos de un nivel antes de pasar al siguiente. En este proyecto, se adpta BFS para operar en una matriz que representa el laberinto. Cada celda de la matriz representa una casilla en el laberinto, donde 0s y 1s indican espacios libres y paredes respectivamente. Es decir, norte (0b0001), sur (0b0010), este (0b0100), oeste (0b1000). De esta forma, el laberinto mostrado se puede representar como:

```python
maze = [
    [0b1001, 0b0001, 0b0011, 0b0111, 0b1100, 0b1001, 0b0011, 0b0101],
    [0b1100, 0b1100, 0b1001, 0b0001, 0b0110, 0b1000, 0b0111, 0b1100],
    [0b1100, 0b1010, 0b0100, 0b1010, 0b0011, 0b0100, 0b1011, 0b0100],
    [0b1000, 0b0111, 0b1000, 0b0011, 0b0101, 0b1000, 0b0101, 0b1100],
    [0b1100, 0b1011, 0b0100, 0b1001, 0b0010, 0b0110, 0b1100, 0b1100],
    [0b1010, 0b0111, 0b1110, 0b1110, 0b1011, 0b0011, 0b0010, 0b0110],
]
```

## ⚙ Configuración y uso
### Prerrequisitos
- [Python 3.x](https://www.python.org/downloads/)
- [esptool](https://github.com/espressif/esptool)
- [Micropython firmware ESP32/WROOM](https://micropython.org/download/ESP32_GENERIC/)
- [opencv-python](https://pypi.org/project/opencv-python/)
- Ver [requirements.txt](https://github.com/queined/bfs-maze-bot/blob/main/requirements.txt)
### Materiales
- ESP32-WROOM
- Servo sg90
- Webcam HD

## ⚖️ Licencia
Este proyecto tiene la licencia MIT; consulte el archivo de [LICENSE](https://github.com/queined/bfs-maze-bot/blob/main/LICENSE) para obtener más detalles.
 

