import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('/home/queined/bfs-maze/maze.jpg')  # Reemplaza 'tu_imagen.jpg' con la ruta de tu imagen

# Coordenadas de los cuatro puntos rojos en las esquinas
puntos = [(50, 50), (50, imagen.shape[0]-50), (imagen.shape[1]-50, 50), (imagen.shape[1]-50, imagen.shape[0]-50)]

# Dibujar la cuadrícula
ancho_celda = imagen.shape[1] // 8
alto_celda = imagen.shape[0] // 6

# Dibujar líneas horizontales
for i in range(1, 6):
    cv2.line(imagen, (0, i * alto_celda), (imagen.shape[1], i * alto_celda), (255, 255, 255), 1)

# Dibujar líneas verticales
for i in range(1, 8):
    cv2.line(imagen, (i * ancho_celda, 0), (i * ancho_celda, imagen.shape[0]), (255, 255, 255), 1)

# Mostrar la imagen con la cuadrícula
cv2.imshow('Imagen con cuadrícula', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
