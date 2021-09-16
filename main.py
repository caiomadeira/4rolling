import os
import dotenv
import nextcord
from nextcord.ext import commands

dotenv.load_dotenv(dotenv.find_dotenv())
client = commands.Bot(command_prefix='4!', intents=nextcord.Intents.all())


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.load_extension(f'cogs.{extension}')


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        if filename == "errors.py":
            pass
        client.load_extension(f'cogs.{filename[:-3]}')


def read_token():
    with open("token.txt", "r") as f:
        linhas = f.readlines()
        return linhas[0].strip()


client.run(read_token())
