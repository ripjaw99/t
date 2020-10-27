import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get
from discord import Intents
import os
import json
import asyncio
import typing
import bs4
import requests
import traceback
import sys
from bs4 import BeautifulSoup
import sqlite3
TOKEN = 'NzE5NzI3NjIyNzgyODQ1MDMx.Xv1DgQ.mlAW3cOZSCqOFiSgkXx1ALQeEQc'
intentss = Intents.all()
bot = commands.Bot(command_prefix='-',intents = intentss, case_insensitive=True, activity=discord.Game(name="-help | Developed by nope#8182"))
bot.remove_command('help')
initial_extensions = ['cogs.moderation',
                      'cogs.stock'
                      ]


if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)
    print('All cogs have been loaded!')

@bot.event
async def on_ready():
    print('Bot is up and running, logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    for guild in bot.guilds:
        print(guild)
   


@bot.group(name='help', invoke_without_command=True)
async def help_cmd(ctx):
    embed = discord.Embed(colour=discord.Colour.blue())
    embed.set_author(name='BigBot Help')
    embed.add_field(name='Moderation:', value='Type -help moderation to find all moderation commands.')
    embed.add_field(name='Fun', value='Type -help fun to find all fun commands.')
    embed.add_field(name='Stocks', value='Type -help stocks to find all the stocks commands.')
    await ctx.channel.send(embed=embed)


@help_cmd.command(name='moderation')
async def mod_sub(ctx):
    embed = discord.Embed(colour=discord.Colour.blue())
    embed.set_author(name='Moderation Help')
    embed.add_field(name='Warn', value='Warns the specified user.')
    embed.add_field(name='Ban', value='Bans the specified user.')
    embed.add_field(name='Kick', value='Kicks the specified user.')
    embed.add_field(name='Mute', value='Mutes the specified user for the specified time or until the unmute command is ran.')
    embed.add_field(name='Unmute', value='Unmutes the specified user.')
    embed.add_field(name='Purge', value='Purges or deletes the specified amount of messages from the channel.')
    embed.add_field(name='Lock', value='Locks the channel for a specified amount of time, or until the unlock command is run.')
    embed.add_field(name='Unlock', value='Unlocks the channel.')
    embed.add_field(name='Setchannel', value='Sets the message edit/delete log channel.')
    await ctx.send(embed=embed)
    



@help_cmd.command(name='fun')
async def fun_sub(ctx):
    await ctx.channel.send('No.')
    
    

@help_cmd.command(name='Stocks', alias='stock')
async def stock_sub(ctx):
    await ctx.channel.send('Maybe.')





    

bot.run(TOKEN)
