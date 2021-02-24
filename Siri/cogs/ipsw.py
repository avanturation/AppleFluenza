import pyapple
from discord.ext import commands
from Siri.bot import Siri
from Siri.embeds.ipsw import *
from Siri.utils.multilang import discrim_region
from Siri.utils.paginator import Paginator
from Siri.utils.logger import Log


class IPSWCogs(commands.Cog):
    patching = False

    def __init__(self, bot) -> None:
        self.bot = bot
        self.logger = Log.cogLogger(self)
        self.client = pyapple.Client()

    @commands.command(name="기기정보", aliases=["device"])
    async def device_command(self, ctx, identfier: str):
        embed_list = []
        guild_region = await discrim_region(ctx.guild)
        msg = await ctx.send("Fetching..")
        device_info = await self.client.device(identfier)
        idevice_embed = await make_embed_idevice(guild_region, device_info)
        for ipsw_data in device_info.firmwares:
            embed_list.append(await make_embed_ipsw(guild_region, ipsw_data))
        embed_list.append(idevice_embed)
        embed_list.reverse()
        page = Paginator(self.bot, ctx, msg, embed_list)
        await page.start()


def setup(bot: Siri):

    if not IPSWCogs.patching:
        bot.add_cog(IPSWCogs(bot))

    elif IPSWCogs.patching:
        return bot.logger.warn(f"IPSWCogs is in patching status.")
