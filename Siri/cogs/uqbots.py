import discord
from discord.ext import commands
from Siri.bot import Siri
from Siri.utils.logger import Log


class UQBOTSCogs(commands.Cog):
    patching = True

    def __init__(self, bot) -> None:
        self.bot = bot
        self.logger = Log.cogLogger(self)


def setup(bot: Siri):

    if not UQBOTSCogs.patching:
        bot.add_cog(UQBOTSCogs(bot))

    elif UQBOTSCogs.patching:
        return bot.logger.warn(f"UQBOTSCogs is in patching status.")
