import discord
from discord.ext import commands
from Siri.bot import Siri
from Siri.utils.logger import Log


class CoreCogs(commands.Cog):
    patching = True

    def __init__(self, bot) -> None:
        self.bot = bot
        self.logger = Log.cogLogger(self)


def setup(bot: Siri):

    if not CoreCogs.patching:
        bot.add_cog(CoreCogs(bot))

    elif CoreCogs.patching:
        return bot.logger.warn(f"CoreCogs is in patching status.")
