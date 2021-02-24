import discord
import pyapple
from discord.ext import commands
from Siri.bot import Siri
from Siri.utils.logger import Log


class MACOSCogs(commands.Cog):
    patching = True

    def __init__(self, bot) -> None:
        self.bot = bot
        self.logger = Log.cogLogger(self)
        self.client = pyapple.Client()


def setup(bot: Siri):

    if not MACOSCogs.patching:
        bot.add_cog(MACOSCogs(bot))

    elif MACOSCogs.patching:
        return bot.logger.warn(f"MACOSCogs is in patching status.")
