import nextcord


class EmbedsCommons:

    @staticmethod
    def embed_short(custom_title, custom_description, custom_image=None):
        embed = nextcord.Embed(title=custom_title, description=custom_description, colour=discord.Colour.dark_magenta())
        embed.set_image(url=custom_image)
        return embed
