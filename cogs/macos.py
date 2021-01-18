import discord
import asyncio
from discord.ext import commands
from utils.swscan import SwScanFetcher
from hurry.filesize import size, alternative
from utils.embed import EmbedUtil


class macOS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed = EmbedUtil()

    @commands.command(name = "맥OS다운로드")
    async def macOSDownload (self, ctx, seed = "publicseed"):
        SWSCAN = SwScanFetcher()
        await ctx.send (f"Apple 서버에서 카탈로그를 불러오는 중 입니다. (현재 시드 : {seed})")
        await SWSCAN.FetchCatalog(seed)
        await SWSCAN.ParseCatalog()
        embed = discord.Embed(
            title = "현재 다운로드 가능한 macOS 목록입니다.",
            description = "번호를 입력해주세요."
        )
        num = 1
        for target in SWSCAN.macos_dict:
            embed.add_field (
                name = f"{num}. {target.product_id} - {target.title}",
                value = f"버전 : {target.version}, 빌드번호 : {target.build}",
                inline = False
            )
            num += 1
        self.embed.footer(embed, ctx.author)
        await ctx.send (embed=embed)
        response = await self.bot.wait_for (
            "message", 
            check=lambda message: message.author == ctx.author,
            timeout = 60
        )
        selected = SWSCAN.macos_dict[int(response.content) - 1]
        embed = discord.Embed (
            title = f"{selected.title} ({selected.build})",
            description = "아래 파일들을 모두 다운하신 후 편하신 방법으로 macOS 설치 앱을 만드세요!\ngibMacOS 속 Makeinstall 와 같은 툴을 사용하세요."
        )
        for pk in selected.packages:
            s = pk[0]
            pkurl = pk[1]
            a = pkurl.split("/")
            embed.add_field (
                name = f"{a[-1]} (용량 : {size(int(s), system=alternative)})",
                value = f"[클릭]({pkurl})",
                inline=False
            ) 
        self.embed.footer(embed, ctx.author)  
        await ctx.send(embed=embed)

def setup (bot):
    bot.add_cog(macOS(bot))