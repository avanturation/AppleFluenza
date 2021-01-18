import discord
from EZPaginator import Paginator
from utils.embed import EmbedUtil
from discord.ext import commands


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed = EmbedUtil()

    async def announce (self, content_Type, content):
        for guilds in self.bot.guilds:
            for channel in guilds.channels:
                try:
                    if channel.topic:
                        if channel.topic.find("시리봇 공지") != -1:
                            if content_Type== "EMBED": await channel.send(embed=content)
                            elif content_Type == "MESSAGE": await channel.send(content)
                except Exception: pass

    @commands.command (name = "공지")
    async def message_announce(self, ctx, *string):
        content = " ".join(string[:])
        await self.announce (content_Type="MESSAGE", content=content)

    
    @commands.command (name = "임베드공지")
    async def embed_announce(self, ctx):
        await ctx.send ("제목 입력")
        title = await self.bot.wait_for (
            "message", 
            check=lambda message: message.author == ctx.author,
            timeout = 60
        )
        await ctx.send ("설명 입력")
        description = await self.bot.wait_for (
            "message", 
            check=lambda message: message.author == ctx.author,
            timeout = 60
        )
        await ctx.send ("사진 URL 입력")
        image = await self.bot.wait_for (
            "message", 
            check=lambda message: message.author == ctx.author,
            timeout = 60
        )
        await ctx.send ("썸네일 URL 입력")
        thumbnail = await self.bot.wait_for (
            "message", 
            check=lambda message: message.author == ctx.author,
            timeout = 60
        )
        embed = discord.Embed (
            title = title.content, description = description.content
        )
        if not image.content == "없음":
            embed.set_image(url = image.content)
        if not thumbnail.content == "없음":
            embed.set_thumbnail(url = thumbnail.content)
        await self.announce("EMBED", embed)
    
    @commands.command(name = "안녕")
    async def hello (self, ctx):
        await ctx.send ("안녕하세요. 무엇을 도와드릴까요?")

    @commands.command(name="핑")
    async def ping(self, ctx):
        t1 = ctx.message.created_at
        ctx2 = await ctx.send('메시지 핑 테스트용 입니다. 무시해주셔도 좋습니다!')
        t2 = ctx2.created_at
        ping = t2 - t1
        pp = str(int(ping.microseconds) / 1000)
        pp = pp.split(".")
        pp = pp[0]
        embed = discord.Embed(title="Pong!")
        embed.add_field(
            name="Websocket", value=f"{round(self.bot.latency * 1000)}ms", inline=True)
        embed.add_field(name="메시지 핑", value=f"{pp}ms", inline=True)
        await ctx2.edit(embed=embed, content="")

    @commands.command(name = "도움")
    async def HelpCmd (self, ctx):
        embed = discord.Embed (
            title = "Siri 도움말",
            description = "Siri 봇의 도움말 입니다."
        )
        embed.add_field(name = "1페이지", value="iOS 관련", inline=False)
        embed.add_field(name = "2페이지", value="macOS 관련", inline=False)
        embed1 = discord.Embed(
            title = "1페이지",
            description = "Siri 봇의 iOS 명령어들 입니다"
        )
        embed1.add_field(name = "IPSW (아이폰 식별자)", value="예시 : 시리야 IPSW iPhone12,1\n해당 아이폰의 최신 iOS를 가져옵니다", inline=False)
        embed2 = discord.Embed(
            title = "2페이지",
            description = "Siri 봇의 macOS 명령어들 입니다"
        )
        embed2.add_field(name = "맥OS다운로드", value="예시 : 시리야 맥OS다운로드\n애플 서버에서 다운로드 할 수 있는 macOS를 출력 후, 원하는 macOS를 다운로드 합니다.", inline=False)
        self.embed.footer(embed, ctx.author)
        self.embed.footer(embed1, ctx.author)
        self.embed.footer(embed2, ctx.author)
        embeds = [embed, embed1, embed2]
        msg = await ctx.send(embed=embed)
        page = Paginator(self.bot, embeds=embeds, message=msg)
        await page.start()
        
        



def setup (bot):
    bot.add_cog(General(bot))