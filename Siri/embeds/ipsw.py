from discord import Embed
from Siri.utils.multilang import get_lang
from typing import List

COLOR = 0x000000


async def make_embed_idevice(region: str, data) -> List[Embed]:
    embed_list = [
        await make_embed_ipsw(region, ipsw_data) for ipsw_data in data.firmwares
    ]

    embed = Embed(title=f":mobile_phone: {data.name} {await get_lang(region,'info')}")
    embed.add_field(
        name=f"{await get_lang(region,'device_identifier')}",
        value=f"{data.identifier}",
        inline=False,
    )
    embed.add_field(name="Boardconfig", value=f"{data.boardconfig}", inline=False)
    embed.add_field(name="Platform", value=f"{data.platform}", inline=False)
    embed.add_field(name="CPID", value=f"{data.cpid}", inline=False)
    embed.add_field(name="BDID", value=f"{data.bdid}", inline=False)
    embed.set_footer(text=await get_lang(region, "device_nextpage"))

    embed_list.append(embed)
    embed_list.reverse()

    return embed_list


async def make_embed_ipsw(region: str, data) -> Embed:
    embed = Embed(title=f":card_box: IPSW {await get_lang(region,'info')}")
    embed.add_field(
        name=f"{await get_lang(region,'ipsw_identifier')}",
        value=f"{data.identifier}",
        inline=False,
    )
    embed.add_field(
        name=f"{await get_lang(region,'ipsw_version')}",
        value=f"{data.version}",
        inline=False,
    )
    embed.add_field(
        name=f"{await get_lang(region,'ipsw_buildid')}",
        value=f"{data.buildid}",
        inline=False,
    )
    embed.add_field(
        name=f"URL",
        value=f"[{await get_lang(region,'click')}]({data.uri})",
        inline=False,
    )
    embed.add_field(
        name=f"SHA1",
        value=f"{data.sha1sum}",
        inline=False,
    )
    embed.add_field(
        name=f"MD5",
        value=f"{data.md5sum}",
        inline=False,
    )
    embed.add_field(
        name=f"{await get_lang(region,'ipsw_filesize')}",
        value=f"{data.filesize[1]}",
        inline=False,
    )
    embed.add_field(
        name=f"{await get_lang(region,'ipsw_releasedate')}",
        value=f"{data.releasedate}",
        inline=False,
    )
    embed.add_field(
        name=f"{await get_lang(region,'ipsw_uploaddate')}",
        value=f"{data.uploaddate}",
        inline=False,
    )
    embed.add_field(
        name=f"{await get_lang(region,'ipsw_signed')}",
        value=f"{data.signed}",
        inline=False,
    )
    return embed
