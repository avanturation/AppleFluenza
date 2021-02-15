from Siri.bot import bot, auto_load_cogs
from .utils.getenv import getenv

token = getenv("TOKEN")

auto_load_cogs(bot)
bot.run(token)