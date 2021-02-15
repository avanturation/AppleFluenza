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
            intents=discord.Intents.all(),
        )
        self.dbkr_token = getenv("KOREANBOTS_TOKEN")
        self.uqbots_token = getenv("UNIQUEBOTS_TOKEN")
        self.logger = Log.defaultLogger("Siri")
        self.discord_logger = Log.discordLogger()


def auto_load_cogs(bot: Siri):
    cmdlist = os.listdir("Siri/cogs/")

    for i in cmdlist:
        if i.endswith(".py") and not i.startswith("__"):
            cmdname = f"Siri.cogs.{i.replace('.py', '')}"

            try:
                bot.load_extension(cmdname)
                bot.logger.log(f"{cmdname} Cog successfully loaded.")

            except Exception as error:
                bot.logger.log(f"{cmdname} failed to load: {error}")


bot = Siri()