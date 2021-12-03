import logging

import discord
import colorlog

FORMATTER = colorlog.ColoredFormatter(
    "%(bold)s%(log_color)s%(levelname)s%(reset)s [%(asctime)s] [%(name)s:%(bold)s%(module)s%(reset)s] %(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        "DEBUG": "green",
        "INFO": "cyan",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "red,bg_white",
    },
    secondary_log_colors={},
    style="%",
)


def create_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    streamhandler = logging.StreamHandler()
    streamhandler.setFormatter(FORMATTER)
    filehandler = logging.FileHandler(f"AppleFluenza/logs/{name}.txt", "a")
    filehandler.setFormatter(FORMATTER)

    logger.addHandler(streamhandler)
    logger.addHandler(filehandler)
    return logger
