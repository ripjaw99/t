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

class Stock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    @commands.command(aliases=['stock'])
    async def stocks(self, ctx, hair):
        try: 
            r=requests.get(f"https://finance.yahoo.com/quote/{hair}?p={hair}&.tsrc=fin-srch")
            soup=bs4.BeautifulSoup(r.text,"html.parser")
            dataname = soup.find("h1", {"data-reactid":"7"}).text
            data = soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
            data2 = soup.find("span", {"data-reactid":"51"}).text
            data3 = soup.find("span", {"data-reactid":"139"}).text 
            embed = discord.Embed(colour=discord.Colour.blue())
            embed.set_author(name=f'{dataname} Stock Info')
            embed.add_field(name = "Stock Price Per Share:", value=data, inline=False)
            embed.add_field(name = "Stock Price Per Share Change:", value=data2, inline=False)
            embed.add_field(name = "Market Cap:", value=data3, inline=False)
            embed.add_field(name = "Link for more info:", value=f"[Click Here](https://finance.yahoo.com/quote/{hair}?p={hair}&.tsrc=fin-srch)", inline=False)
            embed.set_footer(text = "For more info type the command more with the stock code next to it.")
            await ctx.send(embed=embed)
        except AttributeError:
            await ctx.send("That is not a real ticker symbol(stock code), please include a **real** ticker symbol. For a list of ticker symbols, go to https://nopebots.tech/tickers.")


    @commands.command()
    async def more(self, ctx, eye):
        try:
            r=requests.get(f"https://finance.yahoo.com/quote/{eye}?p={eye}&.tsrc=fin-srch")
            soup=bs4.BeautifulSoup(r.text,"html.parser")        
            dataname1 = soup.find("h1", {"data-reactid":"7"}).text
            prevclose = soup.find("span", {"data-reactid":"98"}).text
            newopen = soup.find("span", {"data-reactid":"103"}).text
            bid = soup.find("span", {"data-reactid":"108"}).text
            dayrange = soup.find("td", {"data-reactid":"117"}).text
            volume = soup.find("span", {"data-reactid":"126"}).text
            avgvolume = soup.find("span", {"data-reactid":"131"}).text
            earndate1 = soup.find("span", {"data-reactid":"159"})
            if earndate1 == None:
                earndate1 = "N/A"
            else:
                earndate1 = soup.find("span", {"data-reactid":"159"}).text
            earndate2 = soup.find("span", {"data-reactid":"161"})
            if earndate2 == None:
                earndate2 = earndate1
            else:    
                earndate2 = soup.find("span", {"data-reactid":"161"}).text
            embed = discord.Embed(colour=discord.Colour.blue())
            embed.set_author(name=f'{dataname1} Stock Info')
            embed.add_field(name = "Previous Close:", value=prevclose, inline=False)
            embed.add_field(name = "Today's Open:", value=newopen, inline=False)
            embed.add_field(name = "Bid:", value=bid, inline=False)
            embed.add_field(name = "Volume:", value=volume, inline=False)
            embed.add_field(name = "Average Volume:", value=avgvolume, inline=False)
            embed.add_field(name = "Earnings Dates:", value=f'{earndate1} to {earndate2}', inline=False)
            embed.add_field(name = "Link for more info:", value=f"[Click Here](https://finance.yahoo.com/quote/{eye}?p={eye}&.tsrc=fin-srch)", inline=False)
            await ctx.send(embed=embed)
        except AttributeError:
            await ctx.send("That is not a real ticker symbol(stock code), please include a **real** ticker symbol. For a list of ticker symbols, go to https://nopebots.tech/tickers.")
    

def setup(bot):
    bot.add_cog(Stock(bot))
    

    
    
