"""Módulo que contiene la clase Url"""

class Url:
    """Clase que toma el nombre de la baya y genera su URL"""
    def __init__ (self,name):
        self.name = name
    def create_url(self):
        """Función para crear la URL específica"""    
        return "https://pokeapi.co/api/v2/berry/" + self.name