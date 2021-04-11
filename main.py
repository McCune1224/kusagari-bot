import requests
import os
import twitch
from re import U
from urllib.parse import uses_fragment
import discord
from discord.voice_client import VoiceClient
from discord import message
from discord.utils import DISCORD_EPOCH
from dotenv import load_dotenv
import datetime
from discord.ext import commands
from discord import Embed
import giphy


client = commands.Bot(command_prefix='%')


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.command()
async def ping(ctx):
    await ctx.send(f"Input received {round(client.latency)*1000}ms")


@client.command()
async def streamer(ctx, streamer: str, debug=False):
    live_status = twitch.get_live_status(streamer)
    if live_status == True:
        URL = f"https://twitch.tv/{streamer}"

        streamerInfo = twitch.get_streamer_info(streamer)
        embed = Embed(title=streamerInfo.stream_title, url=URL, colour=discord.Colour(
            0xf79772), timestamp=datetime.datetime.utcnow())
        embed.set_image(url=streamerInfo.profile_pic)
        embed.set_author(name=streamerInfo.username, url=URL,
                         icon_url=streamerInfo.profile_pic)
        embed.add_field(name="Game", value=twitch.get_game_name(
            streamerInfo.game_id), inline=True)

        await ctx.send(f"Hey, {streamer} is **L I V E:**  <{URL}>, go support them! ")
        await ctx.send(embed=embed)

    if live_status == False:
        pass


@client.command()
async def streamerjson(ctx, arg):
    try:
        json_list = twitch._debug_stream(arg)
        await ctx.send(f"**Found {len(json_list)} Streamers:**\n```{json_list}```")
    except:
        await ctx.send(f"Unable to find streamer {arg}")
# @client.command()
# async def embedded(ctx, arg):
#     test = Embed(title=arg)
#     await ctx.send(embed=test)


@client.command()
async def play(ctx, arg: str):
    try:
        author = ctx.message.author
        print(author)
        channel = author.voice.channel
        print(channel)
        await channel.connect() 
    except:
        print(f"Unable to join channel {channel.connect().cr_code}")
# @bot.command()
# async def join(ctx):
#     channel = ctx.author.voice.channel
#     await channel.connect()
# @bot.command()
# async def leave(ctx):
#     await ctx.voice_client.disconnect()

@client.command()
async def gif(ctx,*args):
    arg_phrase = " ".join(args[:])
    try:
        await ctx.send(giphy.send_gif(arg_phrase))
    except:
        print(f"Unable to send GIF of {arg_phrase}")
        await ctx.send(f"No GIF of {arg_phrase} exists...")

# Run the Client
load_dotenv()
client.run(os.environ.get("DISCORD_TOKEN"))
