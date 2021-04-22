import discord
import requests
from discord.ext import commands

client = commands.AutoShardedBot(command_prefix="!")
TOKEN = "INSERTTOKENHERE"

clientid = insertclientidherenoquotes
disbottoken = "INSERTYOURDISBOTTOKENHERE"

async def disbot():
    while True:
        url = f"https://disbot.top/api/v2/bot/{clientid}/update"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = {disbottoken}
        headers["Content-Type"] = "application/x-www-form-urlencoded"

        data = f"serverCount={len(client.guilds)}"


        resp = requests.post(url, headers=headers, data=data)
        print(f"{resp} We did it")

@client.event
async def on_ready():
  print(f"{client.user} has connected to Discord and is sending to Disbot.top")
  client.loop.create_task(disbot())


client.run(TOKEN)
