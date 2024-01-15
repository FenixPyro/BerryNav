"""Módulo main para arrancar el programa"""
from tkinter import Tk
from berries_data.main_gui import PokeApp

if __name__ == "__main__":
    root = Tk()
    app = PokeApp(root)
    app.center_window()
    root.mainloop()
