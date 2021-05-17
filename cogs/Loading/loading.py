import discord
from discord.ext import commands

class Loading(commands.Cog, name='Loading'):
    """
    Purpose of this extension is to allow for loading, unloading, and reloading
    extensions without having to restart the bot.
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def load(self, extension: str):
        """ Loads in an extension """
        self.bot.load_extension(f'cogs.{extension}.{extension.lower()}')

    @commands.command()
    async def unload(self, extension: str):
        """ Unloads and extension """
        self.bot.unload_extension(f'cogs.{extension}.{extension.lower()}')

    @commands.command()
    async def reload(self, extension: str):
        """ Reloads an extension (unload and load) """
        self.bot.reload_extension(f'cogs.{extension}.{extension.lower()}')


def setup(bot):
    bot.add_cog(Loading(bot))
    print('Loading extension is loaded')