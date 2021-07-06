import discord
from discord.ext import commands
from discord import message
import os

class Tools(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        if round(self.client.latency * 1000) <= 50:
            embed=discord.Embed(title="PING", description=f":ping_pong: The ping is **{round(self.client.latency *1000)}** milliseconds!", color=0x44ff44)
        elif round(self.client.latency * 1000) <= 100:
            embed=discord.Embed(title="PING", description=f":ping_pong: The ping is **{round(self.client.latency *1000)}** milliseconds!", color=0xffd000)
        elif round(self.client.latency * 1000) <= 200:
            embed=discord.Embed(title="PING", description=f":ping_pong: The ping is **{round(self.client.latency *1000)}** milliseconds!", color=0xff6600)
        else:
            embed=discord.Embed(title="PING", description=f":ping_pong: The ping is **{round(self.client.latency *1000)}** milliseconds!", color=0x990000)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Tools(client))