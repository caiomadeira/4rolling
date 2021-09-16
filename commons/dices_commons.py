import random
import discord


class DicesCommons:

    async def roll(self, ctx, *, numero=None, sides: int, name_of: str):
        avatar = ctx.message.author.avatar_url
        numero = eval(numero)
        lst = []
        embed = discord.Embed(title="Rolling " + name_of, colour=discord.Colour.dark_magenta())
        embed.set_author(name=ctx.message.author, icon_url=avatar)
        embed.set_thumbnail(url=avatar)
        for _ in range(numero):
            dadoslado = (random.randint(1, sides))
            lst.append(dadoslado)
            embed.add_field(name=name_of, value=dadoslado, inline=True)

        embed.add_field(name='Total', value=sum(lst), inline=True)
        return embed