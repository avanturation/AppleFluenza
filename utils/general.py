import os

def gather_commands(bot):
    command_list = os.listdir("cogs/")
    for i in command_list:
        if i.endswith(".py"):
            command_name = "cogs." + i.replace(".py", "")
            bot.load_extension(command_name)