import asyncio
import orjson
import discord
from typing import Any

from utils.parser import Parser
from discord.ext import commands

TOGOURL = "https://samsung.partnerbot.cloudturing.chat/api/togo/stocks/onsite"
CHANNELID = 800755427200466964

def compare(a, b):
    if a["S21"] < b["S21"]:
        return True
    elif a["S21+"] < b["S21+"]:
        return True
    elif a["S21Ultra"] < b["S21Ultra"]:
        return True

async def GetData():
    data = await Parser.request(TOGOURL)
    data = orjson.loads(data)
    return data["data"]

async def CheckGalaxyToGo(bot: commands.Bot) -> Any:
    channel = bot.get_channel(CHANNELID)
    prev = await GetData()
    while True:
        await asyncio.sleep(60)
        now = await GetData()
        if prev != now:
            for a, b in zip(prev, now):
                if str(a) != str(b)
                    if a["location"] == "경기":
                        if compare(a, b):
                            q, w, e = ""
                            embed = discord.Embed (
                                title=f"알림! {a['name']}점 입고"
                            )
                            if a["S21"] < b["S21"]:
                                q = f"S21: {b['S21']}대, "
                            if a["S21+"] < b["S21+"]:
                                w = f"S21+: {b['S21+']}대, "
                            if a["S21Ultra"] < b["S21Ultra"]:
                                e = f"S21 Ultra: {b['S21Ultra']}대"
                            embed.add_field (
                                name="현재 수량",
                                value=f"{q}{w}{e}"
                            )
                            await channel.send(embed=embed)
                            await channel.send("<@!537227583729958924> <@!295371171979853825>")
        prev = now
                    

