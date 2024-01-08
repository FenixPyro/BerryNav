"""Módulo donde se obtienen los datos base de la pókeAPI"""
import requests
# def get_berry_url(berry_name:str) -> str:
#     """Función que realiza la request y obtiene la url específica de una baya"""
#     url_berry = "https://pokeapi.co/api/v2/berry/"
#     data = requests.get(url_berry, timeout = 5)
#     if data.status_code == 200:
#         berry_data = data.json()
#         berry_data_list = berry_data["results"]
#         while berry_data["next"]:
#             next_data = requests.get((berry_data["next"]), timeout = 5)
#             next_berry_data = next_data.json()
#             berry_data_list.extend(next_berry_data["results"])
#             berry_data = next_berry_data
#         for berry in berry_data_list:
#             if berry["name"] == berry_name:
#                 berry_url = berry["url"]
#         return berry_url
#     else:
#         print("Error obtaining berry data")
#         return None

# bayaurl = get_berry_url("cheri")


def get_berry_url(berry_name:str) -> str:
    """Función que realiza la request y obtiene la url específica de una baya"""
    url_berry = "https://pokeapi.co/api/v2/berry/"
    url_specific_berry = requests.get(url_berry + berry_name, timeout = 5)
    if url_specific_berry.status_code == 200:
        berry_url = 
        return berry_url
    else:
        print("Error obtaining berry data")
        return None

bayaurl = get_berry_url("cheri")

