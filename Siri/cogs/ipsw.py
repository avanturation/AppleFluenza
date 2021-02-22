from discord import client
import pyapple
import discord
from discord.ext import commands
from ..bot import Siri
from ..utils.multilang import discrim_region


class IPSWCogs(commands.Cog):
    patching = False

    def __init__(self, bot) -> None:
        self.bot = bot
        self.logger
        self.client = pyapple.Client()

    @commands.command(name="기기정보", aliases=["device"])
    async def device_command(self, ctx, identfier: str):
        guild_region = discrim_region(ctx.guild)
        device_info = await client.device(identfier)

        embed = discord.Embed(title="")


def setup(bot: Siri):

    if not IPSWCogs.patching:
        bot.add_cog(IPSWCogs(bot))

    elif IPSWCogs.patching:
        return bot.logger.warn(f"IPSW Cog is in patching status.")
