import time

from discord.ext import commands
from discord_components import *
import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())


class BasicLogger(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"4Rolling[{os.getenv('version')}] is [Online]")
        DiscordComponents(bot=self.client)

    @commands.Cog.listener()
    async def on_message(self, message):
        print(f'{message.author} [{message.created_at}]: "{message.content}"')

def setup(client):
    client.add_cog(BasicLogger(client))
