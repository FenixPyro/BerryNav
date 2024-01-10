"""Módulo para acceder a la url del item"""
import requests
from api_request import make_api_request
def get_berry_item_data(berry_name:str) -> str:
    """Función que devuelve la descripción de la baya"""
    try:
        berry_item_url = make_api_request(berry_name)["item"]["url"]
        berry_item_data = requests.get(berry_item_url, timeout = 5)
        if berry_item_data.status_code == 200:
            berry_item = berry_item_data.json()
            return berry_item
    except requests.RequestException as e:
        print(f"Error obtaining berry data: {e}")
        return None
