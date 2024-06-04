from Modules.draw_maze import draw_maze
from Modules.start_robot import start_robot
from Modules import globals
import os
import cv2


import tkinter as tk
from PIL import Image, ImageTk
import os

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GUI con Tkinter")
        self.geometry("400x300")
        
        self.img_label = tk.Label(self)
        self.img_label.pack(pady=10)

        self.draw_button = tk.Button(self, text="Escanear laberinto", command=self.scan_path)
        self.draw_button.pack(pady=5)

        self.start_button = tk.Button(self, text="Iniciar Robot", command=self.start_robot)
        self.start_button.pack(pady=5)

        self.show_image()

    def show_image(self):
        if os.path.exists(globals.imgpath):
            image = Image.open(globals.imgpath)
            photo = ImageTk.PhotoImage(image)
            self.img_label.config(image=photo)
            self.img_label.image = photo
        else:
            self.img_label.config(text="Standby...")

    def scan_path(self):
        draw_maze()
        self.show_image()


    def start_robot(self):
        start_robot()


app = GUI()
app.mainloop()
