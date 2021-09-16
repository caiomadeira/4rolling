from discord.ext import commands
from commons.dices_commons import DicesCommons


class Dices(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def d4(self, ctx, *, numero=None):
        result = await DicesCommons().roll(ctx, numero=numero, sides=4, name_of="D4")
        await ctx.send(embed=result)

    @commands.command()
    async def d6(self, ctx, *, numero=None):
        result = await DicesCommons().roll(ctx, numero=numero, sides=6, name_of="D6")
        await ctx.send(embed=result)

    @commands.command()
    async def d20(self, ctx, *, numero=None):
        result = await DicesCommons().roll(ctx, numero=numero, sides=20, name_of="D20")
        await ctx.send(embed=result)

    @commands.command()
    async def d10(self, ctx, *, numero=None):
        result = await DicesCommons().roll(ctx, numero=numero, sides=10, name_of="D10")
        await ctx.send(embed=result)

    @commands.command()
    async def d12(self, ctx, *, numero=None):
        result = await DicesCommons().roll(ctx, numero=numero, sides=12, name_of="D12")
        await ctx.send(embed=result)

    @commands.command()
    async def d8(self, ctx, *, numero=None):
        result = await DicesCommons().roll(ctx, numero=numero, sides=8, name_of="D8")
        await ctx.send(embed=result)


def setup(client):
    client.add_cog(Dices(client))
