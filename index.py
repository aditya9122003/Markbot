import discord
import os
import random
import datetime
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from dotenv import load_dotenv
from discord.ext import commands
import sqlite3
from Bot_commands import market
from Bot_commands import local
from Bot_commands.variable import variables
from Bot_commands.variable import channelIDS
from Bot_commands import compare



load_dotenv()
BOT_TOKEN = os.getenv('TOKEN')

# bot = commands.Bot(command_prefix='!', case_inse)
bot = discord.Client()

@bot.event
async def on_ready():

    db = sqlite3.connect('localitems.db')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS items (
        name text NOT NULL,
        description text NOT NULL,
        seller text NOT NULL,
        price text NOT NULL,
        image_path text NOT NULL,
        thumbnail_path text NOT NULL
    )''')
    print(f'{bot.user.name} has connected to Discord!')



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello there")

    if message.content.startswith("$market"): 
        msg = market.market(message)
        if (type(msg) == list):
            for mesg in msg:
                await message.channel.send(embed = mesg)
                
        elif (msg == variables.add_message):
            await message.channel.send(msg)
            channel = bot.get_channel(channelIDS.local_inventory_id)
            em_msg = local.em_add_item
            await channel.send("New item added")
            reac = await channel.send(embed = em_msg)
            await reac.add_reaction('🛒')
            await reac.add_reaction('❤️')

        else:
            await message.channel.send(msg)

    if message.content.startswith("$compare"):
        compare.cmp(message.content[9: ])

    if message.content.startswith("$help"):
        msgn = '$hello"- prints "Hello there!"\n"$help"- prints a help list\n"$compare"- compares the products entered by user, and gives appropriate result. For example, “$compare iPhone 13 vs iPhone 12” gives the result, comparing the 2 phones\n"$market"- which should print the way to progress ahead; for example, if you give command of the type “$market flipkart rubik’s cube”, it should show the result of all the rubik’s cubes available on Flipkart. Similarly, we can implement the same in Amazon, Snapdeal and Pepperfry, and access local market.\n  commands in "$market"-\n  1) "$market flipkart product"- searches for the product in Flipkart\n  2) "$market amazon product"- searches for the product in amazon\n  3) "$market snapdeal product"- searches for the product in snapdeal\n  4) "$market pepperfry product"- searches for the product in pepperfry\n  5) "$market flipkart ~a"- opens the main flipkart website. Similar applies to Amazon, Snapdeal, Pepperfry.\n  6) "$market flipkart ~x"- opens the deals of the day page. Similar applies to Amazon which opens the same.\n  7) “$market local add” – this command adds the product into the inventory. The user has to specify the product info after this command. For example- “$market local add --product--description--seller--price—image http link--thumbnail http link”. Here the image and thumbnail have to be http links. Make sure to add "--" between the terms.\n  8) “$market local search”- this command searches for the product name in the inventory. For example- “$market local search name”.'
        await message.channel.send(msgn)

        
@bot.event
async def on_reaction_add(reaction, user):  
    if (reaction.emoji == '🛒' or reaction.emoji == '❤️') and user != bot.user:
        user = await bot.fetch_user(user.id)
        embed_msg = reaction.message.embeds[0]
        await user.send(embed = embed_msg)

        # original = await message.channel.fetch_message(payload.message_id)

# @bot.event
# async def on_raw_reaction_add(payload):
#     userId = payload.user_id
#     channelId = payload.channel_id
#     channel = bot.get_channel(channelId)
#     messageId = payload.message_id
#     user = await bot.fetch_user(userId)
#     if user != bot.user:
#         Omessage = channel.fetch_message(messageId)
#         print(Omessage)

bot.run(BOT_TOKEN)