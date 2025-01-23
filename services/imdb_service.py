import requests
from config import Config

def fetch_imdb_metadata(title):
    url = f"https://imdb-api.com/en/API/SearchTitle/{Config.IMDB_API_KEY}/{title}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

