import json

import aiofiles
from discord import Guild, VoiceRegion
from AppleFluenza.bot import bot

cache = {}


async def open_file(path: str):
    async with aiofiles.open(path, mode="r") as fp:
        f = await fp.read()
    return f


async def discrim_region(object: Guild) -> str:
    fp = await open_file("AppleFluenza/langpack/guild_override.json")
    overrides = json.loads(fp)

    _id = str(object.id)

    if _id in overrides:
        return overrides[_id]

    return "kr" if object.region == VoiceRegion.south_korea else "en"


async def get_lang(region: str, target: str) -> str:
    path = f"AppleFluenza/langpack/{region}.json"

    try:
        fp = await open_file(path)
        lang_pack = json.loads(fp)

    except json.decoder.JSONDecodeError:
        bot.logger.warn(
            f"WARN: Loading langpack for language '{region}' has failed. Using default 'en'"
        )
        fp = await open_file("AppleFluenza/langpack/en.json")
        lang_pack = json.loads(fp)

    cache[path] = lang_pack

    return lang_pack[target]
