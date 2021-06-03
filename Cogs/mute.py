import asyncio

import discord
import motor.motor_asyncio as motor
from discord.ext import commands

from misc import add_entry
from misc.embeds import CommandEmbed


class Mute(commands.Cog):
    def __init__(self, bot: commands.Bot, db: motor.AsyncIOMotorDatabase) -> None:
        self.bot: commands.Bot = bot
        self.db: motor.AsyncIOMotorDatabase = db

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx: commands.Context, member: discord.Member, delay: int = 1, *, reason: str = None) -> None:
        role: discord.Role = await commands.RoleConverter().convert(ctx, "Muted")
        await ctx.send(embed=CommandEmbed(":mute: Muted", member))
        await member.add_roles(role, reason=reason)
        await add_entry(self.db, "mutes", ctx.message.author, member, reason)
        await asyncio.sleep(delay * 60)
        await member.remove_roles(role)
