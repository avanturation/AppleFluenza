import os

import discord
from discord.ext import commands

from .utils.getenv import getenv
from .utils.logger import Log


class Siri(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix="!",
            help_command=None,
            description="A discord bot for Apple firmwares",
            activity=discord.Game("Siri Testing"),
            intents=discord.Intents.all(),
        )
        self.dbkr_token = getenv("KOREANBOTS_TOKEN")
        self.uqbots_token = getenv("UNIQUEBOTS_TOKEN")
        self.logger = Log.defaultLogger("Siri")
        self.discord_logger = Log.discordLogger()

    async def on_ready(self):
        self.logger.info("Siri Ready.")


def auto_load_cogs(bot: Siri):
    cmdlist = os.listdir("Siri/cogs/")

    for i in cmdlist:
        if i.endswith(".py") and not i.startswith("__"):
            cmdname = f"Siri.cogs.{i.replace('.py', '')}"

            try:
                bot.load_extension(cmdname)

            except Exception as error:
                bot.logger.error(f"{cmdname} failed to load: {error}")


bot = Siri()
