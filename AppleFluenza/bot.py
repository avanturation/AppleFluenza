import os

import discord
from discord.ext import commands

from utils.getenv import getenv
from utils.logger import create_logger


class AppleFluenza(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix="!",
            help_command=None,
            activity=discord.Game("applefluenza"),
            intents=discord.Intents.all(),
        )
        self.logger = create_logger("applefluenza")
        self.discord_logger = create_logger("discord")

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
