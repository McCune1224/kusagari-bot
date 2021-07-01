import os
import time
import discord
from discord import client
from discord.ext import commands
from discord import message
from discord.voice_client import VoiceClient
import giphyAPI






class VoiceChat(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.droidDir = os.path.join(os.getcwd(), "droidSounds")

    @commands.command(pass_context=True)
    async def join(self, ctx):
        author = ctx.message.author
        channel = author.voice.channel
        if channel:
            await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client:
            await ctx.guild.voice_client.disconnect()

    @commands.command()
    async def gif(self, ctx, *args):
        arg_phrase = " ".join(args[:])
        try:
            await ctx.send(giphyAPI.send_gif(arg_phrase))
        except:
            print(f"Unable to send GIF of {arg_phrase}")
            await ctx.send(f"No GIF of {arg_phrase} exists...")

    #Need to find windows solution for ffmpeg
    @commands.command()
    async def roger(self, ctx, phrase="roger"):
        author = ctx.message.author
        voice_channel = author.voice.channel
        if voice_channel != None:
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio(
                source=os.path.join(self.droidDir, phrase+".mp3")))
            # Sleep while audio is playing.
            while vc.is_playing():
                time.sleep(.1)
            await vc.disconnect()
        else:
            await ctx.send(str(ctx.author.name) + "is not in a channel.")
        # await ctx.message.delete()


def setup(client):
    client.add_cog(VoiceChat(client))
