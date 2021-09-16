from discord.ext import commands
from discord_components import Button, ButtonStyle, InteractionEventType


class Material(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def material(self, ctx):
        await ctx.send("> Dungeons and Dragons materials and other stuffs.",
                       components=[[Button(label="Player Book[D&D 5]", style=ButtonStyle.URL,
                                           url='https://dnd5ed.github.io/livros/LDJ.pdf'),
                                    Button(label="Monsters Handbook[D&D 5]", style=ButtonStyle.URL,
                                           url='https://dnd5ed.github.io/livros/MM.pdf'),
                                    Button(label="Master Guide[D&D 5]", style=ButtonStyle.URL,
                                           url='https://dnd5ed.github.io/livros/GM.pdf')],
                                   [Button(label="Fantasy Name Generator", url='https://www.fantasynamegenerators.com',
                                           style=ButtonStyle.URL),
                                    Button(label="Dungeon Generator", url='https://donjon.bin.sh/d20/dungeon/',
                                           style=ButtonStyle.URL)]])
        action = await self.client.wait_for("button_click",
                                            check=lambda i: i.component.label.startswith("D6"))
        await action.respond(type=InteractionEventType.ChannelMessageWithSource, content="4!d6 6")


def setup(client):
    client.add_cog(Material(client))
