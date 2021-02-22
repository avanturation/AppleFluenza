import pyapple
from discord.ext import commands
from Siri.bot import Siri
from Siri.embeds.ipsw import *
from Siri.utils.multilang import discrim_region


class IPSWCogs(commands.Cog):
    patching = False

    def __init__(self, bot) -> None:
        self.bot = bot
        self.client = pyapple.Client()

    @commands.command(name="기기정보", aliases=["device"])
    async def device_command(self, ctx, identfier: str):
        embed_list = []
        guild_region = discrim_region(ctx.guild)
        device_info = await self.client.device(identfier)
        idevice_embed = await make_embed_idevice(guild_region, device_info)
        for ipsw_data in device_info["firmwares"]:
            embed_list.append(await make_embed_ipsw(guild_region, ipsw_data))


def setup(bot: Siri):

    if not IPSWCogs.patching:
        bot.add_cog(IPSWCogs(bot))

    elif IPSWCogs.patching:
        return bot.logger.warn(f"IPSW Cog is in patching status.")
