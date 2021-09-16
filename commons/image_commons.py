import io
import aiohttp
import discord


class ImageCommons:

    @staticmethod
    async def img_request(ctx, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return await ctx.channel.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.channel.send(file=discord.File(data, 'icon.gif'))

