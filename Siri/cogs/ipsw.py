from discord.utils import get
import pyapple
from discord.ext import commands
from Siri.bot import Siri
from Siri.embeds.ipsw import *
from Siri.utils.multilang import discrim_region, get_lang
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
        guild_region = await discrim_region(ctx.guild)
        msg = await ctx.send(await get_lang(guild_region, "fetching"))

        device_info = await self.client.device(identfier)

        idevice_embed = await make_embed_idevice(guild_region, device_info)

        page = Paginator(self.bot, ctx, msg, idevice_embed)
        await page.start()

    @commands.command(name="펌웨어", aliases=["ipsw"])
    async def ipsw_command(self, ctx, identifier: str, build_id: str):
        guild_region = await discrim_region(ctx.guild)
        msg = await ctx.send(await get_lang(guild_region, "fetching"))

        ipsw_info = await self.client.ipsw(identifier, build_id)
        ipsw_embed = await make_embed_ipsw(guild_region, ipsw_info)

        await msg.edit(embed=ipsw_embed)


def setup(bot: Siri):

    if not IPSWCogs.patching:
        bot.add_cog(IPSWCogs(bot))

    elif IPSWCogs.patching:
        return bot.logger.warn(f"IPSWCogs is in patching status.")
