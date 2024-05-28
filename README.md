# bfs-maze-bot
Modelo de un robot autónomo capaz de resolver laberintos utilizando una tarjeta esp32 como unidad de control principal. El robot combina el uso del algoritmo de Búsqueda en Anchura (BFS) con técnicas de visión artificial para mapear y navegar a través del laberinto de manera eficiente.
## Diagrama de componentes
La arquitectura del sistema se divide en dos secciones principales: el cliente y la ESP32 (servidor/robot).
![diagram](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/queined/bfs-maze-bot/main/diagram.iuml)
## Búsqueda en Anchura (BFS)
Es un método de exploración de grafos utilizado para recorrer o buscar en estructuras de datos como grafos o árboles. BFS explora los nodos del grafo por niveles, comenzando desde un nodo raíz y explorando todos sus nodos vecinos antes de pasar al siguiente nivel de nodos.

En este proyecto, se ha adaptado el algoritmo BFS para operar con una matriz que representa el laberinto. Cada celda de la matriz corresponde a una casilla en el laberinto, donde las paredes y los espacios libres se representan con unos y ceros, respectivamente.

| Dirección | Valor Binario |
|-----------|---------------|
| Norte     | 0b0001        |
| Sur       | 0b0010        |
| Este      | 0b0100        |
| Oeste     | 0b1000        |

Existen entonces 16 posibles combinaciones a las que se enfrenta el robot en cada posición. De esta forma, un laberinto que luce de esta manera:

[![maze.png](https://i.postimg.cc/mD4TYq8j/maze.png)](https://postimg.cc/Mcskxskf)

Se interpreta como una matriz de números de cuatro bits:

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
 

