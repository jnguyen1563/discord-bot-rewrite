import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

# Read in environment variables
load_dotenv()

# Command prefix for bot
bot = commands.Bot(command_prefix=os.getenv('BOT_COMMAND_PREFIX'))

# Runs when bot is booted up
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online)
    print('Bot is online')

# Code to handle loading bot extensions via cogs
extensions = ['Loading']
for extension in extensions:
    try:
        bot.load_extension(f'cogs.{extension}.{extension.lower()}')
    except Exception as e:
        print(f'Failed to load extension: {extension}')


# Tell the bot to run
bot.run(os.getenv('BOT_API_TOKEN'))