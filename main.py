import os
import discord
from discord.voice_client import VoiceClient
from discord.ext import commands
from dotenv import load_dotenv


client = commands.Bot(command_prefix='%')




@client.command()
async def reload(ctx, description="Reload features and their commands!"):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            print(f"Reloaded {filename[:-3]}")
            client.unload_extension(f"cogs.{filename[:-3]}")
            client.load_extension(f"cogs.{filename[:-3]}")


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="to Your Commands! Get started with %help"))

# Read for available Cogs upon startup
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")

# Run the Client
load_dotenv()
client.run(os.environ.get("DISCORD_TOKEN"))
