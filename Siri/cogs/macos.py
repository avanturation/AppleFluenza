import pyapple
import discord
from discord.ext import commands
from ..bot import Siri


class MACOSCogs(commands.Cog):
    patching = False

    def __init__(self, bot) -> None:
        self.bot = bot
        self.client = pyapple.Client()


def setup(bot: Siri):

    if not MACOSCogs.patching:
        bot.add_cog(MACOSCogs(bot))

    elif MACOSCogs.patching:
        return bot.logger.warn(f"macOS Cog is in patching status.")