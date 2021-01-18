import discord


class EmbedUtil:
    def __init__(self): pass

    @staticmethod
    def footer (embed : discord.Embed, author : discord.abc.User):
        embed.set_footer(text = "Siri 0.0.1", icon_url=author.avatar_url)
        embed.color = 0xffffff

    @staticmethod
    def author (embed : discord.Embed, author : discord.abc.User):
        embed.set_author (
            name = author,
            icon_url= author.avatar_url
        )