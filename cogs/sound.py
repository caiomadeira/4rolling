import os
import random

from discord.ext import commands
from commons.embeds_common import EmbedsCommons
from commons.sfx_common import SfxCommon


class Sound(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Not in voice channel.")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def leave(self, ctx):
        if ctx.author.voice is None:
            await ctx.channel.send(
                embed=EmbedsCommons().embed_short(custom_title=f"{ctx.author} is not in an voice channel.",
                                                  custom_description=""))
        elif ctx.voice_client:
            await ctx.channel.send(
                embed=EmbedsCommons().embed_short(custom_title=f"Leaving",
                                                  custom_description=""))
            await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, sfx):
        try:
            ctx.voice_client.stop()
        except AttributeError:
            await ctx.channel.send(
                embed=EmbedsCommons().embed_short(custom_title=f"{ctx.author} is not in an voice channel.",
                                                  custom_description=""))
        vc = ctx.voice_client
        if sfx == 'panic_town':
            await SfxCommon().play_sfx(ctx, voiceC=vc,
                                       sfx_name=os.getenv("panic_town_name"),
                                       sfx_path=os.getenv("panic_town_path"),
                                       custom_image=os.getenv('panic_town_icon_1'))
        if sfx == 'coastal_town':
            coastal_town_sfx_list = ['coastal_town_icon_1']
            await SfxCommon().play_sfx(ctx, voiceC=vc,
                                       sfx_name=os.getenv("coastal_town_name"),
                                       sfx_path=os.getenv("coastal_town_path"),
                                       custom_image=os.getenv(random.choice(coastal_town_sfx_list)))

        if sfx == 'fireplace_forest':
            fireplace_sfx_list = ['fireplace_forest_icon_1', 'fireplace_forest_icon_2']
            await SfxCommon().play_sfx(ctx, voiceC=vc,
                                       sfx_name=os.getenv("fireplace_forest_name"),
                                       sfx_path=os.getenv("fireplace_forest_path"),
                                       custom_image=os.getenv(random.choice(fireplace_sfx_list)))
        if sfx == 'desert_wind':
            desert_wind_sfx_list = ['desert_wind_icon_1']
            await SfxCommon().play_sfx(ctx, voiceC=vc,
                                       sfx_name=os.getenv("desert_wind_name"),
                                       sfx_path=os.getenv("desert_wind_path"),
                                       custom_image=os.getenv(random.choice(desert_wind_sfx_list)))

        if sfx == 'rain':
            rain_sfx_list = ['rain_icon_1', 'rain_icon_2']
            await SfxCommon().play_sfx(ctx, voiceC=vc,
                                       sfx_name=os.getenv("rain_name"),
                                       sfx_path=os.getenv("rain_path"),
                                       custom_image=os.getenv(random.choice(rain_sfx_list)))

        if sfx == 'tavern':
            tavern_sfx_list = ['tavern_icon_1', 'tavern_icon_2', 'tavern_icon_3']
            await SfxCommon().play_sfx(ctx, voiceC=vc,
                                       sfx_name=os.getenv("tavern_name"),
                                       sfx_path=os.getenv("tavern_path"),
                                       custom_image=os.getenv(random.choice(tavern_sfx_list)))

        if sfx == 'medieval_war':
            medwar_sfx_list = ['ancient_war_icon_1']
            await SfxCommon().play_sfx(ctx, voiceC=vc,
                                       sfx_name=os.getenv("ancient_war_name"),
                                       sfx_path=os.getenv("ancient_war_path"),
                                       custom_image=os.getenv(random.choice(medwar_sfx_list)))


    @commands.command()
    async def pause(self, ctx):
        await ctx.channel.send(
            embed=EmbedsCommons().embed_short(custom_title=f"Paused",
                                              custom_description=""))
        await ctx.voice_client.pause()

    @commands.command()
    async def resume(self, ctx):
        await ctx.channel.send(
            embed=EmbedsCommons().embed_short(custom_title=f"Playing again",
                                              custom_description=""))
        await ctx.voice_client.resume()


def setup(client):
    client.add_cog(Sound(client))
