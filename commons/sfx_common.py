from mutagen.mp3 import MP3
import platform
import discord
from commons.embeds_common import EmbedsCommons
from commons.time_util import seconds_to_hour


class SfxCommon:

    @staticmethod
    async def play_sfx(ctx, voiceC, sfx_name, sfx_path, custom_image=None):
        current_system = platform.system()
        if current_system == 'Windows':
            ffmpeg_exec_path = 'src/ffmpeg-4.4-win/bin/ffmpeg.exe'
            voiceC.play(discord.FFmpegPCMAudio(executable=ffmpeg_exec_path, source=sfx_path))
            audio = MP3(sfx_path)
            await ctx.channel.send(embed=EmbedsCommons().embed_short(custom_title=f'Playing {sfx_name}',
                                                                     custom_description=f'Duration: {seconds_to_hour(time_received=audio.info.length)}\n'
                                                                     f'Bitrate: {audio.info.bitrate}',
                                                                     custom_image=custom_image))
