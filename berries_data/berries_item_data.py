import requests

url_base = "https://pokeapi.co/api/v2/berry/"
def get_berry_item_data(berry_name:str) -> str:
    """Función que devuelve la descripción de la baya"""
    item_data = requests.get(url_base + berry_name,timeout=5)
    if item_data.status_code == 200:
        berry_item_url = item_data.json()["item"]["url"]
        berry_item_data = requests.get(berry_item_url, timeout = 5)
        if berry_item_data.status_code == 200:
            berry_item = berry_item_data.json()
            return berry_item
    else:
        print("Error obtaining berry data")
        return None  
    