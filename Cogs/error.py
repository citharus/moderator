import discord
from discord.ext import commands

from embeds import ErrorEmbed


class Error(commands.Cog):
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error) -> None:
        if isinstance(error, commands.RoleNotFound):
            await ctx.send(embed=ErrorEmbed("Missing role was automatically created. Try again."))
            if "Muted" in error.args[0]:
                await ctx.guild.create_role(name="Muted",
                                            permissions=discord.Permissions(read_message_history=True,
                                                                            read_messages=True),
                                            reason="Automatically created role for mute command.")
