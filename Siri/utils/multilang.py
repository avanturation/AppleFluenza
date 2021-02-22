from discord import Guild, VoiceRegion
from ..bot import bot
import json

cache = {}


def discrim_region(object: Guild) -> str:
    overrides = json.loads("Siri/langpack/guild_override.json")
    _id = str(object.id)

    if _id in overrides:
        return overrides[_id]

    return "kr" if object.region == VoiceRegion.south_korea else "en"


def load_lang_pack(region: str, cog_name: str, target: str) -> str:
    path = f"Siri/langpack/{cog_name}_{region}.json"

    if cache[path]:
        return cache[path][target]

    try:
        lang_pack = json.loads(path)
    except json.decoder.JSONDecodeError:
        bot.logger.warn(
            f"WARN: Loading langpack for language '{region}' has failed. Using default 'en'"
        )
        lang_pack = json.loads(f"Siri/langpack/{cog_name}_en.json")

    cache[path] = lang_pack

    return lang_pack[target]
