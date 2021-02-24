import discord
from discord.ext import commands
from Siri.bot import Siri
from Siri.utils.logger import Log


class OwnersCogs(commands.Cog):
    patching = True

    def __init__(self, bot) -> None:
        self.bot = bot
        self.logger = Log.cogLogger(self)


def setup(bot: Siri):

    if not OwnersCogs.patching:
        bot.add_cog(OwnersCogs(bot))

    elif OwnersCogs.patching:
        return bot.logger.warn(f"OwnersCog is in patching status.")
