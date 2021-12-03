import logging
import sys

from AppleFluenza.bot import auto_load_cogs, bot

from utils.getenv import getenv
from utils.cli import header, option_parser


if __name__ == "__main__":
    header()

    auto_load_cogs(bot)

    optparser = option_parser()
    (options, args) = optparser.parse_args(sys.argv)

    token = getenv("TOKEN")

    if options.debug is not None:
        logging.getLogger().setLevel(logging.DEBUG)
        bot.logger.info("WARNING: AppleFluenza is now in debug mode.")
        token = getenv("TEST_TOKEN")

    if options.override is not None:
        bot.logger.info("Overriding token.")
        token = options.override

    bot.run(token)
