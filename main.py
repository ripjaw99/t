import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get
import os
import json
import asyncio
import typing
from discord import Intents
import random
import datetime
from datetime import date
from datetime import timedelta



 

# ------------------------------Helpful Variables!-----------------------------------------

bot_prefix = '+'


# ------------------BOT TOKEN------------------------------------
BOT_TOKEN = 'NzYyNTQ1MTA3MDIyOTA1MzQ0.X3qteA.Jc_vV7KGBZyR8jrUGmnxDh1qkMg'
intentss = Intents.all()
bot = commands.Bot(command_prefix=bot_prefix, intents = intentss)
bot.remove_command('help')


# ------------------BOT STATUS (RICH PRESENCE)------------------------------------
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="+help | Developed by ENORMOUZ#0753 and nope#8182"))
    #embed = discord.Embed(colour=discord.Colour.blue())
    #embed.set_author(name='Reaction Roles')
    #embed.add_field(name='To get the role:', value='<@&740632024779456593>, react with: \U0001f4b0', inline=False)
    #embed.add_field(name='To get the role:', value='<@&740695007773851728>, react with: \U0001f399', inline=False)
    #embed.add_field(name='To get the role:', value='<@&743774087188316181>, react with: \U0001f3ce', inline=False)
    #embed.add_field(name='To get the role:', value='<@&759396531383173130>, react with: \U0001f4ca', inline=False)
    #embed.add_field(name='To get the role:', value='<@&759396483157327912>, react with: \U0001f5e8', inline=False)
    #channel = bot.get_channel(740631594049601709)
    #message = await channel.send(embed=embed)
    #await message.add_reaction('\U0001f4b0')
    #await message.add_reaction('\U0001f399')
    #await message.add_reaction('\U0001f3ce')
    #await message.add_reaction('\U0001f4ca')
    #await message.add_reaction('\U0001f5e8')


@bot.event
async def on_raw_reaction_add(payload):
    guild = bot.get_guild(payload.guild_id)
    giveping = guild.get_role(740632024779456593)
    announceping = guild.get_role(740695007773851728)
    eventping = guild.get_role(743774087188316181)
    pollping = guild.get_role(759396531383173130)
    deadping = guild.get_role(759396483157327912)
    
    member = guild.get_member(payload.user_id)
    print(member)
    if payload.message_id == 770005071743418408:
        if str(payload.emoji) == '\U0001f4b0': #givewayping
            await member.add_roles(giveping)
            await member.send('You have successfully been given the Giveaway Ping Role.')
        elif str(payload.emoji) == '\U0001f399': #announceping
            await member.add_roles(announceping)
            await member.send('You have successfully been given the Announcement Ping Role.')
        elif str(payload.emoji) == '\U0001f3ce': #event ping
            await member.add_roles(eventping)
            await member.send('You have successfully been given the Event Ping Role.')
        elif str(payload.emoji) == '\U0001f4ca': #pollping
            await member.add_roles(pollping)
            await member.send('You have successfully been given the Poll Ping Role.')
        elif str(payload.emoji) == '\U0001f5e8': #deadchat ping
            await member.add_roles(deadping)
            await member.send('You have successfully been givent the Dead Chat Ping Role.')
        else: 
            return
    else:
        return


@bot.event
async def on_raw_reaction_remove(payload):
    guild = bot.get_guild(payload.guild_id)
    giveping = guild.get_role(740632024779456593)
    announceping = guild.get_role(740695007773851728)
    eventping = guild.get_role(743774087188316181)
    pollping = guild.get_role(759396531383173130)
    deadping = guild.get_role(759396483157327912)
    
    member = guild.get_member(payload.user_id)
    if payload.message_id == 770005071743418408:
        if str(payload.emoji) == '\U0001f4b0': #givewayping
            await member.remove_roles(giveping)
            await member.send('You have successfully removed the Giveaway Ping Role.')
        elif str(payload.emoji) == '\U0001f399': #announceping
            await member.remove_roles(announceping)
            await member.send('You have successfully removed the Announcement Ping Role.')
        elif str(payload.emoji) == '\U0001f3ce': #event ping
            await member.remove_roles(eventping)
            await member.send('You have successfully removed the Event Ping Role.')
        elif str(payload.emoji) == '\U0001f4ca': #pollping
            await member.remove_roles(pollping)
            await member.send('You have successfully removed the Poll Ping Role.')
        elif str(payload.emoji) == '\U0001f5e8': #deadchat ping
            await member.remove_roles(deadping)
            await member.send('You have successfully removed the Dead Chat Ping Role.')
        else: 
            return
    else:
        return



    




# --------------------NORMAL COMMANDS------------------------------------

@bot.command()
async def help(ctx):
    embed = discord.Embed(colour=discord.Colour.green())
    thumb = discord.File("/home/pi/Downloads/BOT.png", filename="BOT.png")
    embed.set_thumbnail(url="attachment://BOT.png")
    embed.set_author(name='List of commands available')
    embed.add_field(name='help:', value='Shows this command', inline=False)
    embed.add_field(name='ticket_ad:', value='Opens an ad ticket.', inline=False)
    embed.add_field(name='ticket_donator:', value='Opens a donator ticket.', inline=False)
    embed.add_field(name='close:', value='Closes the current ticket, only able to be ran in a ticket channel.', inline=False)
    embed.add_field(name='credits:', value ="Shows the bot's creators.", inline=False)
    await ctx.send(embed=embed, file=thumb)

# credits command
@bot.command(name='credits', aliases=['credit'])
async def credits(ctx):
    embed = discord.Embed(colour=discord.Colour.orange())
    embed.set_author(name='Credits!')
    embed.add_field(name='Head Developer', value='nope#8182', inline=False)
    embed.add_field(name='Developer', value='ENORMOUZ#0753', inline=False)

    await ctx.send(embed=embed)

# purge command
@bot.command(name='purge')
@commands.has_permissions(kick_members=True, administrator=True)
async def purge(ctx, amount=0):
    amount = int(amount)
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)

# ticket ads command
@bot.command()
async def ticket_ad(ctx):
    guild = ctx.guild
    roleadd = guild.get_role(769217977995624548)
    await ctx.author.add_roles(roleadd)
    id = 756212977752866917
    category = discord.utils.get(ctx.guild.categories, id=id)
    message_content = "Which plan do you want to buy? Please send (+plus; +premium; +vip; +god; +ultra)"
    guild = ctx.message.guild
    with open("data.json") as f:
        data = json.load(f)

    ticket_number = int(data["ticket-counter"])
    ticket_number += 1
    await ctx.message.delete()  # this code will delete the message the user sends! ( works for any command )
    ticket_channel = await guild.create_text_channel('ad_ticket-{}'.format(ticket_number), category=category)
    await ticket_channel.set_permissions(ctx.guild.get_role(ctx.guild.id), send_messages=False, read_messages=False)

    for role_id in data["valid-roles"]:
        role = ctx.guild.get_role(role_id)

        await ticket_channel.set_permissions(role, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)

    await ticket_channel.set_permissions(ctx.author, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)

    em = discord.Embed(title="New ticket from {}#{}".format(ctx.author.name, ctx.author.discriminator), description= "{}".format(message_content), color=0x00a8ff)

    await ticket_channel.send(embed=em)

    data["ticket-channel-ids"].append(ticket_channel.id)

    data["ticket-counter"] = int(ticket_number)
    with open("data.json", 'w') as f:
        json.dump(data, f)

# ticket donator command
@bot.command()
async def ticket_donator(ctx):
    name = 755398023315587172
    category = discord.utils.get(ctx.guild.categories, id=name)
    message_content = "Which type of donator do you want to buy?Answer with (+donator_1; +donator_2; +donator_3; +donator_custom; +donator_monthly)"
    guild = ctx.message.guild
    with open("data.json") as f:
        data = json.load(f)

    ticket_number = int(data["ticket-counter"])
    ticket_number += 1
    await ctx.message.delete()  # this code will delete the message the user sends! ( works for any command )
    ticket_channel = await guild.create_text_channel('donator_ticket-{}'.format(ticket_number), category=category)
    await ticket_channel.set_permissions(ctx.guild.get_role(ctx.guild.id), send_messages=False, read_messages=False)
    await ctx.send(f'I have created a channel, #{ticket_channel}.')
    for role_id in data["valid-roles"]:
        role = ctx.guild.get_role(role_id)

        await ticket_channel.set_permissions(role, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)

    await ticket_channel.set_permissions(ctx.author, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)

    em = discord.Embed(title="New ticket from {}#{}".format(ctx.author.name, ctx.author.discriminator), description= "{}".format(message_content), color=0x00a8ff)

    await ticket_channel.send(embed=em)

    data["ticket-channel-ids"].append(ticket_channel.id)

    data["ticket-counter"] = int(ticket_number)
    with open("data.json", 'w') as f:
        json.dump(data, f)

# ticket close command
@bot.command(name='close')
async def close(ctx):
    guild = ctx.guild
    with open('data.json') as f:
        data = json.load(f)

    if ctx.channel.id in data["ticket-channel-ids"]:

        channel_id = ctx.channel.id

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "close"

        try:

            em = discord.Embed(title="Skyblock Life", description="Are you sure you want to close this ticket? Reply with `close` if you are sure.", color=0x00a8ff)

            await ctx.send(embed=em)
            await bot.wait_for('message', check=check, timeout=60)
            await  ctx.channel.delete()
            role = guild.get_role(769217977995624548)
            await ctx.author.remove_roles(role)

            index = data["ticket-channel-ids"].index(channel_id)
            del data["ticket-channel-ids"][index]

            with open('data.json', 'w') as f:
                json.dump(data, f)

        except asyncio.TimeoutError:
            em = discord.Embed(title="Skyblock Life", description="You have run out of time to close this ticket. Please run the command again.", color=0x00a8ff)
            await ctx.send(embed=em)

# wood plan command
@bot.command(name='plus')  # command's name and aliases
async def plus(ctx, *arg):
    guild = ctx.guild
    with open('data.json') as f:
        data = json.load(f)

    if ctx.channel.id in data["ticket-channel-ids"]:

        channel_id = ctx.channel.id

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "yes"
        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(name='Plan Selected: Plus Plan')
        # Normal Commands
        embed.add_field(name='SB LIFE ADVERTISEMENT DISCLAIMER', value='For the safety of <@476840904133705751> there are no refunds after a message posted with an @everyone or @here.\nWe do not guarantee any amount of joins because we are not bots where we can make a specific amount of joins.\n\nAnswer with **yes** to this message to confirm you’ve read this disclaimer', inline=True)
        await ctx.send(embed=embed)
        await bot.wait_for('message', check=check, timeout=500)
        await ctx.send('You have agreed to the disclaimer. To continue with the purchase please go to https://paypal.me/maxiamstart and pay the required amount. Please reply with "yes" if you have payed.')
        await bot.wait_for('message', check=check)
        await ctx.send('<@476840904133705751> has the payment been made?')
        def check(message):
            return message.author.id == 476840904133705751 or message.author.id == 713979128969429012 and message.channel == ctx.channel and message.content.lower() == "yes"
        await bot.wait_for('message', check=check)
        await ctx.send('For the giveaway to work, you must invite this bot to your server. https://discord.com/api/oauth2/authorize?client_id=762545107022905344&permissions=1024&scope=bot. Please reply "done" when you have added the bot to your server.')
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "done"
        await bot.wait_for('message', check=check)
        await ctx.send('Please post a permanent invite to your server.')
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        shat = await bot.wait_for('message', check=check)
        await ctx.send('What is the name of your server?')
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        servername = await bot.wait_for('message', check=check)
        await ctx.send('Please post the server description.')
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        serverdescriptor = await bot.wait_for('message', check=check)
        channel = bot.get_channel(754586850542354483)
        embed = discord.Embed(colour=discord.Colour.blue())
        embed.set_author(name='New Giveaway')
        embed.add_field(name='Server:', value=servername.content)
        embed.add_field(name='Description:', value=serverdescriptor.content,inline=False)
        givemessage = await channel.send(embed=embed)
        advchannel = bot.get_channel(755196243810189442)
        em = discord.Embed(colour=discord.Colour.blue())
        em.set_author(name=servername.content)
        em.add_field(name='Description', value=serverdescriptor.content)
        em.add_field(name='Invite', value=shat.content)
        await advchannel.send(embed=em)
        await advchannel.send(shat.content)
        await channel.send(shat.content)
        await givemessage.add_reaction('\U0001f389')
        list = []
        timeout_date = datetime.datetime.now() + timedelta(days=3)
        while True:
            invite = await bot.fetch_invite(shat.content)
            guildid = invite.guild.id
            timeout = timeout_date - datetime.datetime.now()
            timeout = timeout.total_seconds()
            givemessage = await channel.fetch_message(givemessage.id)
            guild = ctx.guild
            guildnew = bot.get_guild(guildid)
            messaged = set()
            nitrorole = guild.get_role(747088018632081464)
            def check(reaction, user):
                return reaction.message == givemessage and user not in messaged
            try:    
                reaction, user = await bot.wait_for('reaction_add', check=check, timeout=timeout)
                if guildnew.get_member(user.id):
                    await user.send('You have successfully registered for the giveaway.')
                elif nitrorole in user.roles:
                    await user.send('You have successfully registered and bypassed requirements for this giveaway')
                else:
                    await user.send("You're not in the server, please join and react again.")
                    member = guild.get_member(user.id)
                    await givemessage.remove_reaction(reaction, member)
            except asyncio.TimeoutError:
                users = await reaction.users().flatten()
                users.remove(guild.me)
                winner = random.choice(users)
                print(users)
                await channel.send(f'Congratulations, {winner.mention}, you have won.')
                return


        


# premium plan command
@bot.command(name='premium')  # command's name and aliases
async def premium(ctx, *arg):
    guild = ctx.guild
    with open('data.json') as f:
        data = json.load(f)

    if ctx.channel.id in data["ticket-channel-ids"]:

        channel_id = ctx.channel.id

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "yes"
        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(name='Plan Selected: Premium Plan')
        # Normal Commands
        embed.add_field(name='SB LIFE ADVERTISEMENT DISCLAIMER', value='For the safety of <@476840904133705751> there are no refunds after a message posted with an @everyone or @here.\nWe do not guarantee any amount of joins because we are not bots where we can make a specific amount of joins.\n\nAnswer with **yes** to this message to confirm you’ve read this disclaimer', inline=True)
        await ctx.send(embed=embed)
        await bot.wait_for('message', check=check, timeout=500)
        await ctx.send('You have agreed to the disclaimer. To continue with the purchase please go to https://paypal.me/maxiamstart and pay the required amount. Please reply with "yes" if you have payed.')
        await bot.wait_for('message', check=check)
        await ctx.send('<@476840904133705751> has the payment been made?')
        def check(message):
            return message.author.id == 476840904133705751 or message.author.id == 713979128969429012 and message.channel == ctx.channel and message.content.lower() == "yes"
        await bot.wait_for('message', check=check)
        await ctx.send('For the giveaway to work, you must invite this bot to your server. https://discord.com/api/oauth2/authorize?client_id=762545107022905344&permissions=1024&scope=bot. Please reply "done" when you have added the bot to your server.')
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "done"
        await bot.wait_for('message', check=check)
        await ctx.send('Please post a permanent invite to your server.')
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        shat = await bot.wait_for('message', check=check)
        await ctx.send('What is the name of your server?')
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        servername = await bot.wait_for('message', check=check)
        await ctx.send('Please post the server description.')
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        serverdescriptor = await bot.wait_for('message', check=check)
        channel = bot.get_channel(754586850542354483)
        embed = discord.Embed(colour=discord.Colour.blue())
        embed.set_author(name='New Giveaway')
        embed.add_field(name='Server:', value=servername.content)
        embed.add_field(name='Description:', value=serverdescriptor.content,inline=False)
        givemessage = await channel.send(embed=embed)
        advchannel = bot.get_channel(755196243810189442)
        em = discord.Embed(colour=discord.Colour.blue())
        em.set_author(name=servername.content)
        em.add_field(name='Description', value=serverdescriptor.content)
        em.add_field(name='Invite', value=shat.content)
        await advchannel.send(embed=em)
        await advchannel.send(shat.content)
        await channel.send(shat.content)
        await givemessage.add_reaction('\U0001f389')
        list = []
        timeout_date = datetime.datetime.now() + timedelta(days=5)
        while True:
            invite = await bot.fetch_invite(shat.content)
            guildid = invite.guild.id
            timeout = timeout_date - datetime.datetime.now()
            timeout = timeout.total_seconds()
            givemessage = await channel.fetch_message(givemessage.id)
            guild = ctx.guild
            guildnew = bot.get_guild(guildid)
            messaged = set()
            nitrorole = guild.get_role(747088018632081464)
            def check(reaction, user):
                return reaction.message == givemessage and user not in messaged
            try:    
                reaction, user = await bot.wait_for('reaction_add', check=check, timeout=timeout)
                if guildnew.get_member(user.id):
                    await user.send('You have successfully registered for the giveaway.')
                elif nitrorole in user.roles:
                    await user.send('You have successfully registered and bypassed requirements for this giveaway')
                else:
                    await user.send("You're not in the server, please join and react again.")
                    member = guild.get_member(user.id)
                    await givemessage.remove_reaction(reaction, member)
            except asyncio.TimeoutError:
                users = await reaction.users().flatten()
                users.remove(guild.me)
                winner = random.choice(users)
                print(users)
                await channel.send(f'Congratulations, {winner.mention}, you have won.')
                return

# iron plan command
@bot.command(name='vip')  # command's name and aliases
async def vip(ctx, *arg):
    guild = ctx.guild
    with open('data.json') as f:
        data = json.load(f)

    if ctx.channel.id in data["ticket-channel-ids"]:

        channel_id = ctx.channel.id

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "yes"
        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(name='Plan Selected: VIP Plan')
        # Normal Commands
        embed.add_field(name='SB LIFE ADVERTISEMENT DISCLAIMER', value='For the safety of <@476840904133705751> there are no refunds after a message posted with an @everyone or @here.\nWe do not guarantee any amount of joins because we are not bots where we can make a specific amount of joins.\n\nAnswer with **yes** to this message to confirm you’ve read this disclaimer', inline=True)
        await ctx.send(embed=embed)
        await bot.wait_for('message', check=check, timeout=500)
        await ctx.send('You have agreed to the disclaimer. To continue with the purchase please go to https://paypal.me/maxiamstart and pay the required amount. Please reply with "yes" if you have payed.')
        await bot.wait_for('message', check=check)
        await ctx.send('<@476840904133705751> has the payment been made?')
        def check(message):
            return message.author.id == 476840904133705751 or message.author.id == 713979128969429012 and message.channel == ctx.channel and message.content.lower() == "yes"
        await bot.wait_for('message', check=check)
        await ctx.send('For the giveaway to work, you must invite this bot to your server. https://discord.com/api/oauth2/authorize?client_id=762545107022905344&permissions=1024&scope=bot. Please reply "done" when you have added the bot to your server.')
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "done"
        await bot.wait_for('message', check=check)
        await ctx.send('Please post a permanent invite to your server.')
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        shat = await bot.wait_for('message', check=check)
        await ctx.send('What is the name of your server?')
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        servername = await bot.wait_for('message', check=check)
        await ctx.send('Please post the server description.')
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        serverdescriptor = await bot.wait_for('message', check=check)
        id = 759538526298570802
        category = discord.utils.get(ctx.guild.categories, id = id)
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=True, send_messages=False, add_reactions=False)
        }
        channel = await category.create_text_channel(f'{servername.content} giveaway', overwrites=overwrites)
        embed = discord.Embed(colour=discord.Colour.blue())
        embed.set_author(name='New Giveaway')
        embed.add_field(name='Server:', value=servername.content)
        embed.add_field(name='Description:', value=serverdescriptor.content,inline=False)
        givemessage = await channel.send(embed=embed)
        await channel.send(shat.content)
        await givemessage.add_reaction('\U0001f389')
        advchannel = bot.get_channel(755196243810189442)
        em = discord.Embed(colour=discord.Colour.blue())
        em.set_author(name=servername.content)
        em.add_field(name='Description', value=serverdescriptor.content)
        em.add_field(name='Invite', value=shat.content)
        await advchannel.send(embed=em)
        await advchannel.send(shat.content)
        list = []
        timeout_date = datetime.datetime.now() + timedelta(days=7)
        while True:
            invite = await bot.fetch_invite(shat.content)
            guildid = invite.guild.id
            timeout = timeout_date - datetime.datetime.now()
            timeout = timeout.total_seconds()
            givemessage = await channel.fetch_message(givemessage.id)
            guild = ctx.guild
            guildnew = bot.get_guild(guildid)
            messaged = set()
            nitrorole = guild.get_role(747088018632081464)
            def check(reaction, user):
                return reaction.message == givemessage and user not in messaged
            try:    
                reaction, user = await bot.wait_for('reaction_add', check=check, timeout=timeout)
                if guildnew.get_member(user.id):
                    await user.send('You have successfully registered for the giveaway.')
                elif nitrorole in user.roles:
                    await user.send('You have successfully registered and bypassed requirements for this giveaway')
                else:
                    await user.send("You're not in the server, please join and react again.")
                    member = guild.get_member(user.id)
                    await givemessage.remove_reaction(reaction, member)
            except asyncio.TimeoutError:
                users = await reaction.users().flatten()
                users.remove(guild.me)
                winner = random.choice(users)
                print(users)
                await channel.send(f'Congratulations, {winner.mention}, you have won.')
                return

# gold plan command
@bot.command(name='god')  # command's name and aliases
async def god(ctx, *arg):
    guild = ctx.guild
    with open('data.json') as f:
        data = json.load(f)

    if ctx.channel.id in data["ticket-channel-ids"]:

        channel_id = ctx.channel.id

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "yes"
        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(name='Plan Selected: God Plan')
        # Normal Commands
        embed.add_field(name='SB LIFE ADVERTISEMENT DISCLAIMER', value='For the safety of <@476840904133705751> there are no refunds after a message posted with an @everyone or @here.\nWe do not guarantee any amount of joins because we are not bots where we can make a specific amount of joins.\n\nAnswer with **yes** to this message to confirm you’ve read this disclaimer', inline=True)
        await ctx.send(embed=embed)
        await bot.wait_for('message', check=check, timeout=500)
        await ctx.send('You have agreed to the disclaimer. To continue with the purchase please go to https://paypal.me/maxiamstart and pay the required amount. Please reply with "yes" if you have payed.')
        await bot.wait_for('message', check=check)
        await ctx.send('<@476840904133705751> has the payment been made?')
        def check(message):
            return message.author.id == 476840904133705751 or message.author.id == 713979128969429012 and message.channel == ctx.channel and message.content.lower() == "yes"
        await bot.wait_for('message', check=check)
        await ctx.send('For the giveaway to work, you must invite this bot to your server. https://discord.com/api/oauth2/authorize?client_id=762545107022905344&permissions=1024&scope=bot. Please reply "done" when you have added the bot to your server.')
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "done"
        await bot.wait_for('message', check=check)
        await ctx.send('Please post a permanent invite to your server.')
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        shat = await bot.wait_for('message', check=check)
        await ctx.send('What is the name of your server?')
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        servername = await bot.wait_for('message', check=check)
        await ctx.send('Please post the server description.')
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        serverdescriptor = await bot.wait_for('message', check=check)
        id = 759538526298570802
        category = discord.utils.get(ctx.guild.categories, id = id)
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=True, send_messages=False, add_reactions=False)
        }
        channel = await category.create_text_channel(f'{servername.content} giveaway', overwrites=overwrites)
        embed = discord.Embed(colour=discord.Colour.blue())
        embed.set_author(name='New Giveaway')
        embed.add_field(name='Server:', value=servername.content)
        embed.add_field(name='Description:', value=serverdescriptor.content,inline=False)
        givemessage = await channel.send(embed=embed)
        await channel.send(shat.content)
        advchannel = bot.get_channel(755196243810189442)
        em = discord.Embed(colour=discord.Colour.blue())
        em.set_author(name=servername.content)
        em.add_field(name='Description', value=serverdescriptor.content)
        em.add_field(name='Invite', value=shat.content)
        await advchannel.send(embed=em)
        await advchannel.send(shat.content)
        await givemessage.add_reaction('\U0001f389')
        list = []
        timeout_date = datetime.datetime.now() + timedelta(days=10)
        while True:
            invite = await bot.fetch_invite(shat.content)
            guildid = invite.guild.id
            timeout = timeout_date - datetime.datetime.now()
            timeout = timeout.total_seconds()
            givemessage = await channel.fetch_message(givemessage.id)
            guild = ctx.guild
            guildnew = bot.get_guild(guildid)
            messaged = set()
            nitrorole = guild.get_role(747088018632081464)
            def check(reaction, user):
                return reaction.message == givemessage and user not in messaged
            try:    
                reaction, user = await bot.wait_for('reaction_add', check=check, timeout=timeout)
                if guildnew.get_member(user.id):
                    await user.send('You have successfully registered for the giveaway.')
                elif nitrorole in user.roles:
                    await user.send('You have successfully registered and bypassed requirements for this giveaway')
                else:
                    await user.send("You're not in the server, please join and react again.")
                    member = guild.get_member(user.id)
                    await givemessage.remove_reaction(reaction, member)
            except asyncio.TimeoutError:
                users = await reaction.users().flatten()
                users.remove(guild.me)
                winner = random.choice(users)
                print(users)
                await channel.send(f'Congratulations, {winner.mention}, you have won.')
                return
            
                

                
# diamond plan command
@bot.command(name='ultra')  # command's name and aliases
async def ultra(ctx, *arg):
    guild = ctx.guild
    with open('data.json') as f:
        data = json.load(f)

    if ctx.channel.id in data["ticket-channel-ids"]:

        channel_id = ctx.channel.id

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "yes"
        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(name='Plan Selected: Ultra Plan')
        # Normal Commands
        embed.add_field(name='SB LIFE ADVERTISEMENT DISCLAIMER', value='For the safety of <@476840904133705751> there are no refunds after a message posted with an @everyone or @here.\nWe do not guarantee any amount of joins because we are not bots where we can make a specific amount of joins.\n\nAnswer with **yes** to this message to confirm you’ve read this disclaimer', inline=True)
        await ctx.send(embed=embed)
        await bot.wait_for('message', check=check, timeout=500)
        await ctx.send('You have agreed to the disclaimer. To continue with the purchase please go to https://paypal.me/maxiamstart and pay the required amount. Please reply with "yes" if you have payed.')
        await bot.wait_for('message', check=check)
        await ctx.send('<@476840904133705751> has the payment been made?')
        def check(message):
            return message.author.id == 476840904133705751 or message.author.id == 713979128969429012 and message.channel == ctx.channel and message.content.lower() == "yes"
        await bot.wait_for('message', check=check)
        await ctx.send('For the giveaway to work, you must invite this bot to your server. https://discord.com/api/oauth2/authorize?client_id=762545107022905344&permissions=1024&scope=bot. Please reply "done" when you have added the bot to your server.')
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "done"
        await bot.wait_for('message', check=check)
        await ctx.send('Please post a permanent invite to your server.')
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        shat = await bot.wait_for('message', check=check)
        await ctx.send('What is the name of your server?')
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        servername = await bot.wait_for('message', check=check)
        await ctx.send('Please post the server description.')
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        serverdescriptor = await bot.wait_for('message', check=check)
        id = 759538526298570802
        category = discord.utils.get(ctx.guild.categories, id = id)
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=True, send_messages=False, add_reactions=False)
        }
        channel = await category.create_text_channel(f'{servername.content} giveaway', overwrites=overwrites)
        embed = discord.Embed(colour=discord.Colour.blue())
        embed.set_author(name='New Giveaway')
        embed.add_field(name='Server:', value=servername.content)
        embed.add_field(name='Description:', value=serverdescriptor.content,inline=False)
        await channel.send('@everyone')
        advchannel = bot.get_channel(755196243810189442)
        em = discord.Embed(colour=discord.Colour.blue())
        em.set_author(name=servername.content)
        em.add_field(name='Description', value=serverdescriptor.content)
        em.add_field(name='Invite', value=shat.content)
        await advchannel.send(embed=em)
        await advchannel.send(shat.content)
        givemessage = await channel.send(embed=embed)
        await channel.send(shat.content)
        await givemessage.add_reaction('\U0001f389')
        list = []
        timeout_date = datetime.datetime.now() + timedelta(days=14)
        while True:
            invite = await bot.fetch_invite(shat.content)
            guildid = invite.guild.id
            timeout = timeout_date - datetime.datetime.now()
            timeout = timeout.total_seconds()
            givemessage = await channel.fetch_message(givemessage.id)
            guild = ctx.guild
            guildnew = bot.get_guild(guildid)
            messaged = set()
            nitrorole = guild.get_role(747088018632081464)
            def check(reaction, user):
                return reaction.message == givemessage and user not in messaged
            try:    
                reaction, user = await bot.wait_for('reaction_add', check=check, timeout=timeout)
                if guildnew.get_member(user.id):
                    await user.send('You have successfully registered for the giveaway.')
                elif nitrorole in user.roles:
                    await user.send('You have successfully registered and bypassed requirements for this giveaway')
                else:
                    await user.send("You're not in the server, please join and react again.")
                    member = guild.get_member(user.id)
                    await givemessage.remove_reaction(reaction, member)
            except asyncio.TimeoutError:
                users = await reaction.users().flatten()
                users.remove(guild.me)
                winner = random.choice(users)
                print(users)
                await channel.send(f'Congratulations, {winner.mention}, you have won.')
                return

# donator 1 plan command
@bot.command(name='donator_1')  # command's name and aliases
async def donator_1(ctx, *arg):
    with open('data.json') as f:
        data = json.load(f)

    if ctx.channel.id in data["ticket-channel-ids"]:

        channel_id = ctx.channel.id

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "yes"
        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(name='Donator Rank Selected: Donator 1')
        # Normal Commands
        embed.add_field(name='SB LIFE DONATION DISCLAIMER', value='For the safety of <@713979128969429012> there are no refunds after a rank given in the server.\n\nTo pay, go to /ah msxi in Hypixel Skyblock and pay the amount you need for the rank.\n\nAnswer with **yes** to this msg to confirm you’ve read this disclaimer', inline=True)
        await ctx.send(embed=embed)
        await bot.wait_for('message', check=check, timeout=60)
        await ctx.send('You have agreed to the disclaimer. Your Donator **1** rank has been ordered. Waiting for <@713979128969429012> .\n\nPlease write your Minecraft IGN in here while waiting, so msxi can check if you paid.')

# donator 2 plan command
@bot.command(name='donator_2')  # command's name and aliases
async def donator_2(ctx, *arg):
    with open('data.json') as f:
        data = json.load(f)

    if ctx.channel.id in data["ticket-channel-ids"]:

        channel_id = ctx.channel.id

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "yes"
        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(name='Donator Rank Selected: Donator 2')
        # Normal Commands
        embed.add_field(name='SB LIFE DONATION DISCLAIMER', value='For the safety of <@713979128969429012> there are no refunds after a rank given in the server.\n\nTo pay, go to /ah msxi in Hypixel Skyblock and pay the amount you need for the rank.\n\nAnswer with **yes** to this msg to confirm you’ve read this disclaimer', inline=True)
        await ctx.send(embed=embed)
        await bot.wait_for('message', check=check, timeout=60)
        await ctx.send('You have agreed to the disclaimer. Your Donator **2** rank has been ordered. Waiting for <@713979128969429012> .\n\nPlease write your Minecraft IGN in here while waiting, so msxi can check if you paid.')

# donator 3 plan command
@bot.command(name='donator_3')  # command's name and aliases
async def donator_3(ctx, *arg):
    with open('data.json') as f:
        data = json.load(f)

    if ctx.channel.id in data["ticket-channel-ids"]:

        channel_id = ctx.channel.id

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "yes"
        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(name='Donator Rank Selected: Donator 3')
        # Normal Commands
        embed.add_field(name='SB LIFE DONATION DISCLAIMER', value='For the safety of <@713979128969429012> there are no refunds after a rank given in the server.\n\nTo pay, go to /ah msxi in Hypixel Skyblock and pay the amount you need for the rank.\n\nAnswer with **yes** to this msg to confirm you’ve read this disclaimer', inline=True)
        await ctx.send(embed=embed)
        await bot.wait_for('message', check=check, timeout=60)
        await ctx.send('You have agreed to the disclaimer. Your Donator **3** rank has been ordered. Waiting for <@713979128969429012> .\n\nPlease write your Minecraft IGN in here while waiting, so msxi can check if you paid.')

# donator custom plan command
@bot.command(name='donator_custom')  # command's name and aliases
async def donator_custom(ctx, *arg):
    with open('data.json') as f:
        data = json.load(f)

    if ctx.channel.id in data["ticket-channel-ids"]:

        channel_id = ctx.channel.id

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "yes"
        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(name='Donator Rank Selected: Donator Custom')
        # Normal Commands
        embed.add_field(name='SB LIFE DONATION DISCLAIMER', value='For the safety of <@713979128969429012> there are no refunds after a rank given in the server.\n\nTo pay, go to /ah msxi in Hypixel Skyblock and pay the amount you need for the rank.\n\nAnswer with **yes** to this msg to confirm you’ve read this disclaimer', inline=True)
        await ctx.send(embed=embed)
        await bot.wait_for('message', check=check, timeout=60)
        await ctx.send('You have agreed to the disclaimer. Your Donator **Custom** rank has been ordered. Waiting for <@713979128969429012> .\n\nPlease write your Minecraft IGN in here while waiting, so msxi can check if you paid.')

# donator monthly plan command
@bot.command(name='donator_monthly')  # command's name and aliases
async def donator_monthly(ctx, *arg):
    with open('data.json') as f:
        data = json.load(f)

    if ctx.channel.id in data["ticket-channel-ids"]:

        channel_id = ctx.channel.id

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "yes"
        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(name='Donator Rank Selected: Donator Monthly')
        # Normal Commands
        embed.add_field(name='SB LIFE DONATION DISCLAIMER', value='For the safety of <@713979128969429012> there are no refunds after a rank given in the server.\n\nTo pay, go to /ah msxi in Hypixel Skyblock and pay the amount you need for the rank.\n\nAnswer with **yes** to this msg to confirm you’ve read this disclaimer', inline=True)
        await ctx.send(embed=embed)
        await bot.wait_for('message', check=check, timeout=60)
        await ctx.send('You have agreed to the disclaimer. Your Donator **Monthly** rank has been ordered. Waiting for <@713979128969429012> .\n\nPlease write your Minecraft IGN in here while waiting, so msxi can check if you paid.')

import asyncio

#mute command 
@bot.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: typing.Optional[discord.Member], mute_time : typing.Optional[str]):
    typetime = mute_time[-1]
    mute_time = int(mute_time[:-1])
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member and not mute_time and not typetime:
        await ctx.send("Who do you want me to mute?")
        return
    if not mute_time and not typetime:
        await member.add_roles(role)
        await ctx.send(f'**Muted {member.mention}.**')
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
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    await ctx.send(f'**Muted {member.mention} for {mute_time} {typetime}.**')
    await asyncio.sleep(mute_time1)
    if role in member.roles:
        await member.remove_roles(role)
        await ctx.send(f'**Unmuted {member.mention}.**')
            
    else:
        return

    
#unmute command
@bot.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: typing.Optional[discord.Member]):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if role not in member.roles:
        await ctx.send("**User is not muted.**")
    else:
        await member.remove_roles(role)
        await ctx.send(f'**Unmuted {member.mention}.**')
        
@bot.event
async def on_member_join(member):
    channel = member.guild.get_channel(769299912759705640)
    await channel.send(f'Please welcome {member.mention} to SBL!')
    role = member.guild.get_role(748087697930846268)
    await member.add_roles(role)
    await member.send('Welcome to SBL, check out our rules, info and announcements channels to stay updated with the server!')
    
    


    
@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: typing.Optional[discord.Member], *, reason = None):
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
        await ctx.guild.ban(member)



@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: typing.Optional[discord.Member], *, reason = None):
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

@bot.command(pass_context=True, aliases=['Unban'])
@commands.has_permissions(ban_members=True)
async def unban(ctx, id: int, *, reason = None):
    member = await bot.fetch_user(id)
    if reason == None:
        await ctx.send("Unbanned " + member.mention + ".")
    else:
        await ctx.send("Unbanned " + member.mention + " for "  + reason + ".")
    await ctx.guild.unban(member, reason=reason)



@bot.command()
@commands.has_permissions(administrator=True)
async def lock(ctx, lockedchannel: typing.Optional[discord.TextChannel], *, reason=None):
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
        


@bot.command()
@commands.has_permissions(administrator=True)
async def unlock(ctx, lockedchannel: typing.Optional[discord.TextChannel], *, reason=None):
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

@bot.command()
async def suggest(ctx, *, suggestion):
    channel = bot.get_channel(753986501825659043)
    guild = ctx.guild
    embed = discord.Embed(colour=discord.Colour.blue())
    embed.set_author(name=f'New Suggestion by {ctx.author}.')
    embed.add_field(name='Sugggestion:',value=suggestion)
    message = await channel.send(embed=embed)
    await ctx.send('Thanks for the suggestion!')
    await message.add_reaction('\U0001f44d')
    await message.add_reaction('\U0001f44e')
    

@bot.command()
async def report(ctx, *, report):
    channel = bot.get_channel(763870119205535765)
    guild = ctx.guild
    embed = discord.Embed(colour=discord.Colour.blue())
    embed.set_author(name=f'New Suggestion by {ctx.author}.')
    embed.add_field(name='Sugggestion:',value=suggestion)
    message = await channel.send(embed=embed)
    await ctx.send('Thanks for the suggestion!')
    await message.add_reaction('\U00002705')
    await message.add_reaction('\U0000274c')
  

        






@bot.command()
@commands.has_permissions(administrator=True)
async def guessnum(ctx, num: int, *, prize):
    if num > 999:
        await ctx.send('Please choose a number below 1000.')
        return
    else:
        guild = ctx.guild
        mutedrole = guild.get_role(751158507373461607)
        channel = bot.get_channel(764056131168501791)
        await ctx.send(f'Ok, {ctx.author.mention}, I have sent the message in {channel.mention} and the game has started!')
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(
                read_messages=True,
                send_messages=True,
            ),
            mutedrole: discord.PermissionOverwrite(
                read_messages=True,
                send_messages=False,
        
            )
  
        }
        await channel.edit(overwrites=overwrites, topic=f'Hosted by: {ctx.author.mention}, Prize: {prize}, Range: 1-1000')
        role = guild.get_role(767805742098022441)
        await channel.send(f'A guess the number game has started! {role.mention} the prize is {prize}, hosted by {ctx.author.mention}.')
        num = str(num)
        def check(message):
            return message.channel == channel and message.content.lower() == num
        message = await bot.wait_for('message', check=check)
        await channel.send(f'Correct! {message.author.mention} has guessed the correct number, the correct number being {num}.')
        await message.author.send(f'Please DM {ctx.author.mention} to claim your prize of {prize}!')
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(
                read_messages=True,
                send_messages=False,
            ),
  
        }
        await channel.edit(overwrites=overwrites, topic=f'No game being hosted. Check back later or wait for a ping!')
            
            
            
            

                    
         
        





# ------------------24/7 UPTIME------------------------------------

# ------------------------------------------------------------------------

bot.run(BOT_TOKEN)
