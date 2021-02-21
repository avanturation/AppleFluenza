from discord import Guild, VoiceRegion
import json


def discrim_region(object: Guild) -> str:
    if object.region == VoiceRegion.south_korea:
        return "kr"
    else:
        return "en"


def load_lang_pack(region: str, cog_name: str, target: str) -> str:
    path = f"Siri/langpack/{cog_name}_{region}.json"
    lang_pack = json.loads(path)
    return lang_pack[target]
