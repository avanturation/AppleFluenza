import os

from discord import Game
from discord import Intents
from discord.ext.commands import Bot

from utils.logger import create_logger

from pyapple import Apple


class AppleFluenza(Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix="!",
            help_command=None,
            activity=Game("applefluenza"),
            intents=Intents.all(),  # this will be removed after the transition to slash is completed
        )

        self.logger = create_logger("applefluenza")
        self.discord_logger = create_logger("discord")

        self.apple = Apple()

    async def on_ready(self):
        self.logger.info("AppleFluenza Ready.")


def auto_load_cogs(bot: AppleFluenza):
    cmdlist = os.listdir("AppleFluenza/cogs/")

    for i in cmdlist:
        if i.endswith(".py") and not i.startswith("__"):
            cmdname = f"AppleFluenza.cogs.{i.replace('.py', '')}"

            try:
                bot.load_extension(cmdname)

            except Exception as error:
                bot.logger.error(f"{cmdname} failed to load: {error}")


bot = AppleFluenza()
