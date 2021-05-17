import asyncio

import discord
from discord.ext import commands

from embeds import CommandEmbed


class Warn(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx: commands.Context, member: discord.Member, *, reason: str = None) -> None:
        pass


class Mute(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx: commands.Context, member: discord.Member, delay: int = 1, *, reason: str = None) -> None:
        role: discord.Role = await commands.RoleConverter().convert(ctx, "Muted")
        await ctx.send(embed=CommandEmbed("Muted", member))
        await member.add_roles(role, reason=reason)
        await asyncio.sleep(delay * 60)
        await member.remove_roles(role)
