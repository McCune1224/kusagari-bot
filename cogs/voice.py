import os
import time
import discord
from discord import client
from discord.ext import commands
from discord import message
from discord.voice_client import VoiceClient






class VoiceChat(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.droidDir = os.path.join(os.getcwd(), "droidMedia")

    # @commands.command(pass_context=True)
    # async def join(self, ctx):
    #     author = ctx.message.author
    #     channel = author.voice.channel
    #     if channel:
    #         await channel.connect()
    #     else:
    #         await ctx.send(f"{author} is not in a voice channel.")

    # @commands.command()
    # async def leave(self, ctx):
    #     if ctx.voice_client:
    #         await ctx.guild.voice_client.disconnect()
    #     else:
    #         await ctx.send("Not currently in a voice channel.")

    

    @commands.command()
    async def roger(self, ctx, phrase="roger"):
        """Join and play a mp3 -> FFmpeg clip to requested user's voice channel. Requires a phrase to search for specific mp3 file"""

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
