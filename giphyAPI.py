import os
import random
from dotenv import load_dotenv
import json
import requests
import sys
import giphy_client
from giphy_client.rest import ApiException


load_dotenv()
GIPHY_TOKEN = os.environ.get('GIPHY_KEY')

giphy_api = giphy_client.DefaultApi()

def search_gif(query):
    try:
        return giphy_api.gifs_search_get(GIPHY_TOKEN, query, limit=20)
    except ApiException as e:
        print(f"Exception was called when searching for {query}:\n{e}")

def send_gif(phrase):
    gifs = search_gif(phrase)
    response = random.choices(list(gifs.data))
    return response[0].url

