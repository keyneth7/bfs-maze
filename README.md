# bfs-maze-bot
Modelo de un robot autónomo capaz de resolver laberintos utilizando una tarjeta ESP32 como unidad de control principal. El robot combina el uso del algoritmo de Búsqueda en Anchura (BFS) con técnicas de visión artificial para mapear y navegar a través del laberinto de manera eficiente.

<p align="center">
  <a href="#presentación">Presentación</a> ·
  <a href="#implementación">Implementación</a> ·
  <a href="#funcionamiento">Funcionamiento</a>
</p>

# Presentación
## 🤖 Arquitectura y caracteristicas
El sistema se divide en dos secciones principales: el cliente y la ESP32 (servidor/robot). La implementación del software está basada en Python y Micropython.

<p align="center">
    <img src="http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/queined/bfs-maze-bot/main/diagram.iuml" width="450">
</p>

El modelo cuenta con una interfaz de usuario que facilita la interacción con el robot. Esta interfaz se encarga de enviar comandos y recibir datos del servidor ESP32. La ESP32 actúa como servidor y controlador principal del robot, gestionando la recepción de comandos del cliente, controlando los servos y ejecutando la navegación en el laberinto.

## 🚩 Algoritmo y laberinto

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
## 💻 Configuración de software
###  Prerrequisitos
- [Python 3.x](https://www.python.org/downloads/)
- Micropython IDE ([Thonny IDE](https://thonny.org), [Mu Editor](https://codewith.mu))
- Micropython firmware ([ESP32/WROOM](https://micropython.org/download/ESP32_GENERIC/))
- [esptool.py](https://pypi.org/project/esptool/)
  
### Setup del cliente
1. Clonar el respositorio.
    ```bash
    $ git clone https://github.com/queined/bfs-maze-bot
    ```
2. Descargar [bfs-robot-v1.0.exe](https://drive.google.com/file/d/12i-oOMuXa5v5DpDR695XDnbXxDeKe0Vz/view?usp=sharing). Si se desea ejecutar desde el código fuente, instalar paquetes desde [requirements.txt](https://github.com/queined/bfs-maze-bot/blob/main/requirements.txt) y ejecutar [app.py](https://github.com/queined/bfs-maze-bot/blob/main/client/app.py).
    ```python
    $ pip install -r requirements.txt
    $ python app.py
    ```

### Setup de la ESP32

1. Instalar el [firmware](https://micropython.org/download/ESP32_GENERIC/) de Micropython para la ESP32/WROOM. Remplaza COMx por el puerto al que esta conectada la ESP32.
    ```bash
    $ python -m esptool --chip esp32 --port COMx --baud 460800 erase_flash
    $ python -m esptool --chip esp32 --port COMx --baud 460800 write_flash -z 0x1000 ESP32_GENERIC-20240222-v1.22.2.bin
    ```
2. Modificar el `SSID` y el `PASSWORD` de la red en [globals.py](https://github.com/queined/bfs-maze-bot/blob/main/esp32/modules/globals.py). Si se define un nuevo laberinto se debe modificar `MAZE`. Luego, cargar los archivos de [esp32](https://github.com/queined/bfs-maze-bot/tree/main/esp32) a la tarjeta.
3. El laberinto físico del ejemplo tiene dimensiones de 2x1.5 metros, y los servomotores están ajustados para desplazarse una casilla siguiendo estas unidades de medida. La calibración de los movimientos debe realizarse en la función [move.py](https://github.com/queined/bfs-maze-bot/blob/main/esp32/modules/move.py)

## ⚙ Configuración de hardware
### Materiales
- ESP32-WROOM
- Microservo SG90
- [DroidCam](https://www.dev47apps.com/) o Webcam HD
- Corte en acrilíco o MDF ([robot.pdf](https://drive.google.com/file/d/1Ww6aeQt7NfRK-QJ9MhmAraJnbKTxphb9/view?usp=drive_link))
- Ruedas de 65mm
- Protoboard o baquela

### Montaje
Coming soon...

# Funcionamiento
<p align="center">
    <img src="https://i.postimg.cc/2j24f1gQ/dummies.png" width="500">
</p>

Si las casillas de "Fin" y "Laberinto" se dejan vacías, se utilizarán por defecto las coordenadas (0,4) como punto de salida y se empleará la matriz del ejemplo que representa el laberinto. Al ejecutar "Escanear laberinto", se abrirá una ventana en la que se debe tomar la captura y seleccionar las cuatro esquinas del laberinto en el orden indicado a continuación.
<br>
<p align="center">
    <img src="https://i.postimg.cc/L41rCZ5s/robot.png" width="350">
</p>
Una vez que se hayan seleccionado las esquinas para ajustar la perspectiva, el procesamiento de imágenes detectará las coordenadas de inicio del robot. Al presionar "Enviar al robot", se enviará una solicitud JSON a través de HTTP que contendrá los datos de las coordenadas a la dirección IP asignada a la ESP32. Se asume que, por defecto, inicialmente el robot siempre debe apuntar hacia el norte.

# Licencia
Este proyecto tiene la licencia MIT; consulte el archivo de [LICENSE](https://github.com/queined/bfs-maze-bot/blob/main/LICENSE) para obtener más detalles.
