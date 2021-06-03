import motor.motor_asyncio as motor
from discord.ext import commands

from misc import ErrorEmbed, add_word, delete_word


class Censor(commands.Cog):
    def __init__(self, bot: commands.Bot, db: motor.AsyncIOMotorDatabase) -> None:
        self.bot: commands.Bot = bot
        self.db: motor.AsyncIOMotorDatabase = db

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def censor(self, ctx: commands.Context, *, word: str) -> None:
        if not await add_word(self.db, word):
            await ctx.send(embed=ErrorEmbed("The word is already censored."))

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def permit(self, ctx: commands.Context, *, word: str) -> None:
        if not await delete_word(self.db, word):
            await ctx.send(embed=ErrorEmbed("The word is not censored."))