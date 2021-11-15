import discord
from discord.enums import Status 
from discord.ext import commands
import os
import json

with open('settings.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

client = commands.Bot(command_prefix='>')

@client.event 
async def on_ready(): 
    await client.change_presence(status = discord.Status.online, activity = discord.Activity(type = 2, name = "Music Bot")) 
    print("Ready!")
    
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Load {extension} !')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unload {extension} !')

@client.command()
async def reload(ctx, extension): 
    client.reload_extension(f'cogs.{extension}')
    await ctx.send(f'Reload {extension} !')

for filename in os.listdir('./cogs'): 
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(jdata['TOKEN']) #Go to settings.json set your Discord bot token