"""Módulo que reúne la información a utilizar de cada baya"""
import requests
from berries_data.berries_item_data import get_berry_item_data
from berries_data.api_request import make_api_request

def get_berry_data(berry_name:str)->list:
    """Función que reúne todos los datos de la baya en una tupla"""
    try:
        berry_data = make_api_request(berry_name)
        flavors_data = berry_data.get("flavors")
        growthtime = berry_data.get("growth_time") * 4
        natural_gift_power = berry_data.get("natural_gift_power")
        natural_gift_type = berry_data.get("natural_gift_type", {}).get("name")
        item_data = get_berry_item_data(berry_name)
        berry_sprite = item_data["sprites"]["default"]
        berry_description = item_data["effect_entries"][0]["effect"]
        berry_flavors = dict()
        for item in flavors_data:
            berry_flavors.update({item["flavor"]["name"]:item["potency"]})
        berry = (berry_description, berry_flavors, growthtime,
                natural_gift_power, natural_gift_type, berry_sprite)
        return berry

    except requests.RequestException as e:
        print(f"Error obtaining berry data: {e}")
        return None
    