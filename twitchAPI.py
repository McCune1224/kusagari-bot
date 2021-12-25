import os
from dotenv import load_dotenv
import json
import requests
import sys

load_dotenv()

# ~~ SAMPLE GET REQUEST AND PRINTING JSON INFO ~~ 
#stream_info = requests.get('https://randomfox.ca/floof/') 
#fox = stream_info.json()
#print(fox['image'])


'''Class to store useful streamer info from'''
class Streamer:
    def __init__(self,username=" ",is_live=False,streamer_title="title",profile_pic=" ",game_id=0):
        self.username = username
        self.is_live = is_live
        self.stream_title = streamer_title
        self.profile_pic = profile_pic
        self.game_id = game_id 



# API Access Info
CLIENT_ID = os.environ.get('TWITCH_CLIENT_ID')
CLIENT_SECRET = os.environ.get('TWITCH_CLIENT_SECRET')
TOKEN = os.environ.get('TWITCH_AUTH_TOKEN')
BASE_URL = 'https://api.twitch.tv/helix/'
HEADERS = {'Client-Id': CLIENT_ID, 'Authorization': 'Bearer {0}'.format(TOKEN)}


'''Makes new OAuth token'''
def _generate_token():
    url = 'https://id.twitch.tv/oauth2/token?client_id={0}&client_secret={1}&grant_type=client_credentials'.format(CLIENT_ID, CLIENT_SECRET)
    response = requests.post(url)
    new_token = response.json()
    print(new_token['access_token'])



eventSubURL = "https://api.twitch.tv/helix/eventsub/subscriptions"

