import asyncio
import orjson
import discord
from typing import Any

from utils.parser import Parser
from discord.ext import commands

TOGOURL = "https://samsung.partnerbot.cloudturing.chat/api/togo/stocks/onsite"
CHANNELID = 800755427200466964

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
                if str(a) != str(b) and a["location"] == "경기":
                    embed = discord.Embed (
                        title=f"알림! {a['name']}점 입고"
                    )
                    embed.add_field (
                        name="현재 수량",
                        value=f"S21: {b['S21']}대, S21+: {b['S21+']}대, S21 Ultra: {b['S21Ultra']}대"
                    )
                    await channel.send(embed=embed)
                    await channel.send("<@!537227583729958924> <@!295371171979853825>")
        prev = now
                    

