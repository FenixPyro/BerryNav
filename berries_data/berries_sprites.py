from berries_item_data import get_berry_item_data
def get_berry_sprite(berry_name:str) -> str:
    """Función que devuelve la URL del sprite de la baya"""
    item_data = get_berry_item_data(berry_name)
    berry_sprite = item_data["sprites"]["default"]
    return berry_sprite
