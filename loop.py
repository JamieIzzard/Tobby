import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

client = discord.Client()

channelweb = '502510555618344960'   #Channel du webhook

@client.event
async def on_ready():
    while True:
        await client.purge_from(client.get_channel(channelweb), limit=10, check=None, before=None, after=None, around=None)
        client.send_message(await client.send_message(client.get_channel(channelweb),"!nbj"))
        time.sleep(15)


client.run(os.getenv('TOKEN'))
