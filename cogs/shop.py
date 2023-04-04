import requests
import discord
import os
import valorant
from discord.ext import commands

KEY = os.environ["VALPY-KEY"]
client = valorant.Client(KEY, locale=None)


class shop(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def shop(self, ctx):





        await ctx.send("To be implemented")




async def setup(client):
    await client.add_cog(shop(client))