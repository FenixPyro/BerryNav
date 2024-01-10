import requests
from url_module import Url
def make_api_request(berry_name):
    berry_url = Url(berry_name)
    url = berry_url.create_url()
    try:
        r = requests.get(url, timeout=2)
        return r.json()
    except requests.RequestException as e:
        print(f"Error making API request: {e}")
        return None
