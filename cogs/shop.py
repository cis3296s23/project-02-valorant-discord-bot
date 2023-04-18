import requests
import discord
import os
import valorant
import re
import json
from discord.ext import commands


with open("cogs/auth.json", "r") as f:
    config = json.load(f)
    username = config["riotUsername"]
    riotPassword = config["riotPassword"]
    region = config["region"]
    token = config["riotToken"]



class shop(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def shop(self, ctx):

        




        await ctx.send("To be implemented")




async def setup(client):
    await client.add_cog(shop(client))