"""Módulo donde se desarrolla la ventana principal"""
from tkinter import *
from tkinter import ttk
from io import BytesIO
from PIL import ImageTk, Image
from berries_sprites import get_berry_sprite
from berries_object import *
import requests
import pandas as pd

root = Tk()
root.title("Pokémon Emerald: Berries")
root.geometry("800x600")

main_frame = ttk.Frame(root)

def get_berry_img (berry_name):
    """Función para obtener una imágen temporal de la baya"""
    response = requests.get(get_berry_sprite(berry_name), timeout = 5)
    berry_sprite =Image.open(BytesIO(response.content))
    return  ImageTk.PhotoImage(berry_sprite)

# def flavors_table(berry_entry):
#     """Función que genera una tabla con los sabores y sus valores"""
#     berry_chosen = Berry(berry_entry)
#     berry_flavors = berry_chosen.flavor
#     df = pd.DataFrame([list(berry_flavors.keys()), list(berry_flavors.values())], index = ["Flavors", "Potency"]).transpose()
#     df["Flavors"] = df["Flavors"].apply(lambda x: x.ljust(15))  # Alineación a la izquierda
#     df["Potency"] = df["Potency"].apply(lambda x: str(x).rjust(15))  
#     table_text = df.to_string(index=False)
#     return table_text

def configure_labels():
    """Función que actualiza la información dependiendo de la entrada del usuario"""
    berry_entry = search_entry.get().lower()
    berry = Berry(berry_entry)
    berry.get_all()
    description_label.configure(text=berry.flavor)
    img = get_berry_img(berry_entry)
    name_label.configure(text= berry_entry.capitalize()+ " Berry")
    natural_gift_label.configure(text=berry.natural_gift)
    growth_time_label.configure(text= "Growth time:" + "\n" + str(berry.growth_time) + " hours" )
    # flavors_label.configure(text=flavors_table(berry_entry))
    if img:
        sprite_label.configure(image=img)
        sprite_label.image = img
    berry_entry = search_entry.get().lower()
    berry = Berry(berry_entry)
    print("Se terminó la ejecución")

description_label = ttk.Label(main_frame, text="", font=("Arial", 11))
search_entry = ttk.Entry(main_frame)
search_button = ttk.Button(main_frame, text = "Search", command = configure_labels)
sprite_label = ttk.Label(main_frame, image = "")
name_label = ttk.Label(main_frame, text = "", font=("Arial", 32))
natural_gift_label = ttk.Label(main_frame, text = "",font=("Arial", 12))
growth_time_label = ttk.Label(main_frame, text = "", font=("Arial", 12))
flavors_label = ttk.Label(main_frame,text= "", font=("Arial", 12))

main_frame.grid(column=0,row=0)
sprite_label.grid(column = 0, row = 0, rowspan = 2)
name_label.grid(column = 1, row = 0, columnspan = 2)
description_label.grid(column = 1, row = 1, columnspan = 2)
search_entry.grid(column=1,row=3)
search_button.grid(column=2,row=3)
natural_gift_label.grid(column=0, row=3)
growth_time_label.grid(column = 1, row = 2, columnspan = 2)
flavors_label.grid(column=0, row=2)

root.mainloop()