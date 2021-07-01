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
    def __init__(self,username="",is_live=False,streamer_title="",profile_pic="",game_id=0):
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

'''returns profile picture of streamer'''
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

'''Query the Twitch API for channel info of inputed streamer'''
def get_live_status(streamer, debug = True):
    #Get JSON Data:
    url = 'https://api.twitch.tv/helix/search/channels?query={0}'.format(streamer)
    response = requests.get(url, headers = HEADERS)
    json_data = response.json()

    if debug == True: 
        print(json_data['data'])

    try:
        #Enumerate JSON data:
        index = 0
        while (index != len(json_data['data'])-1):
            json_streamer_name = json_data['data'][index]['broadcaster_login'] 
            json_is_live = json_data['data'][index]['is_live'] 

            #check if we can find the streamer and if they're live:
            if (json_streamer_name == streamer and json_is_live == False):
                return False
            if (json_streamer_name == streamer and json_is_live == True):
                return True 
            index += 1
    except:
        #can't find streamer 
        print("failed to find any info on streamer {0}".format(streamer))
        return -1

def get_streamer_info(streamer):
    url = 'https://api.twitch.tv/helix/search/channels?query={0}'.format(streamer)
    response = requests.get(url, headers = HEADERS)
    json_data = response.json()

    info = ["broadcaster_login","is_live","title","thumbnail_url","game_id"]
    try:
        #Enumerate JSON data:
        index = 0
        query = json_data['data'][index]
        while (index != len(json_data['data'])-1):
            json_streamer_name = query['broadcaster_login'] 

            #check if we can find the streamer and if they're live:
            if (json_streamer_name == streamer):
                return Streamer(
                    query[info[0]],
                    query[info[1]],
                    query[info[2]],
                    query[info[3]],
                    query[info[4]]
                    )
            index += 1
    except:
        print("unable to find {0}'s info".format(streamer))
        return -1


def get_game_name(id):
    url = BASE_URL+'games?id={0}'.format(id)
    response = requests.get(url, headers = HEADERS)
    json_data = response.json()
    return (json_data['data'][0]['name'])

def _debug_stream(streamer):
    url = 'https://api.twitch.tv/helix/search/channels?query={0}'.format(streamer)
    #  json_data['data'][0]['broadcaster_login'] 

    streamer_list = []
    response = requests.get(url, headers = HEADERS)
    json_data = response.json()
    index = 0
    while (json_data['data'][index]['broadcaster_login'] != streamer or index == 19):
        try:
            index += 1
            streamer_list.append(json_data['data'][index]['broadcaster_login']) 
        except:
            break
    return streamer_list

#curl --location --request
#GET 'https://api.twitch.tv/helix/search/channels?query=a_seagull' \
#--header 'client-id: wbmytr93xzw8zbg0p1izqyzzc5mbiz' \
#--header 'Authorization: Bearer 2gbdx6oar67tqtcmt49t3wpcgycthx'



if __name__ == '__main__':
    if len(sys.argv) == 1:
        get_live_status('hootalin')
    else:
        _debug_stream(sys.argv[1])
