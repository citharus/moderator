import discord
import motor.motor_asyncio as motor
from discord.ext import commands

from misc import add_entry
from misc.embeds import CommandEmbed


class Warn(commands.Cog):
    def __init__(self, bot: commands.Bot, db: motor.AsyncIOMotorDatabase) -> None:
        self.bot: commands.Bot = bot
        self.db: motor.AsyncIOMotorDatabase = db

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx: commands.Context, member: discord.Member, *, reason: str = None) -> None:
        await ctx.send(embed=CommandEmbed(":warning: Warned", member))
        await self._warn(self.db, ctx.message.author, member, reason)

    @staticmethod
    async def _warn(db: motor.AsyncIOMotorDatabase, author: discord.Member, member: discord.Member,
                    reason: str) -> None:
        await add_entry(db, "warns", author, member, reason)
