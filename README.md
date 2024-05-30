# bfs-maze-bot
Modelo de un robot autónomo capaz de resolver laberintos utilizando una tarjeta ESP32 como unidad de control principal. El robot combina el uso del algoritmo de Búsqueda en Anchura (BFS) con técnicas de visión artificial para mapear y navegar a través del laberinto de manera eficiente.

## Tabla de Contenidos

- [bfs-maze-bot](#bfs-maze-bot)
  - [Tabla de Contenidos](#tabla-de-contenidos)
- [Introducción](#introducción)
  - [Arquitectura y caracteristicas](#arquitectura-y-caracteristicas)
  - [Algoritmo y laberinto](#algoritmo-y-laberinto)
- [Implementación](#implementación)
  - [Configuración de software](#configuración-de-software)
    - [Prerrequisitos](#prerrequisitos)
    - [Configuración del cliente](#configuración-del-cliente)
    - [Configuración de la ESP32](#configuración-de-la-esp32)
  - [Configuración de hardware](#configuración-de-hardware)
    - [Materiales](#materiales)
- [Funcionamiento](#funcionamiento)
- [Licencia](#licencia)

# Introducción
## Arquitectura y caracteristicas
El sistema se divide en dos secciones principales: el cliente y la ESP32 (servidor/robot). La implementación del software está basada en Python y Micropython.

<p align="center">
    <img src="http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/queined/bfs-maze-bot/main/diagram.iuml" width="450">
</p>

El modelo cuenta con una interfaz de usuario que facilita la interacción con el robot. Esta interfaz se encarga de enviar comandos y recibir datos del servidor ESP32. La ESP32 actúa como servidor y controlador principal del robot, gestionando la recepción de comandos del cliente, controlando los motores y ejecutando la navegación en el laberinto.

## Algoritmo y laberinto

<p align="center">
    <img src="https://i.postimg.cc/mD4TYq8j/maze.png" width="350">
</p>

[BFS (Búsqueda en Anchura)](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/) es un método para explorar grafos que trabaja en niveles, explorando todos los nodos de un nivel antes de pasar al siguiente. En este proyecto, se adapta BFS para operar en una matriz que representa el laberinto. Cada celda de la matriz representa una casilla en el laberinto, donde 0s y 1s indican espacios libres y paredes respectivamente. Es decir, norte (0b0001), sur (0b0010), este (0b0100), oeste (0b1000). De esta forma, el laberinto mostrado se puede representar como:

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
# Implementación
## Configuración de software
###  Prerrequisitos
- [Python 3.x](https://www.python.org/downloads/)
- Micropython IDE ([Thonny IDE](https://thonny.org), [Mu Editor](https://codewith.mu), [VS Code Pymakr](https://randomnerdtutorials.com/micropython-esp32-esp8266-vs-code-pymakr/))
- Micropython firmware ([ESP32/WROOM](https://micropython.org/download/ESP32_GENERIC/))
  
### Configuración del cliente
1. Clonar el respositorio.
    ```bash
    $ git clone https://github.com/queined/bfs-maze-bot
    ```
2. Instalar paquetes desde [requirements.txt](https://github.com/queined/bfs-maze-bot/blob/main/requirements.txt).
    ```python
    $ pip install -r requirements.txt
    ```
### Configuración de la ESP32

1. Instalar el [firmware](https://micropython.org/download/ESP32_GENERIC/) de Micropython para la ESP32/WROOM.
    ```bash
    $ esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
    $ esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-20190125-v1.10.bin
    ```
2. Modificar el `SSID` y el `PASSWORD` de la red en [main.py](https://github.com/queined/bfs-maze-bot/blob/main/esp32/main.py). Si se define un nuevo laberinto se debe insertar en `MAZE`. Luego, cargar los archivos de [/esp32](https://github.com/queined/bfs-maze-bot/tree/main/esp32) a la tarjeta.


## Configuración de hardware
### Materiales
- ESP32-WROOM
- Microservo SG90
- Webcam HD
- Corte en acrilíco o MDF ([robot.pdf](https://drive.google.com/file/d/1Ww6aeQt7NfRK-QJ9MhmAraJnbKTxphb9/view?usp=drive_link))
- Ruedas de 65mm
- Protoboard o baquela

# Funcionamiento
Work in progress...

# Licencia
Este proyecto tiene la licencia MIT; consulte el archivo de [LICENSE](https://github.com/queined/bfs-maze-bot/blob/main/LICENSE) para obtener más detalles.
 

