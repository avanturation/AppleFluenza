from asyncio import TimeoutError

from discord import Message, Reaction, User
from discord.ext.commands import Context
from AppleFluenza.bot import AppleFluenza

emoji_list = ["◀", "▶", "❎"]


class Paginator:
    def __init__(
        self, bot: AppleFluenza, ctx: Context, msg: Message, embeds: list
    ) -> None:
        self.bot = bot
        self.ctx = ctx
        self.msg = msg
        self.embeds = embeds

    def check(self, reaction: Reaction, user: User) -> bool:
        return user.id == self.ctx.author.id and reaction.emoji in emoji_list

    async def start(self):
        index = 0
        await self.msg.edit(content="", embed=self.embeds[index])

        for emojis in emoji_list:
            await self.msg.add_reaction(emojis)

        while not self.bot.is_closed():
            try:
                result, author = await self.bot.wait_for(
                    "reaction_add", check=self.check, timeout=240.0
                )

                if result.message.id != self.msg.id:
                    continue

                if author.id != self.ctx.author.id:
                    try:
                        await self.msg.remove_reaction(result.emoji, self.ctx.author)

                    except Exception:
                        pass

                    continue

            except TimeoutError:
                await self.msg.clear_reactions()
                break

            if result.emoji == "❎":
                await self.msg.clear_reactions()
                break

            elif result.emoji == "▶":
                index += 1

                if index >= len(self.embeds):
                    index = 0

                await self.msg.edit(embed=self.embeds[index])

                try:
                    await self.msg.remove_reaction(result.emoji, self.ctx.author)

                except Exception:
                    pass

            elif result.emoji == "◀":
                index -= 1

                if index < 0:
                    index = len(self.embeds) - 1

                await self.msg.edit(embed=self.embeds[index])

                try:
                    await self.msg.remove_reaction(result.emoji, self.ctx.author)

                except Exception:
                    pass
