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
import praw
import random
import aiohttp
import datetime
from datetime import date
from datetime import timedelta
import time
import string



reddit = praw.Reddit(client_id='w0Dhd8yns9ck3g',
                    client_secret ='JSlJMG8Adi_co3UslcTuHNYrka0',
                    username='Comfortable-Award650',
                    password='kris1213',
                    user_agent='prawtutv1')
memessubreddit = reddit.subreddit('memes')
memesall_subs =[]
memeshot = memessubreddit.hot(limit=500)
for submission in memeshot:
    memesall_subs.append(submission)
    
    
danksubreddit = reddit.subreddit('dankmemes')
dankall_subs = []
dankhot = danksubreddit.hot(limit=500)
for submission in dankhot:
    dankall_subs.append(submission)

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    
    
    
    
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: typing.Optional[discord.Member], *, reason = None):
        if reason == None:
            await ctx.send('Please include a reason for warning the member.')
            return
        
        else:
        
            def get_random_string(length):
            # Random string with the combination of lower and upper case
                letters = string.ascii_letters
                result_str = ''.join(random.choice(letters) for i in range(length))
                return result_str
            

            
            db = sqlite3.connect('warns.sqlite')
            cursor = db.cursor()
          
        
            
            
            sql = ("INSERT INTO warns(user_id, warn_reason, guild_id, case_id, case_date) VALUES(?,?,?,?,?)")
            val = (member.id, reason, ctx.guild.id, get_random_string(5), str(datetime.datetime.utcnow()))
            
            cursor.execute(sql, val)
            db.commit()
            cursor.close()
            db.close()
            await ctx.send(f"Warned {member.mention} for {reason}.")
            await member.send(f"You were warned in {ctx.guild.name} for {reason}.")

    
    
    @commands.command()
    async def search(self, ctx, member: typing.Optional[discord.Member]):
        db = sqlite3.connect('warns.sqlite')
        cursor = db.cursor()
        cursor.execute('SELECT case_id FROM warns where user_id = ? and guild_id = ?', (member.id, ctx.guild.id,))
        casenum = cursor.fetchall()
        embed = discord.Embed(colour = discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
        embed.set_author(name=f'Warn history for {member.mention}:')
        
        
        for case in casenum:
            cursor.execute('SELECT case_date FROM warns where user_id = ? and guild_id = ? and case_id = ?',(member.id, ctx.guild.id, case[0]))
            date = cursor.fetchone()
            cursor.execute('SELECT warn_reason FROM warns where user_id = ? and guild_id = ? and case_id = ? and case_date = ?', (member.id, ctx.guild.id, case[0], date[0]))
            result = cursor.fetchone()
            embed.add_field(name='Warn', value=f'**Reason:** {result[0]}\n **Case ID:** {case[0]}\n **Date:** {date[0]}', inline = False)
            
        await ctx.send(embed=embed)
        
    
 
    
    @commands.command()
    async def removewarn(self, ctx, case_id):
        db = sqlite3.connect('warns.sqlite')
        cursor = db.cursor()
        cursor.execute('DELETE FROM warns where case_id = ? and guild_id = ?', (case_id, ctx.guild.id,))
        db.commit()
        cursor.close()
        db.close()
        await ctx.send(f'Removed the warn from the user.')
            
 
            


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: typing.Optional[discord.Member], mute_time : typing.Optional[str]):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if role is None:
            role = await ctx.guild.create_role(name='Muted', permissions=discord.Permissions(send_messages=False))
            for channel in ctx.guild.channels:
                await channel.set_permissions(role, send_messages=False, add_reactions=False)
        if mute_time is None:
            await member.add_roles(role)
            await ctx.send(f'**Muted {member.mention}.**')
            return
        else:
            typetime = mute_time[-1]
            mute_time = int(mute_time[:-1])
            role = discord.utils.get(ctx.guild.roles, name="Muted")
            if not member and not mute_time and not typetime:
                await ctx.send("Who do you want me to mute?")
                return
            if typetime == "h" or typetime == "hours":
                mute_time1 = mute_time * 3600
                typetime = "hours"
            elif typetime == "m" or typetime == "minutes":
                mute_time1 = mute_time * 60
                typetime = "minutes"
            elif typetime == "w" or typetime == "weeks":
                mute_time1 = mute_time * 604800
                typetime = "weeks"
            elif typetime == "s" or typetime == "seconds":
                typetime = "seconds"
                mute_time1 = mute_time * 1
            await member.add_roles(role)
            await ctx.send(f'**Muted {member.mention} for {mute_time} {typetime}.**')
            await asyncio.sleep(mute_time1)
            if role in member.roles:
                await member.remove_roles(role)
                await ctx.send(f'**Unmuted {member.mention}.**')  
            else:
                return



    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: typing.Optional[discord.Member]):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if role not in member.roles:
            await ctx.send("**User is not muted.**")
        else:
            await member.remove_roles(role)
            await ctx.send(f'**Unmuted {member.mention}.**')
    


    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: typing.Optional[discord.Member], *, reason = None):
        guild = ctx.guild
        if member.top_role > guild.me.top_role:
            await ctx.send("I'm sorry, I don't have permission to kick this user.")
            return
        else:  
            if reason == None:
                await member.send("**You have been kicked from " + ctx.guild.name + ".**")
                await ctx.send("Kicked " + member.mention + ".")
            else:
                await member.send("**You have been kicked from " + ctx.guild.name + " for " + reason + ".**")
                await ctx.send("Kicked " + member.mention + " for " + reason + ".")
            await ctx.guild.kick(member, reason=reason)
   

    
    @commands.command(pass_context=True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: typing.Optional[discord.Member], *, reason = None):
        guild = ctx.guild
        if member.top_role > guild.me.top_role:
            await ctx.send("I'm sorry, I don't have permission to ban this user.")
            return
        else:  
            if reason == None:
                await member.send("**You have been banned from " + ctx.guild.name + ".**")
                await ctx.send("Banned " + member.mention + ".")
            else:
                await member.send("**You have been banned from " + ctx.guild.name + " for " + reason + ".**")
                await ctx.send("Banned " + member.mention + " for " + reason + ".")
            await ctx.guild.ban(member, reason=reason)


    @commands.command(pass_context=True)
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, id: int, *, reason = None):
        member = await bot.fetch_user(id)
        if reason == None:
            await ctx.send("Unbanned " + member.mention + ".")
        else:
            await ctx.send("Unbanned " + member.mention + " for "  + reason + ".")
        await ctx.guild.unban(member)


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def lock(self, ctx, lockedchannel: typing.Optional[discord.TextChannel], *, reason=None):
        guild = ctx.guild
        if lockedchannel == None:
            channel = ctx.channel
        else:
            channel = lockedchannel
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(
                read_messages=True,
                send_messages=False,
            ),
  
        }    
        
        await channel.edit(overwrites=overwrites)
        if reason == None:
            await ctx.send(f'Locked {channel.mention}.')
        else:
            await ctx.send(f'Locked {channel.mention} for {reason}.')
        

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unlock(self, ctx, lockedchannel: typing.Optional[discord.TextChannel], *, reason=None):
        guild = ctx.guild
        if lockedchannel == None:
            channel = ctx.channel
        else:
            channel = lockedchannel
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(
                read_messages=True,
                send_messages=True,
            ),
  
        }    
        
        await channel.edit(overwrites=overwrites)
        if reason == None:
            await ctx.send(f'Unlocked {channel.mention}.')
        else:
            await ctx.send(f'Unlocked {channel.mention} for {reason}.')
        

    # purge command
    @commands.command(name='purge')
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, amount=0):
        amount = int(amount)
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)
        
        
        
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def setchannel(self, ctx, channel:discord.TextChannel):
        db = sqlite3.connect('channelids.sqlite')
        cursor = db.cursor()
        cursor.execute(f'SELECT channel_id FROM channels WHERE guild_id = {ctx.guild.id}')
        result = cursor.fetchone()
        if result is None:
            sql = ("INSERT INTO channels(guild_id, channel_id) VALUES(?,?)")
            val = (ctx.guild.id, channel.id)
            await ctx.send(f'Channel has been set to {channel.mention}')
        elif result is not None:
            sql = ("UPDATE channels set channel_id = ? WHERE guild_id = ?")
            val = (channel.id, ctx.guild.id)
            await ctx.send(f'Channel has been updated to {channel.mention}')
        cursor.execute(sql,val)
        db.commit()
        cursor.close()
        db.close()
        
        
    @commands.Cog.listener()
    async def on_command(self, ctx):
        db = sqlite3.connect('channelids.sqlite')
        cursor = db.cursor()
        cursor.execute('SELECT channel_id FROM channels WHERE guild_id = ?', (ctx.guild.id,))
        result = cursor.fetchone()
        channel = self.bot.get_channel(id=int(result[0]))
        embed = discord.Embed(timestamp=datetime.datetime.utcnow())
        embed.set_author(name=f'{ctx.command.name} log')
        embed.add_field(name='Author:', value=ctx.author.mention)
        embed.set_footer(text='Command invoked at:')
        await channel.send(embed=embed)
    
    
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        db = sqlite3.connect('channelids.sqlite')
        cursor = db.cursor()
        cursor.execute(f'SELECT channel_id FROM channels WHERE guild_id = {message.guild.id}')
        result = cursor.fetchone()
        channel = self.bot.get_channel(id=int(result[0]))
        embed = discord.Embed()
        embed.set_author(name='Message Deleted')
        embed.add_field(name="Content:", value=message.content)
        embed.add_field(name="Author:", value=message.author)
        embed.add_field(name="Timestamp in UTC:", value=message.created_at)
        await channel.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        try:
            db = sqlite3.connect('channelids.sqlite')
            cursor = db.cursor()
            cursor.execute(f'SELECT channel_id FROM channels WHERE guild_id = {before.guild.id}')
            result = cursor.fetchone()
            channel = self.bot.get_channel(id=int(result[0]))
            embed = discord.Embed()
            embed.set_author(name='Message Edited')
            embed.add_field(name="Old Message:", value=before.content)
            embed.add_field(name="New Message:", value=after.content)
            embed.add_field(name="Author:", value=before.author)
            embed.add_field(name="Timestamp in UTC:", value=before.created_at)
            await channel.send(embed=embed)
        except TypeError:
            randomvariabletodonothing = 0
            

            
        
        
    @commands.command()
    async def meme(self, ctx):
        global memesall_subs
        memesrandom_sub = random.choice(memesall_subs)
        name = memesrandom_sub.title
        url = memesrandom_sub.url
        em = discord.Embed(colour=discord.Colour.blue())
        em.set_author(name=name)
        em.set_image(url=url)
        message = await ctx.send(embed=em)
        await message.add_reaction('\U0001f44d')
        await message.add_reaction('\U0001f44e')
        timeout_date = datetime.datetime.now() + timedelta(seconds=90)
        def check(reaction, user):
            return reaction.message == message
        while True:
            timeout = timeout_date - datetime.datetime.now()
            timeout = timeout.total_seconds()
            message = await ctx.fetch_message(message.id)
            member = ctx.guild.get_member(713979128969429012)
            thebot = ctx.guild.get_member(ctx.guild.me)
            thedumbass = ctx.guild.get_member(625026392853315584)
            reaction, user = await self.bot.wait_for('reaction_add', check=check, timeout=timeout)
            if user == member:
                if str(reaction.emoji) == '\U0001f44d':
                    memesrandom_sub.upvote()
                    await ctx.send(f'{user.mention}, I upvoted the post!')
                elif str(reaction.emoji) == '\U0001f44e':
                    memesrandom_sub.downvote()
                    await ctx.send(f'{user.mention}, I downvoted the post.')
                else:
                    ranovarhfsbfsadjm = 0
            elif user == thebot:
                bruh = 193918
            
            elif user == thedumbass:
                t_end = time.time() + 60 
                while time.time() < t_end:
                    await user.send("We are sorry, you don't have permission to use the bot anymore.")
                    await message.remove_reaction(reaction, user)
                    
            else:
                await ctx.send(f"{user.mention}, I'm sorry you cannot react as you are not the bot owner.")
                await message.remove_reaction(reaction, user)
           
                
            

        
        
    @commands.command()
    async def dankmeme(self, ctx):
        global dankall_subs
        dankrandom_sub = random.choice(dankall_subs)
        name = dankrandom_sub.title
        url = dankrandom_sub.url
        em = discord.Embed(colour=discord.Colour.blue())
        em.set_author(name=name)
        em.set_image(url=url)
        message = await ctx.send(embed=em)
        await message.add_reaction('\U0001f44d')
        await message.add_reaction('\U0001f44e')
        timeout_date = datetime.datetime.now() + timedelta(seconds=90)
        def check(reaction, user):
            return reaction.message == message
        while True:
            timeout = timeout_date - datetime.datetime.now()
            timeout = timeout.total_seconds()
            message = await ctx.fetch_message(message.id)
            member = ctx.guild.get_member(713979128969429012)
            thebot = ctx.guild.get_member(ctx.guild.me)
            thedumbass = ctx.guild.get_member(625026392853315584)
            reaction, user = await self.bot.wait_for('reaction_add', check=check, timeout=timeout)
            if user == member:
                if str(reaction.emoji) == '\U0001f44d':
                    dankrandom_sub.upvote()
                    await ctx.send(f'{user.mention}, I upvoted the post!')
                elif str(reaction.emoji) == '\U0001f44e':
                    dankrandom_sub.downvote()
                    await ctx.send(f'{user.mention}, I downvoted the post.')
                else:
                    ranovarhfsbfsadjm = 0
            elif user == thebot:
                bruh = 193918
            
            elif user == thedumbass:
                t_end = time.time() + 60 
                while time.time() < t_end:
                    await user.send("We are sorry, you don't have permission to use the bot anymore.")
                    await message.remove_reaction(reaction, user)
                    
            else:
                await ctx.send(f"{user.mention}, I'm sorry you cannot react as you are not the bot owner.")
                await message.remove_reaction(reaction, user)
        
   
                    

def setup(bot):
    bot.add_cog(Moderation(bot))


    




