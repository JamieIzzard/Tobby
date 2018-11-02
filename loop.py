import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import datetime
import time
from threading import *
import os

client = discord.Client()

channeltime = '502399480176443394' #Channel où le Bot écrit le repère
channelweb = '502510555618344960'   #Channel du webhook

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, game= discord.Game(name="faire des galipettes", type=1))
    print("The bot is ready!")

async def my_background_task():
    await client.wait_until_ready()
    while True:
        await client.purge_from(client.get_channel(channelweb), limit=10, check=None, before=None, after=None, around=None)
        client.send_message(await client.send_message(client.get_channel(channelweb),"!nbj"))
        await asyncio.sleep(20)
client.loop.create_task(my_background_task())


client.run(os.getenv('TOKEN'))
