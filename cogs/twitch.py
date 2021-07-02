import discord
from discord import client
from discord.embeds import Embed
from discord.ext import commands
import twitchAPI
import datetime 
from discord import Embed
class Twitch(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def streamer(self,ctx, streamer: str):
        live_status = twitchAPI.get_live_status(streamer)
        if live_status == True:
            URL = f"https://twitch.tv/{streamer}"

            streamerInfo = twitchAPI.get_streamer_info(streamer)
            embed = Embed(title=streamerInfo.stream_title, url=URL, colour=discord.Colour(
                0xf79772), timestamp=datetime.datetime.utcnow())
            embed.set_image(url=streamerInfo.profile_pic)
            embed.set_author(name=streamerInfo.username, url=URL,
                            icon_url=streamerInfo.profile_pic)
            embed.add_field(name="Game", value=twitchAPI.get_game_name(
                streamerInfo.game_id), inline=True)

            await ctx.send(f"Hey, {streamer} is **L I V E:**  <{URL}>, go support them! ")
            await ctx.send(embed=embed)

        if live_status == False:
            pass


    @commands.command()
    async def streamerjson(self,ctx, arg):
        try:
            json_list = twitchAPI._debug_stream(arg)
            await ctx.send(f"**Found {len(json_list)} Streamers:**\n```{json_list}```")
        except:
            await ctx.send(f"Unable to find streamer {arg}")   

    @commands.command()
    async def streamerObject(self, ctx, arg):
        streamer = twitchAPI.get_streamer_info(arg)
        await ctx.send()

def setup(client):
    client.add_cog(Twitch(client))