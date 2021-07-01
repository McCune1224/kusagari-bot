import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events for cogs
    @commands.Cog.listener()
    async def on_ready(self):
        print("Example cog loaded")

    @commands.command()
    async def example(self, ctx):
        await ctx.send("Example cog command registered")

def setup(client):
    client.add_cog(Example(client))

