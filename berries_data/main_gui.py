"""Módulo donde se desarrolla la ventana principal"""
from tkinter import ttk
from io import BytesIO
from PIL import ImageTk, Image
import requests
from berries_data.classes import Berry

class PokeApp:
    """Clase que contiene los parámetros de la GUI"""
    def __init__(self,root):
        self.root = root
        self.root.geometry("400x300")
        self.root.title("BerryNav for Pokémon Emerald")
        self.main_frame = ttk.Frame()
        self.create_widgets()

    def center_window(self):
        """Función para centrar la ventana principal"""
        self.root.update_idletasks()
        width = self.main_frame.winfo_reqwidth()
        height = self.main_frame.winfo_reqheight()
        screen_width = self.main_frame.winfo_screenwidth()
        screen_height = self.main_frame.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        """Función que crea los widgets"""
        self.flavors_tree = ttk.Treeview(self.main_frame, columns=(0, 1), height=5, show="headings")
        self.flavors_tree.heading(0, text="Flavors")
        self.flavors_tree.heading(1, text="Potency")
        self.flavors_tree.column(0, width=100, anchor="center")
        self.flavors_tree.column(1, width=100, anchor="center")
        self.description_label = ttk.Label(self.main_frame, text="", font=("Helvetica", 13))
        self.search_entry = ttk.Entry(self.main_frame)
        self.search_button=ttk.Button(self.main_frame,text = "Search",command=self.configure_labels)
        self.sprite_label = ttk.Label(self.main_frame, image = None, borderwidth=1, relief="solid")
        self.name_label = ttk.Label(self.main_frame, text = "", font=("Helvetica", 23))
        self.natural_gift_label = ttk.Label(self.main_frame, text = "", font=("Helvetica", 11))
        self.growth_time_label = ttk.Label(self.main_frame, text = "", font=("Helvetica", 15))
        self.main_frame.grid(column=0,row=0)
        self.name_label.grid(column = 1, row = 0, columnspan = 2)
        self.description_label.grid(column = 1, row = 1, columnspan = 2, padx=(20,20))
        self.search_entry.grid(column=1,row=3)
        self.search_button.grid(column=2,row=3)
        self.natural_gift_label.grid(column=0, row=3, pady=(0,20))
        self.growth_time_label.grid(column = 1, row = 2, columnspan = 2)

    def configure_labels(self):
        """Función que actualiza la información dependiendo de la entrada del usuario"""
        berry_entry = self.search_entry.get().lower()
        berry = Berry(berry_entry)
        berry.get_all()
        self.description_label.configure(text=berry.description)
        response = requests.get(berry.sprite, timeout = 5)
        berry_sprite =Image.open(BytesIO(response.content))
        resized_image = berry_sprite.resize((120, 120))
        img = ImageTk.PhotoImage(resized_image)
        if img:
            self.sprite_label.config(image=img)
            self.sprite_label.image=img
        self.name_label.configure(text= berry_entry.capitalize()+ " Berry")
        self.natural_gift_label.configure(text="Natural Gift" + "\n" + "Type: " +
                                    berry.natural_gift_type.capitalize() +
                                    "\n" + "Power: " + str(berry.natural_gift_power))
        self.growth_time_label.configure(text= "The berries will grow in: " +
                                        str(berry.harvest_time) + " hours" )
        self.flavors_tree.delete(*self.flavors_tree.get_children())
        self.flavors_tree.grid(column=0, row=2, pady=(20,20), padx=(20,0))
        for key, value in berry.flavor.items():
            self.flavors_tree.insert("", "end", values=(key.capitalize(),value))
        self.sprite_label.grid(column = 0, row = 0, rowspan = 2, pady=(20,20), padx=(10,10))
        self.center_window()
