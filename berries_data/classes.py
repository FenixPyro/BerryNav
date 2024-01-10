"""Módulo donde definimos la clase Berry, que contendrá todas sus características"""
from berries_attributes import get_berry_data


class Berry:
    "Clase que define las características de la baya"

    def __init__(self, name):
        self.name = name
        self.flavor = None
        self.natural_gift_power = None
        self.natural_gift_type = None
        self.description = None
        self.sprite = None
        self.growth_time = None

    def get_all(self):
        """Método para reunir la información de la baya"""
        all_data = get_berry_data(self.name)
        self.description = all_data[0]
        self.flavor = all_data[1]
        self.growth_time = all_data[2]
        self.natural_gift_power = all_data[3]
        self.natural_gift_type = all_data[4]
        self.sprite = all_data[5]
        return self.flavor, self.natural_gift_type, self.natural_gift_type, self.description, self.sprite, self.growth_time
