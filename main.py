import os
import discord
from dotenv import load_dotenv
import requests
import json
import twitch

load_dotenv()
token = os.environ.get('DISCORD_TOKEN') 


client = discord.Client()

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$inspire'):
        await message.channel.send(get_quote())

    if message.content.startswith('$busybunni'):
        await message.channel.send(twitch.get_twitch_profile_pic('busybunni'))

    if message.content.startswith('$isonline'):
        await message.channel.send(twitch.is_live('busybunni'))


client.run(os.environ.get("DISCORD_TOKEN"))
