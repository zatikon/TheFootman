#!/usr/bin/env python

import os, sys

import discord
from discord.ext import commands
import aiosqlite
import logging

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

db_path = os.path.join(os.environ["HOME"], ".local/share/zatikon/zatikon.db")

db = None

description = "TEST"

intents = discord.Intents.default()
#intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    global db
    db = await aiosqlite.connect(db_path)
    print('Database connection established.')

@bot.command()
async def stats(ctx):
    async with db.execute("select count(*) from players") as cursor:
        how_many = (await cursor.fetchone())[0]
        await ctx.send(f"We have {how_many} players. REJOICE")


with open(sys.argv[1], "r") as token_file:
    token = token_file.readline().strip()
    bot.run(token)
