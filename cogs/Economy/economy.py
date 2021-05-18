import discord
from discord.ext import commands

import sqlite3
db_path = ''

class Economy(commands.Cog, name='Economy'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['init'])
    async def init_balance(self, ctx, user: discord.User=None):
        # Pass in the specified user, otherwise use the author
        user = ctx.author if not user else user



    


def setup(bot):
    bot.add_cog(Economy(bot))
    print('Economy extension is loaded')