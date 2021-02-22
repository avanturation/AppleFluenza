from discord import Embed
from ..utils.multilang import get_lang

COLOR = 0x000000


async def make_embed_idevice(region: str, data) -> Embed:
    embed = Embed(title=f"{data['name']} {await get_lang(region,'info')}")
    embed.add_field(
        name=f"{await get_lang(region,'device_identifier')}",
        value=f"{data['identifier']}",
        inline=False,
    )
    embed.add_field(name="Boardconfig", value=f"{data['boardconfig']}", inline=False)
    embed.add_field(name="Platform", value=f"{data['platform']}", inline=False)
    embed.add_field(name="CPID", value=f"{data['cpid']}", inline=False)
    embed.add_field(name="BDID", value=f"{data['bdid']}", inline=False)

    return embed


async def make_embed_ipsw(region: str, data) -> Embed:
    embed = Embed(title=f"IPSW {await get_lang(region,'info')}")
    embed.add_field(
        name=f"{await get_lang(region,'ipsw_identifier')}",
        value=f"{data['identifier']}",
        inline=False,
    )
    embed.add_field(
        name=f"{await get_lang(region,'ipsw_version')}",
        value=f"{data['identifier']}",
        inline=False,
    )
    embed.add_field(
        name=f"{await get_lang(region,'ipsw_buildid')}",
        value=f"{data['identifier']}",
        inline=False,
    )
    embed.add_field(
        name=f"URL",
        value=f"[{await get_lang(region,'click')}]({data['uri']})",
        inline=False,
    )
    embed.add_field(
        name=f"SHA1",
        value=f"{data['sha1']}",
        inline=False,
    )
    embed.add_field(
        name=f"MD5",
        value=f"{data['md5']}",
        inline=False,
    )
    embed.add_field(
        name=f"{await get_lang(region,'ipsw_filesize')}",
        value=f"{data['filesize'][1]}",
        inline=False,
    )
    embed.add_field(
        name=f"{await get_lang(region,'ipsw_releasedate')}",
        value=f"{data['releasedate']}",
        inline=False,
    )
    embed.add_field(
        name=f"{await get_lang(region,'ipsw_uploaddate')}",
        value=f"{data['uploaddate']}",
        inline=False,
    )
    embed.add_field(
        name=f"{await get_lang(region,'ipsw_signed')}",
        value=f"{data['signed']}",
        inline=False,
    )
    return embed