import discord
from discord.ext import commands
from ..bot import Siri


class CoreCogs(commands.Cog):
    patching = False

    def __init__(self, bot) -> None:
        self.bot = bot


def setup(bot: Siri):

    if not CoreCogs.patching:
        bot.add_cog(CoreCogs(bot))

    elif CoreCogs.patching:
        return bot.logger.warn(f"Core Cog is in patching status.")