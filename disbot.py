import discord
import requests
from discord.ext import commands

client = commands.AutoShardedBot(command_prefix="!")
TOKEN = "INSERTTOKENHERE"



@client.event
async def on_ready():
  print(f"{client.user} has connected to Discord and is sending to Disbot.top")


client.run(TOKEN)
