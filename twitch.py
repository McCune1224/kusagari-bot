import os
from dotenv import load_dotenv
import json
import requests
import sys

load_dotenv()

# API Access Info
CLIENT_ID = os.environ.get('TWITCH_CLIENT_ID')
TOKEN = os.environ.get('TWITCH_AUTH_TOKEN')
BASE_URL = 'https://api.twitch.tv/helix/'
HEADERS = {'client_id': CLIENT_ID, 'Authorization': 'Bearer {0}'.format(TOKEN)}


#curl --location --request
#GET 'https://api.twitch.tv/helix/search/channels?query=a_seagull' \
#--header 'client-id: wbmytr93xzw8zbg0p1izqyzzc5mbiz' \
#--header 'Authorization: Bearer 2gbdx6oar67tqtcmt49t3wpcgycthx'


