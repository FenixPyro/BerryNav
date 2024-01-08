"""Módulo que reúne la información a utilizar de cada baya"""

import requests
from berries_item_data import get_berry_item_data
url_base = "https://pokeapi.co/api/v2/berry/"
def get_berry_flavors(berry_name:str)->list:
    """Función que reúne todos los sabores de la baya en un diccionario"""
    flavor_data = requests.get(url_base + berry_name, timeout=5)
    if flavor_data.status_code == 200:
        flavors = flavor_data.json()["flavors"]
        berry_flavors = dict()
        for item in flavors:
            berry_flavors.update({item["flavor"]["name"]:item["potency"]})
        return berry_flavors
    else:
        print("Error obtaining berry data")
        return None

def get_berry_growthtime(berry_name:str) -> int:
    """Función que devuelve el tiempo que tarda la baya en crecer"""
    growthtime_data = requests.get(url_base + berry_name,timeout=5)
    if growthtime_data.status_code == 200:
        growthtime = growthtime_data.json()["growth_time"]
        growthtime = growthtime * 4
        return growthtime
    else:
        print("Error obtaining berry data")
        return None

def get_berry_natural_gift(berry_name:str) -> list:
    """Función que reúne la potencia y el tipo del movimiento Natural Gift al poseer la baya"""
    natural_gift_data = requests.get(url_base + berry_name,timeout=0.1)
    if natural_gift_data.status_code == 200:
        natural_gift_power = natural_gift_data.json()["natural_gift_power"]
        natural_gift_type = natural_gift_data.json()["natural_gift_type"]["name"]
        natural_gift_values = list()
        natural_gift_values.append(natural_gift_power)
        natural_gift_values.append(natural_gift_type)
        return "Natural Gift" + "\n" + "Type: " + str(natural_gift_values[1]).capitalize() + "\n" + "Potency: " + str(natural_gift_values[0])
    else:
        print("Error obtaining berry data")
        return None 

def get_berry_description(berry_name:str) -> str:
    """Función que devuelve la descripción de la baya"""
    item_data = get_berry_item_data(berry_name)
    berry_description = item_data["effect_entries"][0]["effect"]
    return berry_description
print(get_berry_growthtime("cheri"))