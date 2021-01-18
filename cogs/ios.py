import discord
import asyncio
import orjson
from discord.ext import commands
from utils.idevice import ipsw_info
from utils.parser import Parser

class iOS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.HTTP = Parser()


    @commands.command (name = "ipsw", aliases = ["IPSW"])
    async def latest_ipsw (self, ctx, model : str):
        embed = await ipsw_info(device_id=model)
        await ctx.send(embed=embed)

    @commands.command (name="갤투고")
    async def GalaxyToGo(self, ctx):
        req = await Parser.request("https://samsung.partnerbot.cloudturing.chat/api/togo/stocks/onsite")
        data = orjson.loads(req)
        data = data["data"]
        embed = discord.Embed(
            title = "Galaxy To Go status (Galaxy S21 Series)"
        )
        for i in data:
            embed.add_field(
                name = f"{i['name']} - {i['location']}",
                value = f"S21: {i['S21']}대, S21+: {i['S21+']}대, S21 Ultra: {i['S21Ultra']}대",
                inline=False
            )
        await ctx.send(embed=embed)

def setup (bot):
    bot.add_cog(iOS(bot))