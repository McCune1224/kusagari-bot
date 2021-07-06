import discord
from discord.ext import commands
import requests
import os 

class StarWars(commands.Cog):
    def __init__(self,client):
        self.client = client
        self.swapiURL = "https://swapi.dev/api/"
        self.droidMedia = os.path.join(os.getcwd(), "droidMedia")

    @commands.command()
    async def swcharacter(self,ctx, character):
        """Using the SWAPI, fetch a character's JSON info and return it as a formatted embeded message"""

        personSearch = f"people/?search={character}"
        swapiInfo = requests.get(self.swapiURL+personSearch) 
        if swapiInfo.status_code != 200:
            await ctx.send("Unable to find Person (HTTP 200)", file=discord.File(os.path.join(self.droidMedia, "fail.jpg")))
        else:
            if swapiInfo.json()["count"] == 0:
                await ctx.send(f"Unable to find Person (No Record of Person '{character}')", file=discord.File(os.path.join(self.droidMedia, "fail.jpg")))
            else:
                swapiInfo = swapiInfo.json()["results"][0]
                await ctx.send(swapiInfo)


def setup(client):
    client.add_cog(StarWars(client))
