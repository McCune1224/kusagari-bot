import discord
from discord.ext import commands
from discord import message
import os
import giphyAPI

class TextChat(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.droidDir = os.path.join(os.getcwd(), "droidMedia")

    @commands.command()
    async def gif(self, ctx, *args):
        arg_phrase = " ".join(args[:])
        try:
            await ctx.send(giphyAPI.send_gif(arg_phrase))
        except:
            print(f"Unable to send GIF of {arg_phrase}")
            await ctx.send(f"No GIF of {arg_phrase} exists...")
    
    @commands.command()
    async def emote(self,ctx, emotion="greviousgamer"):
        await ctx.send(file=discord.File(os.path.join(self.droidDir, f"{emotion}.gif")))


def setup(client):
    client.add_cog(TextChat(client))
