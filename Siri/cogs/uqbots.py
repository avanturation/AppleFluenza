import discord
from discord.ext import commands
from ..bot import Siri


class UQBOTSCogs(commands.Cog):
    patching = False

    def __init__(self, bot) -> None:
        self.bot = bot


def setup(bot: Siri):

    if not UQBOTSCogs.patching:
        bot.add_cog(UQBOTSCogs(bot))

    elif UQBOTSCogs.patching:
        return bot.logger.warn(f"UniqueBots Cog is in patching status.")