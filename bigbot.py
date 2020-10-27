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
bot = commands.Bot(command_prefix='-',intents = intentss, case_insensitive=True)
bot.remove_command('help')
initial_extensions = ['cogs.extension'] 

@bot.event```
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="-help | Developed by nope#8182"))
    print('Bot is up and running, logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    bot.load_extension('cogs.moderation')
    print('Succesfully loaded moderation cog.')
    bot.load_extension('cogs.stock')
    print('Succesfully loaded stocks cog.')
    bot.load_extension('cogs.fun')
    print('Succesfully loaded fun cog.')
    print('All cogs have been loaded, bot is running.')


@bot.group(name='help', invoke_without_command=True)
async def help_cmd(ctx):
    await ctx.channel.send('Subcommands: Moderation, Fun, Stocks.')


@help_cmd.command(name='Moderation')
async def mod_sub(ctx):
    await ctx.channel.send('Yes.')





    
``
bot.run(TOKEN)
