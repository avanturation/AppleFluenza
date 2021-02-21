import pyapple
import discord
from discord.ext import commands
from ..bot import Siri


class IPSWCogs(commands.Cog):
    patching = False

    def __init__(self, bot) -> None:
        self.bot = bot
        self.client = pyapple.Client()


def setup(bot: Siri):

    if not IPSWCogs.patching:
        bot.add_cog(IPSWCogs(bot))

    elif IPSWCogs.patching:
        return bot.logger.warn(f"IPSW Cog is in patching status.")
