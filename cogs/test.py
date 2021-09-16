import nextcord
from discord.ext import commands
import discord
from discord_components import  Button, ButtonStyle, InteractionEventType
from discord_components import *
from nextcord.ext import commands

class Test(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def testGif(self, ctx):
        await ctx.send(file=discord.File('img/test.gif'))

    @commands.command()
    async def testEmbedGif(self, ctx):
        embed = nextcord.Embed(
            title='Sobre 4ROLLING:',
            description='Criado por Caio Madeira (@sudomadeira)',
            colour=discord.Colour.dark_magenta()
        )
        embed.set_image(
            url='https://media.discordapp.net/attachments/729288248119001158/886543504694734848/img_icon.gif?width=676&height=676')

        await ctx.channel.send(embed=embed)

    @commands.command()
    async def testButtonEmbed(self, ctx):

        btn1 = Button(style=ButtonStyle.blue, label="btn1", id="embed1")
        embed1 = discord.Embed(title="embed button test", description="blue btn", colour=discord.Colour.dark_magenta())
        await ctx.send(
            "Embed Button test",
            components=[
                [btn1]
            ]
        )

        buttons = {
            "embed1": embed1
        }

        while True:
            event = await self.client.wait_for("button_click")
            if event.channel is not ctx.channel:
                return
            if event.channel == ctx.channel:
                response = buttons.get(event.component.id)
                if response is None:
                    print(response)
                    await event.channel.send(

                        "Error. Please, Try again"
                    )
                if event.channel == ctx.channel:
                    print(response)
                    await event.respond(
                        embed=response
                    )
    @commands.command()
    async def testDirect(self, ctx):
        owner = ctx.guild.owner
        direct_message = await owner.create_dm()
        await direct_message.send("Hello")


    @commands.command()
    async def testDrop(self, ctx):
        await ctx.send("What you want generate?",
                       components=[
                           Select(placeholder='Select something!', options=[SelectOption(label='A', value='a')])
                       ])
        interact = await self.client.wait_for(InteractionEventType.select_option, check=lambda i: i.component[0].value == 'a')
        await interact.respond(content=f"Dungeon Map selected!")

def setup(client):
    client.add_cog(Test(client))
