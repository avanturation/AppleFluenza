from discord.ext.commands import Cog
from discord.commands import slash_command, Option
from discord import Embed

from AppleFluenza.bot import AppleFluenza

from typing import Dict, Any


class Pallas(Cog):
    def __init__(self, bot: AppleFluenza):
        self.bot = bot

    def __create_pallas_embed(self, asset: Dict[str, Any]) -> Embed:
        embed = Embed(title="Requested Pallas Asset Info")

        for k, v in asset.items():
            if not k in [
                "_AssetReceipt",
                "SystemPartitionPadding",
                "ActualMinimumSystemPartition",
                "MinimumSystemPartition",
                "SystemVolumeSealingOverhead",
                "RSEPTBMDigests",
                "RSEPDigest",
                "SEPTBMDigests",
            ]:
                embed.add_field(name=k, value=v, inline=False)

        return embed

    @slash_command()
    async def pallas(
        self,
        ctx,
        identifier: Option(str, "Your iDevice's identifier"),
        channel: Option(str, "Pallas server's update channel"),
        os_type: Option(str, "OS type to fetch"),
        version: Option(str, "OS version to fetch"),
    ):
        device_info = await self.bot.apple.fetch_device(identifier)

        pallas_asset = await self.bot.apple.get_pallas_asset(
            "SoftwareUpdate",
            os_type,
            version,
            channel,
            identifier,
            device_info.boardconfig.upper(),
        )
        pallas_asset = pallas_asset["Assets"][0]

        await ctx.respond(
            "Request Successful", embed=self.__create_pallas_embed(pallas_asset)
        )


def setup(bot: AppleFluenza):
    bot.add_cog(Pallas(bot))

    bot.logger.info("Pallas cog loaded.")
