import discord
import client
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands

client = Bot(description="ZeroFaith Official Bot", command_prefix="&", pm_help = False)

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+'')
	print('--------')
	print('--------')
	print('Started <Zero Faith>')
	return await client.change_presence(game=discord.Game(name='<Owned by Tanish>')) 

@client.command()
async def ping(*args):
	await client.say("Under Development")

client.run(os.getenv('Token'))
