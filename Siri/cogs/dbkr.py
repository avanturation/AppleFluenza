import discord
from discord.ext import commands
from Siri.bot import Siri


class DBKRCogs(commands.Cog):
    patching = False

    def __init__(self, bot) -> None:
        self.bot = bot


def setup(bot: Siri):

    if not DBKRCogs.patching:
        bot.add_cog(DBKRCogs(bot))

    elif DBKRCogs.patching:
        return bot.logger.warn(f"DBKR Cog is in patching status.")
