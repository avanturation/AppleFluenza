import discord
import pyapple
from discord.ext import commands
from Siri.bot import Siri
from Siri.utils.logger import Log
from Siri.utils.multilang import discrim_region, get_lang

from typing import Optional


class MACOSCogs(commands.Cog):
    patching = True

    def __init__(self, bot) -> None:
        self.bot = bot
        self.logger = Log.cogLogger(self)
        self.client = pyapple.Client()

    @commands.command(name="", aliases=[""])
    async def get_macos(self, ctx, seed: Optional[str] = "publicseed"):
        guild_region = await discrim_region(ctx.guild)
        available_macos = await self.client.available_macos(seed)


def setup(bot: Siri):

    if not MACOSCogs.patching:
        bot.add_cog(MACOSCogs(bot))

    elif MACOSCogs.patching:
        return bot.logger.warn(f"MACOSCogs is in patching status.")
