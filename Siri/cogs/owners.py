import discord
from discord.ext import commands
from Siri.bot import Siri


class OwnersCogs(commands.Cog):
    patching = False

    def __init__(self, bot) -> None:
        self.bot = bot


def setup(bot: Siri):

    if not OwnersCogs.patching:
        bot.add_cog(OwnersCogs(bot))

    elif OwnersCogs.patching:
        return bot.logger.warn(f"Owner Cog is in patching status.")