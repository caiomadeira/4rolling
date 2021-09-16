from discord.ext import commands
import discord
import os


class Info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def version(self, ctx):
        embed_2 = discord.Embed(
            description=f"Current Version: {os.getenv('version')}\n"
                        f"Last Release: {os.getenv('last_release_date')}",
            colour=discord.Colour.dark_magenta())
        await ctx.channel.send(embed=embed_2)

    @commands.command()
    async def about(self, ctx):
        logo_img = os.getenv('logo_img')

        embed = discord.Embed(
            title='Sobre 4ROLLING:',
            description='Criado por Caio Madeira (@sudomadeira)',
            colour=discord.Colour.dark_magenta()
        )
        embed.set_footer(text='Instagram: @sudomadeira \n Twitter: @sudomadeira \n Github: github.com/CaioMadeira')
        embed.set_image(url=logo_img)
        embed.set_thumbnail(url=logo_img)
        embed.add_field(name='SOBRE/ABOUT:', value="> Um BOT para RPG de mesa no discord!\n > Criado por Caio Madeira",
                        inline=True)
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def members(self, ctx):
        embed = discord.Embed(
            description=f"""Total members in Server/Guild: {ctx.guild.member_count}""",
            colour=discord.Colour.dark_magenta()
        )
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, member: discord.Member):
        show_avatar = discord.Embed(color=discord.Color.dark_magenta())
        show_avatar.set_image(url='{}'.format(member.avatar_url))
        await ctx.send(embed=show_avatar)

    @commands.command()
    async def changelog(self, ctx):
        with open('changelog.txt') as f:
            r = f.read()
        embed = discord.Embed(color=discord.Color.dark_magenta())
        embed.add_field(name="CHANGELOG", value=r)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Info(client))
