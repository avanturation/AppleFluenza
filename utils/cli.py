from optparse import OptionParser
from pyfiglet import print_figlet
from termcolor import colored


def option_parser():
    parser = OptionParser(usage="usage: $prog [options]")

    parser.add_option(
        "--debug",
        "--test",
        help="Running AppleFluenza for test purposes. Debug logging and Test token will be enabled.",
        action="store_true",
        dest="debug",
    )

    parser.add_option(
        "--token",
        help="Overriding discord bot token with given value.",
        dest="override",
        default=None,
        type=str,
    )
    return parser


def header():
    print_figlet("AppleFluenza", font="slant")

    print(colored("AppleFluenza - v0.1.0a", attrs=["bold"]))
    print("Discord Chatbot for Apple firmwares - Made by fxrcha with love")
    print()
