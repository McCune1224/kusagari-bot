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


# API Access Info
CLIENT_ID = os.environ.get('TWITCH_CLIENT_ID')
CLIENT_SECRET = os.environ.get('TWITCH_CLIENT_SECRET')
TOKEN = os.environ.get('TWITCH_AUTH_TOKEN')
BASE_URL = 'https://api.twitch.tv/helix/'
HEADERS = {'Client-Id': CLIENT_ID, 'Authorization': 'Bearer {0}'.format(TOKEN)}



def generate_token():
    url = 'https://id.twitch.tv/oauth2/token?client_id={0}&client_secret={1}&grant_type=client_credentials'.format(CLIENT_ID, CLIENT_SECRET)
    response = requests.post(url)
    new_token = response.json()
    return new_token['access_token']


def get_twitch_profile_pic(streamer):
    url = 'https://api.twitch.tv/helix/search/channels?query={0}'.format(streamer)
    #  json_data['data'][0]['broadcaster_login'] 


    print(HEADERS)
    response = requests.get(url, headers = HEADERS)
    print(response.json())
    json_data = response.json()
    print(json_data['data'])
    index = 0
    while json_data['data'][index]['broadcaster_login'] != streamer:
        index += 1
    return json_data['data'][index]['thumbnail_url']

def is_live(streamer):
    url = 'https://api.twitch.tv/helix/search/channels?query={0}'.format(streamer)
    #  json_data['data'][0]['broadcaster_login'] 


    print(HEADERS)
    response = requests.get(url, headers = HEADERS)
    print(response.json())
    json_data = response.json()
    print(json_data['data'])
    index = 0
    while json_data['data'][index]['broadcaster_login'] != streamer:
        index += 1
    if json_data['data'][index]['is_live'] == False:
        return '{0} is offline'.format(streamer)
    if json_data['data'][index]['is_live'] == False:
        return '{0} is offline'.format(streamer)




#curl --location --request
#GET 'https://api.twitch.tv/helix/search/channels?query=a_seagull' \
#--header 'client-id: wbmytr93xzw8zbg0p1izqyzzc5mbiz' \
#--header 'Authorization: Bearer 2gbdx6oar67tqtcmt49t3wpcgycthx'




