""""""""""""""""""""""
4ROLLING
---------------
Criado por Caio Madeira (@sudomaidera)
Disponível no Discord!
2020

"""""""""""""""""""""""
import os
import random
import time
from itertools import cycle
from PIL import Image, ImageDraw, ImageFont, ImageOps
import discord
from discord.ext import commands, tasks
from discord.utils import get

client = commands.Bot(command_prefix="--", case_insensitive=True)
status = cycle(["RPG", "sujo!", "todos na masmorra!", "os dados!"])


mensagens = entrou = 0


# =================================================================
""""""""""""""""""""""

       EVENTOS

"""""""""""""""""""""""

@client.event
async def on_ready():
    change_status.start()
    print("-----------------")
    print(f"\n{client.user.name} está pronto pra jogar!\n")
    print("-----------------")


@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


# =================================================================

@client.event
async def membro_entrou(member):
    global entrou
    entrou += 1

    for channel in member.server.channels:
        if str(channel) == "boas-vindas":
            await client.send_message(f"""Bem vindo ao servidor {member.mention}""")



""""""""""""""""""""""

       COMANDOS

"""""""""""""""""""""""
# =============== INFO ================
@client.command()
async def sobre(mensagem):
    global mensagens
    mensagens += 1

    id = client.get_guild(619011695762866197)  # id do servidor


    LOGO = 'https://media.discordapp.net/attachments/712754644987936858/744679657730998302/4roll-logo.png?width=677&height=677'

    embed_1 = discord.Embed(

        title='Sobre 4ROLLING:',
        description='Criado por Caio Madeira (@sudomadeira)',
        colour=discord.Colour.dark_magenta()

    )

    embed_1.set_footer(text='Instagram: @sudomadeira \n Twitter: @sudomadeira \n Github: github.com/CaioMadeira')
    embed_1.set_image(url=LOGO)
    embed_1.set_thumbnail(url=LOGO)
    embed_1.add_field(name='SOBRE/ABOUT:', value="> Sou um BOT para RPG! \n > Criado por Caio Madeira", inline=True)
    await mensagem.channel.send(embed=embed_1)

@client.command()
async def membros(mensagem):
    global mensagens
    mensagens += 1

    id = client.get_guild(619011695762866197)

    embed_2 = discord.Embed(
        description= f"""> Total de Membros: {id.member_count}""",
        colour=discord.Colour.dark_magenta()

    )
    await mensagem.channel.send(embed=embed_2)


@client.command()
async def versao(mensagem):
    global mensagens
    mensagens += 1

    id = client.get_guild(619011695762866197)

    embed_2 = discord.Embed(
        description="Versão: 1.0.0 \n Release: 16/08/20",
        colour=discord.Colour.dark_magenta()

    )
    await mensagem.channel.send(embed=embed_2)


# ================ AVATAR SHOW ==========================
@client.command()
async def avatar(ctx, member: discord.Member):
    show_avatar = discord.Embed(

        color=discord.Color.dark_magenta()

    )
    show_avatar.set_image(url='{}'.format(member.avatar_url))
    await ctx.send(embed=show_avatar)




# ============== APAGAR MENSAGENS =========================
@client.command(aliases=["limpar50", "limpar100"])
async def limpar(ctx, numero):
    numero = eval(numero)

    if numero:
        await ctx.channel.purge(limit=numero)
        print(f"{numero} mensagens limpas")


# ----------------- COGS - HELP ---------------------------------
@client.command()
async def load(extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(extension):
    client.unload_extension(f'cogs.{extension}')


@client.command()
async def reload(extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

""""""""""""""""""""""

       RPG TOOLS
>D6, D8, D10, D12, D20

"""""""""""""""""""""""


# DADO DE 6 LADOS

@client.command()
async def d6(ctx, *, numero=None):

    avatar = ctx.message.author.avatar_url
    numero = eval(numero)
    lst = []


    embed = discord.Embed(

        title = 'Rolando D6...',
        colour=discord.Colour.dark_magenta()

    )
    embed.set_author(name=ctx.message.author, icon_url=avatar)
    embed.set_thumbnail(url=avatar)
    for _ in range(numero):
        dadoslado = (random.randint(1, 6))
        lst.append(dadoslado)
        embed.add_field(name='D6', value=dadoslado, inline=True)

    embed.add_field(name='Total', value=sum(lst), inline=True)

    await ctx.send(embed=embed)


# DADO DE 20 LADOS
@client.command()
async def d20(ctx, *, numero=None):
    avatar = ctx.message.author.avatar_url
    numero = eval(numero)
    lst = []

    embed = discord.Embed(

        title='Rolando D20...',
        colour=discord.Colour.dark_magenta()

    )
    embed.set_author(name=ctx.message.author, icon_url=avatar)
    embed.set_thumbnail(url=avatar)
    for _ in range(numero):
        dadoslado = (random.randint(1, 20))
        lst.append(dadoslado)
        embed.add_field(name='D20', value=dadoslado, inline=True)

    embed.add_field(name='Total', value=sum(lst), inline=True)

    await ctx.send(embed=embed)


# ::::::::::::::::DADO DE 10 LADOS
@client.command()
async def d10(ctx, *, numero=None):
    avatar = ctx.message.author.avatar_url
    numero = eval(numero)
    lst = []

    embed = discord.Embed(

        title='Rolando D10...',
        colour=discord.Colour.dark_magenta()

    )
    embed.set_author(name=ctx.message.author, icon_url=avatar)
    embed.set_thumbnail(url=avatar)
    for _ in range(numero):
        dadoslado = (random.randint(1, 10))
        lst.append(dadoslado)
        embed.add_field(name='D10', value=dadoslado, inline=True)

    embed.add_field(name='Total', value=sum(lst), inline=True)

    await ctx.send(embed=embed)


# ::::::::::::::::: DADO DE 12 LADOS
@client.command()
async def d12(ctx, *, numero=None):
    avatar = ctx.message.author.avatar_url
    numero = eval(numero)
    lst = []

    embed = discord.Embed(

        title='Rolando D12...',
        colour=discord.Colour.dark_magenta()

    )
    embed.set_author(name=ctx.message.author, icon_url=avatar)
    embed.set_thumbnail(url=avatar)
    for _ in range(numero):
        dadoslado = (random.randint(1, 12))
        lst.append(dadoslado)
        embed.add_field(name='D12', value=dadoslado, inline=True)

    embed.add_field(name='Total', value=sum(lst), inline=True)

    await ctx.send(embed=embed)

# :::::::::::::::::;;DADO DE 8 LADOS
@client.command()
async def d8(ctx, *, numero=None):
    avatar = ctx.message.author.avatar_url
    numero = eval(numero)
    lst = []

    embed = discord.Embed(

        title='Rolando D8...',
        colour=discord.Colour.dark_magenta()

    )
    embed.set_author(name=ctx.message.author, icon_url=avatar)
    embed.set_thumbnail(url=avatar)
    for _ in range(numero):
        dadoslado = (random.randint(1, 8))
        lst.append(dadoslado)
        embed.add_field(name='D8', value=dadoslado, inline=True)

    embed.add_field(name='Total', value=sum(lst), inline=True)

    await ctx.send(embed=embed)
""""""""""""""""""""""

    RPG SOUNDS

"""""""""""""""""""""""
@client.command()
async def lista_sons(ctx):
    await ctx.send(" > 1 - coastal-town \n > 2 - desert-wind \n > 3 - fireplace-forest \n > 4 - panic-town \n > 5 - rain \n > 6 - tavern\n > 7 - war-ambience \n")




# ::::::::::: MUSICA ::::::::::::::
@client.command(pass_context=True, aliasses=['e', 'entrar'])  # metodo para entrar no voice channel
async def entrar(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)

    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)

    else:
        voice = await channel.connect()
        print(f"O Bot se conectou ao {channel}\n")

    await ctx.send(f">{client.user.name} entrou em {channel}")

@client.command(pass_context=True, aliasses=['s', 'sair'])  # metodo para sair do voice channel
async def sair(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f">O bot desconectou do {channel}\n")
        await ctx.send(f"Saiu {channel}")
    else:
        print("Tentaram tirar o Bot do canal, mas ele não está nele")
        await ctx.send(">O Bot não tá no canal! BURR@!")


@client.command(pass_context=True, aliasses=['s', 'sound'])  # metodo para tocar musica no voice channel
async def sound(ctx, *, musica=None):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    musica: str
    volume = 1.0

    if musica == 'fireplace-forest':
        voice.play(discord.FFmpegPCMAudio("music/fireplace-forest"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = volume
        print("Sucesso em reproduzir")
        await ctx.send(f">{channel}: Reproduzindo 𝙵𝚒𝚛𝚎𝚙𝚕𝚊𝚌𝚎 𝙵𝚘𝚛𝚎𝚜𝚝 ")

    if musica == 'rain':
        voice.play(discord.FFmpegPCMAudio("music/rain-3h.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = volume
        print("Sucesso em reproduzir")
        await ctx.send(f">{channel}: Reproduzindo 𝚁𝚊𝚒𝚗")

    if musica == 'desert-wind':
        voice.play(discord.FFmpegPCMAudio("music/desert-wind.m4a"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = volume
        print("Sucesso em reproduzir")
        await ctx.send(f">{channel}: Reproduzindo 𝙳𝚎𝚜𝚎𝚛𝚝 𝚆𝚒𝚗𝚍")

    if musica == 'war':
        voice.play(discord.FFmpegPCMAudio("music/war-ambience.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = volume
        print("Sucesso em reproduzir")
        await ctx.send(f">{channel}: Reproduzindo 𝚆𝚊𝚛")

    if musica == 'coastal-town':
        voice.play(discord.FFmpegPCMAudio("music/coastal-town.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = volume
        print("Sucesso em reproduzir")
        await ctx.send(f">{channel}: Reproduzindo 𝙲𝚘𝚊𝚜𝚝𝚊𝚕 𝚃𝚘𝚠𝚗")

    if musica == 'tavern':
        voice.play(discord.FFmpegPCMAudio("music/tavern.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = volume
        print("Sucesso em reproduzir")
        await ctx.send(f">{channel}: Reproduzindo 𝚃𝚊𝚟𝚎𝚛𝚗")

    if musica == 'panic-town':
        voice.play(discord.FFmpegPCMAudio("music/panic-town.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = volume
        print("Sucesso em reproduzir")
        await ctx.send(f">{channel}: Reproduzindo 𝙿𝚊𝚗𝚒𝚌 𝚃𝚘𝚠𝚗")

@client.command(pass_context=True, aliasses=['pa', 'pause'])  # metodo para pausar
async def pausar(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Música Pausada")
        voice.pause()
        await ctx.send(f">Musica pausada em {channel}")
    else:
        print("Nenhuma musica está tocando")
        await ctx.send(f">Erro em pausar. Nenhuma musica tocando em {channel}")

@client.command(pass_context=True, aliasses=['re', 'retomar'])  # metodo para pausar
async def retomar(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print("Retomando o som")
        voice.resume()
        await ctx.send(f">Musica resumida em {channel}")
    else:
        print("O Player não está pausado")
        await ctx.send(">Som não está pausado")


@client.command(pass_context=True, aliasses=['par', 'parar'])  # metodo para pausar
async def parar(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print(">Som parado")
        voice.stop()
        await ctx.send(f">Som parado em {channel}")
    else:
        print("Nenhum som tocando. Falha em parar")
        await ctx.send(f">Nenhum som tocando em {channel}. Falha em parar")

