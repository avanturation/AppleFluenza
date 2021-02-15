from dotenv import load_dotenv
import os

load_dotenv(verbose=True)


def getenv(key):
    return os.getenv(key)