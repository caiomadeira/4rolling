import asyncio
import logging
import nextcord
from nextcord.ext import commands
from discord.ext import commands
import discord
from commons.time_util import convert
from commons.embeds_common import EmbedsCommons
import os


class Utils(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["limpar"])
    async def clear(self, ctx, messages):
        messages = int(messages)
        if messages:
            await ctx.channel.purge(limit=messages)
            print(f"{messages} cleanned")
            embed = discord.Embed(description=f'{messages} messages erased.',
                                  colour=discord.Colour.dark_magenta())
            await ctx.channel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def remind(self, ctx, time, *, task):
        converted_time = convert(time=time)

        if converted_time == -1:
            await ctx.send(embed=EmbedsCommons().embed_short(custom_title="Invalid time",
                                                             custom_description=""))
            return
        if converted_time == -2:
            await ctx.send(embed=EmbedsCommons().embed_short(custom_title="Time need to be a integer",
                                                             custom_description="ex: 5s or 10m or 3h or 4d"))
            return

        await ctx.send(f"Started reminder for **{task}** and will last **{time}**.")
        await asyncio.sleep(converted_time)
        await ctx.send(f"{ctx.author.mention} your reminder for **{task}** has finished!")

    @remind.error
    async def remind_error(self, error, ctx):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"aaaaaaa")


def setup(client):
    client.add_cog(Utils(client))
