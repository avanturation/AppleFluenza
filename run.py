import discord
import asyncio
import config
from discord.ext import commands
from utils.general import gather_commands
from background.togo import CheckGalaxyToGo

class Siri(commands.Bot):
    def __init__(self, config):
        super().__init__(
            command_prefix=["시리야 ", 
                "Hey Siri, ", 
                "Hey Siri ",
                "-"
            ],
            help_command=None
        )
        self.config = config
        gather_commands(self)
        self.loop = asyncio.get_event_loop()

    async def on_message(self, message):
        if not message.author.bot: 
            await self.process_commands(message)

    async def on_ready(self):
        print ('SiriBot Ready.')
        await self.change_presence(
            activity=discord.Game("NOT FOR COMMERCIAL")
        )
        if not self.user.id == 770612780042551318: 
            print("Warning : Not running on real Siri Bot.")
        self.loop.create_task(CheckGalaxyToGo(self))

    async def on_command_error(self, context, exception):
        if isinstance(exception, commands.CommandInvokeError):
            embed = discord.Embed(
                title = "에러가 발생했습니다!",
                description = "에러가 계속 발생할 시 UniqueCode 서포트서버로 와주세요!"
            )
            embed.add_field (
                name = "에러 내용",
                value = exception
            )
            await context.send(embed=embed)
            
            
bot = Siri(config)
bot.run(config.TOKEN, bot=True)
