from Modules.draw_maze import draw_maze
from Modules.start_robot import start_robot
from Modules import globals
import os
import cv2
import numpy as np
import ast

import tkinter as tk
from PIL import Image, ImageTk


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("bfs-maze-bot")
        self.geometry("350x450")

        self.img_label = tk.Label(self)
        self.img_label.pack(pady=10)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=5)

        self.draw_button = tk.Button(
            button_frame, text="Escanear laberinto", command=self.scan_path
        )
        self.draw_button.pack(side=tk.LEFT, padx=5)

        self.start_value_label = tk.Label(
            self, text=f"Inicio: {globals.start} | Fin: {globals.end}"
        )
        self.start_value_label.pack(pady=10)

        input_frame = tk.Frame(self)
        input_frame.pack(pady=5)

        right_column = tk.Frame(input_frame)
        right_column.pack(side=tk.LEFT, padx=5)

        left_column = tk.Frame(input_frame)
        left_column.pack(side=tk.LEFT, padx=5)

        self.esp32_IP_label = tk.Label(left_column, text="IP de la ESP32:")
        self.esp32_IP_label.pack(pady=5)
        self.esp32_IP_entry = tk.Entry(left_column)
        self.esp32_IP_entry.pack(pady=5)

        self.camera_label = tk.Label(right_column, text="IP de la cámara:")
        self.camera_label.pack(pady=5)
        self.camera_entry = tk.Entry(right_column)
        self.camera_entry.pack(pady=5)

        self.maze_label = tk.Label(left_column, text="Laberinto:")
        self.maze_label.pack(pady=5)
        self.maze_entry = tk.Entry(left_column)
        self.maze_entry.pack(pady=5)

        self.end_label = tk.Label(right_column, text="Fin:")
        self.end_label.pack(pady=5)
        self.end_entry = tk.Entry(right_column)
        self.end_entry.pack(pady=5)

        self.save_button = tk.Button(
            button_frame, text="Guardar valores", command=self.save_globals
        )
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.start_button = tk.Button(
            button_frame, text="Enviar al robot", command=self.start_robot
        )
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.show_image()

    def show_image(self, img=None):
        if img is None:
            img = np.ones((200, 300, 3), dtype=np.uint8) * 255
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = ImageTk.PhotoImage(image=Image.fromarray(img_rgb))
        self.img_label.config(image=img_pil)
        self.img_label.image = img_pil

    def scan_path(self):
        esp32_IP_text = self.esp32_IP_entry.get()
        camera_text = self.camera_entry.get()
        if camera_text.strip() != "":
            globals.camera = "http://" + str(camera_text) + "/video"
            print(globals.camera)
            img = draw_maze()
            self.show_image(img)
            self.start_value_label.config(
                text=f"Inicio: {globals.start} → Fin: {globals.end}"
            )

    def start_robot(self):
        esp32_IP_text = self.esp32_IP_entry.get()
        if esp32_IP_text.strip() != "":
            globals.esp32_IP = "http://" + str(esp32_IP_text)
            print(globals.esp32_IP)
            start_robot()

    def save_globals(self):
        esp32_IP_text = self.esp32_IP_entry.get()
        camera_text = self.camera_entry.get()
        maze_text = self.maze_entry.get()
        end_text = self.end_entry.get()

        if esp32_IP_text.strip() != "":
            globals.esp32_IP = "http://" + str(esp32_IP_text)
        if camera_text.strip() != "":
            globals.camera = "http://" + str(camera_text) + "/video"
        if maze_text.strip() != "":
            globals.maze = ast.literal_eval(maze_text)
        if end_text.strip() != "":
            globals.end = tuple(int(valor) for valor in end_text.split(","))
            self.start_value_label.config(
                text=f"Inicio: {globals.start} → Fin: {globals.end}"
            )


app = GUI()
app.mainloop()
