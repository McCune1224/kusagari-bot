import os
from re import U
from urllib.parse import uses_fragment
from discord import message
from discord.utils import DISCORD_EPOCH
from dotenv import load_dotenv
import requests
import datetime
import twitch
import discord
from discord.ext import commands
from discord import Embed




client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print('Logged in as {0}'.format(client.user))


@client.command()
async def ping(ctx):
    await ctx.send('Input received {0}ms'.format(round(client.latency)*1000))

@client.command()
async def streamer(ctx, streamer: str, debug = False):
    live_status = twitch.get_live_status(streamer)
    if live_status == True:
        URL = "https://twitch.tv/{0}".format(streamer)
        
        streamerInfo = twitch.get_streamer_info(streamer)
        embed = Embed(title=streamerInfo.stream_title, url = URL, colour=discord.Colour(0xf79772), timestamp=datetime.datetime.utcnow())
        embed.set_image(url=streamerInfo.profile_pic)
        embed.set_author(name=streamerInfo.username, url=URL, icon_url=streamerInfo.profile_pic)
        embed.add_field(name="Game", value=twitch.get_game_name(streamerInfo.game_id), inline=True)

        await ctx.send("Hey, {0} is **L I V E:**  <{1}>, go support them! ".format(streamer,URL))
        await ctx.send(embed=embed)

    if live_status == False:
        pass

@client.command()
async def streamerjson(ctx, arg):
    json_list = twitch.debug_stream(arg)
    await ctx.send ("**Found {0} Streamers:**\n```{1}```".format(len(json_list), json_list))

# @client.command()
# async def embedded(ctx, arg):
#     test = Embed(title=arg)
#     await ctx.send(embed=test)





#Run the Client
load_dotenv()
client.run(os.environ.get("DISCORD_TOKEN"))


