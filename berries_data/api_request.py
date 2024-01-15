"""Módulo con la función que realiza la request de la API"""
import requests
from berries_data.url_module import Url

def make_api_request(berry_name):
    """Función que hace la request y lo devuelve en formato json"""
    berry_url = Url(berry_name)
    url = berry_url.create_url()
    try:
        r = requests.get(url, timeout=2)
        return r.json()
    except requests.RequestException as e:
        print(f"Error making API request: {e}")
        return None
