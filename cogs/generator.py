import random

from nextcord.ext import commands
import nextcord
from nextcord import message
import nextcord.abc


class Dropdown(nextcord.ui.Select):

    def __init__(self):
        self.selectOptions = [nextcord.SelectOption(label="test", description="aaa")]
        super().__init__(placeholder="AAAA", max_values=2, min_values=1, options=self.selectOptions)

    async def callback(self, interaction: nextcord.Interaction):
        if self.label[0] == 'AAAA':
            return await interaction.response.send_message("TA GRITANDO PQ")
        return interaction.response.send_message("TESTE")


class DropdownView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown())


class CommandGen(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def lang(self, ctx):
        view1 = DropdownView()
        await ctx.send("aaa", view=view1)


def setup(client):
    client.add_cog(CommandGen(client))
