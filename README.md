# bfs-maze-bot
Modelo de un robot autónomo capaz de resolver laberintos utilizando una tarjeta ESP32 como unidad de control principal. El robot combina el uso del algoritmo de Búsqueda en Anchura (BFS) con técnicas de visión artificial para mapear y navegar a través del laberinto de manera eficiente.

## 🤖 Arquitectura y caracteristicas
El sistema se divide en dos secciones principales: el cliente y la ESP32 (servidor/robot). La implementación del software está basada en Python y Micropython.

<p align="center">
    <img src="http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/queined/bfs-maze-bot/main/diagram.iuml" width="500">
</p>


El modelo posee una interfaz de usuario que permite a interactuar con el robot. Se encarga de enviar comandos y recibir datos del servidor ESP32. La ESP32 actúa como el servidor y el controlador principal del robot. Gestiona la recepción de comandos del cliente, controla los motores y realiza la navegación en el laberinto.

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
- [Micropython firmware ESP32/WROOM](https://micropython.org/download/ESP32_GENERIC/)
- Micropython IDE ([Thonny IDE](https://thonny.org), [Mu Editor](https://codewith.mu), [VS Code Pymakr](https://randomnerdtutorials.com/micropython-esp32-esp8266-vs-code-pymakr/))
### Materiales
- ESP32-WROOM
- Servo sg90
- Webcam HD
  
### ⚙ Configuración del cliente
1. Instalar librerías [requirements.txt](https://github.com/queined/bfs-maze-bot/blob/main/requirements.txt).
    ```python
    pip install -r requirements.txt
    ```
### ⚙ Configuración de la ESP32
1. Instalar el [firmware](https://micropython.org/download/ESP32_GENERIC/) de Micropython para la ESP32/WROOM.
    ```bash
    esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
    esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-20190125-v1.10.bin
    ```
2. Modificar el `SSID` y el `PASSWORD` de la red en [main.py](https://github.com/queined/bfs-maze-bot/blob/main/esp32/main.py). Si definiste un nuevo laberineto deberás insertarlo en `MAZE`. Cargar los archivos de [/esp32](https://github.com/queined/bfs-maze-bot/tree/main/esp32) a la tarjeta. 

## ⚖️ Licencia
Este proyecto tiene la licencia MIT; consulte el archivo de [LICENSE](https://github.com/queined/bfs-maze-bot/blob/main/LICENSE) para obtener más detalles.
 

