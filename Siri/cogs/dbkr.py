import discord
from discord.ext import commands
from Siri.bot import Siri
from Siri.utils.logger import Log


class DBKRCogs(commands.Cog):
    patching = True

    def __init__(self, bot) -> None:
        self.bot = bot
        self.logger = Log.cogLogger(self)


def setup(bot: Siri):

    if not DBKRCogs.patching:
        bot.add_cog(DBKRCogs(bot))

    elif DBKRCogs.patching:
        return bot.logger.warn(f"DBKRCogs is in patching status.")
