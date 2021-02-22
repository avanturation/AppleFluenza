from Siri.bot import auto_load_cogs, bot

from .utils.getenv import getenv

token = getenv("TOKEN")

auto_load_cogs(bot)
bot.run(token)
