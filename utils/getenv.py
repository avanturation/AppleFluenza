import os

from dotenv import load_dotenv

load_dotenv(verbose=True)


def getenv(key):
    return os.getenv(key)
