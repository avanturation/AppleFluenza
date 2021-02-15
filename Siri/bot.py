import os
import discord
from discord.ext import commands
from .utils.getenv import getenv


class Siri(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix="!",
            help_command=None,
            description="A discord bot for Apple firmwares",
            intents=discord.Intents.all(),
        )
        self.dbkr_token = getenv("KOREANBOTS_TOKEN")
        self.uqbts_token = getenv("UNIQUEBOTS_TOKEN")


def auto_load_cogs(bot: Siri):
    cmdlist = os.listdir("Siri/cogs/")

    for i in cmdlist:
        if i.endswith(".py") and not i.startswith("__"):

            cmdname = f"Siri.cogs.{i.replace('.py', '')}"

            try:
                bot.load_extension(cmdname)

            except Exception as error:
                print(f"{cmdname} failed to load: {error}")


bot = Siri()