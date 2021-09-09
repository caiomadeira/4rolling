""""""""""""""""""""""
4ROLLING
---------------
Criado por Caio Madeira (@sudomaidera)
Disponível no Discord!
2020
"""""""""""""""""""""""
from discord.ext import commands


class Como_usar(commands.Cog):

    def __init__(self, client):
        self.client = client

    # eventos
    @commands.Cog.listener()
    async def on_ready(self):
        print('\nTudo certo! BOT ONLINE!')

    # comandos
    @commands.command()
    async def RPG_BOT(self, ctx):
        await ctx.send('oi')

def setup(client):
    client.add_cog(Como_usar(client))
